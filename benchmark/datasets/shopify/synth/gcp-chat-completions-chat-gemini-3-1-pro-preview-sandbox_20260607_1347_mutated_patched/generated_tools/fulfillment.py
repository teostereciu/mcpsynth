import json

def register_tools(mcp, make_request):
    @mcp.tool()
    def get_fulfillments(order_id: int):
        """Retrieve a list of fulfillments for an order."""
        return make_request("GET", f"/orders/{order_id}/fulfillments.json")

    @mcp.tool()
    def get_fulfillment(order_id: int, fulfillment_id: int):
        """Retrieve a single fulfillment by ID."""
        return make_request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")

    @mcp.tool()
    def create_fulfillment(order_id: int, location_id: int, tracking_number: str = None, tracking_urls: list = None, line_items: list = None):
        """Create a new fulfillment for an order."""
        fulfillment = {"location_id": location_id}
        if tracking_number: fulfillment["tracking_number"] = tracking_number
        if tracking_urls: fulfillment["tracking_urls"] = tracking_urls
        if line_items: fulfillment["line_items"] = line_items
        return make_request("POST", f"/orders/{order_id}/fulfillments.json", json_data={"fulfillment": fulfillment})

    @mcp.tool()
    def update_fulfillment(order_id: int, fulfillment_id: int, tracking_number: str = None, tracking_urls: list = None):
        """Update an existing fulfillment."""
        fulfillment = {"id": fulfillment_id}
        if tracking_number: fulfillment["tracking_number"] = tracking_number
        if tracking_urls: fulfillment["tracking_urls"] = tracking_urls
        return make_request("PUT", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json", json_data={"fulfillment": fulfillment})

    @mcp.tool()
    def cancel_fulfillment(order_id: int, fulfillment_id: int):
        """Cancel a fulfillment."""
        return make_request("POST", f"/orders/{order_id}/fulfillments/{fulfillment_id}/cancel.json")

    # Fulfillment Orders
    @mcp.tool()
    def get_fulfillment_orders(order_id: int):
        """Retrieve a list of fulfillment orders for an order."""
        return make_request("GET", f"/orders/{order_id}/fulfillment_orders.json")

    @mcp.tool()
    def get_fulfillment_order(fulfillment_order_id: int):
        """Retrieve a single fulfillment order by ID."""
        return make_request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")

    @mcp.tool()
    def cancel_fulfillment_order(fulfillment_order_id: int):
        """Cancel a fulfillment order."""
        return make_request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json")

    # Locations
    @mcp.tool()
    def get_locations():
        """Retrieve a list of locations."""
        return make_request("GET", "/locations.json")

    @mcp.tool()
    def get_location(location_id: int):
        """Retrieve a single location by ID."""
        return make_request("GET", f"/locations/{location_id}.json")
