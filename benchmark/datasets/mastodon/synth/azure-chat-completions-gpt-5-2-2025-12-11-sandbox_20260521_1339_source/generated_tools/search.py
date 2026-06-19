from typing import Any, Optional

from .client import MastodonClient


def search_v2(
    client: MastodonClient,
    q: str,
    *,
    type: Optional[str] = None,
    offset: Optional[int] = None,
    min_id: Optional[str] = None,
    max_id: Optional[str] = None,
    account_id: Optional[str] = None,
    resolve: Optional[bool] = None,
    exclude_unreviewed: Optional[bool] = None,
    following: Optional[bool] = None,
) -> Any:
    return client.request(
        "GET",
        "/api/v2/search",
        params={
            "q": q,
            "type": type,
            "offset": offset,
            "min_id": min_id,
            "max_id": max_id,
            "account_id": account_id,
            "resolve": resolve,
            "exclude_unreviewed": exclude_unreviewed,
            "following": following,
        },
    )
