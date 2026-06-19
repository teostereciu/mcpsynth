from typing import Any, Dict, Optional

from ._client import request_json


def search(
    q: str,
    *,
    type: Optional[str] = None,
    resolve: Optional[bool] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    following: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {"q": q}
    for k, v in {"type": type, "resolve": resolve, "limit": limit, "offset": offset, "following": following}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/api/v2/search", params=params)
