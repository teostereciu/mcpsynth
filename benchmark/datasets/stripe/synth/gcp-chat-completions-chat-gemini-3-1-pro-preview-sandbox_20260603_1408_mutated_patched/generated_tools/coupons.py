from server import mcp, make_request

@mcp.tool()
def create_coupon(duration: str, percent_off: float = None, amount_off: int = None, currency: str = None, id: str = None) -> dict:
    """Create a Coupon."""
    data = {"duration": duration}
    if percent_off is not None: data["percent_off"] = percent_off
    if amount_off is not None: data["amount_off"] = amount_off
    if currency: data["currency"] = currency
    if id: data["id"] = id
    return make_request("POST", "/coupons", data=data)

@mcp.tool()
def retrieve_coupon(coupon_id: str) -> dict:
    """Retrieve a Coupon."""
    return make_request("GET", f"/coupons/{coupon_id}")

@mcp.tool()
def update_coupon(coupon_id: str, name: str = None) -> dict:
    """Update a Coupon."""
    data = {}
    if name: data["name"] = name
    return make_request("POST", f"/coupons/{coupon_id}", data=data)

@mcp.tool()
def delete_coupon(coupon_id: str) -> dict:
    """Delete a Coupon."""
    return make_request("DELETE", f"/coupons/{coupon_id}")
