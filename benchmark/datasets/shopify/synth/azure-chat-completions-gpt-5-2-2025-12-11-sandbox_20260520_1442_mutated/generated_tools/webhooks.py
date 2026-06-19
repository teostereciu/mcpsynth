from typing import Any, Dict, Optional

from .http_client import request_json


def create_webhook(webhook: Dict[str, Any]) -> Dict[str, Any]:
    """POST /webhooks.json

    Doc: docs/api_webhook.md
    Body wrapper: {"webhook": {...}}
    """
    return request_json("POST", "/webhooks.json", json_body={"webhook": webhook})


def list_webhooks(*, address: Optional[str] = None, topic: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks.json

    Doc: docs/api_webhook.md
    """
    params: Dict[str, Any] = {}
    if address is not None:
        params["address"] = address
    if topic is not None:
        params["topic"] = topic
    return request_json("GET", "/webhooks.json", params=params)


def get_webhook(webhook_id: int) -> Dict[str, Any]:
    """GET /webhooks/{webhook_id}.json

    Doc: docs/api_webhook.md
    """
    return request_json("GET", f"/webhooks/{webhook_id}.json")


def count_webhooks(*, topic: Optional[str] = None, address: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks/count.json

    Doc: docs/api_webhook.md
    """
    params: Dict[str, Any] = {}
    if topic is not None:
        params["topic"] = topic
    if address is not None:
        params["address"] = address
    return request_json("GET", "/webhooks/count.json", params=params)


def update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /webhooks/{webhook_id}.json

    Doc: docs/api_webhook.md
    Body wrapper: {"webhook": {...}}
    """
    return request_json("PUT", f"/webhooks/{webhook_id}.json", json_body={"webhook": webhook})


def delete_webhook(webhook_id: int) -> Dict[str, Any]:
    """DELETE /webhooks/{webhook_id}.json

    Doc: docs/api_webhook.md
    """
    return request_json("DELETE", f"/webhooks/{webhook_id}.json")
