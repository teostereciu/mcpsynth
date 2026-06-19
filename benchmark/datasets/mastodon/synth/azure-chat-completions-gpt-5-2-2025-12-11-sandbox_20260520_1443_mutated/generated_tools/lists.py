from typing import Any, Dict, Optional

from .http import request_json


# Docs: docs/api_lists.md


def list_lists() -> Any:
    """GET /api/v1/lists"""
    return request_json("GET", "/api/v1/lists")


def get_list(list_id: str) -> Any:
    """GET /api/v1/lists/:id"""
    return request_json("GET", f"/api/v1/lists/{list_id}")


def create_list(title: str, *, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    """POST /api/v1/lists"""
    data: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        data["replies_policy"] = replies_policy
    if exclusive is not None:
        data["exclusive"] = str(exclusive).lower()
    return request_json("POST", "/api/v1/lists", data=data)


def update_list(list_id: str, title: str, *, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    """PUT /api/v1/lists/:id"""
    data: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        data["replies_policy"] = replies_policy
    if exclusive is not None:
        data["exclusive"] = str(exclusive).lower()
    return request_json("PUT", f"/api/v1/lists/{list_id}", data=data)


def delete_list(list_id: str) -> Any:
    """DELETE /api/v1/lists/:id"""
    return request_json("DELETE", f"/api/v1/lists/{list_id}")


def get_list_accounts(
    list_id: str,
    *,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    """GET /api/v1/lists/:id/accounts"""
    params: Dict[str, Any] = {}
    for k, v in {"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/api/v1/lists/{list_id}/accounts", params=params)


def add_accounts_to_list(list_id: str, account_ids: list[str]) -> Any:
    """POST /api/v1/lists/:id/accounts"""
    data: Dict[str, Any] = {}
    for i, aid in enumerate(account_ids):
        data[f"account_ids[{i}]"] = aid
    return request_json("POST", f"/api/v1/lists/{list_id}/accounts", data=data)


def remove_accounts_from_list(list_id: str, account_ids: list[str]) -> Any:
    """DELETE /api/v1/lists/:id/accounts"""
    data: Dict[str, Any] = {}
    for i, aid in enumerate(account_ids):
        data[f"account_ids[{i}]"] = aid
    return request_json("DELETE", f"/api/v1/lists/{list_id}/accounts", data=data)
