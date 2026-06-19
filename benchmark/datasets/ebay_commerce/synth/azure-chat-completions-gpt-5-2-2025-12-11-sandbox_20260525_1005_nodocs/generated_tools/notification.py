from typing import Any, Dict, Optional

from .ebay_auth import auth_header, get_base_url, request_json


# Notification API (user token)


def get_public_key() -> Dict[str, Any]:
    """GET /commerce/notification/v1/public_key"""
    url = get_base_url() + "/commerce/notification/v1/public_key"
    res, err = request_json("GET", url, headers={**auth_header(user=True)})
    return err or res  # type: ignore


def get_subscriptions(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription"""
    url = get_base_url() + "/commerce/notification/v1/subscription"
    params = {"limit": limit, "offset": offset}
    res, err = request_json("GET", url, headers={**auth_header(user=True)}, params=params)
    return err or res  # type: ignore


def create_subscription(
    topic_id: str,
    notification_endpoint: str,
    payload_version: str = "1.0",
    filter: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription"""
    url = get_base_url() + "/commerce/notification/v1/subscription"
    body: Dict[str, Any] = {
        "topicId": topic_id,
        "payloadVersion": payload_version,
        "destination": {"endpoint": notification_endpoint},
    }
    if filter is not None:
        body["filter"] = filter
    res, err = request_json("POST", url, headers={**auth_header(user=True), "Content-Type": "application/json"}, json=body)
    return err or res  # type: ignore


def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription/{subscriptionId}"""
    url = get_base_url() + f"/commerce/notification/v1/subscription/{subscription_id}"
    res, err = request_json("GET", url, headers={**auth_header(user=True)})
    return err or res  # type: ignore


def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/subscription/{subscriptionId}"""
    url = get_base_url() + f"/commerce/notification/v1/subscription/{subscription_id}"
    res, err = request_json("DELETE", url, headers={**auth_header(user=True)})
    return err or res  # type: ignore
