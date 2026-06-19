"""
eBay Commerce Notification API tools.
Uses user-token (refresh_token grant).
Base: /commerce/notification/v1
"""

from typing import Optional
import requests
from .auth import BASE_URL, user_headers, safe_json

_BASE = f"{BASE_URL}/commerce/notification/v1"


# ── Subscriptions ─────────────────────────────────────────────────────────────

def get_subscriptions(
    limit: int = 20,
    continuation_token: Optional[str] = None,
) -> dict:
    """
    Return a paginated list of all notification subscriptions for the user.

    Args:
        limit: Number of subscriptions to return (default 20).
        continuation_token: Token for fetching the next page of results.
    """
    url = f"{_BASE}/subscription"
    params: dict = {"limit": limit}
    if continuation_token:
        params["continuation_token"] = continuation_token
    resp = requests.get(url, headers=user_headers(), params=params, timeout=15)
    return safe_json(resp)


def get_subscription(subscription_id: str) -> dict:
    """
    Retrieve a single notification subscription by its ID.

    Args:
        subscription_id: The subscription ID.
    """
    url = f"{_BASE}/subscription/{subscription_id}"
    resp = requests.get(url, headers=user_headers(), timeout=15)
    return safe_json(resp)


def create_subscription(
    topic_id: str,
    endpoint_url: str,
    delivery_config: Optional[dict] = None,
    filter_schema: Optional[dict] = None,
) -> dict:
    """
    Create a new notification subscription for a topic.

    Args:
        topic_id: The notification topic ID (e.g. 'MARKETPLACE_ACCOUNT_DELETION').
        endpoint_url: The HTTPS endpoint URL that will receive notifications.
        delivery_config: Optional delivery configuration dict (e.g. {'deliveryProtocol': 'HTTPS'}).
        filter_schema: Optional filter schema dict to narrow which events trigger the notification.
    """
    url = f"{_BASE}/subscription"
    body: dict = {
        "topicId": topic_id,
        "deliveryConfig": delivery_config or {"endpoint": {"url": endpoint_url}},
    }
    if filter_schema:
        body["filterSchema"] = filter_schema
    resp = requests.post(url, headers=user_headers(), json=body, timeout=15)
    return safe_json(resp)


def update_subscription(
    subscription_id: str,
    endpoint_url: Optional[str] = None,
    status: Optional[str] = None,
    delivery_config: Optional[dict] = None,
) -> dict:
    """
    Update an existing notification subscription.

    Args:
        subscription_id: The subscription ID to update.
        endpoint_url: New endpoint URL (if changing).
        status: New status ('ENABLED' or 'DISABLED').
        delivery_config: Full delivery configuration dict (replaces existing).
    """
    url = f"{_BASE}/subscription/{subscription_id}"
    body: dict = {}
    if delivery_config:
        body["deliveryConfig"] = delivery_config
    elif endpoint_url:
        body["deliveryConfig"] = {"endpoint": {"url": endpoint_url}}
    if status:
        body["status"] = status
    resp = requests.put(url, headers=user_headers(), json=body, timeout=15)
    return safe_json(resp)


def delete_subscription(subscription_id: str) -> dict:
    """
    Delete a notification subscription.

    Args:
        subscription_id: The subscription ID to delete.
    """
    url = f"{_BASE}/subscription/{subscription_id}"
    resp = requests.delete(url, headers=user_headers(), timeout=15)
    return safe_json(resp)


def enable_subscription(subscription_id: str) -> dict:
    """
    Enable a previously disabled notification subscription.

    Args:
        subscription_id: The subscription ID to enable.
    """
    url = f"{_BASE}/subscription/{subscription_id}/enable"
    resp = requests.post(url, headers=user_headers(), json={}, timeout=15)
    return safe_json(resp)


def disable_subscription(subscription_id: str) -> dict:
    """
    Disable an active notification subscription without deleting it.

    Args:
        subscription_id: The subscription ID to disable.
    """
    url = f"{_BASE}/subscription/{subscription_id}/disable"
    resp = requests.post(url, headers=user_headers(), json={}, timeout=15)
    return safe_json(resp)


