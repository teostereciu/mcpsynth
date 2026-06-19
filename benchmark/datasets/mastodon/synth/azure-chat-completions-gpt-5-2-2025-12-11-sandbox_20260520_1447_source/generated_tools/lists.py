from typing import Any, Dict, Optional

from .client import MastodonClient


def lists_list(client: MastodonClient) -> Any:
    return client.request("GET", "/api/v1/lists")


def lists_get(client: MastodonClient, list_id: str) -> Any:
    return client.request("GET", f"/api/v1/lists/{list_id}")


def lists_create(client: MastodonClient, title: str, *, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {"title": title}
    if replies_policy is not None:
        payload["replies_policy"] = replies_policy
    if exclusive is not None:
        payload["exclusive"] = exclusive
    return client.request("POST", "/api/v1/lists", json=payload)


def lists_update(client: MastodonClient, list_id: str, *, title: Optional[str] = None, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if replies_policy is not None:
        payload["replies_policy"] = replies_policy
    if exclusive is not None:
        payload["exclusive"] = exclusive
    return client.request("PUT", f"/api/v1/lists/{list_id}", json=payload)


def lists_delete(client: MastodonClient, list_id: str) -> Any:
    return client.request("DELETE", f"/api/v1/lists/{list_id}")


def lists_accounts_get(client: MastodonClient, list_id: str) -> Any:
    return client.request("GET", f"/api/v1/lists/{list_id}/accounts")


def lists_accounts_add(client: MastodonClient, list_id: str, account_ids: list[str]) -> Any:
    return client.request("POST", f"/api/v1/lists/{list_id}/accounts", json={"account_ids": account_ids})


def lists_accounts_remove(client: MastodonClient, list_id: str, account_ids: list[str]) -> Any:
    # Mastodon expects account_ids in body for DELETE as form-encoded; JSON works on many instances but not guaranteed.
    return client.request("DELETE", f"/api/v1/lists/{list_id}/accounts", params={"account_ids": account_ids})
