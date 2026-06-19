from typing import Any, Dict, Optional

from .jira_client import JiraClient


def get_myself(expand: Optional[str] = None):
    """GET /myself"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/myself", params=params or None)


def get_my_preference(key: str):
    """GET /mypreferences"""
    client = JiraClient()
    return client.request("GET", "/mypreferences", params={"key": key})


def set_my_preference(key: str, value: str):
    """PUT /mypreferences"""
    client = JiraClient()
    # API expects plain string body
    return client.request("PUT", "/mypreferences", params={"key": key}, json=value)


def delete_my_preference(key: str):
    """DELETE /mypreferences"""
    client = JiraClient()
    return client.request("DELETE", "/mypreferences", params={"key": key})
