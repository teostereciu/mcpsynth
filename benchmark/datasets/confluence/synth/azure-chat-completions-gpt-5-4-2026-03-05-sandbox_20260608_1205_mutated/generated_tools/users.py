from typing import Any, List, Optional

from generated_tools.core import client


def get_user(account_id: str, include: Optional[List[str]] = None) -> Any:
    return client.request("GET", "/rest/api/user", params={"accountId": account_id, "include": include})


def get_anonymous_user(include: Optional[List[str]] = None) -> Any:
    return client.request("GET", "/rest/api/user/anonymous", params={"include": include})


def get_current_user(include: Optional[List[str]] = None) -> Any:
    return client.request("GET", "/rest/api/user/current", params={"include": include})


def get_group_memberships_for_user(account_id: Optional[str] = None, username: Optional[str] = None, key: Optional[str] = None, start: Optional[int] = None, limit: Optional[int] = None) -> Any:
    return client.request("GET", "/rest/api/user/memberof", params={"accountId": account_id, "username": username, "key": key, "start": start, "limit": limit})


def get_multiple_users(account_ids: Optional[List[str]] = None, usernames: Optional[List[str]] = None, keys: Optional[List[str]] = None, start: Optional[int] = None, limit: Optional[int] = None, expand: Optional[List[str]] = None) -> Any:
    return client.request("GET", "/rest/api/user/bulk", params={"accountId": account_ids, "username": usernames, "key": keys, "start": start, "limit": limit, "expand": expand})


def get_user_email(account_id: str) -> Any:
    return client.request("GET", "/rest/api/user/email", params={"accountId": account_id})


def get_user_emails_in_batch(account_ids: List[str]) -> Any:
    return client.request("GET", "/rest/api/user/email/bulk", params={"accountId": account_ids})
