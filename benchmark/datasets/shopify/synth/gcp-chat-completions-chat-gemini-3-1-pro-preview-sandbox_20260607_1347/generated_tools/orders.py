from generated_tools.utils import make_request

def register(mcp):
    @mcp.tool()
    def get_orders(limit: int = 50, status: str = "any"):
        """Retrieve a list of orders."""
        params = {"limit": limit, "status": status}
        return make_request("GET", "/orders.json", params=params)

    @mcp.tool()
    def get_order(order_id: int):
        """Retrieve a single order by ID."""
        return make_request("GET", f"/orders/{order_id}.json")

    @mcp.tool()
    def create_order(order: dict):
        """Create a new order."""
        return make_request("POST", "/orders.json", json_data={"order": order})

    @mcp.tool()
    def update_order(order_id: int, order: dict):
        """Update an existing order."""
        return make_request("PUT", f"/orders/{order_id}.json", json_data={"order": order})

    @mcp.tool()
    def delete_order(order_id: int):
        """Delete an order."""
        return make_request("DELETE", f"/orders/{order_id}.json")

    @mcp.tool()
    def get_draft_orders(limit: int = 50):
        """Retrieve a list of draft orders."""
        return make_request("GET", "/draft_orders.json", params={"limit": limit})

    @mcp.tool()
    def get_draft_order(draft_order_id: int):
        """Retrieve a single draft order by ID."""
        return make_request("GET", f"/draft_orders/{draft_order_id}.json")

    @mcp.tool()
    def create_draft_order(draft_order: dict):
        """Create a new draft order."""
        return make_request("POST", "/draft_orders.json", json_data={"draft_order": draft_order})

    @mcp.tool()
    def update_draft_order(draft_order_id: int, draft_order: dict):
        """Update an existing draft order."""
        return make_request("PUT", f"/draft_orders/{draft_order_id}.json", json_data={"draft_order": draft_order})

    @mcp.tool()
    def delete_draft_order(draft_order_id: int):
        """Delete a draft order."""
        return make_request("DELETE", f"/draft_orders/{draft_order_id}.json")

    @mcp.tool()
    def get_order_refunds(order_id: int):
        """Retrieve a list of refunds for an order."""
        return make_request("GET", f"/orders/{order_id}/refunds.json")

    @mcp.tool()
    def create_order_refund(order_id: int, refund: dict):
        """Create a refund for an order."""
        return make_request("POST", f"/orders/{order_id}/refunds.json", json_data={"refund": refund})

    @mcp.tool()
    def get_order_transactions(order_id: int):
        """Retrieve a list of transactions for an order."""
        return make_request("GET", f"/orders/{order_id}/transactions.json")

    @mcp.tool()
    def create_order_transaction(order_id: int, transaction: dict):
        """Create a transaction for an order."""
        return make_request("POST", f"/orders/{order_id}/transactions.json", json_data={"transaction": transaction})
