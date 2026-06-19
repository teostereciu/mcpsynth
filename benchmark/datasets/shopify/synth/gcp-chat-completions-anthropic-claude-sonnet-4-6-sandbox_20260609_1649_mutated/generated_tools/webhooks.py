"""Shopify Admin REST API — Webhooks tools."""
import os, requests
from typing import Optional, Any

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

def _post(path, payload):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=payload, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, payload):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=payload, timeout=30)
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


def list_webhooks(topic: Optional[str] = None, limit: int = 50) -> dict:
    """Retrieve a list of webhooks. Optionally filter by topic."""
    params: dict[str, Any] = {"limit": limit}
    if topic: params["topic"] = topic
    return _get("/webhooks.json", params)

def get_webhook(webhook_id: int) -> dict:
    """Retrieve a single webhook by ID."""
    return _get(f"/webhooks/{webhook_id}.json")

def count_webhooks(topic: Optional[str] = None) -> dict:
    """Retrieve a count of webhooks."""
    params: dict[str, Any] = {}
    if topic: params["topic"] = topic
    return _get("/webhooks/count.json", params)

def create_webhook(topic: str, address: str, format: str = "json",
                   fields: Optional[list] = None,
                   metafield_namespaces: Optional[list] = None) -> dict:
    """Create a new webhook subscription.
    topic: e.g. orders/create, products/update, customers/delete, etc.
    address: destination URL (HTTPS), pubsub://, or ARN
    format: json|xml
    fields: optional list of fields to include in payload
    """
    webhook: dict[str, Any] = {
        "topic": topic,
        "address": address,
        "format": format,
    }
    if fields: webhook["fields"] = fields
    if metafield_namespaces: webhook["metafield_namespaces"] = metafield_namespaces
    return _post("/webhooks.json", {"webhook": webhook})

def update_webhook(webhook_id: int, address: Optional[str] = None,
                   fields: Optional[list] = None,
                   metafield_namespaces: Optional[list] = None) -> dict:
    """Update an existing webhook."""
    webhook: dict[str, Any] = {"id": webhook_id}
    if address is not None: webhook["address"] = address
    if fields is not None: webhook["fields"] = fields
    if metafield_namespaces is not None: webhook["metafield_namespaces"] = metafield_namespaces
    return _put(f"/webhooks/{webhook_id}.json", {"webhook": webhook})

def delete_webhook(webhook_id: int) -> dict:
    """Delete a webhook subscription."""
    return _delete(f"/webhooks/{webhook_id}.json")
