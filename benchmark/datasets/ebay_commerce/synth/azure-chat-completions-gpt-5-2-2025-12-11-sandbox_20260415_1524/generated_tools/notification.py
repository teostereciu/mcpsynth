from typing import Any, Dict, Optional

from .ebay_client import EbayClient


NOTIFICATION_SCOPE_APP = "https://api.ebay.com/oauth/api_scope"


def create_destination(
    *,
    endpoint: str,
    verification_token: str,
    status: str = "ENABLED",
    name: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a notification destination.

    POST /commerce/notification/v1/destination
    OAuth: app token with https://api.ebay.com/oauth/api_scope
    """
    body: Dict[str, Any] = {
        "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
        "status": status,
    }
    if name is not None:
        body["name"] = name

    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/notification/v1/destination",
        json_body=body,
        headers={"Content-Type": "application/json"},
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_destinations() -> Dict[str, Any]:
    """Get all destinations.

    GET /commerce/notification/v1/destination
    """
    client = EbayClient()
    return client.request(
        "GET",
        "/commerce/notification/v1/destination",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_destination(destination_id: str) -> Dict[str, Any]:
    """Get a destination by ID.

    GET /commerce/notification/v1/destination/{destination_id}
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/notification/v1/destination/{destination_id}",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def update_destination(destination_id: str, patch: Dict[str, Any]) -> Dict[str, Any]:
    """Update a destination.

    PUT /commerce/notification/v1/destination/{destination_id}
    Body is destination resource.
    """
    client = EbayClient()
    return client.request(
        "PUT",
        f"/commerce/notification/v1/destination/{destination_id}",
        json_body=patch,
        headers={"Content-Type": "application/json"},
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def delete_destination(destination_id: str) -> Dict[str, Any]:
    """Delete a destination.

    DELETE /commerce/notification/v1/destination/{destination_id}
    """
    client = EbayClient()
    return client.request(
        "DELETE",
        f"/commerce/notification/v1/destination/{destination_id}",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_topics() -> Dict[str, Any]:
    """Get all notification topics.

    GET /commerce/notification/v1/topic
    """
    client = EbayClient()
    return client.request(
        "GET",
        "/commerce/notification/v1/topic",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_topic(topic_id: str) -> Dict[str, Any]:
    """Get a topic by ID.

    GET /commerce/notification/v1/topic/{topic_id}
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/notification/v1/topic/{topic_id}",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def create_subscription(
    *,
    topic_id: str,
    destination_id: str,
    payload: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a subscription for a topic.

    POST /commerce/notification/v1/subscription
    """
    body = payload.copy() if payload else {}
    body.setdefault("topicId", topic_id)
    body.setdefault("destinationId", destination_id)

    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/notification/v1/subscription",
        json_body=body,
        headers={"Content-Type": "application/json"},
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_subscriptions() -> Dict[str, Any]:
    """Get all subscriptions.

    GET /commerce/notification/v1/subscription
    """
    client = EbayClient()
    return client.request(
        "GET",
        "/commerce/notification/v1/subscription",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """Get a subscription by ID.

    GET /commerce/notification/v1/subscription/{subscription_id}
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def update_subscription(subscription_id: str, patch: Dict[str, Any]) -> Dict[str, Any]:
    """Update a subscription.

    PUT /commerce/notification/v1/subscription/{subscription_id}
    """
    client = EbayClient()
    return client.request(
        "PUT",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        json_body=patch,
        headers={"Content-Type": "application/json"},
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """Delete a subscription.

    DELETE /commerce/notification/v1/subscription/{subscription_id}
    """
    client = EbayClient()
    return client.request(
        "DELETE",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def enable_subscription(subscription_id: str) -> Dict[str, Any]:
    """Enable a subscription.

    POST /commerce/notification/v1/subscription/{subscription_id}/enable
    """
    client = EbayClient()
    return client.request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/enable",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def disable_subscription(subscription_id: str) -> Dict[str, Any]:
    """Disable a subscription.

    POST /commerce/notification/v1/subscription/{subscription_id}/disable
    """
    client = EbayClient()
    return client.request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/disable",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def test_subscription(subscription_id: str) -> Dict[str, Any]:
    """Send a test notification for a subscription.

    POST /commerce/notification/v1/subscription/{subscription_id}/test
    """
    client = EbayClient()
    return client.request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/test",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_config() -> Dict[str, Any]:
    """Get notification configuration.

    GET /commerce/notification/v1/config
    """
    client = EbayClient()
    return client.request(
        "GET",
        "/commerce/notification/v1/config",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def update_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Update notification configuration.

    PUT /commerce/notification/v1/config
    """
    client = EbayClient()
    return client.request(
        "PUT",
        "/commerce/notification/v1/config",
        json_body=config,
        headers={"Content-Type": "application/json"},
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_public_key() -> Dict[str, Any]:
    """Get public key for verifying notification signatures.

    GET /commerce/notification/v1/public_key
    """
    client = EbayClient()
    return client.request(
        "GET",
        "/commerce/notification/v1/public_key",
        scope=NOTIFICATION_SCOPE_APP,
        user=False,
        is_media=False,
    )
