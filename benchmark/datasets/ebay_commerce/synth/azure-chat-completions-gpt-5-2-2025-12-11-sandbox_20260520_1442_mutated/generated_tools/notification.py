from typing import Any, Dict, Optional

from .ebay_client import EbayClient


NOTIFICATION_SCOPE = "https://api.ebay.com/oauth/api_scope"


def create_destination(
    *,
    endpoint: str,
    verification_token: str,
    status: str = "ENABLED",
    name: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /commerce/notification/v1/destination"""
    client = EbayClient()
    body: Dict[str, Any] = {
        "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
        "status": status,
    }
    if name is not None:
        body["name"] = name
    return client.request(
        "POST",
        client.api_base,
        "/commerce/notification/v1/destination",
        json_body=body,
        headers={"Content-Type": "application/json"},
        auth="app",
        scope=NOTIFICATION_SCOPE,
    )


def get_destinations(page_size: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    """GET /commerce/notification/v1/destination"""
    client = EbayClient()
    params: Dict[str, Any] = {}
    if page_size is not None:
        params["page_size"] = page_size
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    return client.request(
        "GET",
        client.api_base,
        "/commerce/notification/v1/destination",
        params=params,
        auth="app",
        scope=NOTIFICATION_SCOPE,
    )


def get_destination(destination_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/destination/{destination_id}"""
    client = EbayClient()
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/notification/v1/destination/{destination_id}",
        auth="app",
        scope=NOTIFICATION_SCOPE,
    )


def update_destination(
    destination_id: str,
    *,
    endpoint: str,
    verification_token: str,
    status: str = "ENABLED",
    name: Optional[str] = None,
) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/destination/{destination_id}"""
    client = EbayClient()
    body: Dict[str, Any] = {
        "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
        "status": status,
    }
    if name is not None:
        body["name"] = name
    return client.request(
        "PUT",
        client.api_base,
        f"/commerce/notification/v1/destination/{destination_id}",
        json_body=body,
        headers={"Content-Type": "application/json"},
        auth="app",
        scope=NOTIFICATION_SCOPE,
    )


def delete_destination(destination_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/destination/{destination_id}"""
    client = EbayClient()
    return client.request(
        "DELETE",
        client.api_base,
        f"/commerce/notification/v1/destination/{destination_id}",
        auth="app",
        scope=NOTIFICATION_SCOPE,
    )


def create_subscription(
    *,
    topic_id: str,
    destination_id: str,
    schema_version: str,
    status: str = "DISABLED",
    delivery_protocol: str = "HTTPS",
    format: str = "JSON",
    auth_type: str = "app",
) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription"""
    client = EbayClient()
    body: Dict[str, Any] = {
        "topicId": topic_id,
        "destinationId": destination_id,
        "status": status,
        "payload": {"schemaVersion": schema_version, "deliveryProtocol": delivery_protocol, "format": format},
    }
    return client.request(
        "POST",
        client.api_base,
        "/commerce/notification/v1/subscription",
        json_body=body,
        headers={"Content-Type": "application/json"},
        auth=auth_type,
        scope=NOTIFICATION_SCOPE
        if auth_type == "app"
        else "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
    )


def get_subscriptions(
    page_size: Optional[int] = None,
    continuation_token: Optional[str] = None,
    *,
    auth_type: str = "app",
) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription"""
    client = EbayClient()
    params: Dict[str, Any] = {}
    if page_size is not None:
        params["page_size"] = page_size
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    scope = (
        NOTIFICATION_SCOPE
        if auth_type == "app"
        else "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly"
    )
    return client.request(
        "GET",
        client.api_base,
        "/commerce/notification/v1/subscription",
        params=params,
        auth=auth_type,
        scope=scope,
    )


def get_subscription(subscription_id: str, *, auth_type: str = "app") -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription/{subscription_id}"""
    client = EbayClient()
    scope = (
        NOTIFICATION_SCOPE
        if auth_type == "app"
        else "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly"
    )
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}",
        auth=auth_type,
        scope=scope,
    )


def update_subscription(
    subscription_id: str,
    *,
    destination_id: str,
    schema_version: str,
    status: str,
    delivery_protocol: str = "HTTPS",
    format: str = "JSON",
    auth_type: str = "app",
) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/subscription/{subscription_id}"""
    client = EbayClient()
    body: Dict[str, Any] = {
        "destinationId": destination_id,
        "status": status,
        "payload": {"schemaVersion": schema_version, "deliveryProtocol": delivery_protocol, "format": format},
    }
    scope = (
        NOTIFICATION_SCOPE
        if auth_type == "app"
        else "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
    )
    return client.request(
        "PUT",
        client.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}",
        json_body=body,
        headers={"Content-Type": "application/json"},
        auth=auth_type,
        scope=scope,
    )


