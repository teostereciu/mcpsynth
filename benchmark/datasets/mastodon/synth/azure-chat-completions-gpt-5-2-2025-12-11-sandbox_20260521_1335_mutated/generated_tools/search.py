from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import MastodonClient, compact_params


def search(
    q: str,
    type: Optional[str] = None,
    resolve: Optional[bool] = None,
    following: Optional[bool] = None,
    account_id: Optional[str] = None,
    exclude_unreviewed: Optional[bool] = None,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /api/v2/search

    Docs: docs/api_search.md
    """
    client = MastodonClient()
    params = compact_params(
        {
            "q": q,
            "type": type,
            "resolve": str(bool(resolve)).lower() if resolve is not None else None,
            "following": str(bool(following)).lower() if following is not None else None,
            "account_id": account_id,
            "exclude_unreviewed": str(bool(exclude_unreviewed)).lower() if exclude_unreviewed is not None else None,
            "max_id": max_id,
            "min_id": min_id,
            "limit": limit,
            "offset": offset,
        }
    )
    result, meta = client.request("GET", "/api/v2/search", params=params)
    return {"result": result, "meta": meta}
