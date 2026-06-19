from typing import Any, Dict, Optional

from . import client as _shared
from .client import SCOPE_COMPLIANCE
from . import mcp

API = "/sell/compliance/v1"


@mcp.tool()
def compliance_get_listing_violations(
    compliance_type: str,
    *,
    marketplace_id: str = "EBAY_US",
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    filter: Optional[str] = None,
) -> Any:
    """GET /listing_violation"""
    params: Dict[str, Any] = {"compliance_type": compliance_type}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if filter is not None:
        params["filter"] = filter
    return _shared.client.request(
        "GET",
        API,
        "/listing_violation",
        scope=SCOPE_COMPLIANCE,
        marketplace_id=marketplace_id,
        params=params,
    )


@mcp.tool()
def compliance_get_listing_violations_summary(
    compliance_type: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /listing_violation_summary"""
    return _shared.client.request(
        "GET",
        API,
        "/listing_violation_summary",
        scope=SCOPE_COMPLIANCE,
        marketplace_id=marketplace_id,
        params={"compliance_type": compliance_type},
    )
