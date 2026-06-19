from typing import Any, Optional

from .mastodon_client import MastodonClient

client = MastodonClient()


def get_notifications(max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None, types: Optional[list[str]] = None, exclude_types: Optional[list[str]] = None, account_id: Optional[str] = None, include_filtered: Optional[bool] = None) -> Any:
    params: dict[str, Any] = {"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit, "account_id": account_id, "include_filtered": include_filtered}
    for i, v in enumerate(types or []): params[f"types[{i}]"] = v
    for i, v in enumerate(exclude_types or []): params[f"exclude_types[{i}]"] = v
    return client.request("GET", "/notifications", params={k: v for k, v in params.items() if v is not None})
