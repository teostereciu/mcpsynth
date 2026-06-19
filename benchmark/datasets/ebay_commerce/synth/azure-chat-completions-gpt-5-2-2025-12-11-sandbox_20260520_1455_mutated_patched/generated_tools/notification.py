from __future__ import annotations

from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def get_notification_config() -> Dict[str, Any]:
    """GET /config

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("GET", "/commerce/notification/v1/config")


def update_notification_config(alert_email: str) -> Dict[str, Any]:
    """PUT /config

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "PUT",
        "/commerce/notification/v1/config",
        json={"alertEmail": alert_email},
    )


def create_destination(name: str, status: str, delivery_config: Dict[str, Any]) -> Dict[str, Any]:
    """POST /destination

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "POST",
        "/commerce/notification/v1/destination",
        json={"name": name, "status": status, "deliveryConfig": delivery_config},
    )


def get_destinations() -> Dict[str, Any]:
    """GET /destination

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("GET", "/commerce/notification/v1/destination")


def get_destination(destination_id: str) -> Dict[str, Any]:
    """GET /destination/{destination_id}

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("GET", f"/commerce/notification/v1/destination/{destination_id}")


def update_destination(destination_id: str, name: Optional[str] = None, status: Optional[str] = None, delivery_config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """PUT /destination/{destination_id}

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    payload: Dict[str, Any] = {}
    if name is not None:
        payload["name"] = name
    if status is not None:
        payload["status"] = status
    if delivery_config is not None:
        payload["deliveryConfig"] = delivery_config
    return client.request(
        "PUT",
        f"/commerce/notification/v1/destination/{destination_id}",
        json=payload,
    )


def delete_destination(destination_id: str) -> Dict[str, Any]:
    """DELETE /destination/{destination_id}

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("DELETE", f"/commerce/notification/v1/destination/{destination_id}")


def get_public_key(public_key_id: str) -> Dict[str, Any]:
    """GET /public_key/{public_key_id}

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("GET", f"/commerce/notification/v1/public_key/{public_key_id}")


def create_subscription(topic_id: str, status: str, destination_id: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /subscription

    `payload` can include additional fields supported by eBay (e.g., filter, format, etc.).

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    body: Dict[str, Any] = {"topicId": topic_id, "status": status, "destinationId": destination_id}
    if payload:
        body.update(payload)
    return client.request("POST", "/commerce/notification/v1/subscription", json=body)


def get_subscriptions() -> Dict[str, Any]:
    """GET /subscription

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("GET", "/commerce/notification/v1/subscription")


def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """GET /subscription/{subscription_id}

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("GET", f"/commerce/notification/v1/subscription/{subscription_id}")


def update_subscription(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /subscription/{subscription_id}

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("PUT", f"/commerce/notification/v1/subscription/{subscription_id}", json=payload)


def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """DELETE /subscription/{subscription_id}

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}")


def enable_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /subscription/{subscription_id}/enable

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/enable")


def disable_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /subscription/{subscription_id}/disable

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/disable")


def test_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /subscription/{subscription_id}/test

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/test")


def create_subscription_filter(subscription_id: str, filter_payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /subscription/{subscription_id}/filter

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter",
        json=filter_payload,
    )


def get_subscription_filter(subscription_id: str, filter_id: str) -> Dict[str, Any]:
    """GET /subscription/{subscription_id}/filter/{filter_id}

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "GET",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}",
    )


def delete_subscription_filter(subscription_id: str, filter_id: str) -> Dict[str, Any]:
    """DELETE /subscription/{subscription_id}/filter/{filter_id}

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "DELETE",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}",
    )


def get_topics() -> Dict[str, Any]:
    """GET /topic

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("GET", "/commerce/notification/v1/topic")


def get_topic(topic_id: str) -> Dict[str, Any]:
    """GET /topic/{topic_id}

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("GET", f"/commerce/notification/v1/topic/{topic_id}")
