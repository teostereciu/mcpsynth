from typing import Any, Dict, Optional

from .http_client import EbayHttpClient


class NotificationTools:
    def __init__(self, client: Optional[EbayHttpClient] = None):
        self.client = client or EbayHttpClient()

    # Config
    def get_config(self) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            "/commerce/notification/v1/config",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
        )

    def update_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request(
            "PUT",
            "/commerce/notification/v1/config",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            json_body=config,
            headers={"Content-Type": "application/json"},
        )

    # Destinations
    def create_destination(
        self,
        *,
        endpoint: str,
        verification_token: str,
        status: str = "ENABLED",
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        body: Dict[str, Any] = {
            "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
            "status": status,
        }
        if name is not None:
            body["name"] = name
        return self.client.request(
            "POST",
            "/commerce/notification/v1/destination",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            json_body=body,
            headers={"Content-Type": "application/json"},
        )

    def get_destinations(self, *, limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = int(limit)
        if continuation_token is not None:
            params["continuation_token"] = continuation_token
        return self.client.request(
            "GET",
            "/commerce/notification/v1/destination",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            params=params,
        )

    def get_destination(self, destination_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/notification/v1/destination/{destination_id}",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
        )

    def update_destination(
        self,
        destination_id: str,
        *,
        endpoint: str,
        verification_token: str,
        status: str = "ENABLED",
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        body: Dict[str, Any] = {
            "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
            "status": status,
        }
        if name is not None:
            body["name"] = name
        return self.client.request(
            "PUT",
            f"/commerce/notification/v1/destination/{destination_id}",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            json_body=body,
            headers={"Content-Type": "application/json"},
        )

    def delete_destination(self, destination_id: str) -> Dict[str, Any]:
        return self.client.request(
            "DELETE",
            f"/commerce/notification/v1/destination/{destination_id}",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
        )

    # Topics
    def get_topics(self, *, limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = int(limit)
        if continuation_token is not None:
            params["continuation_token"] = continuation_token
        return self.client.request(
            "GET",
            "/commerce/notification/v1/topic",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            params=params,
        )

    def get_topic(self, topic_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/notification/v1/topic/{topic_id}",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
        )

    # Subscriptions
    def create_subscription(
        self,
        *,
        topic_id: str,
        destination_id: str,
        payload: Optional[Dict[str, Any]] = None,
        user_based: bool = False,
    ) -> Dict[str, Any]:
        body = payload.copy() if payload else {}
        body.setdefault("topicId", topic_id)
        body.setdefault("destinationId", destination_id)
        token_type = "user" if user_based else "app"
        scope = (
            "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
            if user_based
            else "https://api.ebay.com/oauth/api_scope"
        )
        return self.client.request(
            "POST",
            "/commerce/notification/v1/subscription",
            token_type=token_type,
            scope=scope,
            json_body=body,
            headers={"Content-Type": "application/json"},
        )

    def get_subscriptions(
        self,
        *,
        limit: Optional[int] = None,
        continuation_token: Optional[str] = None,
        user_based: bool = False,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = int(limit)
        if continuation_token is not None:
            params["continuation_token"] = continuation_token
        token_type = "user" if user_based else "app"
        scope = (
            "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
            if user_based
            else "https://api.ebay.com/oauth/api_scope"
        )
        return self.client.request(
            "GET",
            "/commerce/notification/v1/subscription",
            token_type=token_type,
            scope=scope,
            params=params,
        )

    def get_subscription(self, subscription_id: str, *, user_based: bool = False) -> Dict[str, Any]:
        token_type = "user" if user_based else "app"
        scope = (
            "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
            if user_based
            else "https://api.ebay.com/oauth/api_scope"
        )
        return self.client.request(
            "GET",
            f"/commerce/notification/v1/subscription/{subscription_id}",
            token_type=token_type,
            scope=scope,
        )

    def update_subscription(
        self,
        subscription_id: str,
        subscription: Dict[str, Any],
        *,
        user_based: bool = False,
    ) -> Dict[str, Any]:
        token_type = "user" if user_based else "app"
        scope = (
            "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
            if user_based
            else "https://api.ebay.com/oauth/api_scope"
        )
        return self.client.request(
            "PUT",
            f"/commerce/notification/v1/subscription/{subscription_id}",
            token_type=token_type,
            scope=scope,
            json_body=subscription,
            headers={"Content-Type": "application/json"},
        )

    def delete_subscription(self, subscription_id: str, *, user_based: bool = False) -> Dict[str, Any]:
        token_type = "user" if user_based else "app"
        scope = (
            "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
            if user_based
            else "https://api.ebay.com/oauth/api_scope"
        )
        return self.client.request(
            "DELETE",
            f"/commerce/notification/v1/subscription/{subscription_id}",
            token_type=token_type,
            scope=scope,
        )

    def enable_subscription(self, subscription_id: str, *, user_based: bool = False) -> Dict[str, Any]:
        token_type = "user" if user_based else "app"
        scope = (
            "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
            if user_based
            else "https://api.ebay.com/oauth/api_scope"
        )
        return self.client.request(
            "POST",
            f"/commerce/notification/v1/subscription/{subscription_id}/enable",
            token_type=token_type,
            scope=scope,
        )

    def disable_subscription(self, subscription_id: str, *, user_based: bool = False) -> Dict[str, Any]:
        token_type = "user" if user_based else "app"
        scope = (
            "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
            if user_based
            else "https://api.ebay.com/oauth/api_scope"
        )
        return self.client.request(
            "POST",
            f"/commerce/notification/v1/subscription/{subscription_id}/disable",
            token_type=token_type,
            scope=scope,
        )

    def test_subscription(self, subscription_id: str, *, user_based: bool = False) -> Dict[str, Any]:
        token_type = "user" if user_based else "app"
        scope = (
            "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription"
            if user_based
            else "https://api.ebay.com/oauth/api_scope"
        )
        return self.client.request(
            "POST",
            f"/commerce/notification/v1/subscription/{subscription_id}/test",
            token_type=token_type,
            scope=scope,
        )

    def test(self) -> Dict[str, Any]:
        return self.client.request(
            "POST",
            "/commerce/notification/v1/test",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
        )

    # Subscription filters
    def create_subscription_filter(self, subscription_id: str, filter_payload: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request(
            "POST",
            f"/commerce/notification/v1/subscription/{subscription_id}/filter",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            json_body=filter_payload,
            headers={"Content-Type": "application/json"},
        )

    def get_subscription_filter(self, subscription_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/notification/v1/subscription/{subscription_id}/filter",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
        )

    def delete_subscription_filter(self, subscription_id: str) -> Dict[str, Any]:
        return self.client.request(
            "DELETE",
            f"/commerce/notification/v1/subscription/{subscription_id}/filter",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
        )

    # Public key
    def get_public_key(self) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            "/commerce/notification/v1/public_key",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
        )
