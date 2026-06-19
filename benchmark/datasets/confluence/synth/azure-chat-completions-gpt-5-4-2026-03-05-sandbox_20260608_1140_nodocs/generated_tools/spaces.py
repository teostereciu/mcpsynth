from typing import Any, Dict, Optional

from generated_tools.confluence_client import client


def list_spaces(limit: int = 25, cursor: Optional[str] = None, keys: Optional[str] = None) -> Dict[str, Any]:
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if keys:
        params["keys"] = keys
    return client.request("GET", "/api/v2/spaces", params=params)


def get_space(space_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/api/v2/spaces/{space_id}")


def create_space(name: str, key: str, description: Optional[str] = None) -> Dict[str, Any]:
    payload = {"name": name, "key": key}
    if description:
        payload["description"] = {"plain": {"value": description}}
    return client.request("POST", "/rest/api/space", json_body=payload)


def delete_space(space_key: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/rest/api/space/{space_key}")
