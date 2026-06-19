from server import mcp, make_request

@mcp.tool()
def create_refund(charge: str = None, payment_intent: str = None, amount: int = None, reason: str = None) -> dict:
    """Create a Refund."""
    data = {}
    if charge: data["charge"] = charge
    if payment_intent: data["payment_intent"] = payment_intent
    if amount: data["amount"] = amount
    if reason: data["reason"] = reason
    return make_request("POST", "/refunds", data=data)

@mcp.tool()
def retrieve_refund(refund_id: str) -> dict:
    """Retrieve a Refund."""
    return make_request("GET", f"/refunds/{refund_id}")

@mcp.tool()
def update_refund(refund_id: str, metadata: str = None) -> dict:
    """Update a Refund."""
    data = {}
    if metadata: data["metadata"] = metadata
    return make_request("POST", f"/refunds/{refund_id}", data=data)
