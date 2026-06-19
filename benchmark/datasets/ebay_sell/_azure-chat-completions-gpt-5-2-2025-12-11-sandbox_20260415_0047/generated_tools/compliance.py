from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

API_ROOT = "/sell/compliance/v1"
SCOPE = "https://api.ebay.com/oauth/api_scope/sell.compliance"


def register(mcp):
    @mcp.tool()
    def compliance_get_listing_violations(
        marketplace_id: str,
        compliance_type: str,
        *,
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """GET /listing_violation - Get listing violations."""
        params: Dict[str, Any] = {"compliance_type": compliance_type}
        if filter is not None:
            params["filter"] = filter
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        return request_json(
            "GET",
            API_ROOT,
            "/listing_violation",
            scope=SCOPE,
            marketplace_id=marketplace_id,
            params=params,
        )

    @mcp.tool()
    def compliance_get_listing_violations_summary(marketplace_id: str, compliance_type: str) -> Dict[str, Any]:
        """GET /listing_violation_summary - Get listing violations summary."""
        return request_json(
            "GET",
            API_ROOT,
            "/listing_violation_summary",
            scope=SCOPE,
            marketplace_id=marketplace_id,
            params={"compliance_type": compliance_type},
        )
