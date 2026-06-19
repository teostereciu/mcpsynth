"""Stripe Tax tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import stripe_request


@mcp.tool()
def tax_rates_create(
    *,
    display_name: str,
    percentage: float,
    inclusive: bool,
    country: Optional[str] = None,
    jurisdiction: Optional[str] = None,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    state: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a tax rate (/v1/tax_rates)."""

    data: Dict[str, Any] = {
        "display_name": display_name,
        "percentage": percentage,
        "inclusive": inclusive,
    }
    if country is not None:
        data["country"] = country
    if jurisdiction is not None:
        data["jurisdiction"] = jurisdiction
    if description is not None:
        data["description"] = description
    if active is not None:
        data["active"] = active
    if metadata is not None:
        data["metadata"] = metadata
    if state is not None:
        data["state"] = state
    return stripe_request("POST", "/v1/tax_rates", data=data)


@mcp.tool()
def tax_calculations_create(
    *,
    currency: str,
    line_items: list[Dict[str, Any]],
    customer_details: Optional[Dict[str, Any]] = None,
    customer: Optional[str] = None,
    shipping_cost: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a Tax Calculation (/v1/tax/calculations)."""

    data: Dict[str, Any] = {"currency": currency, "line_items": line_items}
    if customer_details is not None:
        data["customer_details"] = customer_details
    if customer is not None:
        data["customer"] = customer
    if shipping_cost is not None:
        data["shipping_cost"] = shipping_cost
    return stripe_request("POST", "/v1/tax/calculations", data=data)
