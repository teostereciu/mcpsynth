"""Confluence v2 Spaces API tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

def _auth():
    return (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])

def _base():
    return os.environ["CONFLUENCE_BASE_URL"].rstrip("/")

def _v2(path: str) -> str:
    return f"{_base()}/api/v2{path}"

def _v1(path: str) -> str:
    return f"{_base()}/rest/api{path}"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_spaces(
        keys: str = None,
        space_type: str = None,
        content_status: str = None,
        cursor: str = None,
        max_results: int = 25,
    ) -> dict:
        """List all spaces. Optionally filter by key(s), type, or status."""
        params = {"max_results": max_results}
        if keys:
            params["keys"] = keys
        if space_type:
            params["type"] = space_type
        if content_status:
            params["content_status"] = content_status
        if cursor:
            params["cursor"] = cursor
        try:
            r = requests.get(_v2("/spaces"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_space_by_id(
        space_id: int,
        description_format: str = None,
        include_icon: bool = False,
        include_operations: bool = False,
        include_properties: bool = False,
        include_permissions: bool = False,
        include_labels: bool = False,
    ) -> dict:
        """Get a specific space by its numeric ID."""
        params = {
            "include-icon": include_icon,
            "include-operations": include_operations,
            "include-properties": include_properties,
            "include-permissions": include_permissions,
            "include-labels": include_labels,
        }
        if description_format:
            params["description-format"] = description_format
        try:
            r = requests.get(_v2(f"/spaces/{space_id}"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def create_space(
        name: str,
        key: str = None,
        description_value: str = None,
        description_representation: str = "plain",
        create_private_space: bool = False,
    ) -> dict:
        """Create a new Confluence space."""
        payload: dict = {"name": name}
        if key:
            payload["key"] = key
        if description_value:
            payload["description"] = {
                "value": description_value,
                "representation": description_representation,
            }
        if create_private_space:
            payload["createPrivateSpace"] = True
        try:
            r = requests.post(_v2("/spaces"), json=payload, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def delete_space(space_key: str) -> dict:
        """Delete a space by its key (uses v1 API which supports key-based deletion)."""
        try:
            r = requests.delete(_v1(f"/space/{space_key}"), auth=_auth())
            r.raise_for_status()
            return {"status": "deleted", "space_key": space_key}
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}
