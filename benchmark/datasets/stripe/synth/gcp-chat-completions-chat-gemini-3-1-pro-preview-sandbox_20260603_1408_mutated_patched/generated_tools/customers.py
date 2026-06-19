from server import mcp, make_request

@mcp.tool()
def create_customer(email: str = None, name: str = None, description: str = None, phone: str = None) -> dict:
    """Create a Customer."""
    data = {}
    if email: data["email"] = email
    if name: data["name"] = name
    if description: data["description"] = description
    if phone: data["phone"] = phone
    return make_request("POST", "/customers", data=data)

@mcp.tool()
def retrieve_customer(customer_id: str) -> dict:
    """Retrieve a Customer."""
    return make_request("GET", f"/customers/{customer_id}")

@mcp.tool()
def update_customer(customer_id: str, email: str = None, name: str = None, description: str = None, phone: str = None) -> dict:
    """Update a Customer."""
    data = {}
    if email: data["email"] = email
    if name: data["name"] = name
    if description: data["description"] = description
    if phone: data["phone"] = phone
    return make_request("POST", f"/customers/{customer_id}", data=data)

@mcp.tool()
def delete_customer(customer_id: str) -> dict:
    """Delete a Customer."""
    return make_request("DELETE", f"/customers/{customer_id}")
