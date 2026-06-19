import json

def register_tools(mcp, make_request):
    @mcp.tool()
    def get_customers(limit: int = 50, since_id: int = None):
        """Retrieve a list of customers."""
        params = {"limit": limit}
        if since_id: params["since_id"] = since_id
        return make_request("GET", "/customers.json", params=params)

    @mcp.tool()
    def get_customer(customer_id: int):
        """Retrieve a single customer by ID."""
        return make_request("GET", f"/customers/{customer_id}.json")

    @mcp.tool()
    def create_customer(first_name: str, last_name: str, email: str, phone: str = None, tags: str = None):
        """Create a new customer."""
        customer = {"first_name": first_name, "last_name": last_name, "email": email}
        if phone: customer["phone"] = phone
        if tags: customer["tags"] = tags
        return make_request("POST", "/customers.json", json_data={"customer": customer})

    @mcp.tool()
    def update_customer(customer_id: int, first_name: str = None, last_name: str = None, email: str = None, phone: str = None, tags: str = None):
        """Update an existing customer."""
        customer = {"id": customer_id}
        if first_name: customer["first_name"] = first_name
        if last_name: customer["last_name"] = last_name
        if email: customer["email"] = email
        if phone: customer["phone"] = phone
        if tags: customer["tags"] = tags
        return make_request("PUT", f"/customers/{customer_id}.json", json_data={"customer": customer})

    @mcp.tool()
    def delete_customer(customer_id: int):
        """Delete a customer."""
        return make_request("DELETE", f"/customers/{customer_id}.json")

    @mcp.tool()
    def search_customers(query: str):
        """Search for customers matching a query."""
        return make_request("GET", "/customers/search.json", params={"query": query})
