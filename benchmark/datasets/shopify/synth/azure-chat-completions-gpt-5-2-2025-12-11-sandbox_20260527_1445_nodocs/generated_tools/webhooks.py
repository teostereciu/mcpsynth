from typing import Any, Dict, Optional

from .client import request_json


def list_webhooks(*, limit: int = 50, topic: Optional[str] = None, address: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"limit": limit}
    if topic:
        params["topic"] = topic
    if address:
        params["address"] = address
    return request_json("GET", "/webhooks.json", params=params)


def get_webhook(webhook_id: int) -> Any:
    return request_json("GET", f"/webhooks/{webhook_id}.json")


def create_webhook(webhook: Dict[str, Any]) -> Any:
    return request_json("POST", "/webhooks.json", json={"webhook": webhook})


def update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/webhooks/{webhook_id}.json", json={"webhook": webhook})


def delete_webhook(webhook_id: int) -> Any:
    return request_json("DELETE", f"/webhooks/{webhook_id}.json")
