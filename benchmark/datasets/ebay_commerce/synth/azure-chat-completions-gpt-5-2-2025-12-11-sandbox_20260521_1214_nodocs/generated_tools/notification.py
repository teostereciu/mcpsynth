from typing import Any, Dict, Optional

from .ebay_auth import request_json


# Notification API (user token)


def list_subscriptions(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription"""
    status, body = request_json(
        "GET",
        "/commerce/notification/v1/subscription",
        params={"limit": limit, "offset": offset},
        user=True,
    )
    return {"status": status, "data": body}


def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription/{subscriptionId}"""
    status, body = request_json(
        "GET",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        user=True,
    )
    return {"status": status, "data": body}


def create_subscription(topic_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription"""
    status, body = request_json(
        "POST",
        "/commerce/notification/v1/subscription",
        json={"topicId": topic_id, **payload},
        user=True,
    )
    return {"status": status, "data": body}


def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/subscription/{subscriptionId}"""
    status, body = request_json(
        "DELETE",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        user=True,
    )
    return {"status": status, "data": body}


def list_topics() -> Dict[str, Any]:
    """GET /commerce/notification/v1/topic"""
    status, body = request_json(
        "GET",
        "/commerce/notification/v1/topic",
        user=True,
    )
    return {"status": status, "data": body}
