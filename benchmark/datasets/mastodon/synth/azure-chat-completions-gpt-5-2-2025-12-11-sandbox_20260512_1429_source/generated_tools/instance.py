from typing import Any, Optional

from .http_client import MastodonClient


def get_instance(*, client: Optional[MastodonClient] = None) -> Any:
    """GET /api/v1/instance"""
    client = client or MastodonClient()
    return client.request("GET", "/api/v1/instance")
