from typing import Any, Dict, Optional

from .http_client import ConfluenceClient, ok_or_error


def get_current_user(*, include: Optional[list[str]] = None) -> Dict[str, Any]:
    """GET /rest/api/user/current"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {}
    if include:
        params["include"] = include
    status, body, headers = c.request("GET", "/rest/api/user/current", params=params)
    return ok_or_error(status, body, headers)


def get_user_by_account_id(account_id: str, *, include: Optional[list[str]] = None) -> Dict[str, Any]:
    """GET /rest/api/user?accountId=..."""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"accountId": account_id}
    if include:
        params["include"] = include
    status, body, headers = c.request("GET", "/rest/api/user", params=params)
    return ok_or_error(status, body, headers)


def get_users_bulk(account_ids: list[str]) -> Dict[str, Any]:
    """POST /api/v2/users-bulk"""
    c = ConfluenceClient()
    status, body, headers = c.request("POST", "/api/v2/users-bulk", json_body={"accountIds": account_ids})
    return ok_or_error(status, body, headers)
