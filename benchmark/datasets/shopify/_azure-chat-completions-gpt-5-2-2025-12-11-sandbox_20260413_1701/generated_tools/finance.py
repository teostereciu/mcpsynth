from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp, client


@mcp.tool()
def list_payouts(limit: int = 50, since_id: Optional[Union[int, str]] = None) -> List[Dict[str, Any]]:
    """List payouts (Shopify Payments)."""
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", "/shopify_payments/payouts.json", params=params)


@mcp.tool()
def list_disputes(limit: int = 50) -> List[Dict[str, Any]]:
    """List disputes (Shopify Payments)."""
    return client.request("GET", "/shopify_payments/disputes.json", params={"limit": limit})
