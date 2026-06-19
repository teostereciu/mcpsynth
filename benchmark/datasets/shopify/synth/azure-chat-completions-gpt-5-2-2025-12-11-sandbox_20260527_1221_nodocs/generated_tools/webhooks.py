from typing import Any, Dict, Optional

from .client import request_json


def list_webhooks(*, limit: int = 50, since_id: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    return request_json("GET", "/webhooks.json", params=params)


def get_webhook(webhook_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/webhooks/{webhook_id}.json")


def create_webhook(webhook: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/webhooks.json", json_body={"webhook": webhook})


def update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    body = {"webhook": {**webhook, "id": webhook_id}}
    return request_json("PUT", f"/webhooks/{webhook_id}.json", json_body=body)


def delete_webhook(webhook_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/webhooks/{webhook_id}.json")
