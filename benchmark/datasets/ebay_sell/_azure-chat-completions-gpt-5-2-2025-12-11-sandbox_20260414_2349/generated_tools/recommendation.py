from typing import Any, Dict, Optional

from . import client as _shared
from .client import SCOPE_RECOMMENDATION
from . import mcp

API = "/sell/recommendation/v1"


@mcp.tool()
def recommendation_find_listing_recommendations(
    *,
    request: Optional[Dict[str, Any]] = None,
    filter: str = "recommendationTypes:{AD}",
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /find"""
    params: Dict[str, Any] = {"filter": filter}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return _shared.client.request(
        "POST",
        API,
        "/find",
        scope=SCOPE_RECOMMENDATION,
        marketplace_id=marketplace_id,
        params=params,
        json=request or {},
    )
