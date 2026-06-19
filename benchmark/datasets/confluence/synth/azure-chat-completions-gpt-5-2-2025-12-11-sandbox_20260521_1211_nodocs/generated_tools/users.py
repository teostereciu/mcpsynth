from typing import Any

from .client import ConfluenceClient


def v1_get_current_user() -> Any:
    """GET /rest/api/user/current"""
    c = ConfluenceClient()
    return c.request("GET", "/rest/api/user/current")


def v1_get_user(account_id: str) -> Any:
    """GET /rest/api/user"""
    c = ConfluenceClient()
    return c.request("GET", "/rest/api/user", params={"accountId": account_id})