def get_subscription_config(subscription_id: str) -> dict:
    """
    Retrieve the delivery configuration for a subscription.

    Args:
        subscription_id: The subscription ID.
    """
    url = f"{_BASE}/subscription/{subscription_id}/config"
    resp = requests.get(url, headers=user_headers(), timeout=15)
    return safe_json(resp)


# ── Topics ────────────────────────────────────────────────────────────────────

def get_topics(
    limit: int = 20,
    continuation_token: Optional[str] = None,
) -> dict:
    """
    Return a paginated list of all available notification topics.

    Args:
        limit: Number of topics to return (default 20).
        continuation_token: Token for fetching the next page.
    """
    url = f"{_BASE}/topic"
    params: dict = {"limit": limit}
    if continuation_token:
        params["continuation_token"] = continuation_token
    resp = requests.get(url, headers=user_headers(), params=params, timeout=15)
    return safe_json(resp)


def get_topic(topic_id: str) -> dict:
    """
    Retrieve details for a single notification topic.

    Args:
        topic_id: The notification topic ID.
    """
    url = f"{_BASE}/topic/{topic_id}"
    resp = requests.get(url, headers=user_headers(), timeout=15)
    return safe_json(resp)


# ── Destination (Endpoint) Management ────────────────────────────────────────

def get_destinations(
    limit: int = 20,
    continuation_token: Optional[str] = None,
) -> dict:
    """
    Return a paginated list of all notification destinations (endpoints).

    Args:
        limit: Number of destinations to return (default 20).
        continuation_token: Token for fetching the next page.
    """
    url = f"{_BASE}/destination"
    params: dict = {"limit": limit}
    if continuation_token:
        params["continuation_token"] = continuation_token
    resp = requests.get(url, headers=user_headers(), params=params, timeout=15)
    return safe_json(resp)


def get_destination(destination_id: str) -> dict:
    """
    Retrieve a single notification destination by its ID.

    Args:
        destination_id: The destination ID.
    """
    url = f"{_BASE}/destination/{destination_id}"
    resp = requests.get(url, headers=user_headers(), timeout=15)
    return safe_json(resp)


def create_destination(
    name: str,
    endpoint_url: str,
    verification_token: Optional[str] = None,
) -> dict:
    """
    Create a new notification destination (webhook endpoint).

    Args:
        name: Human-readable name for the destination.
        endpoint_url: The HTTPS URL that will receive notifications.
        verification_token: Optional token used to verify the endpoint.
    """
    url = f"{_BASE}/destination"
    body: dict = {
        "name": name,
        "deliveryConfig": {
            "endpoint": {"url": endpoint_url},
        },
    }
    if verification_token:
        body["deliveryConfig"]["endpoint"]["verificationToken"] = verification_token
    resp = requests.post(url, headers=user_headers(), json=body, timeout=15)
    return safe_json(resp)


def update_destination(
    destination_id: str,
    name: Optional[str] = None,
    endpoint_url: Optional[str] = None,
    verification_token: Optional[str] = None,
) -> dict:
    """
    Update an existing notification destination.

    Args:
        destination_id: The destination ID to update.
        name: New human-readable name.
        endpoint_url: New HTTPS endpoint URL.
        verification_token: New verification token.
    """
    url = f"{_BASE}/destination/{destination_id}"
    body: dict = {}
    if name:
        body["name"] = name
    endpoint: dict = {}
    if endpoint_url:
        endpoint["url"] = endpoint_url
    if verification_token:
        endpoint["verificationToken"] = verification_token
    if endpoint:
        body["deliveryConfig"] = {"endpoint": endpoint}
    resp = requests.put(url, headers=user_headers(), json=body, timeout=15)
    return safe_json(resp)


def delete_destination(destination_id: str) -> dict:
    """
    Delete a notification destination.

    Args:
        destination_id: The destination ID to delete.
    """
    url = f"{_BASE}/destination/{destination_id}"
    resp = requests.delete(url, headers=user_headers(), timeout=15)
    return safe_json(resp)


# ── Public Key ────────────────────────────────────────────────────────────────

def get_public_key(public_key_id: str) -> dict:
    """
    Retrieve the public key used to verify notification signatures.

    Args:
        public_key_id: The public key ID (found in notification headers).
    """
    url = f"{_BASE}/public_key/{public_key_id}"
    resp = requests.get(url, headers=user_headers(), timeout=15)
    return safe_json(resp)
