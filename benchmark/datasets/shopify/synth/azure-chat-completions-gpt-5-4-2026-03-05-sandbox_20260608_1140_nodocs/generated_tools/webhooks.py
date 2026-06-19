from typing import Any, Dict, Optional

from generated_tools.common import clean_params, shopify_request


def list_webhooks(limit: Optional[int] = None, topic: Optional[str] = None, address: Optional[str] = None) -> Any:
    params = clean_params(limit=limit, topic=topic, address=address)
    return shopify_request("GET", "/webhooks.json", params=params)


def get_webhook(webhook_id: int) -> Any:
    return shopify_request("GET", f"/webhooks/{webhook_id}.json")


def create_webhook(webhook: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/webhooks.json", json_body={"webhook": webhook})


def update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Any:
    body = {"webhook": {"id": webhook_id, **webhook}}
    return shopify_request("PUT", f"/webhooks/{webhook_id}.json", json_body=body)


def delete_webhook(webhook_id: int) -> Any:
    return shopify_request("DELETE", f"/webhooks/{webhook_id}.json")
