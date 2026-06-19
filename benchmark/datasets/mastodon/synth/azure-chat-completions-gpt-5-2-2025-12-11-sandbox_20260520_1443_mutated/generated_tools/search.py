from typing import Any, Dict, Optional

from .http import request_json


# Docs: docs/api_search.md


def search(
    q: str,
    *,
    type: Optional[str] = None,
    resolve: Optional[bool] = None,
    following: Optional[bool] = None,
    account_id: Optional[str] = None,
    exclude_unreviewed: Optional[bool] = None,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Any:
    """GET /api/v2/search"""
    params: Dict[str, Any] = {"q": q}
    for k, v in {
        "type": type,
        "resolve": resolve,
        "following": following,
        "account_id": account_id,
        "exclude_unreviewed": exclude_unreviewed,
        "max_id": max_id,
        "min_id": min_id,
        "limit": limit,
        "offset": offset,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/api/v2/search", params=params)
