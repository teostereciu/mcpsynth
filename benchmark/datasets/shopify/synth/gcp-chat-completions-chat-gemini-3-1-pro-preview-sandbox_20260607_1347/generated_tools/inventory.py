from generated_tools.utils import make_request

def register(mcp):
    @mcp.tool()
    def get_inventory_items(ids: str):
        """Retrieve a list of inventory items by comma-separated IDs."""
        return make_request("GET", "/inventory_items.json", params={"ids": ids})

    @mcp.tool()
    def get_inventory_item(inventory_item_id: int):
        """Retrieve a single inventory item by ID."""
        return make_request("GET", f"/inventory_items/{inventory_item_id}.json")

    @mcp.tool()
    def update_inventory_item(inventory_item_id: int, inventory_item: dict):
        """Update an existing inventory item."""
        return make_request("PUT", f"/inventory_items/{inventory_item_id}.json", json_data={"inventory_item": inventory_item})

    @mcp.tool()
    def get_inventory_levels(inventory_item_ids: str = None, location_ids: str = None):
        """Retrieve a list of inventory levels."""
        params = {}
        if inventory_item_ids:
            params["inventory_item_ids"] = inventory_item_ids
        if location_ids:
            params["location_ids"] = location_ids
        return make_request("GET", "/inventory_levels.json", params=params)

    @mcp.tool()
    def set_inventory_level(location_id: int, inventory_item_id: int, available: int):
        """Set the inventory level for an inventory item at a location."""
        data = {
            "location_id": location_id,
            "inventory_item_id": inventory_item_id,
            "available": available
        }
        return make_request("POST", "/inventory_levels/set.json", json_data=data)

    @mcp.tool()
    def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int):
        """Adjust the inventory level for an inventory item at a location."""
        data = {
            "location_id": location_id,
            "inventory_item_id": inventory_item_id,
            "available_adjustment": available_adjustment
        }
        return make_request("POST", "/inventory_levels/adjust.json", json_data=data)
