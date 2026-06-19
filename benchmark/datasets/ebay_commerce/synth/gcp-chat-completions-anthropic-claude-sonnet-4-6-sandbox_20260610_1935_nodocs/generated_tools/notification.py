"""
eBay Commerce Notification API tools.
Base path: /commerce/notification/v1
Auth: user token (refresh_token)
"""

from .auth import user_get, user_post, user_put, user_delete

_BASE = "/commerce/notification/v1"


# ---------------------------------------------------------------------------
# Subscriptions
# ---------------------------------------------------------------------------

def get_subscriptions(
    limit: int = 20,
    continuation_token: str | None = None,
) -> dict:
    """
    List all notification subscriptions for the authenticated user.

    Args:
        limit: Number of subscriptions to return (max 100).
        continuation_token: Token for paginating through results.

    Returns:
        Dict with subscriptions list and pagination info.
    """
    params: dict = {"limit": limit}
    if continuation_token:
        params["continuation_token"] = continuation_token
    return user_get(f"{_BASE}/subscription", params=params)


def get_subscription(subscription_id: str) -> dict:
    """
    Retrieve details for a specific notification subscription.

    Args:
        subscription_id: The subscription ID.

    Returns:
        Dict with subscriptionId, topicId, status, destination, etc.
    """
    return user_get(f"{_BASE}/subscription/{subscription_id}")


def create_subscription(
    topic_id: str,
    destination_id: str,
    status: str = "ENABLED",
    payload: dict | None = None,
) -> dict:
    """
    Create a new notification subscription for a topic.

    Args:
        topic_id: The notification topic to subscribe to (e.g. "MARKETPLACE_ACCOUNT_DELETION").
        destination_id: The destination endpoint ID to receive notifications.
        status: Subscription status — ENABLED or DISABLED (default ENABLED).
        payload: Optional payload configuration dict.

    Returns:
        Dict with the created subscription details including subscriptionId.
    """
    body: dict = {
        "topicId": topic_id,
        "destinationId": destination_id,
        "status": status,
    }
    if payload:
        body["payload"] = payload
    return user_post(f"{_BASE}/subscription", json_body=body)


def update_subscription(
    subscription_id: str,
    status: str | None = None,
    destination_id: str | None = None,
    payload: dict | None = None,
) -> dict:
    """
    Update an existing notification subscription.

    Args:
        subscription_id: The subscription ID to update.
        status: New status — ENABLED or DISABLED.
        destination_id: New destination endpoint ID.
        payload: Updated payload configuration dict.

    Returns:
        Dict with updated subscription details.
    """
    body: dict = {}
    if status:
        body["status"] = status
    if destination_id:
        body["destinationId"] = destination_id
    if payload:
        body["payload"] = payload
    return user_put(f"{_BASE}/subscription/{subscription_id}", json_body=body)


def delete_subscription(subscription_id: str) -> dict:
    """
    Delete a notification subscription.

    Args:
        subscription_id: The subscription ID to delete.

    Returns:
        Dict confirming deletion or error details.
    """
    return user_delete(f"{_BASE}/subscription/{subscription_id}")


def enable_subscription(subscription_id: str) -> dict:
    """
    Enable a previously disabled notification subscription.

    Args:
        subscription_id: The subscription ID to enable.

    Returns:
        Dict with updated subscription status.
    """
    return user_post(f"{_BASE}/subscription/{subscription_id}/enable")


def disable_subscription(subscription_id: str) -> dict:
    """
    Disable an active notification subscription without deleting it.

    Args:
        subscription_id: The subscription ID to disable.

    Returns:
        Dict with updated subscription status.
    """
    return user_post(f"{_BASE}/subscription/{subscription_id}/disable")


# ---------------------------------------------------------------------------
# Destinations (webhook endpoints)
# ---------------------------------------------------------------------------

def get_destinations(
    limit: int = 20,
    continuation_token: str | None = None,
) -> dict:
    """
    List all notification destinations (webhook endpoints) for the authenticated user.

    Args:
        limit: Number of destinations to return (max 100).
        continuation_token: Token for paginating through results.

    Returns:
        Dict with destinations list and pagination info.
    """
    params: dict = {"limit": limit}
    if continuation_token:
        params["continuation_token"] = continuation_token
    return user_get(f"{_BASE}/destination", params=params)


