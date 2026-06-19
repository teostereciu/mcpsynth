from typing import Any, Dict, Optional

from .http_client import MastodonClient


def home_timeline(*, params: Optional[Dict[str, Any]] = None, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/timelines/home"""
    client = client or MastodonClient()
    return client.request("GET", "/api/v1/timelines/home", params=params)


def public_timeline(*, params: Optional[Dict[str, Any]] = None, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/timelines/public"""
    client = client or MastodonClient()
    return client.request("GET", "/api/v1/timelines/public", params=params)


def hashtag_timeline(*, hashtag: str, params: Optional[Dict[str, Any]] = None, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/timelines/tag/:hashtag"""
    client = client or MastodonClient()
    return client.request("GET", f"/api/v1/timelines/tag/{hashtag}", params=params)


def list_timeline(*, list_id: str, params: Optional[Dict[str, Any]] = None, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/timelines/list/:list_id"""
    client = client or MastodonClient()
    return client.request("GET", f"/api/v1/timelines/list/{list_id}", params=params)
