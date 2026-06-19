"""Shopify Admin REST API — Price Rules, Discount Codes tools."""
import os, requests
from mcp.server.fastmcp import FastMCP

BASE_URL = f"https://{os.environ.get('SHOPIFY_STORE_URL', '')}/admin/api/2026-01"

def _headers():
    return {
        "X-Shopify-Access-Token": os.environ.get("SHOPIFY_ACCESS_TOKEN", ""),
        "Content-Type": "application/json",
    }

def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _post(path, body=None):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=body, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, body):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=body, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _delete(path):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=_headers(), timeout=30)
        if r.status_code == 200:
            return r.json()
        return {"status": r.status_code}
    except Exception as e:
        return {"error": str(e)}


def register_discounts(mcp: FastMCP):

    # ── Price Rules ───────────────────────────────────────────────────────────

    @mcp.tool()
    def list_price_rules(
        limit: int = 50,
        since_id: int = None,
        created_at_min: str = None,
        created_at_max: str = None,
        starts_at_min: str = None,
        ends_at_min: str = None,
        fields: str = None,
    ) -> dict:
        """Retrieve a list of price rules."""
        params = {"limit": limit}
        if since_id: params["since_id"] = since_id
        if created_at_min: params["created_at_min"] = created_at_min
        if created_at_max: params["created_at_max"] = created_at_max
        if starts_at_min: params["starts_at_min"] = starts_at_min
        if ends_at_min: params["ends_at_min"] = ends_at_min
        if fields: params["fields"] = fields
        return _get("/price_rules.json", params)

    @mcp.tool()
    def get_price_rule(price_rule_id: int) -> dict:
        """Retrieve a single price rule by ID."""
        return _get(f"/price_rules/{price_rule_id}.json")

    @mcp.tool()
    def count_price_rules() -> dict:
        """Retrieve a count of all price rules."""
        return _get("/price_rules/count.json")

    @mcp.tool()
    def create_price_rule(
        title: str,
        value_type: str,
        value: str,
        customer_selection: str,
        target_type: str,
        target_selection: str,
        allocation_method: str,
        starts_at: str,
        ends_at: str = None,
        usage_limit: int = None,
        once_per_customer: bool = False,
        entitled_product_ids: list = None,
        entitled_variant_ids: list = None,
        entitled_collection_ids: list = None,
        prerequisite_subtotal_range: dict = None,
        prerequisite_quantity_range: dict = None,
    ) -> dict:
        """Create a price rule.
        value_type: fixed_amount|percentage.
        target_type: line_item|shipping_line.
        target_selection: all|entitled.
        allocation_method: each|across.
        customer_selection: all|prerequisite."""
        rule = {
            "title": title,
            "value_type": value_type,
            "value": value,
            "customer_selection": customer_selection,
            "target_type": target_type,
            "target_selection": target_selection,
            "allocation_method": allocation_method,
            "starts_at": starts_at,
            "once_per_customer": once_per_customer,
        }
        if ends_at: rule["ends_at"] = ends_at
        if usage_limit: rule["usage_limit"] = usage_limit
        if entitled_product_ids: rule["entitled_product_ids"] = entitled_product_ids
        if entitled_variant_ids: rule["entitled_variant_ids"] = entitled_variant_ids
        if entitled_collection_ids: rule["entitled_collection_ids"] = entitled_collection_ids
        if prerequisite_subtotal_range: rule["prerequisite_subtotal_range"] = prerequisite_subtotal_range
        if prerequisite_quantity_range: rule["prerequisite_quantity_range"] = prerequisite_quantity_range
        return _post("/price_rules.json", {"price_rule": rule})

    @mcp.tool()
    def update_price_rule(
        price_rule_id: int,
        title: str = None,
        value: str = None,
        ends_at: str = None,
        usage_limit: int = None,
        once_per_customer: bool = None,
    ) -> dict:
        """Update an existing price rule."""
        rule = {}
        if title: rule["title"] = title
        if value: rule["value"] = value
        if ends_at is not None: rule["ends_at"] = ends_at
        if usage_limit is not None: rule["usage_limit"] = usage_limit
        if once_per_customer is not None: rule["once_per_customer"] = once_per_customer
        return _put(f"/price_rules/{price_rule_id}.json", {"price_rule": rule})

    @mcp.tool()
    def delete_price_rule(price_rule_id: int) -> dict:
        """Delete a price rule."""
        return _delete(f"/price_rules/{price_rule_id}.json")

    # ── Discount Codes ────────────────────────────────────────────────────────

    @mcp.tool()
    def list_discount_codes(price_rule_id: int, limit: int = 50) -> dict:
        """Retrieve a list of discount codes for a price rule."""
        return _get(f"/price_rules/{price_rule_id}/discount_codes.json", {"limit": limit})

    @mcp.tool()
    def get_discount_code(price_rule_id: int, discount_code_id: int) -> dict:
        """Retrieve a single discount code."""
        return _get(f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")

    @mcp.tool()
    def count_discount_codes() -> dict:
        """Retrieve a count of discount codes for the shop."""
        return _get("/discount_codes/count.json")

    @mcp.tool()
    def create_discount_code(price_rule_id: int, code: str) -> dict:
        """Create a discount code for a price rule."""
        return _post(f"/price_rules/{price_rule_id}/discount_codes.json", {"discount_code": {"code": code}})

    @mcp.tool()
    def update_discount_code(price_rule_id: int, discount_code_id: int, code: str) -> dict:
        """Update an existing discount code."""
        return _put(
            f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
            {"discount_code": {"code": code}},
        )

    @mcp.tool()
    def delete_discount_code(price_rule_id: int, discount_code_id: int) -> dict:
        """Delete a discount code."""
        return _delete(f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")

    @mcp.tool()
    def create_discount_code_batch(price_rule_id: int, codes: list) -> dict:
        """Create a batch of discount codes for a price rule. codes: list of code strings."""
        discount_codes = [{"code": c} for c in codes]
        return _post(f"/price_rules/{price_rule_id}/batch.json", {"discount_codes": discount_codes})
