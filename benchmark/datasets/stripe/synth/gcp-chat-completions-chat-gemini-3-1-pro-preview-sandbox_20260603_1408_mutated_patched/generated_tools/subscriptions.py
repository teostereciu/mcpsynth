from server import mcp, make_request

@mcp.tool()
def create_subscription(customer: str, price: str) -> dict:
    """Create a Subscription."""
    data = {
        "customer": customer,
        "items[0][price]": price
    }
    return make_request("POST", "/subscriptions", data=data)

@mcp.tool()
def retrieve_subscription(subscription_id: str) -> dict:
    """Retrieve a Subscription."""
    return make_request("GET", f"/subscriptions/{subscription_id}")

@mcp.tool()
def update_subscription(subscription_id: str, cancel_at_period_end: bool = None) -> dict:
    """Update a Subscription."""
    data = {}
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = "true" if cancel_at_period_end else "false"
    return make_request("POST", f"/subscriptions/{subscription_id}", data=data)

@mcp.tool()
def cancel_subscription(subscription_id: str) -> dict:
    """Cancel a Subscription."""
    return make_request("DELETE", f"/subscriptions/{subscription_id}")
