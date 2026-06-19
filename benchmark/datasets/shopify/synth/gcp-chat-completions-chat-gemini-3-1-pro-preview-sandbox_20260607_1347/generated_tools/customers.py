from generated_tools.utils import make_request

def register(mcp):
    @mcp.tool()
    def get_customers(limit: int = 50):
        """Retrieve a list of customers."""
        return make_request("GET", "/customers.json", params={"limit": limit})

    @mcp.tool()
    def get_customer(customer_id: int):
        """Retrieve a single customer by ID."""
        return make_request("GET", f"/customers/{customer_id}.json")

    @mcp.tool()
    def create_customer(customer: dict):
        """Create a new customer."""
        return make_request("POST", "/customers.json", json_data={"customer": customer})

    @mcp.tool()
    def update_customer(customer_id: int, customer: dict):
        """Update an existing customer."""
        return make_request("PUT", f"/customers/{customer_id}.json", json_data={"customer": customer})

    @mcp.tool()
    def delete_customer(customer_id: int):
        """Delete a customer."""
        return make_request("DELETE", f"/customers/{customer_id}.json")

    @mcp.tool()
    def search_customers(query: str):
        """Search for customers matching a query."""
        return make_request("GET", "/customers/search.json", params={"query": query})
