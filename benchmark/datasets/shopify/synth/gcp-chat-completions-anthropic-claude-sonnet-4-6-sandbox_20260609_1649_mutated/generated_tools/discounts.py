"""Shopify Admin REST API — Price Rules and Discount Codes tools."""
import os, requests
from typing import Optional, Any

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

def _post(path, payload):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=payload, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, payload):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=payload, timeout=30)
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


# ── Price Rules ───────────────────────────────────────────────────────────────

def list_price_rules(limit: int = 50) -> dict:
    """Retrieve a list of price rules."""
    return _get("/price_rules.json", {"limit": limit})

def get_price_rule(price_rule_id: int) -> dict:
    """Retrieve a single price rule."""
    return _get(f"/price_rules/{price_rule_id}.json")

def count_price_rules() -> dict:
    """Retrieve a count of all price rules."""
    return _get("/price_rules/count.json")

def create_price_rule(title: str, value_type: str, value: str,
                      target_type: str, target_selection: str,
                      allocation_method: str, customer_selection: str,
                      starts_at: Optional[str] = None, ends_at: Optional[str] = None,
                      usage_limit: Optional[int] = None,
                      once_per_customer: bool = False,
                      entitled_product_ids: Optional[list] = None,
                      entitled_variant_ids: Optional[list] = None,
                      entitled_collection_ids: Optional[list] = None,
                      entitled_country_ids: Optional[list] = None,
                      prerequisite_subtotal_range: Optional[dict] = None,
                      prerequisite_quantity_range: Optional[dict] = None,
                      prerequisite_shipping_price_range: Optional[dict] = None,
                      prerequisite_to_entitlement_quantity_ratio: Optional[dict] = None,
                      allocation_limit: Optional[int] = None) -> dict:
    """Create a price rule.
    value_type: fixed_amount|percentage
    target_type: line_item|shipping_line
    target_selection: all|entitled
    allocation_method: each|across
    customer_selection: all|prerequisite
    """
    rule: dict[str, Any] = {
        "title": title,
        "value_type": value_type,
        "value": value,
        "target_type": target_type,
        "target_selection": target_selection,
        "allocation_method": allocation_method,
        "customer_selection": customer_selection,
        "once_per_customer": once_per_customer,
    }
    if starts_at: rule["starts_at"] = starts_at
    if ends_at: rule["ends_at"] = ends_at
    if usage_limit is not None: rule["usage_limit"] = usage_limit
    if entitled_product_ids: rule["entitled_product_ids"] = entitled_product_ids
    if entitled_variant_ids: rule["entitled_variant_ids"] = entitled_variant_ids
    if entitled_collection_ids: rule["entitled_collection_ids"] = entitled_collection_ids
    if entitled_country_ids: rule["entitled_country_ids"] = entitled_country_ids
    if prerequisite_subtotal_range: rule["prerequisite_subtotal_range"] = prerequisite_subtotal_range
    if prerequisite_quantity_range: rule["prerequisite_quantity_range"] = prerequisite_quantity_range
    if prerequisite_shipping_price_range: rule["prerequisite_shipping_price_range"] = prerequisite_shipping_price_range
    if prerequisite_to_entitlement_quantity_ratio: rule["prerequisite_to_entitlement_quantity_ratio"] = prerequisite_to_entitlement_quantity_ratio
    if allocation_limit is not None: rule["allocation_limit"] = allocation_limit
    return _post("/price_rules.json", {"price_rule": rule})

def update_price_rule(price_rule_id: int, title: Optional[str] = None,
                      value: Optional[str] = None, ends_at: Optional[str] = None,
                      usage_limit: Optional[int] = None,
                      once_per_customer: Optional[bool] = None) -> dict:
    """Update an existing price rule."""
    rule: dict[str, Any] = {"id": price_rule_id}
    if title is not None: rule["title"] = title
    if value is not None: rule["value"] = value
    if ends_at is not None: rule["ends_at"] = ends_at
    if usage_limit is not None: rule["usage_limit"] = usage_limit
    if once_per_customer is not None: rule["once_per_customer"] = once_per_customer
    return _put(f"/price_rules/{price_rule_id}.json", {"price_rule": rule})

def delete_price_rule(price_rule_id: int) -> dict:
    """Delete a price rule."""
    return _delete(f"/price_rules/{price_rule_id}.json")


# ── Discount Codes ────────────────────────────────────────────────────────────

def list_discount_codes(price_rule_id: int) -> dict:
    """Retrieve a list of discount codes for a price rule."""
    return _get(f"/price_rules/{price_rule_id}/discount_codes.json")

def get_discount_code(price_rule_id: int, discount_code_id: int) -> dict:
    """Retrieve a single discount code."""
    return _get(f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")

def count_discount_codes() -> dict:
    """Retrieve a count of discount codes for a shop."""
    return _get("/discount_codes/count.json")

def create_discount_code(price_rule_id: int, code: str) -> dict:
    """Create a discount code for a price rule."""
    return _post(f"/price_rules/{price_rule_id}/discount_codes.json",
                 {"discount_code": {"code": code}})

def create_discount_code_batch(price_rule_id: int, codes: list) -> dict:
    """Create a batch of discount codes for a price rule.
    codes: list of {"code": "CODE_VALUE"} dicts
    """
    return _post(f"/price_rules/{price_rule_id}/batch.json",
                 {"discount_codes": codes})

def update_discount_code(price_rule_id: int, discount_code_id: int, code: str) -> dict:
    """Update an existing discount code."""
    return _put(f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json",
                {"discount_code": {"code": code}})

def delete_discount_code(price_rule_id: int, discount_code_id: int) -> dict:
    """Delete a discount code."""
    return _delete(f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")
