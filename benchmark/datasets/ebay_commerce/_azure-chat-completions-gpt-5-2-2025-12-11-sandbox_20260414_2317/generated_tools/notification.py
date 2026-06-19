"""Tools for eBay Commerce Notification API (webhooks)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json


# -------- Config --------

def get_notification_config(user_auth: bool = False) -> Dict[str, Any]:
    """Get notification configuration.

    Docs: GET /commerce/notification/v1/config
    Auth: docs indicate application token; allow user_auth toggle.
    """

    status, data, _ = request_json(
        "GET",
        "/commerce/notification/v1/config",
        user_auth=user_auth,
        media=False,
    )
    return data


def update_notification_config(config: Dict[str, Any], user_auth: bool = False) -> Dict[str, Any]:
    """Update notification configuration.

    Docs: PUT /commerce/notification/v1/config
    """

    status, data, _ = request_json(
        "PUT",
        "/commerce/notification/v1/config",
        json_body=config,
        user_auth=user_auth,
        media=False,
    )
    return data


# -------- Destinations --------

def get_destinations(limit: Optional[int] = None, continuation_token: Optional[str] = None, user_auth: bool = False) -> Dict[str, Any]:
    """List destinations.

    Docs: GET /commerce/notification/v1/destination
    """

    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if continuation_token is not None:
        params["continuation_token"] = continuation_token

    status, data, _ = request_json(
        "GET",
        "/commerce/notification/v1/destination",
        params=params or None,
        user_auth=user_auth,
        media=False,
    )
    return data


def get_destination(destination_id: str, user_auth: bool = False) -> Dict[str, Any]:
    """Get destination details.

    Docs: GET /commerce/notification/v1/destination/{destination_id}
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/notification/v1/destination/{destination_id}",
        user_auth=user_auth,
        media=False,
    )
    return data


def create_destination(name: str, endpoint: str, verification_token: str, user_auth: bool = False) -> Dict[str, Any]:
    """Create a destination.

    Docs: POST /commerce/notification/v1/destination
    """

    body = {"name": name, "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token}}
    status, data, _ = request_json(
        "POST",
        "/commerce/notification/v1/destination",
        json_body=body,
        user_auth=user_auth,
        media=False,
    )
    return data


def update_destination(destination_id: str, name: Optional[str] = None, endpoint: Optional[str] = None, verification_token: Optional[str] = None, user_auth: bool = False) -> Dict[str, Any]:
    """Update a destination.

    Docs: PUT /commerce/notification/v1/destination/{destination_id}
    """

    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if endpoint is not None or verification_token is not None:
        body["deliveryConfig"] = {}
        if endpoint is not None:
            body["deliveryConfig"]["endpoint"] = endpoint
        if verification_token is not None:
            body["deliveryConfig"]["verificationToken"] = verification_token

    status, data, _ = request_json(
        "PUT",
        f"/commerce/notification/v1/destination/{destination_id}",
        json_body=body,
        user_auth=user_auth,
        media=False,
    )
    return data


def delete_destination(destination_id: str, user_auth: bool = False) -> Dict[str, Any]:
    """Delete a destination.

    Docs: DELETE /commerce/notification/v1/destination/{destination_id}
    """

    status, data, _ = request_json(
        "DELETE",
        f"/commerce/notification/v1/destination/{destination_id}",
        user_auth=user_auth,
        media=False,
    )
    return data


# -------- Topics --------

def get_topics(limit: Optional[int] = None, continuation_token: Optional[str] = None, user_auth: bool = False) -> Dict[str, Any]:
    """List topics.

    Docs: GET /commerce/notification/v1/topic
    """

    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if continuation_token is not None:
        params["continuation_token"] = continuation_token

    status, data, _ = request_json(
        "GET",
        "/commerce/notification/v1/topic",
        params=params or None,
        user_auth=user_auth,
        media=False,
    )
    return data


def get_topic(topic_id: str, user_auth: bool = False) -> Dict[str, Any]:
    """Get topic details.

    Docs: GET /commerce/notification/v1/topic/{topic_id}
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/notification/v1/topic/{topic_id}",
        user_auth=user_auth,
        media=False,
    )
    return data


# -------- Subscriptions --------

def get_subscriptions(limit: Optional[int] = None, continuation_token: Optional[str] = None, user_auth: bool = False) -> Dict[str, Any]:
    """List subscriptions.

    Docs: GET /commerce/notification/v1/subscription
    """

    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if continuation_token is not None:
        params["continuation_token"] = continuation_token

    status, data, _ = request_json(
        "GET",
        "/commerce/notification/v1/subscription",
        params=params or None,
        user_auth=user_auth,
        media=False,
    )
    return data


def get_subscription(subscription_id: str, user_auth: bool = False) -> Dict[str, Any]:
    """Get subscription details.

    Docs: GET /commerce/notification/v1/subscription/{subscription_id}
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        user_auth=user_auth,
        media=False,
    )
    return data


def create_subscription(topic_id: str, destination_id: str, payload: Optional[Dict[str, Any]] = None, user_auth: bool = False) -> Dict[str, Any]:
    """Create a subscription.

    Docs: POST /commerce/notification/v1/subscription
    """

    body: Dict[str, Any] = {"topicId": topic_id, "destinationId": destination_id}
    if payload:
        body.update(payload)

    status, data, _ = request_json(
        "POST",
        "/commerce/notification/v1/subscription",
        json_body=body,
        user_auth=user_auth,
        media=False,
    )
    return data


def update_subscription(subscription_id: str, payload: Dict[str, Any], user_auth: bool = False) -> Dict[str, Any]:
    """Update a subscription.

    Docs: PUT /commerce/notification/v1/subscription/{subscription_id}
    """

    status, data, _ = request_json(
        "PUT",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        json_body=payload,
        user_auth=user_auth,
        media=False,
    )
    return data


def delete_subscription(subscription_id: str, user_auth: bool = False) -> Dict[str, Any]:
    """Delete a subscription.

    Docs: DELETE /commerce/notification/v1/subscription/{subscription_id}
    """

    status, data, _ = request_json(
        "DELETE",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        user_auth=user_auth,
        media=False,
    )
    return data


def enable_subscription(subscription_id: str, user_auth: bool = False) -> Dict[str, Any]:
    """Enable a subscription.

    Docs: POST /commerce/notification/v1/subscription/{subscription_id}/enable
    """

    status, data, _ = request_json(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/enable",
        json_body={},
        user_auth=user_auth,
        media=False,
    )
    return data


def disable_subscription(subscription_id: str, user_auth: bool = False) -> Dict[str, Any]:
    """Disable a subscription.

    Docs: POST /commerce/notification/v1/subscription/{subscription_id}/disable
    """

    status, data, _ = request_json(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/disable",
        json_body={},
        user_auth=user_auth,
        media=False,
    )
    return data


def test_subscription(subscription_id: str, user_auth: bool = False) -> Dict[str, Any]:
    """Test a subscription.

    Docs: POST /commerce/notification/v1/subscription/{subscription_id}/test
    """

    status, data, _ = request_json(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/test",
        json_body={},
        user_auth=user_auth,
        media=False,
    )
    return data


def get_public_key(user_auth: bool = False) -> Dict[str, Any]:
    """Get public key for verifying notifications.

    Docs: GET /commerce/notification/v1/public_key
    """

    status, data, _ = request_json(
        "GET",
        "/commerce/notification/v1/public_key",
        user_auth=user_auth,
        media=False,
    )
    return data
