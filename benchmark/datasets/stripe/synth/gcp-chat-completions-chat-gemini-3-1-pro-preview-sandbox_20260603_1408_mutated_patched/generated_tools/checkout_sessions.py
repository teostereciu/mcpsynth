from server import mcp, make_request

@mcp.tool()
def create_checkout_session(success_url: str, cancel_url: str, mode: str = "payment", price: str = None, quantity: int = 1, customer: str = None) -> dict:
    """Create a Checkout Session."""
    data = {
        "success_url": success_url,
        "cancel_url": cancel_url,
        "mode": mode
    }
    if price:
        data["line_items[0][price]"] = price
        data["line_items[0][quantity]"] = quantity
    if customer:
        data["customer"] = customer
    return make_request("POST", "/checkout/sessions", data=data)

@mcp.tool()
def retrieve_checkout_session(session_id: str) -> dict:
    """Retrieve a Checkout Session."""
    return make_request("GET", f"/checkout/sessions/{session_id}")
