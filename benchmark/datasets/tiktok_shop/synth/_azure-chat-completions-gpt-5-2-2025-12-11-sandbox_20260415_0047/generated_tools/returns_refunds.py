from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import tiktok_request


@mcp.tool()
def returns_search_returns(status: Optional[str] = None, page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Search returns/refunds.

    API: POST /return_refund/202602/returns/search
    """

    body: Dict[str, Any] = {"page_size": page_size}
    if status:
        body["status"] = status
    if page_token:
        body["page_token"] = page_token
    return tiktok_request("POST", "/return_refund/202602/returns/search", body=body)


@mcp.tool()
def cancellations_search(status: Optional[str] = None, page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Search cancellation requests.

    API: POST /return_refund/202602/cancellations/search
    """

    body: Dict[str, Any] = {"page_size": page_size}
    if status:
        body["status"] = status
    if page_token:
        body["page_token"] = page_token
    return tiktok_request("POST", "/return_refund/202602/cancellations/search", body=body)
