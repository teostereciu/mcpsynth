from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import ShopifyClient, unwrap_envelope


# Price rules

@mcp.tool()
def create_price_rule(price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """Create a price rule (POST /price_rules.json)."""
    client = ShopifyClient()
    data = client.request("POST", "/price_rules.json", body={"price_rule": price_rule})
    return unwrap_envelope(data)


@mcp.tool()
def list_price_rules(limit: int = 50, fields: Optional[str] = None) -> List[Dict[str, Any]]:
    """List price rules (GET /price_rules.json)."""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields
    data = client.request("GET", "/price_rules.json", params=params)
    return unwrap_envelope(data)


@mcp.tool()
def get_price_rule(price_rule_id: Union[int, str]) -> Dict[str, Any]:
    """Get a price rule (GET /price_rules/{id}.json)."""
    client = ShopifyClient()
    data = client.request("GET", f"/price_rules/{price_rule_id}.json")
    return unwrap_envelope(data)


@mcp.tool()
def update_price_rule(price_rule_id: Union[int, str], price_rule: Dict[str, Any]) -> Dict[str, Any]:
    """Update a price rule (PUT /price_rules/{id}.json)."""
    client = ShopifyClient()
    payload = dict(price_rule)
    payload["id"] = int(price_rule_id) if str(price_rule_id).isdigit() else price_rule_id
    data = client.request("PUT", f"/price_rules/{price_rule_id}.json", body={"price_rule": payload})
    return unwrap_envelope(data)


@mcp.tool()
def delete_price_rule(price_rule_id: Union[int, str]) -> Dict[str, Any]:
    """Delete a price rule (DELETE /price_rules/{id}.json)."""
    client = ShopifyClient()
    return client.request("DELETE", f"/price_rules/{price_rule_id}.json")


# Discount codes

@mcp.tool()
def create_discount_code(price_rule_id: Union[int, str], code: str) -> Dict[str, Any]:
    """Create a discount code for a price rule (POST /price_rules/{id}/discount_codes.json)."""
    client = ShopifyClient()
    data = client.request(
        "POST",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        body={"discount_code": {"code": code}},
    )
    return unwrap_envelope(data)


@mcp.tool()
def list_discount_codes(price_rule_id: Union[int, str], limit: int = 50) -> List[Dict[str, Any]]:
    """List discount codes for a price rule (GET /price_rules/{id}/discount_codes.json)."""
    client = ShopifyClient()
    data = client.request(
        "GET",
        f"/price_rules/{price_rule_id}/discount_codes.json",
        params={"limit": limit},
    )
    return unwrap_envelope(data)


@mcp.tool()
def get_discount_code(price_rule_id: Union[int, str], discount_code_id: Union[int, str]) -> Dict[str, Any]:
    """Get a discount code (GET /price_rules/{id}/discount_codes/{discount_code_id}.json)."""
    client = ShopifyClient()
    data = client.request(
        "GET",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
    )
    return unwrap_envelope(data)


@mcp.tool()
def update_discount_code(
    price_rule_id: Union[int, str],
    discount_code_id: Union[int, str],
    discount_code: Dict[str, Any],
) -> Dict[str, Any]:
    """Update a discount code (PUT /price_rules/{id}/discount_codes/{discount_code_id}.json)."""
    client = ShopifyClient()
    payload = dict(discount_code)
    payload["id"] = int(discount_code_id) if str(discount_code_id).isdigit() else discount_code_id
    data = client.request(
        "PUT",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
        body={"discount_code": payload},
    )
    return unwrap_envelope(data)


@mcp.tool()
def delete_discount_code(price_rule_id: Union[int, str], discount_code_id: Union[int, str]) -> Dict[str, Any]:
    """Delete a discount code (DELETE /price_rules/{id}/discount_codes/{discount_code_id}.json)."""
    client = ShopifyClient()
    return client.request(
        "DELETE",
        f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
    )


@mcp.tool()
def create_discount_code_batch(price_rule_id: Union[int, str], codes: List[str]) -> Dict[str, Any]:
    """Create a discount code creation job (POST /price_rules/{id}/batch.json)."""
    client = ShopifyClient()
    body = {"discount_codes": [{"code": c} for c in codes]}
    data = client.request("POST", f"/price_rules/{price_rule_id}/batch.json", body=body)
    return unwrap_envelope(data)
