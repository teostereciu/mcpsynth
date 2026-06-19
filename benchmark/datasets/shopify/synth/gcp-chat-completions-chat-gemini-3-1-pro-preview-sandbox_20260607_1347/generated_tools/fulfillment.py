from generated_tools.utils import make_request

def register(mcp):
    @mcp.tool()
    def get_locations():
        """Retrieve a list of locations."""
        return make_request("GET", "/locations.json")

    @mcp.tool()
    def get_location(location_id: int):
        """Retrieve a single location by ID."""
        return make_request("GET", f"/locations/{location_id}.json")

    @mcp.tool()
    def get_order_fulfillments(order_id: int):
        """Retrieve a list of fulfillments for an order."""
        return make_request("GET", f"/orders/{order_id}/fulfillments.json")

    @mcp.tool()
    def create_order_fulfillment(order_id: int, fulfillment: dict):
        """Create a fulfillment for an order."""
        return make_request("POST", f"/orders/{order_id}/fulfillments.json", json_data={"fulfillment": fulfillment})

    @mcp.tool()
    def update_order_fulfillment(order_id: int, fulfillment_id: int, fulfillment: dict):
        """Update a fulfillment for an order."""
        return make_request("PUT", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json", json_data={"fulfillment": fulfillment})

    @mcp.tool()
    def get_fulfillment_orders(order_id: int):
        """Retrieve a list of fulfillment orders for an order."""
        return make_request("GET", f"/orders/{order_id}/fulfillment_orders.json")

    @mcp.tool()
    def get_fulfillment_order(fulfillment_order_id: int):
        """Retrieve a single fulfillment order by ID."""
        return make_request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")
