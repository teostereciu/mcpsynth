"""Stripe Radar tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import stripe_request


@mcp.tool()
def radar_value_lists_create(
    *,
    alias: str,
    name: str,
    item_type: str = "string",
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a Radar value list (/v1/radar/value_lists)."""

    data: Dict[str, Any] = {"alias": alias, "name": name, "item_type": item_type}
    if metadata is not None:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/radar/value_lists", data=data)
