from typing import Any, Dict, Optional

from ._client import get_client


def create_webhook(webhook: Dict[str, Any]) -> Dict[str, Any]:
    """POST /webhooks.json

    Doc: docs/api_webhook.md
    """
    return get_client().request("POST", "/webhooks.json", json_body={"webhook": webhook})


def list_webhooks(*, limit: Optional[int] = None, since_id: Optional[int] = None, topic: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks.json

    Doc: docs/api_webhook.md
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    if topic is not None:
        params["topic"] = topic
    return get_client().request("GET", "/webhooks.json", params=params)


def get_webhook(webhook_id: int) -> Dict[str, Any]:
    """GET /webhooks/{webhook_id}.json

    Doc: docs/api_webhook.md
    """
    return get_client().request("GET", f"/webhooks/{webhook_id}.json")


def count_webhooks(*, topic: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks/count.json

    Doc: docs/api_webhook.md
    """
    params: Dict[str, Any] = {}
    if topic is not None:
        params["topic"] = topic
    return get_client().request("GET", "/webhooks/count.json", params=params)


def update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /webhooks/{webhook_id}.json

    Doc: docs/api_webhook.md
    """
    return get_client().request("PUT", f"/webhooks/{webhook_id}.json", json_body={"webhook": {**webhook, "id": webhook_id}})


def delete_webhook(webhook_id: int) -> Dict[str, Any]:
    """DELETE /webhooks/{webhook_id}.json

    Doc: docs/api_webhook.md
    """
    return get_client().request("DELETE", f"/webhooks/{webhook_id}.json")
