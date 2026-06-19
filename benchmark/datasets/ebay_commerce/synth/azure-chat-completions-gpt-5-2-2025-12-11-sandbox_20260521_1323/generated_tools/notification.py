from typing import Any, Dict, Optional

from .http_client import EbayClient


NOTIFICATION_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_config() -> Dict[str, Any]:
    """GET /commerce/notification/v1/config

    Doc: docs/api_commerce_notification_resources_config_methods_getConfig.md
    """
    client = EbayClient()
    return client.request("GET", "/commerce/notification/v1/config", scope=NOTIFICATION_SCOPE)


def update_config(payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/config

    Doc: docs/api_commerce_notification_resources_config_methods_updateConfig.md
    """
    client = EbayClient()
    return client.request("PUT", "/commerce/notification/v1/config", json_body=payload, scope=NOTIFICATION_SCOPE)


def create_destination(endpoint: str, verification_token: str, status: str = "ENABLED", name: Optional[str] = None) -> Dict[str, Any]:
    """POST /commerce/notification/v1/destination

    Doc: docs/api_commerce_notification_resources_destination_methods_createDestination.md
    """
    body: Dict[str, Any] = {
        "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
        "status": status,
    }
    if name is not None:
        body["name"] = name
    client = EbayClient()
    return client.request("POST", "/commerce/notification/v1/destination", json_body=body, scope=NOTIFICATION_SCOPE)


def get_destinations() -> Dict[str, Any]:
    """GET /commerce/notification/v1/destination

    Doc: docs/api_commerce_notification_resources_destination_methods_getDestinations.md
    """
    client = EbayClient()
    return client.request("GET", "/commerce/notification/v1/destination", scope=NOTIFICATION_SCOPE)


def get_destination(destination_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/destination/{destination_id}

    Doc: docs/api_commerce_notification_resources_destination_methods_getDestination.md
    """
    client = EbayClient()
    return client.request("GET", f"/commerce/notification/v1/destination/{destination_id}", scope=NOTIFICATION_SCOPE)


def update_destination(destination_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/destination/{destination_id}

    Doc: docs/api_commerce_notification_resources_destination_methods_updateDestination.md
    """
    client = EbayClient()
    return client.request("PUT", f"/commerce/notification/v1/destination/{destination_id}", json_body=payload, scope=NOTIFICATION_SCOPE)


def delete_destination(destination_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/destination/{destination_id}

    Doc: docs/api_commerce_notification_resources_destination_methods_deleteDestination.md
    """
    client = EbayClient()
    return client.request("DELETE", f"/commerce/notification/v1/destination/{destination_id}", scope=NOTIFICATION_SCOPE)


def get_topics() -> Dict[str, Any]:
    """GET /commerce/notification/v1/topic

    Doc: docs/api_commerce_notification_resources_topic_methods_getTopics.md
    """
    client = EbayClient()
    return client.request("GET", "/commerce/notification/v1/topic", scope=NOTIFICATION_SCOPE)


def get_topic(topic_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/topic/{topic_id}

    Doc: docs/api_commerce_notification_resources_topic_methods_getTopic.md
    """
    client = EbayClient()
    return client.request("GET", f"/commerce/notification/v1/topic/{topic_id}", scope=NOTIFICATION_SCOPE)


def create_subscription(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription

    Doc: docs/api_commerce_notification_resources_subscription_methods_createSubscription.md
    """
    client = EbayClient()
    return client.request("POST", "/commerce/notification/v1/subscription", json_body=payload, scope=NOTIFICATION_SCOPE)


def get_subscriptions() -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription

    Doc: docs/api_commerce_notification_resources_subscription_methods_getSubscriptions.md
    """
    client = EbayClient()
    return client.request("GET", "/commerce/notification/v1/subscription", scope=NOTIFICATION_SCOPE)


def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription/{subscription_id}

    Doc: docs/api_commerce_notification_resources_subscription_methods_getSubscription.md
    """
    client = EbayClient()
    return client.request("GET", f"/commerce/notification/v1/subscription/{subscription_id}", scope=NOTIFICATION_SCOPE)


def update_subscription(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/subscription/{subscription_id}

    Doc: docs/api_commerce_notification_resources_subscription_methods_updateSubscription.md
    """
    client = EbayClient()
    return client.request("PUT", f"/commerce/notification/v1/subscription/{subscription_id}", json_body=payload, scope=NOTIFICATION_SCOPE)


def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/subscription/{subscription_id}

    Doc: docs/api_commerce_notification_resources_subscription_methods_deleteSubscription.md
    """
    client = EbayClient()
    return client.request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}", scope=NOTIFICATION_SCOPE)


def enable_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/enable

    Doc: docs/api_commerce_notification_resources_subscription_methods_enableSubscription.md
    """
    client = EbayClient()
    return client.request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/enable", scope=NOTIFICATION_SCOPE)


def disable_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/disable

    Doc: docs/api_commerce_notification_resources_subscription_methods_disableSubscription.md
    """
    client = EbayClient()
    return client.request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/disable", scope=NOTIFICATION_SCOPE)


def test_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/test

    Doc: docs/api_commerce_notification_resources_subscription_methods_testSubscription.md
    """
    client = EbayClient()
    return client.request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/test", scope=NOTIFICATION_SCOPE)


def create_subscription_filter(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/filter

    Doc: docs/api_commerce_notification_resources_subscription_methods_createSubscriptionFilter.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        f"/commerce/notification/v1/subscription/{subscription_id}/filter",
        json_body=payload,
        scope=NOTIFICATION_SCOPE,
    )


def get_subscription_filter(subscription_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription/{subscription_id}/filter

    Doc: docs/api_commerce_notification_resources_subscription_methods_getSubscriptionFilter.md
    """
    client = EbayClient()
    return client.request("GET", f"/commerce/notification/v1/subscription/{subscription_id}/filter", scope=NOTIFICATION_SCOPE)


def delete_subscription_filter(subscription_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/subscription/{subscription_id}/filter

    Doc: docs/api_commerce_notification_resources_subscription_methods_deleteSubscriptionFilter.md
    """
    client = EbayClient()
    return client.request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}/filter", scope=NOTIFICATION_SCOPE)


def get_public_key(public_key_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/public_key/{public_key_id}

    Doc: docs/api_commerce_notification_resources_public_key_methods_getPublicKey.md
    """
    client = EbayClient()
    return client.request("GET", f"/commerce/notification/v1/public_key/{public_key_id}", scope=NOTIFICATION_SCOPE)
