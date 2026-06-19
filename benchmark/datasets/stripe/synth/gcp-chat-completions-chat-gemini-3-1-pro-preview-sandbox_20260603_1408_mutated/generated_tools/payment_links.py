from server import mcp, make_request

@mcp.tool()
def create_payment_link(price: str, quantity: int = 1) -> dict:
    """Create a Payment Link."""
    data = {
        "line_items[0][price]": price,
        "line_items[0][quantity]": quantity
    }
    return make_request("POST", "/payment_links", data=data)

@mcp.tool()
def retrieve_payment_link(payment_link_id: str) -> dict:
    """Retrieve a Payment Link."""
    return make_request("GET", f"/payment_links/{payment_link_id}")

@mcp.tool()
def update_payment_link(payment_link_id: str, active: bool = None) -> dict:
    """Update a Payment Link."""
    data = {}
    if active is not None:
        data["active"] = "true" if active else "false"
    return make_request("POST", f"/payment_links/{payment_link_id}", data=data)