def get_destination(destination_id: str) -> dict:
    """
    Retrieve details for a specific notification destination.

    Args:
        destination_id: The destination ID.

    Returns:
        Dict with destinationId, name, status, deliveryConfig (endpoint URL), etc.
    """
    return user_get(f"{_BASE}/destination/{destination_id}")


def create_destination(
    name: str,
    endpoint_url: str,
    verification_token: str | None = None,
    alert_email: str | None = None,
) -> dict:
    """
    Create a new notification destination (webhook endpoint).

    Args:
        name: Human-readable name for this destination.
        endpoint_url: HTTPS URL that will receive notification POST requests.
        verification_token: Optional token eBay will include in verification challenges.
        alert_email: Optional email address for delivery failure alerts.

    Returns:
        Dict with the created destination including destinationId.
    """
    delivery_config: dict = {"endpoint": {"url": endpoint_url}}
    if verification_token:
        delivery_config["endpoint"]["verificationToken"] = verification_token
    body: dict = {"name": name, "deliveryConfig": delivery_config}
    if alert_email:
        body["alertEmail"] = alert_email
    return user_post(f"{_BASE}/destination", json_body=body)


def update_destination(
    destination_id: str,
    name: str | None = None,
    endpoint_url: str | None = None,
    verification_token: str | None = None,
    alert_email: str | None = None,
) -> dict:
    """
    Update an existing notification destination.

    Args:
        destination_id: The destination ID to update.
        name: New human-readable name.
        endpoint_url: New HTTPS webhook URL.
        verification_token: New verification token.
        alert_email: New alert email address.

    Returns:
        Dict with updated destination details.
    """
    body: dict = {}
    if name:
        body["name"] = name
    if endpoint_url or verification_token:
        endpoint: dict = {}
        if endpoint_url:
            endpoint["url"] = endpoint_url
        if verification_token:
            endpoint["verificationToken"] = verification_token
        body["deliveryConfig"] = {"endpoint": endpoint}
    if alert_email:
        body["alertEmail"] = alert_email
    return user_put(f"{_BASE}/destination/{destination_id}", json_body=body)


def delete_destination(destination_id: str) -> dict:
    """
    Delete a notification destination.

    Args:
        destination_id: The destination ID to delete.

    Returns:
        Dict confirming deletion or error details.
    """
    return user_delete(f"{_BASE}/destination/{destination_id}")


# ---------------------------------------------------------------------------
# Topics
# ---------------------------------------------------------------------------

def get_topics(
    limit: int = 20,
    continuation_token: str | None = None,
) -> dict:
    """
    List all available notification topics.

    Args:
        limit: Number of topics to return (max 100).
        continuation_token: Token for paginating through results.

    Returns:
        Dict with topics list including topicId, description, status, etc.
    """
    params: dict = {"limit": limit}
    if continuation_token:
        params["continuation_token"] = continuation_token
    return user_get(f"{_BASE}/topic", params=params)


def get_topic(topic_id: str) -> dict:
    """
    Retrieve details for a specific notification topic.

    Args:
        topic_id: The topic ID (e.g. "MARKETPLACE_ACCOUNT_DELETION").

    Returns:
        Dict with topicId, description, status, supportedPayloadVersion, etc.
    """
    return user_get(f"{_BASE}/topic/{topic_id}")


# ---------------------------------------------------------------------------
# Public key (for verifying incoming notifications)
# ---------------------------------------------------------------------------

def get_public_key(public_key_id: str) -> dict:
    """
    Retrieve the eBay public key used to verify notification signatures.

    Args:
        public_key_id: The public key ID included in notification headers.

    Returns:
        Dict with publicKeyId, key (PEM), algorithm, digest, etc.
    """
    return user_get(f"{_BASE}/public_key/{public_key_id}")


# ---------------------------------------------------------------------------
# Config (notification application config)
# ---------------------------------------------------------------------------

def get_notification_config() -> dict:
    """
    Retrieve the notification configuration for the authenticated application.

    Returns:
        Dict with alertEmail and other application-level notification settings.
    """
    return user_get(f"{_BASE}/config")


def update_notification_config(alert_email: str) -> dict:
    """
    Update the application-level notification configuration.

    Args:
        alert_email: Email address for notification delivery failure alerts.

    Returns:
        Dict with updated config or confirmation.
    """
    return user_put(f"{_BASE}/config", json_body={"alertEmail": alert_email})
