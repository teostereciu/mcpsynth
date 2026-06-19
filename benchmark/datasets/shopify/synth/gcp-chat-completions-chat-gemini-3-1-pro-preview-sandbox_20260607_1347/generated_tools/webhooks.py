from generated_tools.utils import make_request

def register(mcp):
    @mcp.tool()
    def get_webhooks():
        """Retrieve a list of webhooks."""
        return make_request("GET", "/webhooks.json")

    @mcp.tool()
    def get_webhook(webhook_id: int):
        """Retrieve a single webhook by ID."""
        return make_request("GET", f"/webhooks/{webhook_id}.json")

    @mcp.tool()
    def create_webhook(webhook: dict):
        """Create a new webhook."""
        return make_request("POST", "/webhooks.json", json_data={"webhook": webhook})

    @mcp.tool()
    def update_webhook(webhook_id: int, webhook: dict):
        """Update an existing webhook."""
        return make_request("PUT", f"/webhooks/{webhook_id}.json", json_data={"webhook": webhook})

    @mcp.tool()
    def delete_webhook(webhook_id: int):
        """Delete a webhook."""
        return make_request("DELETE", f"/webhooks/{webhook_id}.json")
