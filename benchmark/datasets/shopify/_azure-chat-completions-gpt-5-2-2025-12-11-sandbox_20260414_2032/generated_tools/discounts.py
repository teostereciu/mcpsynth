from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import shopify_request, unwrap_envelope


# Price Rules
@mcp.tool()
def create_price_rule(price_rule: Dict[str, Any]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Create a price rule."""

    data = shopify_request("POST", "/price_rules.json", body={"price_rule": price_rule})
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def list_price_rules(limit: int = 50, fields: Optional[str] = None) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List price rules."""

    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields

    data = shopify_request("GET", "/price_rules.json", params=params)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def get_price_rule(price_rule_id: Union[int, str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Get a price rule."""

    data = shopify_request("GET", f"/price_rules/{price_rule_id}.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def update_price_rule(price_rule_id: Union[int, str], price_rule: Dict[str, Any]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Update a price rule."""

    payload = dict(price_rule)
    payload["id"] = int(price_rule_id) if str(price_rule_id).isdigit() else price_rule_id
    data = shopify_request("PUT", f"/price_rules/{price_rule_id}.json", body={"price_rule": payload})
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def delete_price_rule(price_rule_id: Union[int, str]) -> Dict[str, Any]:
    """Delete a price rule."""

    data = shopify_request("DELETE", f"/price_rules/{price_rule_id}.json")
    if "error" in data:
        return data
    return {"ok": True}


@mcp.tool()
def count_price_rules() -> Union[int, Dict[str, Any]]:
    """Count price rules."""

    data = shopify_request("GET", "/price_rules/count.json")
    if "error" in data:
        return data
    unwrapped = unwrap_envelope(data)
    if isinstance(unwrapped, dict) and "count" in unwrapped:
        return int(unwrapped["count"])
    return unwrapped


# Discount Codes
@mcp.tool()
def create_discount_code(price_rule_id: Union[int, str], code: str) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Create a discount code for a price rule."""

    data = shopify_request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        body={"discount_code": {"code": code}},
    )
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def list_discount_codes(price_rule_id: Union[int, str], limit: int = 50) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List discount codes for a price rule."""

    data = shopify_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params={"limit": limit})
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def get_discount_code(price_rule_id: Union[int, str], discount_code_id: Union[int, str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Get a discount code."""

    data = shopify_request("GET", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def update_discount_code(
    price_rule_id: Union[int, str],
    discount_code_id: Union[int, str],
    discount_code: Dict[str, Any],
) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Update a discount code."""

    payload = dict(discount_code)
    payload["id"] = int(discount_code_id) if str(discount_code_id).isdigit() else discount_code_id
    data = shopify_request(
        "PUT",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        body={"discount_code": payload},
    )
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def delete_discount_code(price_rule_id: Union[int, str], discount_code_id: Union[int, str]) -> Dict[str, Any]:
    """Delete a discount code."""

    data = shopify_request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")
    if "error" in data:
        return data
    return {"ok": True}


@mcp.tool()
def count_discount_codes(times_used: Optional[int] = None, times_used_min: Optional[int] = None, times_used_max: Optional[int] = None) -> Union[int, Dict[str, Any]]:
    """Count discount codes for the shop."""

    params: Dict[str, Any] = {}
    if times_used is not None:
        params["times_used"] = times_used
    if times_used_min is not None:
        params["times_used_min"] = times_used_min
    if times_used_max is not None:
        params["times_used_max"] = times_used_max

    data = shopify_request("GET", "/discount_codes/count.json", params=params or None)
    if "error" in data:
        return data
    unwrapped = unwrap_envelope(data)
    if isinstance(unwrapped, dict) and "count" in unwrapped:
        return int(unwrapped["count"])
    return unwrapped


@mcp.tool()
def create_discount_code_batch(price_rule_id: Union[int, str], codes: List[str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Create a discount code creation job (batch) for a price rule."""

    body = {"discount_codes": [{"code": c} for c in codes]}
    data = shopify_request("POST", f"/price_rules/{price_rule_id}/batch.json", body=body)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def get_discount_code_batch(price_rule_id: Union[int, str], batch_id: Union[int, str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Get a discount code creation job."""

    data = shopify_request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def list_discount_codes_for_batch(price_rule_id: Union[int, str], batch_id: Union[int, str], limit: int = 50) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List discount codes for a discount code creation job."""

    data = shopify_request(
        "GET",
        f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json",
        params={"limit": limit},
    )
    if "error" in data:
        return data
    return unwrap_envelope(data)
