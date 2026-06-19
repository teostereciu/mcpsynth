import json

def register_tools(mcp, make_request):
    @mcp.tool()
    def get_webhooks(limit: int = 50, topic: str = None):
        """Retrieve a list of webhooks."""
        params = {"limit": limit}
        if topic: params["topic"] = topic
        return make_request("GET", "/webhooks.json", params=params)

    @mcp.tool()
    def get_webhook(webhook_id: int):
        """Retrieve a single webhook by ID."""
        return make_request("GET", f"/webhooks/{webhook_id}.json")

    @mcp.tool()
    def create_webhook(topic: str, address: str, format: str = "json"):
        """Create a new webhook."""
        webhook = {"topic": topic, "address": address, "format": format}
        return make_request("POST", "/webhooks.json", json_data={"webhook": webhook})

    @mcp.tool()
    def update_webhook(webhook_id: int, address: str = None, topic: str = None):
        """Update an existing webhook."""
        webhook = {"id": webhook_id}
        if address: webhook["address"] = address
        if topic: webhook["topic"] = topic
        return make_request("PUT", f"/webhooks/{webhook_id}.json", json_data={"webhook": webhook})

    @mcp.tool()
    def delete_webhook(webhook_id: int):
        """Delete a webhook."""
        return make_request("DELETE", f"/webhooks/{webhook_id}.json")
