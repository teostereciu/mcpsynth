from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import request_json


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
    params: Dict[str, Any] = {"q": q}
    if type is not None:
        params["type"] = type
    if resolve is not None:
        params["resolve"] = str(bool(resolve)).lower()
    if following is not None:
        params["following"] = str(bool(following)).lower()
    if account_id is not None:
        params["account_id"] = account_id
    if exclude_unreviewed is not None:
        params["exclude_unreviewed"] = str(bool(exclude_unreviewed)).lower()
    if max_id is not None:
        params["max_id"] = max_id
    if min_id is not None:
        params["min_id"] = min_id
    if limit is not None:
        params["limit"] = int(limit)
    if offset is not None:
        params["offset"] = int(offset)

    # Public without resolve/offset; but we can send token if present.
    require_auth = bool(resolve) or (offset is not None)
    return request_json("GET", "/api/v2/search", params=params, require_auth=require_auth)
