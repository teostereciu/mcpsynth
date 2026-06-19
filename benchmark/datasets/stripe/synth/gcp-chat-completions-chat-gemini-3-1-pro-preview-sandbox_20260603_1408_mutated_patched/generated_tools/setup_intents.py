from server import mcp, make_request

@mcp.tool()
def create_setup_intent(customer: str = None, payment_method: str = None, confirm: bool = False) -> dict:
    """Create a SetupIntent."""
    data = {}
    if customer: data["customer"] = customer
    if payment_method: data["payment_method"] = payment_method
    if confirm: data["confirm"] = "true"
    return make_request("POST", "/setup_intents", data=data)

@mcp.tool()
def retrieve_setup_intent(intent_id: str) -> dict:
    """Retrieve a SetupIntent."""
    return make_request("GET", f"/setup_intents/{intent_id}")

@mcp.tool()
def update_setup_intent(intent_id: str, customer: str = None, payment_method: str = None) -> dict:
    """Update a SetupIntent."""
    data = {}
    if customer: data["customer"] = customer
    if payment_method: data["payment_method"] = payment_method
    return make_request("POST", f"/setup_intents/{intent_id}", data=data)

@mcp.tool()
def cancel_setup_intent(intent_id: str, cancellation_reason: str = None) -> dict:
    """Cancel a SetupIntent."""
    data = {}
    if cancellation_reason: data["cancellation_reason"] = cancellation_reason
    return make_request("POST", f"/setup_intents/{intent_id}/cancel", data=data)

@mcp.tool()
def confirm_setup_intent(intent_id: str, payment_method: str = None) -> dict:
    """Confirm a SetupIntent."""
    data = {}
    if payment_method: data["payment_method"] = payment_method
    return make_request("POST", f"/setup_intents/{intent_id}/confirm", data=data)
