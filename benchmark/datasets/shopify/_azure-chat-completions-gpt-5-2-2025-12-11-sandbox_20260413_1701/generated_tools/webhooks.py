from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp, client


@mcp.tool()
def list_webhooks(limit: int = 50, topic: Optional[str] = None, address: Optional[str] = None) -> List[Dict[str, Any]]:
    """Retrieve a list of webhooks."""
    params: Dict[str, Any] = {"limit": limit}
    if topic is not None:
        params["topic"] = topic
    if address is not None:
        params["address"] = address
    return client.request("GET", "/webhooks.json", params=params)


@mcp.tool()
def get_webhook(webhook_id: Union[int, str]) -> Dict[str, Any]:
    """Retrieve a single webhook."""
    return client.request("GET", f"/webhooks/{webhook_id}.json")


@mcp.tool()
def count_webhooks(topic: Optional[str] = None) -> Dict[str, Any]:
    """Receive a count of all webhooks."""
    params = {"topic": topic} if topic else None
    return client.request("GET", "/webhooks/count.json", params=params)


@mcp.tool()
def create_webhook(
    topic: str,
    address: str,
    format: str = "json",
    fields: Optional[List[str]] = None,
    metafield_namespaces: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Create a new webhook."""
    webhook: Dict[str, Any] = {"topic": topic, "address": address, "format": format}
    if fields is not None:
        webhook["fields"] = fields
    if metafield_namespaces is not None:
        webhook["metafield_namespaces"] = metafield_namespaces
    return client.request("POST", "/webhooks.json", body={"webhook": webhook})


@mcp.tool()
def update_webhook(webhook_id: Union[int, str], webhook: Dict[str, Any]) -> Dict[str, Any]:
    """Modify an existing webhook."""
    payload = dict(webhook)
    payload["id"] = int(webhook_id) if str(webhook_id).isdigit() else webhook_id
    return client.request("PUT", f"/webhooks/{webhook_id}.json", body={"webhook": payload})


@mcp.tool()
def delete_webhook(webhook_id: Union[int, str]) -> Dict[str, Any]:
    """Remove an existing webhook."""
    return client.request("DELETE", f"/webhooks/{webhook_id}.json", unwrap=False)
