"""Shopify Admin REST API — Fulfillment, FulfillmentOrder, InventoryItem, InventoryLevel tools."""
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


# ── Fulfillments ──────────────────────────────────────────────────────────────

def create_fulfillment(line_items_by_fulfillment_order: list,
                       tracking_info: Optional[dict] = None,
                       notify_customer: bool = False,
                       origin_address: Optional[dict] = None) -> dict:
    """Create a fulfillment for one or many fulfillment orders.
    line_items_by_fulfillment_order: list of {fulfillment_order_id, fulfillment_order_line_items?}
    tracking_info: {number, url, company}
    """
    fulfillment: dict[str, Any] = {
        "line_items_by_fulfillment_order": line_items_by_fulfillment_order,
        "notify_customer": notify_customer,
    }
    if tracking_info: fulfillment["tracking_info"] = tracking_info
    if origin_address: fulfillment["origin_address"] = origin_address
    return _post("/fulfillments.json", {"fulfillment": fulfillment})

def cancel_fulfillment(fulfillment_id: int) -> dict:
    """Cancel a fulfillment."""
    return _post(f"/fulfillments/{fulfillment_id}/cancel.json", {})

def update_fulfillment_tracking(fulfillment_id: int, tracking_info: dict,
                                notify_customer: bool = True) -> dict:
    """Update tracking information for a fulfillment.
    tracking_info: {number, url, company}
    """
    return _post(f"/fulfillments/{fulfillment_id}/update_tracking.json", {
        "fulfillment": {
            "tracking_info": tracking_info,
            "notify_customer": notify_customer,
        }
    })

def list_fulfillments_for_order(order_id: int) -> dict:
    """Retrieve fulfillments associated with an order."""
    return _get(f"/orders/{order_id}/fulfillments.json")

def get_fulfillment(order_id: int, fulfillment_id: int) -> dict:
    """Retrieve a single fulfillment."""
    return _get(f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")

def count_fulfillments(order_id: int) -> dict:
    """Retrieve a count of fulfillments for an order."""
    return _get(f"/orders/{order_id}/fulfillments/count.json")

def list_fulfillments_for_fulfillment_order(fulfillment_order_id: int) -> dict:
    """Retrieve fulfillments associated with a fulfillment order."""
    return _get(f"/fulfillment_orders/{fulfillment_order_id}/fulfillments.json")


# ── Fulfillment Orders ────────────────────────────────────────────────────────

def get_fulfillment_order(fulfillment_order_id: int) -> dict:
    """Retrieve a specific fulfillment order."""
    return _get(f"/fulfillment_orders/{fulfillment_order_id}.json")

def list_fulfillment_orders_for_order(order_id: int) -> dict:
    """Retrieve a list of fulfillment orders for a specific order."""
    return _get(f"/orders/{order_id}/fulfillment_orders.json")

def cancel_fulfillment_order(fulfillment_order_id: int) -> dict:
    """Cancel a fulfillment order."""
    return _post(f"/fulfillment_orders/{fulfillment_order_id}/cancel.json", {})

def close_fulfillment_order(fulfillment_order_id: int, message: Optional[str] = None) -> dict:
    """Mark a fulfillment order as incomplete."""
    payload: dict[str, Any] = {}
    if message: payload["message"] = message
    return _post(f"/fulfillment_orders/{fulfillment_order_id}/close.json",
                 {"fulfillment_order": payload})

def hold_fulfillment_order(fulfillment_order_id: int, reason: str,
                           reason_notes: Optional[str] = None,
                           notify_merchant: bool = False) -> dict:
    """Hold fulfillment of a fulfillment order.
    reason: awaiting_payment|high_risk_of_fraud|incorrect_address|inventory_out_of_stock|other
    """
    hold: dict[str, Any] = {"reason": reason, "notify_merchant": notify_merchant}
    if reason_notes: hold["reason_notes"] = reason_notes
    return _post(f"/fulfillment_orders/{fulfillment_order_id}/hold.json",
                 {"fulfillment_hold": hold})

def release_fulfillment_order_hold(fulfillment_order_id: int) -> dict:
    """Release all holds on a fulfillment order."""
    return _post(f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json", {})

def move_fulfillment_order(fulfillment_order_id: int, new_location_id: int) -> dict:
    """Move a fulfillment order to a new location."""
    return _post(f"/fulfillment_orders/{fulfillment_order_id}/move.json",
                 {"fulfillment_order": {"new_location_id": new_location_id}})

def open_fulfillment_order(fulfillment_order_id: int) -> dict:
    """Mark a fulfillment order as open."""
    return _post(f"/fulfillment_orders/{fulfillment_order_id}/open.json", {})

def reschedule_fulfillment_order(fulfillment_order_id: int, new_fulfill_at: str) -> dict:
    """Reschedule the fulfill_at time of a scheduled fulfillment order."""
    return _post(f"/fulfillment_orders/{fulfillment_order_id}/reschedule.json",
                 {"fulfillment_order": {"new_fulfill_at": new_fulfill_at}})


# ── Inventory Items ───────────────────────────────────────────────────────────

def list_inventory_items(ids: str, limit: int = 50) -> dict:
    """Retrieve inventory items by comma-separated IDs."""
    return _get("/inventory_items.json", {"ids": ids, "limit": limit})

def get_inventory_item(inventory_item_id: int) -> dict:
    """Retrieve a single inventory item by ID."""
    return _get(f"/inventory_items/{inventory_item_id}.json")

def update_inventory_item(inventory_item_id: int, sku: Optional[str] = None,
                          cost: Optional[str] = None, tracked: Optional[bool] = None,
                          country_code_of_origin: Optional[str] = None,
                          harmonized_system_code: Optional[str] = None) -> dict:
    """Update an existing inventory item."""
    item: dict[str, Any] = {"id": inventory_item_id}
    if sku is not None: item["sku"] = sku
    if cost is not None: item["cost"] = cost
    if tracked is not None: item["tracked"] = tracked
    if country_code_of_origin is not None: item["country_code_of_origin"] = country_code_of_origin
    if harmonized_system_code is not None: item["harmonized_system_code"] = harmonized_system_code
    return _put(f"/inventory_items/{inventory_item_id}.json", {"inventory_item": item})
