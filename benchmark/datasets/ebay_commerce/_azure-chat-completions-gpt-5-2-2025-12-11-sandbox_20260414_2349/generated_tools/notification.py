from __future__ import annotations

from typing import Any, Dict, Optional

from .http import commerce_base_url, request_json


API_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_config() -> Dict[str, Any]:
    """GET /commerce/notification/v1/config (user token in practice; docs show api_scope).

    We'll use user_auth=True because notification management is typically user-context.
    """
    return request_json(
        "GET",
        commerce_base_url(),
        "/commerce/notification/v1/config",
        user_auth=True,
        scope=API_SCOPE,
    )


def update_config(payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/config"""
    return request_json(
        "PUT",
        commerce_base_url(),
        "/commerce/notification/v1/config",
        json_body=payload,
        user_auth=True,
        scope=API_SCOPE,
    )


def get_destinations(limit: int = 20, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    """GET /commerce/notification/v1/destination"""
    params: Dict[str, Any] = {"limit": limit}
    if continuation_token:
        params["continuation_token"] = continuation_token
    return request_json(
        "GET",
        commerce_base_url(),
        "/commerce/notification/v1/destination",
        params=params,
        user_auth=True,
        scope=API_SCOPE,
    )


def get_destination(destination_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/destination/{destination_id}"""
    return request_json(
        "GET",
        commerce_base_url(),
        f"/commerce/notification/v1/destination/{destination_id}",
        user_auth=True,
        scope=API_SCOPE,
    )


def create_destination(name: str, endpoint: str, verification_token: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/destination"""
    body = {"name": name, "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token}}
    return request_json(
        "POST",
        commerce_base_url(),
        "/commerce/notification/v1/destination",
        json_body=body,
        user_auth=True,
        scope=API_SCOPE,
    )


def update_destination(destination_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/destination/{destination_id}"""
    return request_json(
        "PUT",
        commerce_base_url(),
        f"/commerce/notification/v1/destination/{destination_id}",
        json_body=payload,
        user_auth=True,
        scope=API_SCOPE,
    )


def delete_destination(destination_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/destination/{destination_id}"""
    return request_json(
        "DELETE",
        commerce_base_url(),
        f"/commerce/notification/v1/destination/{destination_id}",
        user_auth=True,
        scope=API_SCOPE,
    )


def get_topics(limit: int = 20, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    """GET /commerce/notification/v1/topic"""
    params: Dict[str, Any] = {"limit": limit}
    if continuation_token:
        params["continuation_token"] = continuation_token
    return request_json(
        "GET",
        commerce_base_url(),
        "/commerce/notification/v1/topic",
        params=params,
        user_auth=True,
        scope=API_SCOPE,
    )


def get_topic(topic_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/topic/{topic_id}"""
    return request_json(
        "GET",
        commerce_base_url(),
        f"/commerce/notification/v1/topic/{topic_id}",
        user_auth=True,
        scope=API_SCOPE,
    )


def get_subscriptions(limit: int = 20, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription"""
    params: Dict[str, Any] = {"limit": limit}
    if continuation_token:
        params["continuation_token"] = continuation_token
    return request_json(
        "GET",
        commerce_base_url(),
        "/commerce/notification/v1/subscription",
        params=params,
        user_auth=True,
        scope=API_SCOPE,
    )


def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription/{subscription_id}"""
    return request_json(
        "GET",
        commerce_base_url(),
        f"/commerce/notification/v1/subscription/{subscription_id}",
        user_auth=True,
        scope=API_SCOPE,
    )


def create_subscription(topic_id: str, destination_id: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription

    payload may include: status, payload fields, etc.
    """
    body: Dict[str, Any] = {"topicId": topic_id, "destinationId": destination_id}
    if payload:
        body.update(payload)
    return request_json(
        "POST",
        commerce_base_url(),
        "/commerce/notification/v1/subscription",
        json_body=body,
        user_auth=True,
        scope=API_SCOPE,
    )


def update_subscription(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/subscription/{subscription_id}"""
    return request_json(
        "PUT",
        commerce_base_url(),
        f"/commerce/notification/v1/subscription/{subscription_id}",
        json_body=payload,
        user_auth=True,
        scope=API_SCOPE,
    )


def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/subscription/{subscription_id}"""
    return request_json(
        "DELETE",
        commerce_base_url(),
        f"/commerce/notification/v1/subscription/{subscription_id}",
        user_auth=True,
        scope=API_SCOPE,
    )


def enable_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/enable"""
    return request_json(
        "POST",
        commerce_base_url(),
        f"/commerce/notification/v1/subscription/{subscription_id}/enable",
        user_auth=True,
        scope=API_SCOPE,
    )


def disable_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/disable"""
    return request_json(
        "POST",
        commerce_base_url(),
        f"/commerce/notification/v1/subscription/{subscription_id}/disable",
        user_auth=True,
        scope=API_SCOPE,
    )


def test_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/test"""
    return request_json(
        "POST",
        commerce_base_url(),
        f"/commerce/notification/v1/subscription/{subscription_id}/test",
        user_auth=True,
        scope=API_SCOPE,
    )


def get_public_key() -> Dict[str, Any]:
    """GET /commerce/notification/v1/public_key"""
    return request_json(
        "GET",
        commerce_base_url(),
        "/commerce/notification/v1/public_key",
        user_auth=True,
        scope=API_SCOPE,
    )
