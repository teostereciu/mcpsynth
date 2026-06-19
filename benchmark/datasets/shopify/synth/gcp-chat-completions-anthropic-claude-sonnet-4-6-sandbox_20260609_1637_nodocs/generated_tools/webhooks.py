"""Shopify Admin REST API — Webhooks tools."""

import os, requests
from mcp.server.fastmcp import FastMCP

def _session():
    token = os.environ["SHOPIFY_ACCESS_TOKEN"]
    store = os.environ["SHOPIFY_STORE_URL"]
    base  = f"https://{store}/admin/api/2026-01"
    s = requests.Session()
    s.headers.update({"X-Shopify-Access-Token": token, "Content-Type": "application/json"})
    return s, base

def register(mcp: FastMCP):

    @mcp.tool()
    def list_webhooks(topic: str = "", limit: int = 50) -> dict:
        """List webhooks. Optionally filter by topic (e.g. 'orders/create')."""
        s, base = _session()
        params: dict = {"limit": limit}
        if topic:
            params["topic"] = topic
        r = s.get(f"{base}/webhooks.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_webhook(webhook_id: str) -> dict:
        """Get a webhook by ID."""
        s, base = _session()
        r = s.get(f"{base}/webhooks/{webhook_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_webhook(topic: str, address: str, format: str = "json",
                       fields: list = [], metafield_namespaces: list = []) -> dict:
        """Create a webhook subscription.
        topic examples: orders/create, orders/updated, products/create,
                        customers/create, fulfillments/create, refunds/create,
                        checkouts/create, app/uninstalled."""
        s, base = _session()
        data: dict = {"topic": topic, "address": address, "format": format}
        if fields:                data["fields"]                = fields
        if metafield_namespaces:  data["metafield_namespaces"]  = metafield_namespaces
        r = s.post(f"{base}/webhooks.json", json={"webhook": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_webhook(webhook_id: str, address: str = "",
                       fields: list = []) -> dict:
        """Update a webhook's endpoint URL or fields."""
        s, base = _session()
        data: dict = {}
        if address: data["address"] = address
        if fields:  data["fields"]  = fields
        r = s.put(f"{base}/webhooks/{webhook_id}.json", json={"webhook": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_webhook(webhook_id: str) -> dict:
        """Delete a webhook subscription."""
        s, base = _session()
        r = s.delete(f"{base}/webhooks/{webhook_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "webhook_id": webhook_id}

    @mcp.tool()
    def count_webhooks(topic: str = "") -> dict:
        """Count webhooks, optionally filtered by topic."""
        s, base = _session()
        params = {}
        if topic:
            params["topic"] = topic
        r = s.get(f"{base}/webhooks/count.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()
