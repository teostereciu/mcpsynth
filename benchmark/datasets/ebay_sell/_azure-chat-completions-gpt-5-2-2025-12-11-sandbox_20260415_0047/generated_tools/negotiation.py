from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

API_ROOT = "/sell/negotiation/v1"
SCOPE = "https://api.ebay.com/oauth/api_scope/sell.negotiation"


def register(mcp):
    @mcp.tool()
    def negotiation_find_eligible_items(
        marketplace_id: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """GET /find_eligible_items - Find eligible items."""
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        return request_json(
            "GET",
            API_ROOT,
            "/find_eligible_items",
            scope=SCOPE,
            marketplace_id=marketplace_id,
            params=params or None,
        )

    @mcp.tool()
    def negotiation_send_offer_to_interested_buyers(marketplace_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /send_offer_to_interested_buyers - Send offers to interested buyers."""
        return request_json(
            "POST",
            API_ROOT,
            "/send_offer_to_interested_buyers",
            scope=SCOPE,
            marketplace_id=marketplace_id,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )
