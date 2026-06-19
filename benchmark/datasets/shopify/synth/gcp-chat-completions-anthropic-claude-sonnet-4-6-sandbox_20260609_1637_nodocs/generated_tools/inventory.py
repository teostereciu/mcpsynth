"""Shopify Admin REST API — Inventory Items & Levels tools."""

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

    # ── Inventory Items ───────────────────────────────────────────────────────

    @mcp.tool()
    def list_inventory_items(ids: str = "", limit: int = 50) -> dict:
        """List inventory items. ids: comma-separated inventory item IDs."""
        s, base = _session()
        params: dict = {"limit": limit}
        if ids:
            params["ids"] = ids
        r = s.get(f"{base}/inventory_items.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_inventory_item(inventory_item_id: str) -> dict:
        """Get a single inventory item by ID."""
        s, base = _session()
        r = s.get(f"{base}/inventory_items/{inventory_item_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_inventory_item(inventory_item_id: str, sku: str = "",
                              tracked: bool = None, cost: str = "",
                              country_code_of_origin: str = "",
                              province_code_of_origin: str = "") -> dict:
        """Update an inventory item (SKU, tracking, cost, origin)."""
        s, base = _session()
        data: dict = {}
        if sku:                      data["sku"]                      = sku
        if tracked is not None:      data["tracked"]                  = tracked
        if cost:                     data["cost"]                     = cost
        if country_code_of_origin:   data["country_code_of_origin"]   = country_code_of_origin
        if province_code_of_origin:  data["province_code_of_origin"]  = province_code_of_origin
        r = s.put(f"{base}/inventory_items/{inventory_item_id}.json",
                  json={"inventory_item": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    # ── Inventory Levels ──────────────────────────────────────────────────────

    @mcp.tool()
    def list_inventory_levels(inventory_item_ids: str = "",
                              location_ids: str = "", limit: int = 50) -> dict:
        """List inventory levels. Provide inventory_item_ids and/or location_ids
        as comma-separated strings."""
        s, base = _session()
        params: dict = {"limit": limit}
        if inventory_item_ids: params["inventory_item_ids"] = inventory_item_ids
        if location_ids:       params["location_ids"]       = location_ids
        r = s.get(f"{base}/inventory_levels.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def set_inventory_level(inventory_item_id: str, location_id: str,
                            available: int) -> dict:
        """Set the inventory level (available quantity) for an item at a location."""
        s, base = _session()
        r = s.post(f"{base}/inventory_levels/set.json",
                   json={"inventory_item_id": inventory_item_id,
                         "location_id": location_id,
                         "available": available})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def adjust_inventory_level(inventory_item_id: str, location_id: str,
                               available_adjustment: int) -> dict:
        """Adjust inventory level by a relative amount (positive or negative)."""
        s, base = _session()
        r = s.post(f"{base}/inventory_levels/adjust.json",
                   json={"inventory_item_id": inventory_item_id,
                         "location_id": location_id,
                         "available_adjustment": available_adjustment})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def connect_inventory_level(inventory_item_id: str, location_id: str,
                                relocate_if_necessary: bool = False) -> dict:
        """Connect an inventory item to a location."""
        s, base = _session()
        r = s.post(f"{base}/inventory_levels/connect.json",
                   json={"inventory_item_id": inventory_item_id,
                         "location_id": location_id,
                         "relocate_if_necessary": relocate_if_necessary})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_inventory_level(inventory_item_id: str, location_id: str) -> dict:
        """Disconnect an inventory item from a location."""
        s, base = _session()
        r = s.delete(f"{base}/inventory_levels.json",
                     params={"inventory_item_id": inventory_item_id,
                             "location_id": location_id})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "inventory_item_id": inventory_item_id,
                "location_id": location_id}
