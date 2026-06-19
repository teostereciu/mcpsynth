from typing import Any, Dict, Optional, List

from .http_client import ConfluenceClient


def get_current_user(*, expand: Optional[List[str]] = None) -> Dict[str, Any]:
    """GET /wiki/rest/api/user/current"""
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return ConfluenceClient().request("GET", "/rest/api/user/current", params=params)  # type: ignore[return-value]


def get_user_by_account_id(*, account_id: str, expand: Optional[List[str]] = None) -> Dict[str, Any]:
    """GET /wiki/rest/api/user?accountId={accountId}"""
    params: Dict[str, Any] = {"accountId": account_id}
    if expand:
        params["expand"] = expand
    return ConfluenceClient().request("GET", "/rest/api/user", params=params)  # type: ignore[return-value]


def get_users_bulk(*, account_ids: List[str]) -> Dict[str, Any]:
    """POST /wiki/api/v2/users-bulk"""
    payload = {"accountIds": account_ids}
    return ConfluenceClient().request("POST", "/api/v2/users-bulk", json=payload)  # type: ignore[return-value]
