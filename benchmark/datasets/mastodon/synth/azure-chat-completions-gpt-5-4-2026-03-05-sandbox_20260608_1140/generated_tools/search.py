from typing import Optional

from generated_tools.common import clean_params, mastodon_request


def search(q: str, type: Optional[str] = None, resolve: Optional[bool] = None, following: Optional[bool] = None, account_id: Optional[str] = None, exclude_unreviewed: Optional[bool] = None, max_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None):
    return mastodon_request("GET", "/api/v2/search", params=clean_params(q=q, type=type, resolve=resolve, following=following, account_id=account_id, exclude_unreviewed=exclude_unreviewed, max_id=max_id, min_id=min_id, limit=limit, offset=offset))
