"""Balance and balance transactions."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import stripe_request


@mcp.tool()
def balance_retrieve() -> Dict[str, Any]:
    """Retrieve account balance (/v1/balance)."""

    return stripe_request("GET", "/v1/balance")


@mcp.tool()
def balance_transactions_list(*, limit: int = 10, type: Optional[str] = None) -> Dict[str, Any]:
    """List balance transactions (/v1/balance_transactions)."""

    query: Dict[str, Any] = {"limit": limit}
    if type is not None:
        query["type"] = type
    return stripe_request("GET", "/v1/balance_transactions", query=query)
