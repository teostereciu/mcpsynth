from server import mcp, make_request

@mcp.tool()
def create_product(name: str, description: str = None, active: bool = True) -> dict:
    """Create a Product."""
    data = {"name": name}
    if description: data["description"] = description
    if not active: data["active"] = "false"
    return make_request("POST", "/products", data=data)

@mcp.tool()
def retrieve_product(product_id: str) -> dict:
    """Retrieve a Product."""
    return make_request("GET", f"/products/{product_id}")

@mcp.tool()
def update_product(product_id: str, name: str = None, description: str = None, active: bool = None) -> dict:
    """Update a Product."""
    data = {}
    if name: data["name"] = name
    if description: data["description"] = description
    if active is not None: data["active"] = "true" if active else "false"
    return make_request("POST", f"/products/{product_id}", data=data)

@mcp.tool()
def delete_product(product_id: str) -> dict:
    """Delete a Product."""
    return make_request("DELETE", f"/products/{product_id}")
