from server import mcp, make_request

@mcp.tool()
def create_charge(amount: int, currency: str, source: str = None, customer: str = None, description: str = None) -> dict:
    """Create a Charge."""
    data = {"amount": amount, "currency": currency}
    if source: data["source"] = source
    if customer: data["customer"] = customer
    if description: data["description"] = description
    return make_request("POST", "/charges", data=data)

@mcp.tool()
def retrieve_charge(charge_id: str) -> dict:
    """Retrieve a Charge."""
    return make_request("GET", f"/charges/{charge_id}")

@mcp.tool()
def update_charge(charge_id: str, customer: str = None, description: str = None, receipt_email: str = None) -> dict:
    """Update a Charge."""
    data = {}
    if customer: data["customer"] = customer
    if description: data["description"] = description
    if receipt_email: data["receipt_email"] = receipt_email
    return make_request("POST", f"/charges/{charge_id}", data=data)
