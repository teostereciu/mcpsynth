"""Shopify Admin REST API — Webhooks tools."""
import os, requests
from mcp.server.fastmcp import FastMCP

BASE_URL = f"https://{os.environ.get('SHOPIFY_STORE_URL', '')}/admin/api/2026-01"

def _headers():
    return {
        "X-Shopify-Access-Token": os.environ.get("SHOPIFY_ACCESS_TOKEN", ""),
        "Content-Type": "application/json",
    }

def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _post(path, body=None):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=body, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, body):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=body, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _delete(path):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=_headers(), timeout=30)
        if r.status_code == 200:
            return r.json()
        return {"status": r.status_code}
    except Exception as e:
        return {"error": str(e)}


def register_webhooks(mcp: FastMCP):

    @mcp.tool()
    def list_webhooks(
        limit: int = 50,
        topic: str = None,
        address: str = None,
        fields: str = None,
    ) -> dict:
        """Retrieve a list of webhooks. topic example: orders/create, customers/update."""
        params = {"limit": limit}
        if topic: params["topic"] = topic
        if address: params["address"] = address
        if fields: params["fields"] = fields
        return _get("/webhooks.json", params)

    @mcp.tool()
    def get_webhook(webhook_id: int, fields: str = None) -> dict:
        """Retrieve a single webhook by ID."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/webhooks/{webhook_id}.json", params)

    @mcp.tool()
    def count_webhooks(topic: str = None, address: str = None) -> dict:
        """Retrieve a count of webhooks."""
        params = {}
        if topic: params["topic"] = topic
        if address: params["address"] = address
        return _get("/webhooks/count.json", params)

    @mcp.tool()
    def create_webhook(
        topic: str,
        address: str,
        format: str = "json",
        fields: list = None,
        metafield_namespaces: list = None,
    ) -> dict:
        """Create a new webhook subscription.
        topic: e.g. orders/create, products/update, customers/delete.
        address: HTTPS URL, pubsub://project:topic, or ARN for EventBridge."""
        webhook = {"topic": topic, "address": address, "format": format}
        if fields: webhook["fields"] = fields
        if metafield_namespaces: webhook["metafield_namespaces"] = metafield_namespaces
        return _post("/webhooks.json", {"webhook": webhook})

    @mcp.tool()
    def update_webhook(
        webhook_id: int,
        address: str = None,
        fields: list = None,
        metafield_namespaces: list = None,
    ) -> dict:
        """Update an existing webhook subscription."""
        webhook = {}
        if address: webhook["address"] = address
        if fields is not None: webhook["fields"] = fields
        if metafield_namespaces is not None: webhook["metafield_namespaces"] = metafield_namespaces
        return _put(f"/webhooks/{webhook_id}.json", {"webhook": webhook})

    @mcp.tool()
    def delete_webhook(webhook_id: int) -> dict:
        """Delete a webhook subscription."""
        return _delete(f"/webhooks/{webhook_id}.json")
