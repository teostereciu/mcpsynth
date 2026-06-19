from server import mcp, make_request

@mcp.tool()
def create_price(currency: str, unit_amount: int, product: str, recurring_interval: str = None) -> dict:
    """Create a Price."""
    data = {
        "currency": currency,
        "unit_amount": unit_amount,
        "product": product
    }
    if recurring_interval:
        data["recurring[interval]"] = recurring_interval
    return make_request("POST", "/prices", data=data)

@mcp.tool()
def retrieve_price(price_id: str) -> dict:
    """Retrieve a Price."""
    return make_request("GET", f"/prices/{price_id}")

@mcp.tool()
def update_price(price_id: str, active: bool = None) -> dict:
    """Update a Price."""
    data = {}
    if active is not None: data["active"] = "true" if active else "false"
    return make_request("POST", f"/prices/{price_id}", data=data)
