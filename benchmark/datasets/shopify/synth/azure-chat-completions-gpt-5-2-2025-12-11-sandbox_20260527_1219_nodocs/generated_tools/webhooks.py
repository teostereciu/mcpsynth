from typing import Any, Dict, Optional

from shopify_client import ShopifyClient, build_pagination_params


def list_webhooks(*, limit: Optional[int] = 50, page_info: Optional[str] = None, since_id: Optional[int] = None, topic: Optional[str] = None, address: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks.json"""
    c = ShopifyClient()
    params = build_pagination_params(limit=limit, page_info=page_info, since_id=since_id)
    if topic is not None:
        params["topic"] = topic
    if address is not None:
        params["address"] = address
    return c.request("GET", "/webhooks.json", params=params)


def get_webhook(*, webhook_id: int) -> Dict[str, Any]:
    """GET /webhooks/{webhook_id}.json"""
    c = ShopifyClient()
    return c.request("GET", f"/webhooks/{webhook_id}.json")


def create_webhook(*, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """POST /webhooks.json"""
    c = ShopifyClient()
    return c.request("POST", "/webhooks.json", json={"webhook": webhook})


def update_webhook(*, webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /webhooks/{webhook_id}.json"""
    c = ShopifyClient()
    body = {"webhook": {**webhook, "id": webhook_id}}
    return c.request("PUT", f"/webhooks/{webhook_id}.json", json=body)


def delete_webhook(*, webhook_id: int) -> Dict[str, Any]:
    """DELETE /webhooks/{webhook_id}.json"""
    c = ShopifyClient()
    return c.request("DELETE", f"/webhooks/{webhook_id}.json")
