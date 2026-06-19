from server import mcp, make_request

@mcp.tool()
def create_account(type: str, country: str = None, email: str = None) -> dict:
    """Create an Account."""
    data = {"type": type}
    if country: data["country"] = country
    if email: data["email"] = email
    return make_request("POST", "/accounts", data=data)

@mcp.tool()
def retrieve_account(account_id: str) -> dict:
    """Retrieve an Account."""
    return make_request("GET", f"/accounts/{account_id}")

@mcp.tool()
def update_account(account_id: str, email: str = None) -> dict:
    """Update an Account."""
    data = {}
    if email: data["email"] = email
    return make_request("POST", f"/accounts/{account_id}", data=data)

@mcp.tool()
def delete_account(account_id: str) -> dict:
    """Delete an Account."""
    return make_request("DELETE", f"/accounts/{account_id}")

@mcp.tool()
def create_transfer(amount: int, currency: str, destination: str, description: str = None) -> dict:
    """Create a Transfer."""
    data = {
        "amount": amount,
        "currency": currency,
        "destination": destination
    }
    if description: data["description"] = description
    return make_request("POST", "/transfers", data=data)

@mcp.tool()
def retrieve_transfer(transfer_id: str) -> dict:
    """Retrieve a Transfer."""
    return make_request("GET", f"/transfers/{transfer_id}")

@mcp.tool()
def update_transfer(transfer_id: str, description: str = None) -> dict:
    """Update a Transfer."""
    data = {}
    if description: data["description"] = description
    return make_request("POST", f"/transfers/{transfer_id}", data=data)

@mcp.tool()
def create_payout(amount: int, currency: str, destination: str = None, method: str = None) -> dict:
    """Create a Payout."""
    data = {
        "amount": amount,
        "currency": currency
    }
    if destination: data["destination"] = destination
    if method: data["method"] = method
    return make_request("POST", "/payouts", data=data)

@mcp.tool()
def retrieve_payout(payout_id: str) -> dict:
    """Retrieve a Payout."""
    return make_request("GET", f"/payouts/{payout_id}")

@mcp.tool()
def update_payout(payout_id: str, metadata: str = None) -> dict:
    """Update a Payout."""
    data = {}
    if metadata: data["metadata"] = metadata
    return make_request("POST", f"/payouts/{payout_id}", data=data)
