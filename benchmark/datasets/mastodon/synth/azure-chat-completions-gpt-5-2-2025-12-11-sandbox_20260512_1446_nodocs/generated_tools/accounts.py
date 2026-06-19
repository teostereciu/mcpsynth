from typing import Any, Dict, Optional

from ._client import request_json


def verify_credentials() -> Any:
    return request_json("GET", "/api/v1/accounts/verify_credentials")


def get_account(account_id: str) -> Any:
    return request_json("GET", f"/api/v1/accounts/{account_id}")


def follow_account(account_id: str, *, reblogs: Optional[bool] = None, notify: Optional[bool] = None) -> Any:
    data: Dict[str, Any] = {}
    if reblogs is not None:
        data["reblogs"] = reblogs
    if notify is not None:
        data["notify"] = notify
    return request_json("POST", f"/api/v1/accounts/{account_id}/follow", data=data or None)


def unfollow_account(account_id: str) -> Any:
    return request_json("POST", f"/api/v1/accounts/{account_id}/unfollow")


def get_followers(account_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    return request_json("GET", f"/api/v1/accounts/{account_id}/followers", params=params or None)


def get_following(account_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    return request_json("GET", f"/api/v1/accounts/{account_id}/following", params=params or None)
