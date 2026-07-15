"""modules.halopsa_split._lazy — async lazy client wrapper."""

import requests

from modules.halopsa._common import _HaloAPIClient

class _LazyClient:
    """
    Module-level proxy that auto-initializes from Bifrost integration.
    Provides zero-config authentication experience.

    Note: Client is NOT cached - always fetches fresh credentials to ensure
    token refreshes are picked up immediately.
    """
    _integration_name: str = 'HaloPSA'
    _auth_type: str = 'oauth'

    async def _ensure_client(self):
        from bifrost import integrations
        integration = await integrations.get(self._integration_name)
        if not integration:
            raise RuntimeError(f"Integration '{self._integration_name}' not found")
        config = integration.config or {}
        session = requests.Session()
        if integration.oauth and integration.oauth.access_token:
            session.headers['Authorization'] = f'Bearer {integration.oauth.access_token}'
        else:
            raise RuntimeError('OAuth not configured or access token missing')
        base_url = config.get('base_url', '')
        if not base_url:
            raise RuntimeError(f"base_url not configured for integration '{self._integration_name}'")
        timeout = float(config.get('timeout', 30.0))
        max_retries = int(config.get('max_retries', 3))
        base_backoff = float(config.get('base_backoff', 1.0))
        max_backoff = float(config.get('max_backoff', 60.0))
        return _HaloAPIClient(base_url, session, timeout=timeout, max_retries=max_retries, base_backoff=base_backoff, max_backoff=max_backoff)

    def __getattr__(self, name: str):
        """Proxy attribute access to the real client."""

        async def method_wrapper(*args, **kwargs):
            client = await self._ensure_client()
            method = getattr(client, name)
            return method(*args, **kwargs)
        return method_wrapper

_lazy = _LazyClient()
