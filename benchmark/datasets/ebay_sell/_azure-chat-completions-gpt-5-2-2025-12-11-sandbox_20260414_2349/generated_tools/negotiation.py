from typing import Any, Dict, Optional

from . import client as _shared
from .client import SCOPE_NEGOTIATION
from . import mcp

API = "/sell/negotiation/v1"


@mcp.tool()
def negotiation_find_eligible_items(
    *,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /find_eligible_items"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return _shared.client.request(
        "GET",
        API,
        "/find_eligible_items",
        scope=SCOPE_NEGOTIATION,
        marketplace_id=marketplace_id,
        params=params or None,
    )


@mcp.tool()
def negotiation_send_offer_to_interested_buyers(
    request: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /send_offer_to_interested_buyers"""
    return _shared.client.request(
        "POST",
        API,
        "/send_offer_to_interested_buyers",
        scope=SCOPE_NEGOTIATION,
        marketplace_id=marketplace_id,
        json=request,
    )
