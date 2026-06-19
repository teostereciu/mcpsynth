from generated_tools.utils import make_request

def register(mcp):
    @mcp.tool()
    def get_metafields():
        """Retrieve a list of metafields."""
        return make_request("GET", "/metafields.json")

    @mcp.tool()
    def get_metafield(metafield_id: int):
        """Retrieve a single metafield by ID."""
        return make_request("GET", f"/metafields/{metafield_id}.json")

    @mcp.tool()
    def create_metafield(metafield: dict):
        """Create a new metafield."""
        return make_request("POST", "/metafields.json", json_data={"metafield": metafield})

    @mcp.tool()
    def update_metafield(metafield_id: int, metafield: dict):
        """Update an existing metafield."""
        return make_request("PUT", f"/metafields/{metafield_id}.json", json_data={"metafield": metafield})

    @mcp.tool()
    def delete_metafield(metafield_id: int):
        """Delete a metafield."""
        return make_request("DELETE", f"/metafields/{metafield_id}.json")

    @mcp.tool()
    def get_product_metafields(product_id: int):
        """Retrieve a list of metafields for a product."""
        return make_request("GET", f"/products/{product_id}/metafields.json")

    @mcp.tool()
    def create_product_metafield(product_id: int, metafield: dict):
        """Create a new metafield for a product."""
        return make_request("POST", f"/products/{product_id}/metafields.json", json_data={"metafield": metafield})
