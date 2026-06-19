from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import MastodonClient, compact_params


def list_lists() -> Dict[str, Any]:
    """GET /api/v1/lists

    Docs: docs/api_lists.md
    """
    client = MastodonClient()
    result, meta = client.request("GET", "/api/v1/lists")
    return {"result": result, "meta": meta}


def get_list(list_id: str) -> Dict[str, Any]:
    """GET /api/v1/lists/:id

    Docs: docs/api_lists.md
    """
    client = MastodonClient()
    result, meta = client.request("GET", f"/api/v1/lists/{list_id}")
    return {"result": result, "meta": meta}


def create_list(title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Dict[str, Any]:
    """POST /api/v1/lists

    Docs: docs/api_lists.md
    """
    client = MastodonClient()
    data = compact_params(
        {
            "title": title,
            "replies_policy": replies_policy,
            "exclusive": str(bool(exclusive)).lower() if exclusive is not None else None,
        }
    )
    result, meta = client.request("POST", "/api/v1/lists", data=data)
    return {"result": result, "meta": meta}


def update_list(list_id: str, title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Dict[str, Any]:
    """PUT /api/v1/lists/:id

    Docs: docs/api_lists.md
    """
    client = MastodonClient()
    data = compact_params(
        {
            "title": title,
            "replies_policy": replies_policy,
            "exclusive": str(bool(exclusive)).lower() if exclusive is not None else None,
        }
    )
    result, meta = client.request("PUT", f"/api/v1/lists/{list_id}", data=data)
    return {"result": result, "meta": meta}


def delete_list(list_id: str) -> Dict[str, Any]:
    """DELETE /api/v1/lists/:id

    Docs: docs/api_lists.md
    """
    client = MastodonClient()
    result, meta = client.request("DELETE", f"/api/v1/lists/{list_id}")
    return {"result": result, "meta": meta}


def get_list_accounts(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /api/v1/lists/:id/accounts

    Docs: docs/api_lists.md
    """
    client = MastodonClient()
    params = compact_params({"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id})
    result, meta = client.request("GET", f"/api/v1/lists/{list_id}/accounts", params=params)
    return {"result": result, "meta": meta}


def add_accounts_to_list(list_id: str, account_ids: list[str]) -> Dict[str, Any]:
    """POST /api/v1/lists/:id/accounts

    Docs: docs/api_lists.md
    """
    client = MastodonClient()
    data: Dict[str, Any] = {}
    for i, aid in enumerate(account_ids):
        data[f"account_ids[{i}]"] = aid
    result, meta = client.request("POST", f"/api/v1/lists/{list_id}/accounts", data=data)
    return {"result": result, "meta": meta}


def remove_accounts_from_list(list_id: str, account_ids: list[str]) -> Dict[str, Any]:
    """DELETE /api/v1/lists/:id/accounts

    Docs: docs/api_lists.md
    """
    client = MastodonClient()
    data: Dict[str, Any] = {}
    for i, aid in enumerate(account_ids):
        data[f"account_ids[{i}]"] = aid
    result, meta = client.request("DELETE", f"/api/v1/lists/{list_id}/accounts", data=data)
    return {"result": result, "meta": meta}
