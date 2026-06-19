from typing import Optional

from generated_tools.common import clean_params, mastodon_request


def list_favourites(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None):
    return mastodon_request("GET", "/api/v1/favourites", params=clean_params(limit=limit, max_id=max_id, since_id=since_id, min_id=min_id))
