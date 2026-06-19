from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http_client import request_json


def verify_account_credentials() -> Dict[str, Any]:
    return request_json("GET", "/api/v1/accounts/verify_credentials", require_auth=True)


def get_account(account_id: str) -> Dict[str, Any]:
    return request_json("GET", f"/api/v1/accounts/{account_id}", require_auth=False)


def follow_account(account_id: str, reblogs: Optional[bool] = None, notify: Optional[bool] = None, languages: Optional[List[str]] = None) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if reblogs is not None:
        data["reblogs"] = str(bool(reblogs)).lower()
    if notify is not None:
        data["notify"] = str(bool(notify)).lower()
    if languages is not None:
        data["languages[]"] = languages
    return request_json("POST", f"/api/v1/accounts/{account_id}/follow", data=data or None, require_auth=True)


def unfollow_account(account_id: str) -> Dict[str, Any]:
    return request_json("POST", f"/api/v1/accounts/{account_id}/unfollow", require_auth=True)


def get_account_followers(account_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    return request_json("GET", f"/api/v1/accounts/{account_id}/followers", params=params or None, require_auth=False)


def get_account_following(account_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    return request_json("GET", f"/api/v1/accounts/{account_id}/following", params=params or None, require_auth=False)
