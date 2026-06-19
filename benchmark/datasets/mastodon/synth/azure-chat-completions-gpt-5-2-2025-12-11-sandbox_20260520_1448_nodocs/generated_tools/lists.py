from typing import Any, Dict, Optional

from .client import MastodonClient


def list_lists() -> Any:
    """GET /api/v1/lists"""
    client = MastodonClient()
    return client.request("GET", "/api/v1/lists")


def get_list(list_id: str) -> Any:
    """GET /api/v1/lists/{id}"""
    client = MastodonClient()
    return client.request("GET", f"/api/v1/lists/{list_id}")


def create_list(title: str, *, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    """POST /api/v1/lists"""
    client = MastodonClient()
    payload: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        payload["replies_policy"] = replies_policy
    if exclusive is not None:
        payload["exclusive"] = exclusive
    return client.request("POST", "/api/v1/lists", json=payload)


def update_list(list_id: str, *, title: Optional[str] = None, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    """PUT /api/v1/lists/{id}"""
    client = MastodonClient()
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if replies_policy is not None:
        payload["replies_policy"] = replies_policy
    if exclusive is not None:
        payload["exclusive"] = exclusive
    return client.request("PUT", f"/api/v1/lists/{list_id}", json=payload)


def delete_list(list_id: str) -> Any:
    """DELETE /api/v1/lists/{id}"""
    client = MastodonClient()
    return client.request("DELETE", f"/api/v1/lists/{list_id}")


def add_accounts_to_list(list_id: str, account_ids: list) -> Any:
    """POST /api/v1/lists/{id}/accounts"""
    client = MastodonClient()
    payload = {"account_ids": account_ids}
    return client.request("POST", f"/api/v1/lists/{list_id}/accounts", json=payload)


def remove_accounts_from_list(list_id: str, account_ids: list) -> Any:
    """DELETE /api/v1/lists/{id}/accounts"""
    client = MastodonClient()
    params = {"account_ids": account_ids}
    return client.request("DELETE", f"/api/v1/lists/{list_id}/accounts", params=params)


def get_list_accounts(list_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    """GET /api/v1/lists/{id}/accounts"""
    client = MastodonClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", f"/api/v1/lists/{list_id}/accounts", params=params)
