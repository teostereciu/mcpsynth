from typing import Any, Dict, Optional

from .client import MastodonClient


def search_v2(
    client: MastodonClient,
    q: str,
    *,
    type: Optional[str] = None,
    resolve: Optional[bool] = None,
    following: Optional[bool] = None,
    account_id: Optional[str] = None,
    offset: Optional[int] = None,
    min_id: Optional[str] = None,
    max_id: Optional[str] = None,
    exclude_unreviewed: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {"q": q}
    if type is not None:
        params["type"] = type
    if resolve is not None:
        params["resolve"] = "true" if resolve else "false"
    if following is not None:
        params["following"] = "true" if following else "false"
    if account_id is not None:
        params["account_id"] = account_id
    if offset is not None:
        params["offset"] = offset
    if min_id is not None:
        params["min_id"] = min_id
    if max_id is not None:
        params["max_id"] = max_id
    if exclude_unreviewed is not None:
        params["exclude_unreviewed"] = "true" if exclude_unreviewed else "false"

    return client.request("GET", "/api/v2/search", params=params)
