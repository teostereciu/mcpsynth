from typing import Any, Dict, List, Optional

from ._client import request_json


def verify_account_credentials() -> Any:
    return request_json("GET", "/api/v1/accounts/verify_credentials")


def get_account(account_id: str) -> Any:
    return request_json("GET", f"/api/v1/accounts/{account_id}")


def follow_account(account_id: str, *, reblogs: Optional[bool] = None, notify: Optional[bool] = None, languages: Optional[List[str]] = None) -> Any:
    data: Dict[str, Any] = {}
    if reblogs is not None:
        data["reblogs"] = "true" if reblogs else "false"
    if notify is not None:
        data["notify"] = "true" if notify else "false"
    if languages:
        for i, lang in enumerate(languages):
            data[f"languages[{i}]"] = lang
    return request_json("POST", f"/api/v1/accounts/{account_id}/follow", data=data)


def unfollow_account(account_id: str) -> Any:
    return request_json("POST", f"/api/v1/accounts/{account_id}/unfollow")


def get_account_followers(account_id: str, *, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if limit is not None:
        params["limit"] = str(limit)
    return request_json("GET", f"/api/v1/accounts/{account_id}/followers", params=params)


def get_account_following(account_id: str, *, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if limit is not None:
        params["limit"] = str(limit)
    return request_json("GET", f"/api/v1/accounts/{account_id}/following", params=params)
