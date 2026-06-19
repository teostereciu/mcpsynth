"""Stripe Financial Connections tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import stripe_request


@mcp.tool()
def financial_connections_sessions_create(
    *,
    customer: str,
    permissions: list[str],
    filters: Optional[Dict[str, Any]] = None,
    prefetch: Optional[list[str]] = None,
    return_url: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a Financial Connections session (/v1/financial_connections/sessions)."""

    data: Dict[str, Any] = {
        "account_holder": {"type": "customer", "customer": customer},
        "permissions": permissions,
    }
    if filters is not None:
        data["filters"] = filters
    if prefetch is not None:
        data["prefetch"] = prefetch
    if return_url is not None:
        data["return_url"] = return_url
    return stripe_request("POST", "/v1/financial_connections/sessions", data=data)
