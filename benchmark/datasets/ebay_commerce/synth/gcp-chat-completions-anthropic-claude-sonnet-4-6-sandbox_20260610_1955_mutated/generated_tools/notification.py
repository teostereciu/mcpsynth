"""
eBay Commerce Notification API tools.
Uses app token (client_credentials) for most operations.
Base: /commerce/notification/v1
"""
from typing import Optional
import requests
from .auth import BASE_URL, app_headers, safe_json

NOTIF_BASE = f"{BASE_URL}/commerce/notification/v1"


def _headers() -> dict:
    return app_headers()


# ── Config ─────────────────────────────────────────────────────────────────

def get_notification_config() -> dict:
    """
    Retrieve the current notification configuration for the application.
    Returns the alertEmail address configured for Notification API alerts.
    """
    try:
        resp = requests.get(
            f"{NOTIF_BASE}/config",
            headers=_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def update_notification_config(alert_email: str) -> dict:
    """
    Create or update the notification configuration for the application.
    Sets the alert email address for Notification API alerts.

    Args:
        alert_email: Email address to receive Notification API alerts.
    """
    try:
        resp = requests.put(
            f"{NOTIF_BASE}/config",
            headers=_headers(),
            json={"alertEmail": alert_email},
            timeout=30,
        )
        return {"status_code": resp.status_code, "success": resp.ok}
    except Exception as e:
        return {"error": str(e)}


# ── Destinations ────────────────────────────────────────────────────────────

def create_destination(
    endpoint: str,
    verification_token: str,
    status: str = "ENABLED",
    name: Optional[str] = None,
) -> dict:
    """
    Create a notification destination — an HTTPS endpoint that receives push notifications.
    Returns the destination ID in the Location header.

    Args:
        endpoint: HTTPS URL of the destination endpoint (no localhost or internal IPs).
        verification_token: Token for endpoint verification (32-80 alphanumeric chars, _ or -).
        status: ENABLED or DISABLED (default ENABLED).
        name: Optional seller-specified name for the destination.
    """
    try:
        body: dict = {
            "deliveryConfig": {
                "endpoint": endpoint,
                "verificationToken": verification_token,
            },
            "status": status,
        }
        if name:
            body["name"] = name

        resp = requests.post(
            f"{NOTIF_BASE}/destination",
            headers=_headers(),
            json=body,
            timeout=30,
        )
        result = {"status_code": resp.status_code, "success": resp.ok}
        location = resp.headers.get("Location")
        if location:
            result["_location"] = location
            result["destination_id"] = location.rstrip("/").split("/")[-1]
        if resp.content:
            result.update(safe_json(resp))
        return result
    except Exception as e:
        return {"error": str(e)}


def get_destination(destination_id: str) -> dict:
    """
    Retrieve details for a specific notification destination by ID.
    Returns name, status, deliveryConfig (endpoint and verificationToken).

    Args:
        destination_id: The unique identifier of the destination.
    """
    try:
        resp = requests.get(
            f"{NOTIF_BASE}/destination/{destination_id}",
            headers=_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_destinations(
    page_size: int = 20,
    continuation_token: Optional[str] = None,
) -> dict:
    """
    Retrieve a paginated list of all notification destinations.
    Returns destination names, statuses, and delivery configurations.

    Args:
        page_size: Results per page (10-100, default 20).
        continuation_token: Token for fetching the next page of results.
    """
    try:
        params: dict = {"page_size": page_size}
        if continuation_token:
            params["continuation_token"] = continuation_token

        resp = requests.get(
            f"{NOTIF_BASE}/destination",
            headers=_headers(),
            params=params,
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def update_destination(
    destination_id: str,
    endpoint: str,
    verification_token: str,
    status: str = "ENABLED",
    name: Optional[str] = None,
) -> dict:
    """
    Update an existing notification destination.

    Args:
        destination_id: The unique identifier of the destination to update.
        endpoint: HTTPS URL of the destination endpoint.
        verification_token: Token for endpoint verification (32-80 chars).
        status: ENABLED or DISABLED.
        name: Optional seller-specified name.
    """
    try:
        body: dict = {
            "deliveryConfig": {
                "endpoint": endpoint,
                "verificationToken": verification_token,
            },
            "status": status,
        }
        if name:
            body["name"] = name

        resp = requests.put(
            f"{NOTIF_BASE}/destination/{destination_id}",
            headers=_headers(),
            json=body,
            timeout=30,
        )
        return {"status_code": resp.status_code, "success": resp.ok}
    except Exception as e:
        return {"error": str(e)}


def delete_destination(destination_id: str) -> dict:
    """
    Delete a notification destination.

    Args:
        destination_id: The unique identifier of the destination to delete.
    """
    try:
        resp = requests.delete(
            f"{NOTIF_BASE}/destination/{destination_id}",
            headers=_headers(),
            timeout=30,
        )
        return {"status_code": resp.status_code, "success": resp.ok}
    except Exception as e:
        return {"error": str(e)}


# ── Topics ──────────────────────────────────────────────────────────────────

def get_notification_topic(topic_id: str) -> dict:
    """
    Retrieve details for a specific notification topic by ID.
    Returns description, status, context, scope, supported payloads, and filterable flag.

    Args:
        topic_id: The unique identifier of the notification topic.
    """
    try:
        resp = requests.get(
            f"{NOTIF_BASE}/topic/{topic_id}",
            headers=_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_notification_topics(
    page_size: int = 20,
    continuation_token: Optional[str] = None,
) -> dict:
    """
    Retrieve a paginated list of all supported notification topics.
    Returns topic IDs, descriptions, statuses, supported payloads, and filterable flags.

    Args:
        page_size: Results per page (10-100, default 20).
        continuation_token: Token for fetching the next page of results.
    """
    try:
        params: dict = {"page_size": page_size}
        if continuation_token:
            params["continuation_token"] = continuation_token

        resp = requests.get(
            f"{NOTIF_BASE}/topic",
            headers=_headers(),
            params=params,
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


# ── Public Key ──────────────────────────────────────────────────────────────

def get_public_key(public_key_id: str) -> dict:
    """
    Retrieve a public key for verifying notification signatures.

    Args:
        public_key_id: The unique identifier of the public key.
    """
    try:
        resp = requests.get(
            f"{NOTIF_BASE}/public_key/{public_key_id}",
            headers=_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


# ── Subscriptions ───────────────────────────────────────────────────────────

def create_subscription(
    topic_id: str,
    destination_id: str,
    schema_version: str,
    status: str = "DISABLED",
    delivery_protocol: str = "HTTPS",
    payload_format: str = "JSON",
) -> dict:
    """
    Create a subscription to a notification topic.
    Create in DISABLED mode first, test it, then enable it.

    Args:
        topic_id: The notification topic ID to subscribe to (use get_notification_topics).
        destination_id: The destination ID to receive notifications (use get_destinations).
        schema_version: Schema version for the topic (use get_notification_topic to find it).
        status: ENABLED or DISABLED (default DISABLED — recommended to test first).
        delivery_protocol: Delivery protocol (default HTTPS — only supported value).
        payload_format: Payload format (default JSON — only supported value).
    """
    try:
        body = {
            "topicId": topic_id,
            "destinationId": destination_id,
            "payload": {
                "schemaVersion": schema_version,
                "deliveryProtocol": delivery_protocol,
                "format": payload_format,
            },
            "status": status,
        }
        resp = requests.post(
            f"{NOTIF_BASE}/subscription",
            headers=_headers(),
            json=body,
            timeout=30,
        )
        result = {"status_code": resp.status_code, "success": resp.ok}
        location = resp.headers.get("Location")
        if location:
            result["_location"] = location
            result["subscription_id"] = location.rstrip("/").split("/")[-1]
        if resp.content:
            result.update(safe_json(resp))
        return result
    except Exception as e:
        return {"error": str(e)}


def get_subscription(subscription_id: str) -> dict:
    """
    Retrieve details for a specific subscription by ID.
    Returns topicId, destinationId, filterId, payload, status, and creationDate.

    Args:
        subscription_id: The unique identifier of the subscription.
    """
    try:
        resp = requests.get(
            f"{NOTIF_BASE}/subscription/{subscription_id}",
            headers=_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_subscriptions(
    page_size: int = 20,
    continuation_token: Optional[str] = None,
) -> dict:
    """
    Retrieve a paginated list of all subscriptions.

    Args:
        page_size: Results per page (10-100, default 20).
        continuation_token: Token for fetching the next page of results.
    """
    try:
        params: dict = {"page_size": page_size}
        if continuation_token:
            params["continuation_token"] = continuation_token

        resp = requests.get(
            f"{NOTIF_BASE}/subscription",
            headers=_headers(),
            params=params,
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def update_subscription(
    subscription_id: str,
    destination_id: str,
    schema_version: str,
    status: str,
    delivery_protocol: str = "HTTPS",
    payload_format: str = "JSON",
) -> dict:
    """
    Update an existing subscription.

    Args:
        subscription_id: The unique identifier of the subscription to update.
        destination_id: The destination ID to receive notifications.
        schema_version: Schema version for the topic.
        status: ENABLED or DISABLED.
        delivery_protocol: Delivery protocol (default HTTPS).
        payload_format: Payload format (default JSON).
    """
    try:
        body = {
            "destinationId": destination_id,
            "payload": {
                "schemaVersion": schema_version,
                "deliveryProtocol": delivery_protocol,
                "format": payload_format,
            },
            "status": status,
        }
        resp = requests.put(
            f"{NOTIF_BASE}/subscription/{subscription_id}",
            headers=_headers(),
            json=body,
            timeout=30,
        )
        return {"status_code": resp.status_code, "success": resp.ok}
    except Exception as e:
        return {"error": str(e)}


def delete_subscription(subscription_id: str) -> dict:
    """
    Delete a subscription (regardless of its status).

    Args:
        subscription_id: The unique identifier of the subscription to delete.
    """
    try:
        resp = requests.delete(
            f"{NOTIF_BASE}/subscription/{subscription_id}",
            headers=_headers(),
            timeout=30,
        )
        return {"status_code": resp.status_code, "success": resp.ok}
    except Exception as e:
        return {"error": str(e)}


def enable_subscription(subscription_id: str) -> dict:
    """
    Enable a disabled subscription so it starts receiving notifications.

    Args:
        subscription_id: The unique identifier of the subscription to enable.
    """
    try:
        resp = requests.post(
            f"{NOTIF_BASE}/subscription/{subscription_id}/enable",
            headers=_headers(),
            timeout=30,
        )
        return {"status_code": resp.status_code, "success": resp.ok}
    except Exception as e:
        return {"error": str(e)}


def disable_subscription(subscription_id: str) -> dict:
    """
    Disable an enabled subscription to pause notifications.

    Args:
        subscription_id: The unique identifier of the subscription to disable.
    """
    try:
        resp = requests.post(
            f"{NOTIF_BASE}/subscription/{subscription_id}/disable",
            headers=_headers(),
            timeout=30,
        )
        return {"status_code": resp.status_code, "success": resp.ok}
    except Exception as e:
        return {"error": str(e)}


def test_subscription(subscription_id: str) -> dict:
    """
    Send a mocked test notification payload to the subscription's destination.
    Use this to verify your endpoint is working before enabling the subscription.
    Returns a notificationId to distinguish test payloads from real ones.

    Args:
        subscription_id: The unique identifier of the subscription to test.
    """
    try:
        resp = requests.post(
            f"{NOTIF_BASE}/subscription/{subscription_id}/test",
            headers=_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def create_subscription_filter(subscription_id: str, filter_schema: dict) -> dict:
    """
    Create a filter for a subscription. Only notifications matching the filter criteria
    will be sent to the destination. The filter uses JSON Schema Core (2020-12+).
    New filters start in PENDING status and move to ENABLED after validation.

    Args:
        subscription_id: The unique identifier of the subscription.
        filter_schema: A valid JSON Schema Core document describing filter criteria.
    """
    try:
        resp = requests.post(
            f"{NOTIF_BASE}/subscription/{subscription_id}/filter",
            headers=_headers(),
            json={"filterSchema": filter_schema},
            timeout=30,
        )
        result = {"status_code": resp.status_code, "success": resp.ok}
        location = resp.headers.get("Location")
        if location:
            result["_location"] = location
            result["filter_id"] = location.rstrip("/").split("/")[-1]
        if resp.content:
            result.update(safe_json(resp))
        return result
    except Exception as e:
        return {"error": str(e)}


def get_subscription_filter(subscription_id: str, filter_id: str) -> dict:
    """
    Retrieve details for a specific subscription filter.
    Returns filterId, filterSchema, filterStatus, subscriptionId, and creationDate.

    Args:
        subscription_id: The unique identifier of the subscription.
        filter_id: The unique identifier of the subscription filter.
    """
    try:
        resp = requests.get(
            f"{NOTIF_BASE}/subscription/{subscription_id}/filter/{filter_id}",
            headers=_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def delete_subscription_filter(subscription_id: str, filter_id: str) -> dict:
    """
    Disable the active filter on a subscription (so a new filter can be added).
    Only ENABLED filters can be deleted; PENDING filters cannot.

    Args:
        subscription_id: The unique identifier of the subscription.
        filter_id: The unique identifier of the subscription filter to delete.
    """
    try:
        resp = requests.delete(
            f"{NOTIF_BASE}/subscription/{subscription_id}/filter/{filter_id}",
            headers=_headers(),
            timeout=30,
        )
        return {"status_code": resp.status_code, "success": resp.ok}
    except Exception as e:
        return {"error": str(e)}