def delete_subscription(subscription_id: str, *, auth_type: str = "app") -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/subscription/{subscription_id}"""
    client = EbayClient()
    scope = (
        NOTIFICATION_SCOPE
        if auth_type == "app"
        else "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
    )
    return client.request(
        "DELETE",
        client.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}",
        auth=auth_type,
        scope=scope,
    )


def enable_subscription(subscription_id: str, *, auth_type: str = "app") -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/enable"""
    client = EbayClient()
    scope = (
        NOTIFICATION_SCOPE
        if auth_type == "app"
        else "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
    )
    return client.request(
        "POST",
        client.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}/enable",
        auth=auth_type,
        scope=scope,
    )


def disable_subscription(subscription_id: str, *, auth_type: str = "app") -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/disable"""
    client = EbayClient()
    scope = (
        NOTIFICATION_SCOPE
        if auth_type == "app"
        else "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
    )
    return client.request(
        "POST",
        client.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}/disable",
        auth=auth_type,
        scope=scope,
    )


def test_subscription(subscription_id: str, *, auth_type: str = "app") -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/test"""
    client = EbayClient()
    scope = (
        NOTIFICATION_SCOPE
        if auth_type == "app"
        else "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
    )
    return client.request(
        "POST",
        client.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}/test",
        auth=auth_type,
        scope=scope,
    )


def get_topics(page_size: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    """GET /commerce/notification/v1/topic"""
    client = EbayClient()
    params: Dict[str, Any] = {}
    if page_size is not None:
        params["page_size"] = page_size
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    return client.request(
        "GET",
        client.api_base,
        "/commerce/notification/v1/topic",
        params=params,
        auth="app",
        scope=NOTIFICATION_SCOPE,
    )


def get_topic(topic_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/topic/{topic_id}"""
    client = EbayClient()
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/notification/v1/topic/{topic_id}",
        auth="app",
        scope=NOTIFICATION_SCOPE,
    )


def get_notification_config() -> Dict[str, Any]:
    """GET /commerce/notification/v1/config"""
    client = EbayClient()
    return client.request(
        "GET",
        client.api_base,
        "/commerce/notification/v1/config",
        auth="app",
        scope=NOTIFICATION_SCOPE,
    )


def update_notification_config(alert_email: str) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/config"""
    client = EbayClient()
    return client.request(
        "PUT",
        client.api_base,
        "/commerce/notification/v1/config",
        json_body={"alertEmail": alert_email},
        headers={"Content-Type": "application/json"},
        auth="app",
        scope=NOTIFICATION_SCOPE,
    )


def get_public_key(public_key_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/public_key/{public_key_id}"""
    client = EbayClient()
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/notification/v1/public_key/{public_key_id}",
        auth="app",
        scope=NOTIFICATION_SCOPE,
    )


def create_subscription_filter(
    subscription_id: str,
    filter_schema: Dict[str, Any],
    *,
    auth_type: str = "app",
) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/filter"""
    client = EbayClient()
    scope = (
        NOTIFICATION_SCOPE
        if auth_type == "app"
        else "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
    )
    return client.request(
        "POST",
        client.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}/filter",
        json_body={"filterSchema": filter_schema},
        headers={"Content-Type": "application/json"},
        auth=auth_type,
        scope=scope,
    )


def get_subscription_filter(
    subscription_id: str,
    filter_id: str,
    *,
    auth_type: str = "app",
) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}"""
    client = EbayClient()
    scope = (
        NOTIFICATION_SCOPE
        if auth_type == "app"
        else "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly"
    )
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}",
        auth=auth_type,
        scope=scope,
    )


def delete_subscription_filter(
    subscription_id: str,
    filter_id: str,
    *,
    auth_type: str = "app",
) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}"""
    client = EbayClient()
    scope = (
        NOTIFICATION_SCOPE
        if auth_type == "app"
        else "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
    )
    return client.request(
        "DELETE",
        client.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}",
        auth=auth_type,
        scope=scope,
    )
