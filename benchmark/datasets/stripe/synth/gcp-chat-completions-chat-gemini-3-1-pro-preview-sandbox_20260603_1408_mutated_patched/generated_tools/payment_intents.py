from server import mcp, make_request

@mcp.tool()
def create_payment_intent(amount: int, currency: str, customer: str = None, description: str = None, payment_method: str = None, confirm: bool = False) -> dict:
    """Create a PaymentIntent."""
    data = {"amount": amount, "currency": currency}
    if customer: data["customer"] = customer
    if description: data["description"] = description
    if payment_method: data["payment_method"] = payment_method
    if confirm: data["confirm"] = "true"
    return make_request("POST", "/payment_intents", data=data)

@mcp.tool()
def retrieve_payment_intent(intent_id: str) -> dict:
    """Retrieve a PaymentIntent."""
    return make_request("GET", f"/payment_intents/{intent_id}")

@mcp.tool()
def update_payment_intent(intent_id: str, amount: int = None, currency: str = None, customer: str = None, description: str = None) -> dict:
    """Update a PaymentIntent."""
    data = {}
    if amount: data["amount"] = amount
    if currency: data["currency"] = currency
    if customer: data["customer"] = customer
    if description: data["description"] = description
    return make_request("POST", f"/payment_intents/{intent_id}", data=data)

@mcp.tool()
def cancel_payment_intent(intent_id: str, cancellation_reason: str = None) -> dict:
    """Cancel a PaymentIntent."""
    data = {}
    if cancellation_reason: data["cancellation_reason"] = cancellation_reason
    return make_request("POST", f"/payment_intents/{intent_id}/cancel", data=data)

@mcp.tool()
def confirm_payment_intent(intent_id: str, payment_method: str = None) -> dict:
    """Confirm a PaymentIntent."""
    data = {}
    if payment_method: data["payment_method"] = payment_method
    return make_request("POST", f"/payment_intents/{intent_id}/confirm", data=data)
