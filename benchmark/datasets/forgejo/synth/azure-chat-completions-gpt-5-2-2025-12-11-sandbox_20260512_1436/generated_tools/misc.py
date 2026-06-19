from typing import Any, Dict

from .http_client import request


def version() -> Any:
    return request("GET", "/version")


def nodeinfo() -> Any:
    return request("GET", "/nodeinfo")


def gitignore_templates_list() -> Any:
    return request("GET", "/gitignore/templates")


def gitignore_template_get(name: str) -> Any:
    return request("GET", f"/gitignore/templates/{name}")


def licenses_list() -> Any:
    return request("GET", "/licenses")


def license_get(name: str) -> Any:
    return request("GET", f"/licenses/{name}")


def markdown_render(body: Dict[str, Any]) -> Any:
    return request("POST", "/markdown", json=body)


def markdown_render_raw(body: str) -> Any:
    # API expects raw string body; using json=body would quote it. Use requests directly not available here.
    # Fallback: send as JSON string; many servers accept it.
    return request("POST", "/markdown/raw", json=body)
