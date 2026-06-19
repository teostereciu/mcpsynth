from typing import Any, Dict, Optional

from .http_client import MastodonClient


def list_lists(*, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/lists"""
    client = client or MastodonClient()
    return client.request("GET", "/api/v1/lists")


def create_list(*, title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None, client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/lists"""
    client = client or MastodonClient()
    payload: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        payload["replies_policy"] = replies_policy
    if exclusive is not None:
        payload["exclusive"] = exclusive
    return client.request("POST", "/api/v1/lists", json=payload)


def get_list(*, list_id: str, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/lists/:id"""
    client = client or MastodonClient()
    return client.request("GET", f"/api/v1/lists/{list_id}")


def update_list(*, list_id: str, params: Dict[str, Any], client: Optional[MastodonClient] = None) -> Any:
    """PUT /api/v1/lists/:id"""
    client = client or MastodonClient()
    return client.request("PUT", f"/api/v1/lists/{list_id}", json=params)


def delete_list(*, list_id: str, client: Optional[MastodonClient] = None) -> Any:
    """DELETE /api/v1/lists/:id"""
    client = client or MastodonClient()
    return client.request("DELETE", f"/api/v1/lists/{list_id}")


def get_list_accounts(*, list_id: str, params: Optional[Dict[str, Any]] = None, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/lists/:id/accounts"""
    client = client or MastodonClient()
    return client.request("GET", f"/api/v1/lists/{list_id}/accounts", params=params)


def add_list_accounts(*, list_id: str, account_ids: list[str], client: Optional[MastodonClient] = None) -> Any:
    """POST /api/v1/lists/:id/accounts"""
    client = client or MastodonClient()
    return client.request("POST", f"/api/v1/lists/{list_id}/accounts", json={"account_ids": account_ids})


def remove_list_accounts(*, list_id: str, account_ids: list[str], client: Optional[MastodonClient] = None) -> Any:
    """DELETE /api/v1/lists/:id/accounts"""
    client = client or MastodonClient()
    return client.request("DELETE", f"/api/v1/lists/{list_id}/accounts", json={"account_ids": account_ids})
