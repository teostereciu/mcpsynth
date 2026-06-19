from typing import Any, Optional

from confluence_client import client


def get_user(account_id: str, expand: Optional[list[str]] = None) -> Any:
    return client.request("GET", "/rest/api/user", params={"accountId": account_id, "expand": expand})


def get_anonymous_user(expand: Optional[list[str]] = None) -> Any:
    return client.request("GET", "/rest/api/user/anonymous", params={"expand": expand})


def get_current_user(expand: Optional[list[str]] = None) -> Any:
    return client.request("GET", "/rest/api/user/current", params={"expand": expand})


def get_user_group_memberships(
    account_id: str,
    start: Optional[int] = None,
    limit: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        "/rest/api/user/memberof",
        params={"accountId": account_id, "start": start, "limit": limit},
    )


def get_users_bulk(
    account_id: Optional[list[str]] = None,
    username: Optional[list[str]] = None,
    key: Optional[list[str]] = None,
    start: Optional[int] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
) -> Any:
    return client.request(
        "GET",
        "/rest/api/user/bulk",
        params={
            "accountId": account_id,
            "username": username,
            "key": key,
            "start": start,
            "limit": limit,
            "expand": expand,
        },
    )


def get_user_email(account_id: str) -> Any:
    return client.request("GET", "/rest/api/user/email", params={"accountId": account_id})


def get_user_emails_bulk(account_id: list[str]) -> Any:
    return client.request("GET", "/rest/api/user/email/bulk", params={"accountId": account_id})
