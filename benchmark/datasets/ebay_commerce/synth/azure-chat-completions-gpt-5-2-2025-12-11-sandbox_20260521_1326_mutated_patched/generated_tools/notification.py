from typing import Any, Dict, Optional

from .http import EbayAuth, request_json


AUTH = EbayAuth()


def get_config() -> Dict[str, Any]:
    """GET /commerce/notification/v1/config"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="GET", path="/commerce/notification/v1/config", access_token=token)


def update_config(payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/config"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="PUT", path="/commerce/notification/v1/config", json_body=payload, access_token=token)


def create_destination(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/notification/v1/destination"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="POST", path="/commerce/notification/v1/destination", json_body=payload, access_token=token)


def get_destinations() -> Dict[str, Any]:
    """GET /commerce/notification/v1/destination"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="GET", path="/commerce/notification/v1/destination", access_token=token)


def get_destination(destination_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/destination/{destination_id}"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="GET", path=f"/commerce/notification/v1/destination/{destination_id}", access_token=token)


def update_destination(destination_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/destination/{destination_id}"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="PUT", path=f"/commerce/notification/v1/destination/{destination_id}", json_body=payload, access_token=token)


def delete_destination(destination_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/destination/{destination_id}"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="DELETE", path=f"/commerce/notification/v1/destination/{destination_id}", access_token=token)


def get_topics() -> Dict[str, Any]:
    """GET /commerce/notification/v1/topic"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="GET", path="/commerce/notification/v1/topic", access_token=token)


def get_topic(topic_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/topic/{topic_id}"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="GET", path=f"/commerce/notification/v1/topic/{topic_id}", access_token=token)


def create_subscription(payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="POST", path="/commerce/notification/v1/subscription", json_body=payload, access_token=token)


def get_subscriptions() -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="GET", path="/commerce/notification/v1/subscription", access_token=token)


def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription/{subscription_id}"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="GET", path=f"/commerce/notification/v1/subscription/{subscription_id}", access_token=token)


def update_subscription(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /commerce/notification/v1/subscription/{subscription_id}"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="PUT", path=f"/commerce/notification/v1/subscription/{subscription_id}", json_body=payload, access_token=token)


def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/subscription/{subscription_id}"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="DELETE", path=f"/commerce/notification/v1/subscription/{subscription_id}", access_token=token)


def enable_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/enable"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="POST", path=f"/commerce/notification/v1/subscription/{subscription_id}/enable", access_token=token)


def disable_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/disable"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="POST", path=f"/commerce/notification/v1/subscription/{subscription_id}/disable", access_token=token)


def test_subscription(subscription_id: str) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/test"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="POST", path=f"/commerce/notification/v1/subscription/{subscription_id}/test", access_token=token)


def create_subscription_filter(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/notification/v1/subscription/{subscription_id}/filter"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="POST", path=f"/commerce/notification/v1/subscription/{subscription_id}/filter", json_body=payload, access_token=token)


def get_subscription_filter(subscription_id: str) -> Dict[str, Any]:
    """GET /commerce/notification/v1/subscription/{subscription_id}/filter"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="GET", path=f"/commerce/notification/v1/subscription/{subscription_id}/filter", access_token=token)


def delete_subscription_filter(subscription_id: str) -> Dict[str, Any]:
    """DELETE /commerce/notification/v1/subscription/{subscription_id}/filter"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="DELETE", path=f"/commerce/notification/v1/subscription/{subscription_id}/filter", access_token=token)


def get_public_key() -> Dict[str, Any]:
    """GET /commerce/notification/v1/public_key"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(method="GET", path="/commerce/notification/v1/public_key", access_token=token)
