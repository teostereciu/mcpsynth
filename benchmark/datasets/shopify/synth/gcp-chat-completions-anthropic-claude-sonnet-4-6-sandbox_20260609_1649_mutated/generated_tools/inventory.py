"""Shopify Admin REST API — Inventory Levels and Locations tools."""
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

def _delete(path, params=None):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        if r.status_code == 200:
            return r.json()
        return {"status": r.status_code}
    except Exception as e:
        return {"error": str(e)}


# ── Inventory Levels ──────────────────────────────────────────────────────────

def list_inventory_levels(location_ids: Optional[str] = None,
                          inventory_item_ids: Optional[str] = None,
                          limit: int = 50) -> dict:
    """Retrieve a list of inventory levels. Provide location_ids and/or inventory_item_ids."""
    params: dict[str, Any] = {"limit": limit}
    if location_ids: params["location_ids"] = location_ids
    if inventory_item_ids: params["inventory_item_ids"] = inventory_item_ids
    return _get("/inventory_levels.json", params)

def adjust_inventory_level(inventory_item_id: int, location_id: int,
                           available_adjustment: int) -> dict:
    """Adjust the inventory level of an inventory item at a location.
    Use positive values to increase, negative to decrease.
    """
    return _post("/inventory_levels/adjust.json", {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available_adjustment": available_adjustment,
    })

def set_inventory_level(inventory_item_id: int, location_id: int,
                        available: int,
                        disconnect_if_necessary: bool = False) -> dict:
    """Set the inventory level for an inventory item at a location."""
    return _post("/inventory_levels/set.json", {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available": available,
        "disconnect_if_necessary": disconnect_if_necessary,
    })

def connect_inventory_item_to_location(inventory_item_id: int, location_id: int,
                                       relocate_if_necessary: bool = False) -> dict:
    """Connect an inventory item to a location."""
    return _post("/inventory_levels/connect.json", {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "relocate_if_necessary": relocate_if_necessary,
    })

def delete_inventory_level(inventory_item_id: int, location_id: int) -> dict:
    """Delete an inventory level (disconnect item from location)."""
    return _delete("/inventory_levels.json", {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
    })


# ── Locations ─────────────────────────────────────────────────────────────────

def list_locations(limit: int = 50) -> dict:
    """Retrieve a list of locations."""
    return _get("/locations.json", {"limit": limit})

def get_location(location_id: int) -> dict:
    """Retrieve a single location by its ID."""
    return _get(f"/locations/{location_id}.json")

def count_locations() -> dict:
    """Retrieve a count of locations."""
    return _get("/locations/count.json")

def get_location_inventory_levels(location_id: int, limit: int = 50) -> dict:
    """Retrieve a list of inventory levels for a location."""
    return _get(f"/locations/{location_id}/inventory_levels.json", {"limit": limit})
