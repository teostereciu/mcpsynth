from typing import Any, Dict, Optional

from .http_client import MastodonClient


def search_v2(*, q: str, params: Optional[Dict[str, Any]] = None, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v2/search"""
    client = client or MastodonClient()
    p = dict(params or {})
    p["q"] = q
    return client.request("GET", "/api/v2/search", params=p)
