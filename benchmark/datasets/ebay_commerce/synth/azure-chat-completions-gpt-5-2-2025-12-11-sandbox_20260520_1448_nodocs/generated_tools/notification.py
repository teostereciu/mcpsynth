from typing import Any, Dict, Optional

from .ebay_http import EbayClient, compact, json_loads_maybe


USER_SCOPE = "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"


def get_public_key() -> Dict[str, Any]:
    """GET /commerce/notification/v1/public_key"""
    c = EbayClient()
    return c.request("GET", "/commerce/notification/v1/public_key", user_scope=USER_SCOPE)


def get_subscriptions() -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription"""
    c = EbayClient()
    return c.request("GET", "/commerce/notification/v1/subscription", user_scope=USER_SCOPE)


def create_subscription(subscription: Any) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription"""
    c = EbayClient()
    body = json_loads_maybe(subscription)
    if not isinstance(body, dict):
        return {"error": "subscription must be a JSON object"}
    return c.request("POST", "/commerce/notification/v1/subscription", json_body=body, user_scope=USER_SCOPE)


def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription/{subscriptionId}"""
    c = EbayClient()
    return c.request(
        "GET",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        user_scope=USER_SCOPE,
    )


def update_subscription(subscription_id: str, subscription: Any) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/subscription/{subscriptionId}"""
    c = EbayClient()
    body = json_loads_maybe(subscription)
    if not isinstance(body, dict):
        return {"error": "subscription must be a JSON object"}
    return c.request(
        "PUT",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        json_body=body,
        user_scope=USER_SCOPE,
    )


def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/subscription/{subscriptionId}"""
    c = EbayClient()
    return c.request(
        "DELETE",
        f"/commerce/notification/v1/subscription/{subscription_id}",
        user_scope=USER_SCOPE,
    )


def get_destination(destination_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/destination/{destinationId}"""
    c = EbayClient()
    return c.request(
        "GET",
        f"/commerce/notification/v1/destination/{destination_id}",
        user_scope=USER_SCOPE,
    )


def get_destinations() -> Dict[str, Any]:
    """GET /commerce/notification/v1/destination"""
    c = EbayClient()
    return c.request("GET", "/commerce/notification/v1/destination", user_scope=USER_SCOPE)


def create_destination(destination: Any) -> Dict[str, Any]:
    """POST /commerce/notification/v1/destination"""
    c = EbayClient()
    body = json_loads_maybe(destination)
    if not isinstance(body, dict):
        return {"error": "destination must be a JSON object"}
    return c.request("POST", "/commerce/notification/v1/destination", json_body=body, user_scope=USER_SCOPE)


def update_destination(destination_id: str, destination: Any) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/destination/{destinationId}"""
    c = EbayClient()
    body = json_loads_maybe(destination)
    if not isinstance(body, dict):
        return {"error": "destination must be a JSON object"}
    return c.request(
        "PUT",
        f"/commerce/notification/v1/destination/{destination_id}",
        json_body=body,
        user_scope=USER_SCOPE,
    )


def delete_destination(destination_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/destination/{destinationId}"""
    c = EbayClient()
    return c.request(
        "DELETE",
        f"/commerce/notification/v1/destination/{destination_id}",
        user_scope=USER_SCOPE,
    )
