from typing import Any, Dict

from .client import request_json


def list_webhooks(limit: int = 50) -> Dict[str, Any]:
    return request_json("GET", "/webhooks.json", params={"limit": limit})


def get_webhook(webhook_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/webhooks/{webhook_id}.json")


def create_webhook(webhook: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/webhooks.json", json={"webhook": webhook})


def update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("PUT", f"/webhooks/{webhook_id}.json", json={"webhook": webhook})


def delete_webhook(webhook_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/webhooks/{webhook_id}.json")
