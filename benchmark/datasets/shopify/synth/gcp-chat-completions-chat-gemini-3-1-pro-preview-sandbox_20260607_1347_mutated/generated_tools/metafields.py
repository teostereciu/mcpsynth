import json

def register_tools(mcp, make_request):
    @mcp.tool()
    def get_metafields(limit: int = 50, namespace: str = None, key: str = None):
        """Retrieve a list of metafields for the shop."""
        params = {"limit": limit}
        if namespace: params["namespace"] = namespace
        if key: params["key"] = key
        return make_request("GET", "/metafields.json", params=params)

    @mcp.tool()
    def get_metafield(metafield_id: int):
        """Retrieve a single metafield by ID."""
        return make_request("GET", f"/metafields/{metafield_id}.json")

    @mcp.tool()
    def create_metafield(namespace: str, key: str, value: str, type: str = "single_line_text_field"):
        """Create a new metafield for the shop."""
        metafield = {
            "namespace": namespace,
            "key": key,
            "value": value,
            "type": type
        }
        return make_request("POST", "/metafields.json", json_data={"metafield": metafield})

    @mcp.tool()
    def update_metafield(metafield_id: int, value: str, type: str = None):
        """Update an existing metafield."""
        metafield = {"id": metafield_id, "value": value}
        if type: metafield["type"] = type
        return make_request("PUT", f"/metafields/{metafield_id}.json", json_data={"metafield": metafield})

    @mcp.tool()
    def delete_metafield(metafield_id: int):
        """Delete a metafield."""
        return make_request("DELETE", f"/metafields/{metafield_id}.json")

    # Resource Metafields (e.g., Product Metafields)
    @mcp.tool()
    def get_resource_metafields(resource: str, resource_id: int, limit: int = 50):
        """Retrieve a list of metafields for a specific resource (e.g., resource='products', resource_id=123)."""
        return make_request("GET", f"/{resource}/{resource_id}/metafields.json", params={"limit": limit})

    @mcp.tool()
    def create_resource_metafield(resource: str, resource_id: int, namespace: str, key: str, value: str, type: str = "single_line_text_field"):
        """Create a new metafield for a specific resource."""
        metafield = {
            "namespace": namespace,
            "key": key,
            "value": value,
            "type": type
        }
        return make_request("POST", f"/{resource}/{resource_id}/metafields.json", json_data={"metafield": metafield})
