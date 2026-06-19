from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http_client import request_json


def list_lists() -> Dict[str, Any]:
    return request_json("GET", "/api/v1/lists", require_auth=True)


def get_list(list_id: str) -> Dict[str, Any]:
    return request_json("GET", f"/api/v1/lists/{list_id}", require_auth=True)


def create_list(title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Dict[str, Any]:
    data: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        data["replies_policy"] = replies_policy
    if exclusive is not None:
        data["exclusive"] = str(bool(exclusive)).lower()
    return request_json("POST", "/api/v1/lists", data=data, require_auth=True)


def update_list(list_id: str, title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Dict[str, Any]:
    data: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        data["replies_policy"] = replies_policy
    if exclusive is not None:
        data["exclusive"] = str(bool(exclusive)).lower()
    return request_json("PUT", f"/api/v1/lists/{list_id}", data=data, require_auth=True)


def delete_list(list_id: str) -> Dict[str, Any]:
    return request_json("DELETE", f"/api/v1/lists/{list_id}", require_auth=True)


def get_list_accounts(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    return request_json("GET", f"/api/v1/lists/{list_id}/accounts", params=params or None, require_auth=True)


def add_accounts_to_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    data: Dict[str, Any] = {"account_ids[]": account_ids}
    return request_json("POST", f"/api/v1/lists/{list_id}/accounts", data=data, require_auth=True)


def remove_accounts_from_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    data: Dict[str, Any] = {"account_ids[]": account_ids}
    return request_json("DELETE", f"/api/v1/lists/{list_id}/accounts", data=data, require_auth=True)
