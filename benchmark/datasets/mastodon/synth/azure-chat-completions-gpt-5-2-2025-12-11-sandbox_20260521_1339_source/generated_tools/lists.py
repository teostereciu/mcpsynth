from typing import Any, Dict, List, Optional

from .client import MastodonClient


def lists_list(client: MastodonClient) -> Any:
    return client.request("GET", "/api/v1/lists")


def lists_get(client: MastodonClient, list_id: str) -> Any:
    return client.request("GET", f"/api/v1/lists/{list_id}")


def lists_create(client: MastodonClient, title: str, *, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {"title": title, "replies_policy": replies_policy, "exclusive": exclusive}
    return client.request("POST", "/api/v1/lists", json=payload)


def lists_update(client: MastodonClient, list_id: str, *, title: Optional[str] = None, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {"title": title, "replies_policy": replies_policy, "exclusive": exclusive}
    return client.request("PUT", f"/api/v1/lists/{list_id}", json=payload)


def lists_delete(client: MastodonClient, list_id: str) -> Any:
    return client.request("DELETE", f"/api/v1/lists/{list_id}")


def lists_accounts_list(client: MastodonClient, list_id: str, *, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    return client.request(
        "GET",
        f"/api/v1/lists/{list_id}/accounts",
        params={"limit": limit, "max_id": max_id, "since_id": since_id},
    )


def lists_accounts_add(client: MastodonClient, list_id: str, account_ids: List[str]) -> Any:
    return client.request("POST", f"/api/v1/lists/{list_id}/accounts", json={"account_ids": account_ids})


def lists_accounts_remove(client: MastodonClient, list_id: str, account_ids: List[str]) -> Any:
    return client.request("DELETE", f"/api/v1/lists/{list_id}/accounts", json={"account_ids": account_ids})
