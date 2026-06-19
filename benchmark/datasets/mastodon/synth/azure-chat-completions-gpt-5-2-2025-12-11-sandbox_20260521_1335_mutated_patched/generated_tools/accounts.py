from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import MastodonClient, compact_params


def verify_account_credentials() -> Dict[str, Any]:
    """GET /api/v1/accounts/verify_credentials

    Docs: docs/api_accounts.md
    """
    client = MastodonClient()
    result, meta = client.request("GET", "/api/v1/accounts/verify_credentials")
    return {"result": result, "meta": meta}


def get_account(account_id: str) -> Dict[str, Any]:
    """GET /api/v1/accounts/:id

    Docs: docs/api_accounts.md
    """
    client = MastodonClient()
    result, meta = client.request("GET", f"/api/v1/accounts/{account_id}")
    return {"result": result, "meta": meta}


def follow_account(account_id: str, reblogs: Optional[bool] = None, notify: Optional[bool] = None, languages: Optional[list[str]] = None) -> Dict[str, Any]:
    """POST /api/v1/accounts/:id/follow

    Docs: docs/api_accounts.md
    """
    client = MastodonClient()
    data: Dict[str, Any] = {}
    if reblogs is not None:
        data["reblogs"] = str(bool(reblogs)).lower()
    if notify is not None:
        data["notify"] = str(bool(notify)).lower()
    if languages is not None:
        for i, lang in enumerate(languages):
            data[f"languages[{i}]"] = lang
    result, meta = client.request("POST", f"/api/v1/accounts/{account_id}/follow", data=data)
    return {"result": result, "meta": meta}


def unfollow_account(account_id: str) -> Dict[str, Any]:
    """POST /api/v1/accounts/:id/unfollow

    Docs: docs/api_accounts.md
    """
    client = MastodonClient()
    result, meta = client.request("POST", f"/api/v1/accounts/{account_id}/unfollow")
    return {"result": result, "meta": meta}


def get_account_followers(account_id: str, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v1/accounts/:id/followers

    Docs: docs/api_accounts.md
    """
    client = MastodonClient()
    params = compact_params({"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit})
    result, meta = client.request("GET", f"/api/v1/accounts/{account_id}/followers", params=params)
    return {"result": result, "meta": meta}


def get_account_following(account_id: str, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v1/accounts/:id/following

    Docs: docs/api_accounts.md
    """
    client = MastodonClient()
    params = compact_params({"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit})
    result, meta = client.request("GET", f"/api/v1/accounts/{account_id}/following", params=params)
    return {"result": result, "meta": meta}
