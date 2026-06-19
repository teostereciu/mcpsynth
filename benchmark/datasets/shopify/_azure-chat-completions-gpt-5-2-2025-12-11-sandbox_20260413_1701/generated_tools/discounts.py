from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp, client


# ---- Price rules ----

@mcp.tool()
def list_price_rules(limit: int = 50) -> List[Dict[str, Any]]:
    """Retrieve a list of price rules."""
    return client.request("GET", "/price_rules.json", params={"limit": limit})


@mcp.tool()
def get_price_rule(price_rule_id: Union[int, str]) -> Dict[str, Any]:
    """Retrieve a single price rule."""
    return client.request("GET", f"/price_rules/{price_rule_id}.json")


@mcp.tool()
def count_price_rules() -> Dict[str, Any]:
    """Retrieve a count of all price rules."""
    return client.request("GET", "/price_rules/count.json")


@mcp.tool()
def create_price_rule(price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """Create a price rule."""
    return client.request("POST", "/price_rules.json", body={"price_rule": price_rule})


@mcp.tool()
def update_price_rule(price_rule_id: Union[int, str], price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """Update an existing price rule."""
    payload = dict(price_rule)
    payload["id"] = int(price_rule_id) if str(price_rule_id).isdigit() else price_rule_id
    return client.request("PUT", f"/price_rules/{price_rule_id}.json", body={"price_rule": payload})


@mcp.tool()
def delete_price_rule(price_rule_id: Union[int, str]) -> Dict[str, Any]:
    """Delete a price rule."""
    return client.request("DELETE", f"/price_rules/{price_rule_id}.json", unwrap=False)


# ---- Discount codes ----

@mcp.tool()
def create_discount_code(price_rule_id: Union[int, str], code: str) -> Dict[str, Any]:
    """Create a discount code for a price rule."""
    return client.request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        body={"discount_code": {"code": code}},
    )


@mcp.tool()
def list_discount_codes(price_rule_id: Union[int, str], limit: int = 50) -> List[Dict[str, Any]]:
    """Retrieve a list of discount codes for a price rule."""
    return client.request(
        "GET",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        params={"limit": limit},
    )


@mcp.tool()
def get_discount_code(price_rule_id: Union[int, str], discount_code_id: Union[int, str]) -> Dict[str, Any]:
    """Retrieve a single discount code."""
    return client.request(
        "GET",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
    )


@mcp.tool()
def update_discount_code(
    price_rule_id: Union[int, str],
    discount_code_id: Union[int, str],
    discount_code: Dict[str, Any],
) -> Dict[str, Any]:
    """Update an existing discount code."""
    payload = dict(discount_code)
    payload["id"] = int(discount_code_id) if str(discount_code_id).isdigit() else discount_code_id
    return client.request(
        "PUT",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        body={"discount_code": payload},
    )


@mcp.tool()
def delete_discount_code(price_rule_id: Union[int, str], discount_code_id: Union[int, str]) -> Dict[str, Any]:
    """Delete a discount code."""
    return client.request(
        "DELETE",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        unwrap=False,
    )


@mcp.tool()
def count_discount_codes(
    times_used: Optional[int] = None,
    times_used_min: Optional[int] = None,
    times_used_max: Optional[int] = None,
) -> Dict[str, Any]:
    """Retrieve a count of discount codes for a shop."""
    params: Dict[str, Any] = {}
    for k, v in {"times_used": times_used, "times_used_min": times_used_min, "times_used_max": times_used_max}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/discount_codes/count.json", params=params or None)


@mcp.tool()
def lookup_discount_code(code: str) -> Dict[str, Any]:
    """Lookup the location of a discount code (deprecated endpoint).

    Note: Shopify returns the location in the Location header; this tool returns the raw response envelope.
    """
    # We can't access headers with current client; return unwrapped body if any.
    return client.request("GET", "/discount_codes/lookup.json", params={"code": code}, unwrap=False)


@mcp.tool()
def create_discount_code_batch(price_rule_id: Union[int, str], codes: List[str]) -> Dict[str, Any]:
    """Create a discount code creation job (batch)."""
    return client.request(
        "POST",
        f"/price_rules/{price_rule_id}/batch.json",
        body={"discount_codes": [{"code": c} for c in codes]},
    )


@mcp.tool()
def get_discount_code_batch(price_rule_id: Union[int, str], batch_id: Union[int, str]) -> Dict[str, Any]:
    """Retrieve a discount code creation job."""
    return client.request("GET", f"/price_rules/{price_rule_id}/batch/{batch_id}.json")


@mcp.tool()
def list_discount_codes_for_batch(
    price_rule_id: Union[int, str],
    batch_id: Union[int, str],
    limit: int = 50,
) -> List[Dict[str, Any]]:
    """Retrieve discount codes for a discount code creation job."""
    return client.request(
        "GET",
        f"/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json",
        params={"limit": limit},
    )
