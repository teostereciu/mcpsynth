from typing import Any, Dict, Optional

from .http_client import EbayHTTP


NOTIFICATION_SCOPE_APP = "https://api.ebay.com/oauth/api_scope"


def get_config() -> Dict[str, Any]:
    """GET /commerce/notification/v1/config

    Doc: docs/api_commerce_notification_resources_config_methods_getConfig.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        "/commerce/notification/v1/config",
        scope=NOTIFICATION_SCOPE_APP,
    )


def update_config(payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/config

    Doc: docs/api_commerce_notification_resources_config_methods_updateConfig.md
    """
    http = EbayHTTP()
    return http.request(
        "PUT",
        http.oauth.api_base,
        "/commerce/notification/v1/config",
        scope=NOTIFICATION_SCOPE_APP,
        json=payload,
        headers={"Content-Type": "application/json"},
    )


def create_destination(*, endpoint: str, verification_token: str, status: str = "ENABLED", name: Optional[str] = None) -> Dict[str, Any]:
    """POST /commerce/notification/v1/destination

    Doc: docs/api_commerce_notification_resources_destination_methods_createDestination.md
    """
    http = EbayHTTP()
    body: Dict[str, Any] = {
        "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
        "status": status,
    }
    if name is not None:
        body["name"] = name

    return http.request(
        "POST",
        http.oauth.api_base,
        "/commerce/notification/v1/destination",
        scope=NOTIFICATION_SCOPE_APP,
        json=body,
        headers={"Content-Type": "application/json"},
    )


def get_destinations() -> Dict[str, Any]:
    """GET /commerce/notification/v1/destination

    Doc: docs/api_commerce_notification_resources_destination_methods_getDestinations.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        "/commerce/notification/v1/destination",
        scope=NOTIFICATION_SCOPE_APP,
    )


def get_destination(destination_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/destination/{destination_id}

    Doc: docs/api_commerce_notification_resources_destination_methods_getDestination.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/notification/v1/destination/{destination_id}",
        scope=NOTIFICATION_SCOPE_APP,
    )


def update_destination(destination_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/destination/{destination_id}

    Doc: docs/api_commerce_notification_resources_destination_methods_updateDestination.md
    """
    http = EbayHTTP()
    return http.request(
        "PUT",
        http.oauth.api_base,
        f"/commerce/notification/v1/destination/{destination_id}",
        scope=NOTIFICATION_SCOPE_APP,
        json=payload,
        headers={"Content-Type": "application/json"},
    )


def delete_destination(destination_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/destination/{destination_id}

    Doc: docs/api_commerce_notification_resources_destination_methods_deleteDestination.md
    """
    http = EbayHTTP()
    return http.request(
        "DELETE",
        http.oauth.api_base,
        f"/commerce/notification/v1/destination/{destination_id}",
        scope=NOTIFICATION_SCOPE_APP,
    )


def get_public_key() -> Dict[str, Any]:
    """GET /commerce/notification/v1/public_key

    Doc: docs/api_commerce_notification_resources_public_key_methods_getPublicKey.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        "/commerce/notification/v1/public_key",
        scope=NOTIFICATION_SCOPE_APP,
    )


def get_topics() -> Dict[str, Any]:
    """GET /commerce/notification/v1/topic

    Doc: docs/api_commerce_notification_resources_topic_methods_getTopics.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        "/commerce/notification/v1/topic",
        scope=NOTIFICATION_SCOPE_APP,
    )


def get_topic(topic_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/topic/{topic_id}

    Doc: docs/api_commerce_notification_resources_topic_methods_getTopic.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/notification/v1/topic/{topic_id}",
        scope=NOTIFICATION_SCOPE_APP,
    )


def create_subscription(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription

    Doc: docs/api_commerce_notification_resources_subscription_methods_createSubscription.md
    """
    http = EbayHTTP()
    return http.request(
        "POST",
        http.oauth.api_base,
        "/commerce/notification/v1/subscription",
        scope=NOTIFICATION_SCOPE_APP,
        json=payload,
        headers={"Content-Type": "application/json"},
    )


def get_subscriptions(*, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription

    Doc: docs/api_commerce_notification_resources_subscription_methods_getSubscriptions.md
    """
    http = EbayHTTP()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    return http.request(
        "GET",
        http.oauth.api_base,
        "/commerce/notification/v1/subscription",
        scope=NOTIFICATION_SCOPE_APP,
        params=params or None,
    )


def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription/{subscription_id}

    Doc: docs/api_commerce_notification_resources_subscription_methods_getSubscription.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}",
        scope=NOTIFICATION_SCOPE_APP,
    )


def update_subscription(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/subscription/{subscription_id}

    Doc: docs/api_commerce_notification_resources_subscription_methods_updateSubscription.md
    """
    http = EbayHTTP()
    return http.request(
        "PUT",
        http.oauth.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}",
        scope=NOTIFICATION_SCOPE_APP,
        json=payload,
        headers={"Content-Type": "application/json"},
    )


def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/subscription/{subscription_id}

    Doc: docs/api_commerce_notification_resources_subscription_methods_deleteSubscription.md
    """
    http = EbayHTTP()
    return http.request(
        "DELETE",
        http.oauth.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}",
        scope=NOTIFICATION_SCOPE_APP,
    )


def enable_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/enable

    Doc: docs/api_commerce_notification_resources_subscription_methods_enableSubscription.md
    """
    http = EbayHTTP()
    return http.request(
        "POST",
        http.oauth.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}/enable",
        scope=NOTIFICATION_SCOPE_APP,
    )


def disable_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/disable

    Doc: docs/api_commerce_notification_resources_subscription_methods_disableSubscription.md
    """
    http = EbayHTTP()
    return http.request(
        "POST",
        http.oauth.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}/disable",
        scope=NOTIFICATION_SCOPE_APP,
    )


def test_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/test

    Doc: docs/api_commerce_notification_resources_subscription_methods_testSubscription.md
    """
    http = EbayHTTP()
    return http.request(
        "POST",
        http.oauth.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}/test",
        scope=NOTIFICATION_SCOPE_APP,
    )


def create_subscription_filter(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/filter

    Doc: docs/api_commerce_notification_resources_subscription_methods_createSubscriptionFilter.md
    """
    http = EbayHTTP()
    return http.request(
        "POST",
        http.oauth.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}/filter",
        scope=NOTIFICATION_SCOPE_APP,
        json=payload,
        headers={"Content-Type": "application/json"},
    )


def get_subscription_filter(subscription_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription/{subscription_id}/filter

    Doc: docs/api_commerce_notification_resources_subscription_methods_getSubscriptionFilter.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}/filter",
        scope=NOTIFICATION_SCOPE_APP,
    )


def delete_subscription_filter(subscription_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/subscription/{subscription_id}/filter

    Doc: docs/api_commerce_notification_resources_subscription_methods_deleteSubscriptionFilter.md
    """
    http = EbayHTTP()
    return http.request(
        "DELETE",
        http.oauth.api_base,
        f"/commerce/notification/v1/subscription/{subscription_id}/filter",
        scope=NOTIFICATION_SCOPE_APP,
    )


def test(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/notification/v1/test

    Doc: docs/api_commerce_notification_resources_subscription_methods_test.md
    """
    http = EbayHTTP()
    return http.request(
        "POST",
        http.oauth.api_base,
        "/commerce/notification/v1/test",
        scope=NOTIFICATION_SCOPE_APP,
        json=payload,
        headers={"Content-Type": "application/json"},
    )
