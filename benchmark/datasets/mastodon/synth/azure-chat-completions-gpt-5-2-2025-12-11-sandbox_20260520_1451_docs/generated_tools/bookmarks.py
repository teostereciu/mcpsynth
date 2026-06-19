from typing import Any, Dict, Optional

from ._client import request_json


def list_bookmarks(*, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if limit is not None:
        params["limit"] = str(limit)
    return request_json("GET", "/api/v1/bookmarks", params=params)
