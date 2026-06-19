from typing import Any, Dict, Optional

from jira_client import JiraClient


def get_filter(client: JiraClient, filter_id: str, expand: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/filter/{filter_id}", params=params)


def my_filters(client: JiraClient, expand: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", "/filter/my", params=params)


def create_filter(client: JiraClient, name: str, jql: str, description: Optional[str] = None, favourite: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {"name": name, "jql": jql}
    if description is not None:
        payload["description"] = description
    if favourite is not None:
        payload["favourite"] = favourite
    return client.request("POST", "/filter", json=payload)


def update_filter(client: JiraClient, filter_id: str, updates: Dict[str, Any]) -> Any:
    return client.request("PUT", f"/filter/{filter_id}", json=updates)


def delete_filter(client: JiraClient, filter_id: str) -> Any:
    return client.request("DELETE", f"/filter/{filter_id}")
