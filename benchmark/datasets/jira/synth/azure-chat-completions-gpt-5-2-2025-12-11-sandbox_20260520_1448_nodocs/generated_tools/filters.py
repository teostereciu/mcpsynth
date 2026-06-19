from typing import Any, Dict, Optional

from jira_client import JiraClient


def get_filter(filter_id: str, expand: Optional[str] = None) -> Any:
    """GET /filter/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/filter/{filter_id}", params=params)


def list_my_filters(expand: Optional[str] = None) -> Any:
    """GET /filter/my"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", "/filter/my", params=params)


def create_filter(name: str, jql: str, description: Optional[str] = None, favourite: bool = False, share_permissions: Optional[list] = None, edit_permissions: Optional[list] = None) -> Any:
    """POST /filter"""
    client = JiraClient()
    payload: Dict[str, Any] = {"name": name, "jql": jql, "favourite": favourite}
    if description is not None:
        payload["description"] = description
    if share_permissions is not None:
        payload["sharePermissions"] = share_permissions
    if edit_permissions is not None:
        payload["editPermissions"] = edit_permissions
    return client.request("POST", "/filter", json=payload)


def update_filter(filter_id: str, payload: Dict[str, Any]) -> Any:
    """PUT /filter/{id}"""
    client = JiraClient()
    return client.request("PUT", f"/filter/{filter_id}", json=payload)


def delete_filter(filter_id: str) -> Any:
    """DELETE /filter/{id}"""
    client = JiraClient()
    return client.request("DELETE", f"/filter/{filter_id}")
