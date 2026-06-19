import json

def register_tools(mcp, make_request):
    @mcp.tool()
    def get_orders(limit: int = 50, status: str = "any", financial_status: str = "any", fulfillment_status: str = "any"):
        """Retrieve a list of orders."""
        params = {
            "limit": limit,
            "status": status,
            "financial_status": financial_status,
            "fulfillment_status": fulfillment_status
        }
        return make_request("GET", "/orders.json", params=params)

    @mcp.tool()
    def get_order(order_id: int):
        """Retrieve a single order by ID."""
        return make_request("GET", f"/orders/{order_id}.json")

    @mcp.tool()
    def create_order(line_items: list, customer: dict = None, financial_status: str = "pending"):
        """Create a new order."""
        order = {"line_items": line_items, "financial_status": financial_status}
        if customer: order["customer"] = customer
        return make_request("POST", "/orders.json", json_data={"order": order})

    @mcp.tool()
    def update_order(order_id: int, note: str = None, tags: str = None):
        """Update an existing order."""
        order = {"id": order_id}
        if note: order["note"] = note
        if tags: order["tags"] = tags
        return make_request("PUT", f"/orders/{order_id}.json", json_data={"order": order})

    @mcp.tool()
    def delete_order(order_id: int):
        """Delete an order."""
        return make_request("DELETE", f"/orders/{order_id}.json")

    # Draft Orders
    @mcp.tool()
    def get_draft_orders(limit: int = 50):
        """Retrieve a list of draft orders."""
        return make_request("GET", "/draft_orders.json", params={"limit": limit})

    @mcp.tool()
    def get_draft_order(draft_order_id: int):
        """Retrieve a single draft order by ID."""
        return make_request("GET", f"/draft_orders/{draft_order_id}.json")

    @mcp.tool()
    def create_draft_order(line_items: list, customer: dict = None, use_customer_default_address: bool = True):
        """Create a new draft order."""
        draft_order = {"line_items": line_items, "use_customer_default_address": use_customer_default_address}
        if customer: draft_order["customer"] = customer
        return make_request("POST", "/draft_orders.json", json_data={"draft_order": draft_order})

    @mcp.tool()
    def complete_draft_order(draft_order_id: int, payment_pending: bool = False):
        """Complete a draft order to create an order."""
        return make_request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params={"payment_pending": payment_pending})

    # Refunds
    @mcp.tool()
    def get_refunds(order_id: int):
        """Retrieve a list of refunds for an order."""
        return make_request("GET", f"/orders/{order_id}/refunds.json")

    @mcp.tool()
    def create_refund(order_id: int, refund_line_items: list, notify: bool = False):
        """Create a refund for an order."""
        refund = {"refund_line_items": refund_line_items, "notify": notify}
        return make_request("POST", f"/orders/{order_id}/refunds.json", json_data={"refund": refund})

    # Transactions
    @mcp.tool()
    def get_transactions(order_id: int):
        """Retrieve a list of transactions for an order."""
        return make_request("GET", f"/orders/{order_id}/transactions.json")

    @mcp.tool()
    def create_transaction(order_id: int, amount: str, kind: str, gateway: str = "bogus"):
        """Create a transaction for an order."""
        transaction = {"amount": amount, "kind": kind, "gateway": gateway}
        return make_request("POST", f"/orders/{order_id}/transactions.json", json_data={"transaction": transaction})
