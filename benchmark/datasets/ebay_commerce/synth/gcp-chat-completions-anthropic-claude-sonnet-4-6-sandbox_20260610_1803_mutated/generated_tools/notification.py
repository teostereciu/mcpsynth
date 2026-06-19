"""
eBay Commerce Notification API tools.
Base URL: https://api.sandbox.ebay.com/commerce/notification/v1
Auth: App token (client_credentials) for most endpoints.
"""

import requests
from .auth import app_headers, _base_url


def _notif_url(path: str) -> str:
    return f"{_base_url()}/commerce/notification/v1{path}"


def _app_json_headers() -> dict:
    h = app_headers()
    h["Content-Type"] = "application/json"
    return h


# ── Config ────────────────────────────────────────────────────────────────────

def get_notification_config() -> dict:
    """
    Retrieve the current notification configuration (alert email address).
    """
    try:
        resp = requests.get(
            _notif_url("/config"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def update_notification_config(alert_email: str) -> dict:
    """
    Create or update the notification configuration with an alert email address.
    Returns {"status": "updated"} on success (HTTP 204).
    """
    try:
        resp = requests.put(
            _notif_url("/config"),
            headers=_app_json_headers(),
            json={"alertEmail": alert_email},
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "updated"}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ── Destinations ──────────────────────────────────────────────────────────────

def create_destination(
    endpoint: str,
    verification_token: str,
    status: str = "ENABLED",
    name: str | None = None,
) -> dict:
    """
    Create a notification destination (webhook endpoint).
    endpoint: HTTPS URL to receive push notifications.
    verification_token: 32-80 chars, alphanumeric/underscore/hyphen.
    status: ENABLED or DISABLED.
    name: optional human-readable name.
    Returns {"location": "<destination_id_url>"} on success.
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
            _notif_url("/destination"),
            headers=_app_json_headers(),
            json=body,
            timeout=30,
        )
        if resp.status_code in (200, 201, 204):
            location = resp.headers.get("Location", "")
            return {"status": "created", "location": location}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_destination(destination_id: str) -> dict:
    """
    Retrieve details for a specific notification destination.
    Returns destinationId, name, status, deliveryConfig (endpoint, verificationToken).
    """
    try:
        resp = requests.get(
            _notif_url(f"/destination/{destination_id}"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_destinations(
    page_size: int | None = None,
    continuation_token: str | None = None,
) -> dict:
    """
    Retrieve a paginated list of all notification destinations.
    """
    try:
        params: dict = {}
        if page_size is not None:
            params["page_size"] = page_size
        if continuation_token:
            params["continuation_token"] = continuation_token
        resp = requests.get(
            _notif_url("/destination"),
            headers=app_headers(),
            params=params,
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def update_destination(
    destination_id: str,
    endpoint: str,
    verification_token: str,
    status: str = "ENABLED",
    name: str | None = None,
) -> dict:
    """
    Update an existing notification destination.
    Returns {"status": "updated"} on success (HTTP 204).
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
            _notif_url(f"/destination/{destination_id}"),
            headers=_app_json_headers(),
            json=body,
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "updated"}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def delete_destination(destination_id: str) -> dict:
    """
    Delete a notification destination. Only disabled/marked-down destinations can be deleted.
    Returns {"status": "deleted"} on success (HTTP 204).
    """
    try:
        resp = requests.delete(
            _notif_url(f"/destination/{destination_id}"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "deleted"}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ── Subscriptions ─────────────────────────────────────────────────────────────

def create_subscription(
    topic_id: str,
    destination_id: str,
    schema_version: str,
    status: str = "DISABLED",
    delivery_protocol: str = "HTTPS",
    format: str = "JSON",
) -> dict:
    """
    Create a subscription for a notification topic.
    topic_id: use get_notification_topics() to find topic IDs.
    destination_id: use get_destinations() to find destination IDs.
    schema_version: use get_notification_topic() to find supported schema versions.
    status: ENABLED or DISABLED (start DISABLED to test first).
    Returns {"status": "created", "location": "<subscription_url>"} on success.
    """
    try:
        body = {
            "topicId": topic_id,
            "destinationId": destination_id,
            "payload": {
                "deliveryProtocol": delivery_protocol,
                "format": format,
                "schemaVersion": schema_version,
            },
            "status": status,
        }
        resp = requests.post(
            _notif_url("/subscription"),
            headers=_app_json_headers(),
            json=body,
            timeout=30,
        )
        if resp.status_code in (200, 201):
            location = resp.headers.get("Location", "")
            return {"status": "created", "location": location}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_subscription(subscription_id: str) -> dict:
    """
    Retrieve details for a specific subscription.
    Returns subscriptionId, topicId, status, creationDate, payload, destinationId, filterId.
    """
    try:
        resp = requests.get(
            _notif_url(f"/subscription/{subscription_id}"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_subscriptions(
    page_size: int | None = None,
    continuation_token: str | None = None,
) -> dict:
    """
    Retrieve a paginated list of all subscriptions.
    """
    try:
        params: dict = {}
        if page_size is not None:
            params["page_size"] = page_size
        if continuation_token:
            params["continuation_token"] = continuation_token
        resp = requests.get(
            _notif_url("/subscription"),
            headers=app_headers(),
            params=params,
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def update_subscription(
    subscription_id: str,
    destination_id: str,
    schema_version: str,
    status: str,
    delivery_protocol: str = "HTTPS",
    format: str = "JSON",
) -> dict:
    """
    Update an existing subscription.
    Returns {"status": "updated"} on success (HTTP 204).
    """
    try:
        body = {
            "destinationId": destination_id,
            "payload": {
                "deliveryProtocol": delivery_protocol,
                "format": format,
                "schemaVersion": schema_version,
            },
            "status": status,
        }
        resp = requests.put(
            _notif_url(f"/subscription/{subscription_id}"),
            headers=_app_json_headers(),
            json=body,
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "updated"}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def delete_subscription(subscription_id: str) -> dict:
    """
    Delete a subscription (can be deleted regardless of status).
    Returns {"status": "deleted"} on success (HTTP 204).
    """
    try:
        resp = requests.delete(
            _notif_url(f"/subscription/{subscription_id}"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "deleted"}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def enable_subscription(subscription_id: str) -> dict:
    """
    Enable a disabled subscription to start receiving notifications.
    Returns {"status": "enabled"} on success (HTTP 204).
    """
    try:
        resp = requests.post(
            _notif_url(f"/subscription/{subscription_id}/enable"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "enabled"}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def disable_subscription(subscription_id: str) -> dict:
    """
    Disable an enabled subscription to pause notifications.
    Returns {"status": "disabled"} on success (HTTP 204).
    """
    try:
        resp = requests.post(
            _notif_url(f"/subscription/{subscription_id}/disable"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "disabled"}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def test_subscription(subscription_id: str) -> dict:
    """
    Send a mocked test payload to the subscription's destination endpoint.
    Returns notificationId on success (HTTP 202).
    """
    try:
        resp = requests.post(
            _notif_url(f"/subscription/{subscription_id}/test"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code in (200, 202):
            return resp.json() if resp.text else {"status": "test_sent"}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def create_subscription_filter(subscription_id: str, filter_schema: dict) -> dict:
    """
    Create a filter for a subscription using a JSON Schema Core document.
    filter_schema: a valid JSON Schema (2020-12+) describing filter criteria.
    Returns {"status": "created", "location": "<filter_url>"} on success.
    """
    try:
        resp = requests.post(
            _notif_url(f"/subscription/{subscription_id}/filter"),
            headers=_app_json_headers(),
            json={"filterSchema": filter_schema},
            timeout=30,
        )
        if resp.status_code in (200, 201):
            location = resp.headers.get("Location", "")
            return {"status": "created", "location": location}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_subscription_filter(subscription_id: str, filter_id: str) -> dict:
    """
    Retrieve details for a specific subscription filter.
    Returns filterId, filterSchema, filterStatus, subscriptionId, creationDate.
    """
    try:
        resp = requests.get(
            _notif_url(f"/subscription/{subscription_id}/filter/{filter_id}"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def delete_subscription_filter(subscription_id: str, filter_id: str) -> dict:
    """
    Disable the active filter on a subscription.
    Returns {"status": "deleted"} on success (HTTP 204).
    """
    try:
        resp = requests.delete(
            _notif_url(f"/subscription/{subscription_id}/filter/{filter_id}"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "deleted"}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ── Topics ────────────────────────────────────────────────────────────────────

def get_notification_topic(topic_id: str) -> dict:
    """
    Retrieve details for a specific notification topic including supported schema versions,
    formats, delivery protocols, filterable flag, and required authorization scopes.
    """
    try:
        resp = requests.get(
            _notif_url(f"/topic/{topic_id}"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_notification_topics(
    page_size: int | None = None,
    continuation_token: str | None = None,
) -> dict:
    """
    Retrieve a paginated list of all supported notification topics.
    """
    try:
        params: dict = {}
        if page_size is not None:
            params["page_size"] = page_size
        if continuation_token:
            params["continuation_token"] = continuation_token
        resp = requests.get(
            _notif_url("/topic"),
            headers=app_headers(),
            params=params,
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ── Public Key ────────────────────────────────────────────────────────────────

def get_public_key(public_key_id: str) -> dict:
    """
    Retrieve a public key by ID for validating eBay push notification signatures.
    The public_key_id is extracted from the X-EBAY-SIGNATURE header of a notification.
    Returns algorithm, digest, and key fields.
    """
    try:
        resp = requests.get(
            _notif_url(f"/public_key/{public_key_id}"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
