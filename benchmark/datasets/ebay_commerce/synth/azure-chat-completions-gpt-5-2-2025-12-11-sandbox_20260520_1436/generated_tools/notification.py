from typing import Any, Dict, Optional

from .ebay_client import EbayClient


APP_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_config() -> Any:
    """GET /commerce/notification/v1/config

    Doc: docs/api_commerce_notification_resources_config_methods_getConfig.md
    """
    client = EbayClient()
    return client.request("GET", "/commerce/notification/v1/config")


def update_config(payload: Dict[str, Any]) -> Any:
    """PUT /commerce/notification/v1/config

    Doc: docs/api_commerce_notification_resources_config_methods_updateConfig.md
    """
    client = EbayClient()
    return client.request("PUT", "/commerce/notification/v1/config", json_body=payload)


def create_destination(delivery_config: Dict[str, Any], status: str, name: Optional[str] = None) -> Any:
    """POST /commerce/notification/v1/destination

    Doc: docs/api_commerce_notification_resources_destination_methods_createDestination.md
    """
    client = EbayClient()
    body: Dict[str, Any] = {"deliveryConfig": delivery_config, "status": status}
    if name is not None:
        body["name"] = name
    return client.request("POST", "/commerce/notification/v1/destination", json_body=body)


def get_destinations() -> Any:
    """GET /commerce/notification/v1/destination

    Doc: docs/api_commerce_notification_resources_destination_methods_getDestinations.md
    """
    client = EbayClient()
    return client.request("GET", "/commerce/notification/v1/destination")


def get_destination(destination_id: str) -> Any:
    """GET /commerce/notification/v1/destination/{destination_id}

    Doc: docs/api_commerce_notification_resources_destination_methods_getDestination.md
    """
    client = EbayClient()
    return client.request("GET", f"/commerce/notification/v1/destination/{destination_id}")


def update_destination(destination_id: str, payload: Dict[str, Any]) -> Any:
    """PUT /commerce/notification/v1/destination/{destination_id}

    Doc: docs/api_commerce_notification_resources_destination_methods_updateDestination.md
    """
    client = EbayClient()
    return client.request("PUT", f"/commerce/notification/v1/destination/{destination_id}", json_body=payload)


def delete_destination(destination_id: str) -> Any:
    """DELETE /commerce/notification/v1/destination/{destination_id}

    Doc: docs/api_commerce_notification_resources_destination_methods_deleteDestination.md
    """
    client = EbayClient()
    return client.request("DELETE", f"/commerce/notification/v1/destination/{destination_id}")


def get_topics() -> Any:
    """GET /commerce/notification/v1/topic

    Doc: docs/api_commerce_notification_resources_topic_methods_getTopics.md
    """
    client = EbayClient()
    return client.request("GET", "/commerce/notification/v1/topic")


def get_topic(topic_id: str) -> Any:
    """GET /commerce/notification/v1/topic/{topic_id}

    Doc: docs/api_commerce_notification_resources_topic_methods_getTopic.md
    """
    client = EbayClient()
    return client.request("GET", f"/commerce/notification/v1/topic/{topic_id}")


def create_subscription(payload: Dict[str, Any]) -> Any:
    """POST /commerce/notification/v1/subscription

    Doc: docs/api_commerce_notification_resources_subscription_methods_createSubscription.md
    """
    client = EbayClient()
    return client.request("POST", "/commerce/notification/v1/subscription", json_body=payload)


def get_subscriptions() -> Any:
    """GET /commerce/notification/v1/subscription

    Doc: docs/api_commerce_notification_resources_subscription_methods_getSubscriptions.md
    """
    client = EbayClient()
    return client.request("GET", "/commerce/notification/v1/subscription")


def get_subscription(subscription_id: str) -> Any:
    """GET /commerce/notification/v1/subscription/{subscription_id}

    Doc: docs/api_commerce_notification_resources_subscription_methods_getSubscription.md
    """
    client = EbayClient()
    return client.request("GET", f"/commerce/notification/v1/subscription/{subscription_id}")


def update_subscription(subscription_id: str, payload: Dict[str, Any]) -> Any:
    """PUT /commerce/notification/v1/subscription/{subscription_id}

    Doc: docs/api_commerce_notification_resources_subscription_methods_updateSubscription.md
    """
    client = EbayClient()
    return client.request("PUT", f"/commerce/notification/v1/subscription/{subscription_id}", json_body=payload)


def delete_subscription(subscription_id: str) -> Any:
    """DELETE /commerce/notification/v1/subscription/{subscription_id}

    Doc: docs/api_commerce_notification_resources_subscription_methods_deleteSubscription.md
    """
    client = EbayClient()
    return client.request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}")


def enable_subscription(subscription_id: str) -> Any:
    """POST /commerce/notification/v1/subscription/{subscription_id}/enable

    Doc: docs/api_commerce_notification_resources_subscription_methods_enableSubscription.md
    """
    client = EbayClient()
    return client.request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/enable")


def disable_subscription(subscription_id: str) -> Any:
    """POST /commerce/notification/v1/subscription/{subscription_id}/disable

    Doc: docs/api_commerce_notification_resources_subscription_methods_disableSubscription.md
    """
    client = EbayClient()
    return client.request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/disable")


def test_subscription(subscription_id: str) -> Any:
    """POST /commerce/notification/v1/subscription/{subscription_id}/test

    Doc: docs/api_commerce_notification_resources_subscription_methods_testSubscription.md
    """
    client = EbayClient()
    return client.request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/test")


def create_subscription_filter(subscription_id: str, payload: Dict[str, Any]) -> Any:
    """POST /commerce/notification/v1/subscription/{subscription_id}/filter

    Doc: docs/api_commerce_notification_resources_subscription_methods_createSubscriptionFilter.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter",
        json_body=payload,
    )


def get_subscription_filter(subscription_id: str) -> Any:
    """GET /commerce/notification/v1/subscription/{subscription_id}/filter

    Doc: docs/api_commerce_notification_resources_subscription_methods_getSubscriptionFilter.md
    """
    client = EbayClient()
    return client.request("GET", f"/commerce/notification/v1/subscription/{subscription_id}/filter")


def delete_subscription_filter(subscription_id: str) -> Any:
    """DELETE /commerce/notification/v1/subscription/{subscription_id}/filter

    Doc: docs/api_commerce_notification_resources_subscription_methods_deleteSubscriptionFilter.md
    """
    client = EbayClient()
    return client.request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}/filter")


def get_public_key() -> Any:
    """GET /commerce/notification/v1/public_key

    Doc: docs/api_commerce_notification_resources_public_key_methods_getPublicKey.md
    """
    client = EbayClient()
    return client.request("GET", "/commerce/notification/v1/public_key")
