from typing import Any, Dict, Optional

from ._client import get_client


def create_webhook(webhook: Dict[str, Any]) -> Dict[str, Any]:
    """POST /webhooks.json

    Doc: docs/api_webhook.md
    Body wrapper: {"webhook": {...}}
    """
    client = get_client()
    return client.request("POST", "/webhooks.json", json={"webhook": webhook})


def list_webhooks(
    *,
    address: Optional[str] = None,
    topic: Optional[str] = None,
    fields: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /webhooks.json

    Doc: docs/api_webhook.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    for k, v in {
        "address": address,
        "topic": topic,
        "fields": fields,
        "limit": limit,
        "since_id": since_id,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/webhooks.json", params=params or None)


def get_webhook(webhook_id: int) -> Dict[str, Any]:
    """GET /webhooks/{webhook_id}.json

    Doc: docs/api_webhook.md
    """
    client = get_client()
    return client.request("GET", f"/webhooks/{webhook_id}.json")


def count_webhooks(*, topic: Optional[str] = None, address: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks/count.json

    Doc: docs/api_webhook.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    if topic is not None:
        params["topic"] = topic
    if address is not None:
        params["address"] = address
    return client.request("GET", "/webhooks/count.json", params=params or None)


def update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /webhooks/{webhook_id}.json

    Doc: docs/api_webhook.md
    Body wrapper: {"webhook": {..., "id": webhook_id}}
    """
    client = get_client()
    body = dict(webhook)
    body.setdefault("id", webhook_id)
    return client.request("PUT", f"/webhooks/{webhook_id}.json", json={"webhook": body})


def delete_webhook(webhook_id: int) -> Dict[str, Any]:
    """DELETE /webhooks/{webhook_id}.json

    Doc: docs/api_webhook.md
    """
    client = get_client()
    return client.request("DELETE", f"/webhooks/{webhook_id}.json")
