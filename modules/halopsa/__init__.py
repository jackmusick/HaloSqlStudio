"""modules.halopsa — lazy-loading split SDK (experiment)."""

from __future__ import annotations
import importlib
from modules.halopsa._common import DotDict, SDKError
from modules.halopsa._lazy import _lazy
from modules.halopsa._routing import METHOD_TO_MODULE

_loaded_modules: dict[str, object] = {}


def _ensure_submodule(name: str):
    mod = _loaded_modules.get(name)
    if mod is None:
        mod = importlib.import_module(f"modules.halopsa.{name}")
        _loaded_modules[name] = mod
    return mod


def __getattr__(name: str):
    submodule = METHOD_TO_MODULE.get(name)
    if submodule is not None:
        mod = _ensure_submodule(submodule)
        fn = getattr(mod, name, None)
        if fn is None:
            raise AttributeError(f"{name!r} not in modules.halopsa.{submodule}")
        async def _bound(*args, **kwargs):
            client = await _lazy._ensure_client()
            return fn(client, *args, **kwargs)
        return _bound
    raise AttributeError(f"module 'modules.halopsa' has no attribute {name!r}")


__all__ = ["DotDict", "SDKError"]
