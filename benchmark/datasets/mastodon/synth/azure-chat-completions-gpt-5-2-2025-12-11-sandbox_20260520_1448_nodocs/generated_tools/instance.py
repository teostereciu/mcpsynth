from typing import Any

from .client import MastodonClient


def get_instance() -> Any:
    """GET /api/v2/instance"""
    client = MastodonClient()
    return client.request("GET", "/api/v2/instance")
