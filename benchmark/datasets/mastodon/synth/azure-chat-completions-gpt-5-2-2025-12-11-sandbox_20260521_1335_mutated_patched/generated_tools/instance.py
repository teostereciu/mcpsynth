from __future__ import annotations

from typing import Any, Dict

from .http_client import MastodonClient


def get_instance() -> Dict[str, Any]:
    """GET /api/v2/instance

    Docs: docs/api_instance.md
    """
    client = MastodonClient()
    result, meta = client.request("GET", "/api/v2/instance")
    return {"result": result, "meta": meta}
