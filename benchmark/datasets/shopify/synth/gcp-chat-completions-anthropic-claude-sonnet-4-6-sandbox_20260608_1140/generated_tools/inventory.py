"""Shopify Admin REST API — Inventory Items, Inventory Levels, Locations tools."""
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

def _delete(path, params=None):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        if r.status_code == 200:
            return r.json()
        return {"status": r.status_code}
    except Exception as e:
        return {"error": str(e)}


def register_inventory(mcp: FastMCP):

    # ── Inventory Items ───────────────────────────────────────────────────────

    @mcp.tool()
    def list_inventory_items(ids: str, limit: int = 50) -> dict:
        """Retrieve inventory items by comma-separated IDs (required)."""
        return _get("/inventory_items.json", {"ids": ids, "limit": limit})

    @mcp.tool()
    def get_inventory_item(inventory_item_id: int) -> dict:
        """Retrieve a single inventory item by ID."""
        return _get(f"/inventory_items/{inventory_item_id}.json")

    @mcp.tool()
    def update_inventory_item(
        inventory_item_id: int,
        sku: str = None,
        cost: str = None,
        tracked: bool = None,
        country_code_of_origin: str = None,
        province_code_of_origin: str = None,
        harmonized_system_code: str = None,
    ) -> dict:
        """Update an existing inventory item."""
        item = {}
        if sku is not None: item["sku"] = sku
        if cost is not None: item["cost"] = cost
        if tracked is not None: item["tracked"] = tracked
        if country_code_of_origin is not None: item["country_code_of_origin"] = country_code_of_origin
        if province_code_of_origin is not None: item["province_code_of_origin"] = province_code_of_origin
        if harmonized_system_code is not None: item["harmonized_system_code"] = harmonized_system_code
        return _put(f"/inventory_items/{inventory_item_id}.json", {"inventory_item": item})

    # ── Inventory Levels ──────────────────────────────────────────────────────

    @mcp.tool()
    def list_inventory_levels(
        inventory_item_ids: str = None,
        location_ids: str = None,
        limit: int = 50,
    ) -> dict:
        """Retrieve a list of inventory levels. Provide inventory_item_ids or location_ids."""
        params = {"limit": limit}
        if inventory_item_ids: params["inventory_item_ids"] = inventory_item_ids
        if location_ids: params["location_ids"] = location_ids
        return _get("/inventory_levels.json", params)

    @mcp.tool()
    def adjust_inventory_level(
        inventory_item_id: int,
        location_id: int,
        available_adjustment: int,
    ) -> dict:
        """Adjust the inventory level of an inventory item at a location.
        Use positive values to increase, negative to decrease."""
        return _post("/inventory_levels/adjust.json", {
            "inventory_item_id": inventory_item_id,
            "location_id": location_id,
            "available_adjustment": available_adjustment,
        })

    @mcp.tool()
    def set_inventory_level(
        inventory_item_id: int,
        location_id: int,
        available: int,
        disconnect_if_necessary: bool = False,
    ) -> dict:
        """Set the inventory level for an inventory item at a location."""
        return _post("/inventory_levels/set.json", {
            "inventory_item_id": inventory_item_id,
            "location_id": location_id,
            "available": available,
            "disconnect_if_necessary": disconnect_if_necessary,
        })

    @mcp.tool()
    def connect_inventory_item_to_location(
        inventory_item_id: int,
        location_id: int,
        relocate_if_necessary: bool = False,
    ) -> dict:
        """Connect an inventory item to a location."""
        return _post("/inventory_levels/connect.json", {
            "inventory_item_id": inventory_item_id,
            "location_id": location_id,
            "relocate_if_necessary": relocate_if_necessary,
        })

    @mcp.tool()
    def delete_inventory_level(inventory_item_id: int, location_id: int) -> dict:
        """Delete an inventory level from a location (disconnect item from location)."""
        return _delete("/inventory_levels.json", {
            "inventory_item_id": inventory_item_id,
            "location_id": location_id,
        })

    # ── Locations ─────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_locations(limit: int = 50) -> dict:
        """Retrieve a list of locations."""
        return _get("/locations.json", {"limit": limit})

    @mcp.tool()
    def get_location(location_id: int) -> dict:
        """Retrieve a single location by its ID."""
        return _get(f"/locations/{location_id}.json")

    @mcp.tool()
    def count_locations() -> dict:
        """Retrieve a count of locations."""
        return _get("/locations/count.json")

    @mcp.tool()
    def get_location_inventory_levels(location_id: int, limit: int = 50) -> dict:
        """Retrieve a list of inventory levels for a location."""
        return _get(f"/locations/{location_id}/inventory_levels.json", {"limit": limit})
