"""Shopify Admin REST API — Price Rules & Discount Codes tools."""

import os, requests
from mcp.server.fastmcp import FastMCP

def _session():
    token = os.environ["SHOPIFY_ACCESS_TOKEN"]
    store = os.environ["SHOPIFY_STORE_URL"]
    base  = f"https://{store}/admin/api/2026-01"
    s = requests.Session()
    s.headers.update({"X-Shopify-Access-Token": token, "Content-Type": "application/json"})
    return s, base

def register(mcp: FastMCP):

    # ── Price Rules ───────────────────────────────────────────────────────────

    @mcp.tool()
    def list_price_rules(limit: int = 50, page_info: str = "") -> dict:
        """List all price rules."""
        s, base = _session()
        params: dict = {"limit": limit}
        if page_info:
            params["page_info"] = page_info
        r = s.get(f"{base}/price_rules.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_price_rule(price_rule_id: str) -> dict:
        """Get a price rule by ID."""
        s, base = _session()
        r = s.get(f"{base}/price_rules/{price_rule_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_price_rule(title: str, value_type: str, value: str,
                          customer_selection: str = "all",
                          target_type: str = "line_item",
                          target_selection: str = "all",
                          allocation_method: str = "across",
                          starts_at: str = "",
                          ends_at: str = "",
                          usage_limit: int = 0,
                          once_per_customer: bool = False) -> dict:
        """Create a price rule.
        value_type: percentage|fixed_amount.
        value: negative number e.g. '-10.0' for 10% off."""
        s, base = _session()
        data: dict = {
            "title": title,
            "value_type": value_type,
            "value": value,
            "customer_selection": customer_selection,
            "target_type": target_type,
            "target_selection": target_selection,
            "allocation_method": allocation_method,
            "once_per_customer": once_per_customer,
        }
        if starts_at:   data["starts_at"]   = starts_at
        if ends_at:     data["ends_at"]     = ends_at
        if usage_limit: data["usage_limit"] = usage_limit
        r = s.post(f"{base}/price_rules.json", json={"price_rule": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_price_rule(price_rule_id: str, title: str = "", value: str = "",
                          ends_at: str = "", usage_limit: int = 0,
                          once_per_customer: bool = None) -> dict:
        """Update a price rule."""
        s, base = _session()
        data: dict = {}
        if title:                    data["title"]              = title
        if value:                    data["value"]              = value
        if ends_at:                  data["ends_at"]            = ends_at
        if usage_limit:              data["usage_limit"]        = usage_limit
        if once_per_customer is not None:
            data["once_per_customer"] = once_per_customer
        r = s.put(f"{base}/price_rules/{price_rule_id}.json",
                  json={"price_rule": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_price_rule(price_rule_id: str) -> dict:
        """Delete a price rule."""
        s, base = _session()
        r = s.delete(f"{base}/price_rules/{price_rule_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "price_rule_id": price_rule_id}

    # ── Discount Codes ────────────────────────────────────────────────────────

    @mcp.tool()
    def list_discount_codes(price_rule_id: str, limit: int = 50) -> dict:
        """List discount codes for a price rule."""
        s, base = _session()
        r = s.get(f"{base}/price_rules/{price_rule_id}/discount_codes.json",
                  params={"limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_discount_code(price_rule_id: str, discount_code_id: str) -> dict:
        """Get a specific discount code."""
        s, base = _session()
        r = s.get(
            f"{base}/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_discount_code(price_rule_id: str, code: str) -> dict:
        """Create a discount code for a price rule."""
        s, base = _session()
        r = s.post(f"{base}/price_rules/{price_rule_id}/discount_codes.json",
                   json={"discount_code": {"code": code}})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_discount_code(price_rule_id: str, discount_code_id: str,
                             code: str) -> dict:
        """Update a discount code."""
        s, base = _session()
        r = s.put(
            f"{base}/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
            json={"discount_code": {"code": code}})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_discount_code(price_rule_id: str, discount_code_id: str) -> dict:
        """Delete a discount code."""
        s, base = _session()
        r = s.delete(
            f"{base}/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "discount_code_id": discount_code_id}

    @mcp.tool()
    def lookup_discount_code(code: str) -> dict:
        """Look up a discount code by its code string (across all price rules)."""
        s, base = _session()
        r = s.get(f"{base}/discount_codes/lookup.json", params={"code": code})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()
