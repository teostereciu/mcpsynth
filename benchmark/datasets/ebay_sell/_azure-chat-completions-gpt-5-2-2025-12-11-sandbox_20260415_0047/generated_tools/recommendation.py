from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

API_ROOT = "/sell/recommendation/v1"
SCOPE = "https://api.ebay.com/oauth/api_scope/sell.recommendation"


def register(mcp):
    @mcp.tool()
    def recommendation_find_listing_recommendations(
        marketplace_id: str,
        *,
        payload: Optional[Dict[str, Any]] = None,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """POST /find - Find listing recommendations."""
        params: Dict[str, Any] = {}
        if filter is not None:
            params["filter"] = filter
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        return request_json(
            "POST",
            API_ROOT,
            "/find",
            scope=SCOPE,
            marketplace_id=marketplace_id,
            headers={"Content-Type": "application/json"},
            params=params or None,
            json_body=payload or {},
        )
