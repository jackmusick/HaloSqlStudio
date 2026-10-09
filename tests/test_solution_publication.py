"""Release contract for the portable Halo SQL Studio Solution."""

import ast
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_solution_manifest_closes_over_its_runtime_dependencies():
    apps = yaml.safe_load((ROOT / ".bifrost/apps.yaml").read_text())["apps"]
    connections = yaml.safe_load((ROOT / ".bifrost/connections.yaml").read_text())["connections"]
    events = yaml.safe_load((ROOT / ".bifrost/events.yaml").read_text())["events"]
    workflows = yaml.safe_load((ROOT / ".bifrost/workflows.yaml").read_text())["workflows"]

    app = next(iter(apps.values()))
    assert app["path"] == "apps/halo-sql-studio"
    assert app["role_names"] == ["Service Managers"]
    halo_connection = connections["HaloPSA"]
    base_url = next(item for item in halo_connection["template"]["config_schema"] if item["key"] == "base_url")
    assert base_url["type"] == "string"
    assert base_url["required"]
    assert "including /api" in base_url["description"]
    assert halo_connection["template"]["oauth"]["oauth_flow_type"] == "client_credentials"

    workflow_paths = {workflow_id: item["path"] for workflow_id, item in workflows.items()}
    for event in events.values():
        for subscription in event["subscriptions"]:
            if subscription["target_type"] == "workflow":
                assert subscription["workflow_id"] in workflow_paths

    for workflow in workflows.values():
        source = ROOT / workflow["path"]
        assert source.is_file()
        functions = {
            node.name
            for node in ast.parse(source.read_text()).body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        assert workflow["function_name"] in functions

    assert (ROOT / "modules/halopsa/reporting.py").is_file()
    for import_source in (ROOT / "functions").rglob("*.py"):
        for node in ast.walk(ast.parse(import_source.read_text())):
            if not isinstance(node, ast.ImportFrom) or not node.module:
                continue
            if not node.module.startswith("modules"):
                continue
            module_path = ROOT / (node.module.replace(".", "/") + ".py")
            package_path = ROOT / node.module.replace(".", "/") / "__init__.py"
            assert module_path.is_file() or package_path.is_file()


def test_browser_sdk_is_platform_injected_not_pinned_to_an_instance():
    app_root = ROOT / "apps/halo-sql-studio"
    package = json.loads((app_root / "package.json").read_text())
    lock = json.loads((app_root / "package-lock.json").read_text())

    assert "bifrost" not in package["dependencies"]
    assert "node_modules/bifrost" not in lock["packages"]
    assert ".env*" in (ROOT / ".gitignore").read_text().splitlines()
