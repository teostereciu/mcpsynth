from typing import Any, Dict, Optional

from .client import ShopifyClient, build_params


def create_webhook(webhook: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /webhooks.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/webhooks.json", json_body={"webhook": webhook})


def list_webhooks(
    *,
    client: Optional[ShopifyClient] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    topic: Optional[str] = None,
    address: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /webhooks.json"""
    client = client or ShopifyClient()
    return client.request(
        "GET",
        "/webhooks.json",
        params=build_params(limit=limit, since_id=since_id, topic=topic, address=address),
    )


def get_webhook(webhook_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/webhooks/{webhook_id}.json")


def count_webhooks(*, client: Optional[ShopifyClient] = None, topic: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/webhooks/count.json", params=build_params(topic=topic))


def update_webhook(webhook_id: int, webhook: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    body = {"webhook": {**webhook, "id": webhook_id}}
    return client.request("PUT", f"/webhooks/{webhook_id}.json", json_body=body)


def delete_webhook(webhook_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/webhooks/{webhook_id}.json")
