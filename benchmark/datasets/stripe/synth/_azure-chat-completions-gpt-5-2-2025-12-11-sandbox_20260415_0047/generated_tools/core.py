"""Core generic Stripe tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import stripe_request


@mcp.tool()
def stripe_request_raw(
    method: str,
    path: str,
    query: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    api_key: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """Call an arbitrary Stripe API endpoint.

    Args:
      method: HTTP method (GET/POST/DELETE)
      path: Full path starting with /v1 (e.g., /v1/customers)
      query: Query parameters
      data: Form body parameters (nested dict/list supported)
      api_key: Optional override API key
      idempotency_key: Optional idempotency key
      stripe_account: Optional Connect account header
    """

    if not path.startswith("/"):
        path = "/" + path
    return stripe_request(
        method,
        path,
        query=query,
        data=data,
        api_key=api_key,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )
