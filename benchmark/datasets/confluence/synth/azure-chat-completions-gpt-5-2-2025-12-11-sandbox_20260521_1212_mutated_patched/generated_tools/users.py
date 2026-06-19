from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def get_current_user(include: Optional[list[str]] = None) -> Dict[str, Any]:
    """GET /wiki/rest/api/user/current"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {}
    if include is not None:
        params["expand"] = include
    return client.request("GET", "/rest/api/user/current", params=params)


def get_user_by_account_id(account_id: str, include: Optional[list[str]] = None) -> Dict[str, Any]:
    """GET /wiki/rest/api/user?accountId=..."""
    client = ConfluenceClient()
    params: Dict[str, Any] = {"accountId": account_id}
    if include is not None:
        params["expand"] = include
    return client.request("GET", "/rest/api/user", params=params)
