from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import shopify_request, unwrap_envelope


@mcp.tool()
def list_webhooks(limit: int = 250, topic: Optional[str] = None) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List webhook subscriptions for the app."""

    params: Dict[str, Any] = {"limit": limit}
    if topic:
        params["topic"] = topic

    data = shopify_request("GET", "/webhooks.json", params=params)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def get_webhook(webhook_id: Union[int, str]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Get a webhook subscription."""

    data = shopify_request("GET", f"/webhooks/{webhook_id}.json")
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def create_webhook(topic: str, address: str, format: str = "json", fields: Optional[List[str]] = None) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Create a webhook subscription."""

    webhook: Dict[str, Any] = {"topic": topic, "address": address, "format": format}
    if fields is not None:
        webhook["fields"] = fields

    data = shopify_request("POST", "/webhooks.json", body={"webhook": webhook})
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def update_webhook(webhook_id: Union[int, str], webhook: Dict[str, Any]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Update a webhook subscription."""

    payload = dict(webhook)
    payload["id"] = int(webhook_id) if str(webhook_id).isdigit() else webhook_id
    data = shopify_request("PUT", f"/webhooks/{webhook_id}.json", body={"webhook": payload})
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def delete_webhook(webhook_id: Union[int, str]) -> Dict[str, Any]:
    """Delete a webhook subscription."""

    data = shopify_request("DELETE", f"/webhooks/{webhook_id}.json")
    if "error" in data:
        return data
    return {"ok": True}


@mcp.tool()
def count_webhooks(topic: Optional[str] = None) -> Union[int, Dict[str, Any]]:
    """Count webhook subscriptions."""

    params = {"topic": topic} if topic else None
    data = shopify_request("GET", "/webhooks/count.json", params=params)
    if "error" in data:
        return data
    unwrapped = unwrap_envelope(data)
    if isinstance(unwrapped, dict) and "count" in unwrapped:
        return int(unwrapped["count"])
    return unwrapped
