from typing import Any, Dict, Optional

from .client import ConfluenceClient


def v2_list_spaces(*, limit: int = 25, cursor: Optional[str] = None) -> Any:
    """GET /api/v2/spaces"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return c.request("GET", "/api/v2/spaces", params=params)


def v2_get_space(space_id: str) -> Any:
    """GET /api/v2/spaces/{id}"""
    c = ConfluenceClient()
    return c.request("GET", f"/api/v2/spaces/{space_id}")


def v1_get_space_by_key(space_key: str) -> Any:
    """GET /rest/api/space/{spaceKey}"""
    c = ConfluenceClient()
    return c.request("GET", f"/rest/api/space/{space_key}")


def v1_create_space(*, key: str, name: str, description_plain: str = "") -> Any:
    """POST /rest/api/space"""
    c = ConfluenceClient()
    payload: Dict[str, Any] = {
        "key": key,
        "name": name,
        "description": {"plain": {"value": description_plain, "representation": "plain"}},
    }
    return c.request("POST", "/rest/api/space", json=payload, expected=(200, 201))


def v1_delete_space(space_key: str) -> Any:
    """DELETE /rest/api/space/{spaceKey}"""
    c = ConfluenceClient()
    return c.request("DELETE", f"/rest/api/space/{space_key}", expected=(202, 204))
