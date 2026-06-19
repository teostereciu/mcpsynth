from typing import Any, Dict, Optional

from .jira_client import JiraClient


def get_filter(filter_id: int, expand: Optional[str] = None) -> Dict[str, Any]:
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


def create_filter(name: str, jql: str, description: Optional[str] = None, favourite: Optional[bool] = None) -> Dict[str, Any]:
    """POST /filter"""
    client = JiraClient()
    payload: Dict[str, Any] = {"name": name, "jql": jql}
    if description is not None:
        payload["description"] = description
    if favourite is not None:
        payload["favourite"] = favourite
    return client.request("POST", "/filter", json=payload)


def update_filter(filter_id: int, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /filter/{id}"""
    client = JiraClient()
    return client.request("PUT", f"/filter/{filter_id}", json=payload)


def delete_filter(filter_id: int) -> Dict[str, Any]:
    """DELETE /filter/{id}"""
    client = JiraClient()
    return client.request("DELETE", f"/filter/{filter_id}")
