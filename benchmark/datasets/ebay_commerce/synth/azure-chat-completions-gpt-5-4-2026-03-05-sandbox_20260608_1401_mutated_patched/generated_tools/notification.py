from typing import Any, Dict, Optional

from .ebay_common import client


def get_notification_config() -> Dict[str, Any]:
    return client.request("GET", "/commerce/notification/v1/config", token_type="app")


def update_notification_config(alert_email: str) -> Dict[str, Any]:
    return client.request(
        "PUT",
        "/commerce/notification/v1/config",
        token_type="app",
        headers={"Content-Type": "application/json"},
        json_body={"alertEmail": alert_email},
    )


def create_destination(endpoint: str, verification_token: str, status: str, name: Optional[str] = None) -> Dict[str, Any]:
    body = {
        "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
        "status": status,
        "name": name,
    }
    return client.request(
        "POST",
        "/commerce/notification/v1/destination",
        token_type="app",
        headers={"Content-Type": "application/json"},
        json_body=body,
    )


def get_destinations(page_size: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/commerce/notification/v1/destination",
        token_type="app",
        params={"limit": page_size, "continuation_token": continuation_token},
    )


def get_destination(destination_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/notification/v1/destination/{destination_id}", token_type="app")


def update_destination(destination_id: str, endpoint: str, verification_token: str, status: str, name: Optional[str] = None) -> Dict[str, Any]:
    body = {
        "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
        "status": status,
        "name": name,
    }
    return client.request(
        "PUT",
        f"/commerce/notification/v1/destination/{destination_id}",
        token_type="app",
        headers={"Content-Type": "application/json"},
        json_body=body,
    )


def delete_destination(destination_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/commerce/notification/v1/destination/{destination_id}", token_type="app")


def get_public_key(public_key_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/notification/v1/public_key/{public_key_id}", token_type="app")


def get_topics(page_size: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/commerce/notification/v1/topic",
        token_type="app",
        params={"limit": page_size, "continuation_token": continuation_token},
    )


def get_topic(topic_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/notification/v1/topic/{topic_id}", token_type="app")


def get_subscriptions(page_size: Optional[int] = None, continuation_token: Optional[str] = None, user_scope: bool = False) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/commerce/notification/v1/subscription",
        token_type="user" if user_scope else "app",
        params={"limit": page_size, "continuation_token": continuation_token},
    )


def create_subscription(topic_id: str, status: str, destination_id: str, schema_version: str, fmt: str = "JSON", delivery_protocol: str = "HTTPS", user_scope: bool = False) -> Dict[str, Any]:
    body = {
        "topicId": topic_id,
        "status": status,
        "destinationId": destination_id,
        "payload": {
            "schemaVersion": schema_version,
            "format": fmt,
            "deliveryProtocol": delivery_protocol,
        },
    }
    return client.request(
        "POST",
        "/commerce/notification/v1/subscription",
        token_type="user" if user_scope else "app",
        headers={"Content-Type": "application/json"},
        json_body=body,
    )


def update_subscription(subscription_id: str, status: str, destination_id: str, schema_version: str, fmt: str = "JSON", delivery_protocol: str = "HTTPS", user_scope: bool = False) -> Dict[str, Any]:
    body = {
        "status": status,
        "destinationId": destination_id,
        "payload": {
            "schemaVersion": schema_version,
            "format": fmt,
            "deliveryProtocol": delivery_protocol,
        },
    }
    return client.request(
        "PUT",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        token_type="user" if user_scope else "app",
        headers={"Content-Type": "application/json"},
        json_body=body,
    )


def get_subscription(subscription_id: str, user_scope: bool = False) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        token_type="user" if user_scope else "app",
    )


def delete_subscription(subscription_id: str, user_scope: bool = False) -> Dict[str, Any]:
    return client.request(
        "DELETE",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        token_type="user" if user_scope else "app",
    )


def create_subscription_filter(subscription_id: str, filter_schema: dict, user_scope: bool = False) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter",
        token_type="user" if user_scope else "app",
        headers={"Content-Type": "application/json"},
        json_body={"filterSchema": filter_schema},
    )


def delete_subscription_filter(subscription_id: str, filter_id: str, user_scope: bool = False) -> Dict[str, Any]:
    return client.request(
        "DELETE",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}",
        token_type="user" if user_scope else "app",
    )


def get_subscription_filter(subscription_id: str, filter_id: str, user_scope: bool = False) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}",
        token_type="user" if user_scope else "app",
    )
