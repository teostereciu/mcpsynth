from typing import Any, Dict, Optional

from .common import client


def get_config() -> Dict[str, Any]:
    return client.request("GET", "/commerce/notification/v1/config", "user")


def update_config(body: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", "/commerce/notification/v1/config", "user", json_body=body)


def create_destination(body: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/commerce/notification/v1/destination", "user", json_body=body)


def get_destination(destination_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/notification/v1/destination/{destination_id}", "user")


def delete_destination(destination_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/commerce/notification/v1/destination/{destination_id}", "user")


def get_destinations(limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    return client.request("GET", "/commerce/notification/v1/destination", "user", params={"limit": limit, "continuation_token": continuation_token})


def create_subscription(body: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/commerce/notification/v1/subscription", "user", json_body=body)


def get_subscription(subscription_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/notification/v1/subscription/{subscription_id}", "user")


def update_subscription(subscription_id: str, body: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/commerce/notification/v1/subscription/{subscription_id}", "user", json_body=body)


def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}", "user")


def get_subscriptions(limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    return client.request("GET", "/commerce/notification/v1/subscription", "user", params={"limit": limit, "continuation_token": continuation_token})


def get_topics(limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    return client.request("GET", "/commerce/notification/v1/topic", "user", params={"limit": limit, "continuation_token": continuation_token})


def get_topic(topic_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/notification/v1/topic/{topic_id}", "user")
