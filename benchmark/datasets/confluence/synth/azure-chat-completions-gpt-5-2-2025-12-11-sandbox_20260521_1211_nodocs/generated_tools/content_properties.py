from typing import Any, Dict, Optional

from .client import ConfluenceClient


def v1_get_content_property(content_id: str, key: str) -> Any:
    """GET /rest/api/content/{id}/property/{key}"""
    c = ConfluenceClient()
    return c.request("GET", f"/rest/api/content/{content_id}/property/{key}")


def v1_set_content_property(
    content_id: str,
    key: str,
    *,
    value: Any,
    version_number: Optional[int] = None,
) -> Any:
    """PUT /rest/api/content/{id}/property/{key}"""
    c = ConfluenceClient()
    payload: Dict[str, Any] = {"key": key, "value": value}
    if version_number is not None:
        payload["version"] = {"number": version_number}
    return c.request("PUT", f"/rest/api/content/{content_id}/property/{key}", json=payload)
