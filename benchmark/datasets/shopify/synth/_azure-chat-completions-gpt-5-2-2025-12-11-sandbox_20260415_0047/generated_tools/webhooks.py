from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import ShopifyClient, unwrap_envelope


@mcp.tool()
def list_webhooks(limit: int = 50, topic: Optional[str] = None) -> List[Dict[str, Any]]:
    """List webhooks (GET /webhooks.json)."""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if topic:
        params["topic"] = topic
    data = client.request("GET", "/webhooks.json", params=params)
    return unwrap_envelope(data)


@mcp.tool()
def get_webhook(webhook_id: Union[int, str]) -> Dict[str, Any]:
    """Get a webhook (GET /webhooks/{id}.json)."""
    client = ShopifyClient()
    data = client.request("GET", f"/webhooks/{webhook_id}.json")
    return unwrap_envelope(data)


@mcp.tool()
def create_webhook(topic: str, address: str, format: str = "json", fields: Optional[List[str]] = None) -> Dict[str, Any]:
    """Create a webhook (POST /webhooks.json)."""
    client = ShopifyClient()
    webhook: Dict[str, Any] = {"topic": topic, "address": address, "format": format}
    if fields is not None:
        webhook["fields"] = fields
    data = client.request("POST", "/webhooks.json", body={"webhook": webhook})
    return unwrap_envelope(data)


@mcp.tool()
def update_webhook(webhook_id: Union[int, str], webhook: Dict[str, Any]) -> Dict[str, Any]:
    """Update a webhook (PUT /webhooks/{id}.json)."""
    client = ShopifyClient()
    payload = dict(webhook)
    payload["id"] = int(webhook_id) if str(webhook_id).isdigit() else webhook_id
    data = client.request("PUT", f"/webhooks/{webhook_id}.json", body={"webhook": payload})
    return unwrap_envelope(data)


@mcp.tool()
def delete_webhook(webhook_id: Union[int, str]) -> Dict[str, Any]:
    """Delete a webhook (DELETE /webhooks/{id}.json)."""
    client = ShopifyClient()
    return client.request("DELETE", f"/webhooks/{webhook_id}.json")
