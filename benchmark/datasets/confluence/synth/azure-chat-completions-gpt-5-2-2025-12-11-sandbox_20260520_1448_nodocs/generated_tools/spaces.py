import os
from typing import Any, Dict, Optional

from .http import confluence_request


def list_spaces(limit: int = 25, cursor: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return confluence_request("GET", "/api/v2/spaces", params=params)


def get_space(space_id: Optional[int] = None, space_key: Optional[str] = None) -> Dict[str, Any]:
    if space_id is not None:
        return confluence_request("GET", f"/api/v2/spaces/{space_id}")
    if space_key is None:
        space_key = os.environ.get("CONFLUENCE_SPACE_KEY")
    if not space_key:
        return {"error": "Provide space_id or space_key (or set CONFLUENCE_SPACE_KEY)"}
    return confluence_request("GET", f"/rest/api/space/{space_key}")


def create_space(key: str, name: str, description_plain: str = "") -> Dict[str, Any]:
    payload = {
        "key": key,
        "name": name,
        "description": {"plain": {"value": description_plain, "representation": "plain"}},
    }
    return confluence_request("POST", "/rest/api/space", json=payload)


def delete_space(space_id: int) -> Dict[str, Any]:
    return confluence_request("DELETE", f"/api/v2/spaces/{space_id}")
