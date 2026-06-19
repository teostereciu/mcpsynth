from typing import Any, Dict, Optional

from ._client import request_json


def list_lists() -> Any:
    return request_json("GET", "/api/v1/lists")


def get_list(list_id: str) -> Any:
    return request_json("GET", f"/api/v1/lists/{list_id}")


def create_list(title: str, *, replies_policy: Optional[str] = None) -> Any:
    data: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        data["replies_policy"] = replies_policy
    return request_json("POST", "/api/v1/lists", data=data)


def update_list(list_id: str, *, title: Optional[str] = None, replies_policy: Optional[str] = None) -> Any:
    data: Dict[str, Any] = {}
    if title is not None:
        data["title"] = title
    if replies_policy is not None:
        data["replies_policy"] = replies_policy
    return request_json("PUT", f"/api/v1/lists/{list_id}", data=data or None)


def delete_list(list_id: str) -> Any:
    return request_json("DELETE", f"/api/v1/lists/{list_id}")


def add_accounts_to_list(list_id: str, account_ids: list[str]) -> Any:
    return request_json("POST", f"/api/v1/lists/{list_id}/accounts", data={"account_ids": account_ids})


def remove_accounts_from_list(list_id: str, account_ids: list[str]) -> Any:
    return request_json("DELETE", f"/api/v1/lists/{list_id}/accounts", data={"account_ids": account_ids})


def get_list_accounts(list_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/api/v1/lists/{list_id}/accounts", params=params or None)
