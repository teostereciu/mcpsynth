from typing import Any, Dict, Optional

from .http import request_json


# Docs: docs/api_accounts.md


def verify_account_credentials() -> Any:
    """GET /api/v1/accounts/verify_credentials"""
    return request_json("GET", "/api/v1/accounts/verify_credentials")


def get_account(account_id: str) -> Any:
    """GET /api/v1/accounts/{id}"""
    return request_json("GET", f"/api/v1/accounts/{account_id}")


def get_account_statuses(
    account_id: str,
    *,
    limit: Optional[int] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    pinned: Optional[bool] = None,
    exclude_replies: Optional[bool] = None,
    exclude_reblogs: Optional[bool] = None,
    only_media: Optional[bool] = None,
    tagged: Optional[str] = None,
) -> Any:
    """GET /api/v1/accounts/{id}/statuses"""
    params: Dict[str, Any] = {}
    for k, v in {
        "limit": limit,
        "max_id": max_id,
        "since_id": since_id,
        "min_id": min_id,
        "pinned": pinned,
        "exclude_replies": exclude_replies,
        "exclude_reblogs": exclude_reblogs,
        "only_media": only_media,
        "tagged": tagged,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/api/v1/accounts/{account_id}/statuses", params=params)


def get_account_followers(
    account_id: str,
    *,
    limit: Optional[int] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> Any:
    """GET /api/v1/accounts/{id}/followers"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/api/v1/accounts/{account_id}/followers", params=params)


def get_account_following(
    account_id: str,
    *,
    limit: Optional[int] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> Any:
    """GET /api/v1/accounts/{id}/following"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/api/v1/accounts/{account_id}/following", params=params)


def follow_account(
    account_id: str,
    *,
    reblogs: Optional[bool] = None,
    notify: Optional[bool] = None,
    languages: Optional[list[str]] = None,
) -> Any:
    """POST /api/v1/accounts/{id}/follow"""
    data: Dict[str, Any] = {}
    if reblogs is not None:
        data["reblogs"] = str(reblogs).lower()
    if notify is not None:
        data["notify"] = str(notify).lower()
    if languages is not None:
        # Mastodon expects languages[]
        for i, lang in enumerate(languages):
            data[f"languages[{i}]"] = lang
    return request_json("POST", f"/api/v1/accounts/{account_id}/follow", data=data)


def unfollow_account(account_id: str) -> Any:
    """POST /api/v1/accounts/{id}/unfollow"""
    return request_json("POST", f"/api/v1/accounts/{account_id}/unfollow")
