from server import mcp, make_request

@mcp.tool()
def create_promotion_code(coupon: str, code: str = None, active: bool = True) -> dict:
    """Create a Promotion Code."""
    data = {"coupon": coupon}
    if code: data["code"] = code
    if not active: data["active"] = "false"
    return make_request("POST", "/promotion_codes", data=data)

@mcp.tool()
def retrieve_promotion_code(promotion_code_id: str) -> dict:
    """Retrieve a Promotion Code."""
    return make_request("GET", f"/promotion_codes/{promotion_code_id}")

@mcp.tool()
def update_promotion_code(promotion_code_id: str, active: bool = None) -> dict:
    """Update a Promotion Code."""
    data = {}
    if active is not None: data["active"] = "true" if active else "false"
    return make_request("POST", f"/promotion_codes/{promotion_code_id}", data=data)
