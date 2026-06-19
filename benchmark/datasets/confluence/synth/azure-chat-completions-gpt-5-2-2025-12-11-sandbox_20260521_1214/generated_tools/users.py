from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def get_current_user(*, expand: Optional[list[str]] = None) -> Dict[str, Any]:
    """GET /wiki/rest/api/user/current"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", "/rest/api/user/current", params=params or None)


def get_user_by_account_id(*, account_id: str, expand: Optional[list[str]] = None) -> Dict[str, Any]:
    """GET /wiki/rest/api/user"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {"accountId": account_id}
    if expand:
        params["expand"] = expand
    return client.request("GET", "/rest/api/user", params=params)
