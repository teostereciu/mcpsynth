from typing import Any, Dict, Optional

from .client import MastodonClient


def search(client: MastodonClient, q: str, resolve: Optional[bool] = None, limit: Optional[int] = None, offset: Optional[int] = None, following: Optional[bool] = None, type: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"q": q}
    for k, v in {"resolve": resolve, "limit": limit, "offset": offset, "following": following, "type": type}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/api/v2/search", params=params)
