from typing import Any, Dict, List, Optional

from ._client import request_json


def list_lists() -> Any:
    return request_json("GET", "/api/v1/lists")


def get_list(list_id: str) -> Any:
    return request_json("GET", f"/api/v1/lists/{list_id}")


def create_list(title: str, *, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    data: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        data["replies_policy"] = replies_policy
    if exclusive is not None:
        data["exclusive"] = "true" if exclusive else "false"
    return request_json("POST", "/api/v1/lists", data=data)


def update_list(list_id: str, title: str, *, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    data: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        data["replies_policy"] = replies_policy
    if exclusive is not None:
        data["exclusive"] = "true" if exclusive else "false"
    return request_json("PUT", f"/api/v1/lists/{list_id}", data=data)


def delete_list(list_id: str) -> Any:
    return request_json("DELETE", f"/api/v1/lists/{list_id}")


def get_list_accounts(list_id: str, *, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if limit is not None:
        params["limit"] = str(limit)
    return request_json("GET", f"/api/v1/lists/{list_id}/accounts", params=params)


def add_accounts_to_list(list_id: str, account_ids: List[str]) -> Any:
    data: Dict[str, Any] = {}
    for i, aid in enumerate(account_ids):
        data[f"account_ids[{i}]"] = aid
    return request_json("POST", f"/api/v1/lists/{list_id}/accounts", data=data)


def remove_accounts_from_list(list_id: str, account_ids: List[str]) -> Any:
    data: Dict[str, Any] = {}
    for i, aid in enumerate(account_ids):
        data[f"account_ids[{i}]"] = aid
    return request_json("DELETE", f"/api/v1/lists/{list_id}/accounts", data=data)
