"""eBay Commerce Notification API tools (webhooks, subscriptions, destinations, topics)."""
from mcp.server.fastmcp import FastMCP
from .auth import get_app_token, get_base_url

def register(mcp: FastMCP):

    def _headers(token: dict) -> dict:
        return {"Authorization": f"Bearer {token['access_token']}"}

    def _json_headers(token: dict) -> dict:
        return {
            "Authorization": f"Bearer {token['access_token']}",
            "Content-Type": "application/json",
        }

    # ── Config ─────────────────────────────────────────────────────────────────

    @mcp.tool()
    def get_notification_config() -> dict:
        """Retrieve the current Notification API configuration (alert email address)."""
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/config"
        try:
            resp = requests.get(url, headers=_headers(token), timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_notification_config(alert_email: str) -> dict:
        """Create or update the Notification API configuration with an alert email address.

        Args:
            alert_email: Email address for Notification API alerts.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/config"
        try:
            resp = requests.put(url, headers=_json_headers(token),
                                json={"alertEmail": alert_email}, timeout=30)
            if resp.status_code in (200, 204):
                return {"status": "updated"}
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    # ── Destinations ───────────────────────────────────────────────────────────

    @mcp.tool()
    def create_destination(
        endpoint: str,
        verification_token: str,
        status: str = "ENABLED",
        name: str = "",
    ) -> dict:
        """Create a notification destination endpoint.

        Args:
            endpoint: HTTPS URL of the destination endpoint.
            verification_token: 32-80 character token (alphanumeric, underscores, hyphens).
            status: ENABLED or DISABLED (default: ENABLED).
            name: Optional name for the destination.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/destination"
        payload: dict = {
            "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
            "status": status,
        }
        if name:
            payload["name"] = name
        try:
            resp = requests.post(url, headers=_json_headers(token), json=payload, timeout=30)
            if resp.status_code in (200, 201, 204):
                result = resp.json() if resp.text else {}
                result["location"] = resp.headers.get("Location", "")
                return result
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_destination(destination_id: str) -> dict:
        """Retrieve details for a specific notification destination.

        Args:
            destination_id: The unique identifier of the destination.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/destination/{destination_id}"
        try:
            resp = requests.get(url, headers=_headers(token), timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_destinations(limit: str = "20", continuation_token: str = "") -> dict:
        """Retrieve a paginated list of all notification destinations.

        Args:
            limit: Max results per page (10-100, default 20).
            continuation_token: Token for next page of results.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/destination"
        params = {}
        if limit:
            params["limit"] = limit
        if continuation_token:
            params["continuation_token"] = continuation_token
        try:
            resp = requests.get(url, headers=_headers(token), params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_destination(
        destination_id: str,
        endpoint: str,
        verification_token: str,
        status: str = "ENABLED",
        name: str = "",
    ) -> dict:
        """Update an existing notification destination.

        Args:
            destination_id: The unique identifier of the destination to update.
            endpoint: HTTPS URL of the destination endpoint.
            verification_token: 32-80 character verification token.
            status: ENABLED or DISABLED.
            name: Optional name for the destination.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/destination/{destination_id}"
        payload: dict = {
            "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
            "status": status,
        }
        if name:
            payload["name"] = name
        try:
            resp = requests.put(url, headers=_json_headers(token), json=payload, timeout=30)
            if resp.status_code in (200, 204):
                return {"status": "updated"}
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_destination(destination_id: str) -> dict:
        """Delete a notification destination.

        Args:
            destination_id: The unique identifier of the destination to delete.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/destination/{destination_id}"
        try:
            resp = requests.delete(url, headers=_headers(token), timeout=30)
            if resp.status_code in (200, 204):
                return {"status": "deleted"}
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    # ── Topics ─────────────────────────────────────────────────────────────────

    @mcp.tool()
    def get_notification_topic(topic_id: str) -> dict:
        """Retrieve details for a specific notification topic.

        Args:
            topic_id: The unique identifier of the notification topic.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/topic/{topic_id}"
        try:
            resp = requests.get(url, headers=_headers(token), timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_notification_topics(limit: str = "20", continuation_token: str = "") -> dict:
        """Retrieve a paginated list of all supported notification topics.

        Args:
            limit: Max results per page (10-100, default 20).
            continuation_token: Token for next page of results.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/topic"
        params = {}
        if limit:
            params["limit"] = limit
        if continuation_token:
            params["continuation_token"] = continuation_token
        try:
            resp = requests.get(url, headers=_headers(token), params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    # ── Subscriptions ──────────────────────────────────────────────────────────

    @mcp.tool()
    def create_subscription(
        topic_id: str,
        destination_id: str,
        schema_version: str,
        status: str = "DISABLED",
        delivery_protocol: str = "HTTPS",
        format: str = "JSON",
    ) -> dict:
        """Create a notification subscription for a topic.

        Args:
            topic_id: The unique identifier of the notification topic.
            destination_id: The unique identifier of the destination endpoint.
            schema_version: Schema version for the topic (from get_notification_topic).
            status: ENABLED or DISABLED (default: DISABLED for testing first).
            delivery_protocol: Delivery protocol (currently only HTTPS supported).
            format: Payload format (currently only JSON supported).
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/subscription"
        payload = {
            "topicId": topic_id,
            "destinationId": destination_id,
            "status": status,
            "payload": {
                "deliveryProtocol": delivery_protocol,
                "format": format,
                "schemaVersion": schema_version,
            },
        }
        try:
            resp = requests.post(url, headers=_json_headers(token), json=payload, timeout=30)
            if resp.status_code in (200, 201):
                result = resp.json() if resp.text else {}
                result["location"] = resp.headers.get("Location", "")
                return result
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_subscription(subscription_id: str) -> dict:
        """Retrieve details for a specific notification subscription.

        Args:
            subscription_id: The unique identifier of the subscription.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/subscription/{subscription_id}"
        try:
            resp = requests.get(url, headers=_headers(token), timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_subscriptions(limit: str = "20", continuation_token: str = "") -> dict:
        """Retrieve a paginated list of all notification subscriptions.

        Args:
            limit: Max results per page (10-100, default 20).
            continuation_token: Token for next page of results.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/subscription"
        params = {}
        if limit:
            params["limit"] = limit
        if continuation_token:
            params["continuation_token"] = continuation_token
        try:
            resp = requests.get(url, headers=_headers(token), params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_subscription(
        subscription_id: str,
        destination_id: str,
        schema_version: str,
        status: str,
        delivery_protocol: str = "HTTPS",
        format: str = "JSON",
    ) -> dict:
        """Update an existing notification subscription.

        Args:
            subscription_id: The unique identifier of the subscription to update.
            destination_id: The unique identifier of the destination endpoint.
            schema_version: Schema version for the topic.
            status: ENABLED or DISABLED.
            delivery_protocol: Delivery protocol (currently only HTTPS supported).
            format: Payload format (currently only JSON supported).
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/subscription/{subscription_id}"
        payload = {
            "destinationId": destination_id,
            "status": status,
            "payload": {
                "deliveryProtocol": delivery_protocol,
                "format": format,
                "schemaVersion": schema_version,
            },
        }
        try:
            resp = requests.put(url, headers=_json_headers(token), json=payload, timeout=30)
            if resp.status_code in (200, 204):
                return {"status": "updated"}
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_subscription(subscription_id: str) -> dict:
        """Delete a notification subscription.

        Args:
            subscription_id: The unique identifier of the subscription to delete.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/subscription/{subscription_id}"
        try:
            resp = requests.delete(url, headers=_headers(token), timeout=30)
            if resp.status_code in (200, 204):
                return {"status": "deleted"}
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def enable_subscription(subscription_id: str) -> dict:
        """Enable a disabled notification subscription.

        Args:
            subscription_id: The unique identifier of the subscription to enable.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/subscription/{subscription_id}/enable"
        try:
            resp = requests.post(url, headers=_headers(token), timeout=30)
            if resp.status_code in (200, 204):
                return {"status": "enabled"}
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def disable_subscription(subscription_id: str) -> dict:
        """Disable an active notification subscription.

        Args:
            subscription_id: The unique identifier of the subscription to disable.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/subscription/{subscription_id}/disable"
        try:
            resp = requests.post(url, headers=_headers(token), timeout=30)
            if resp.status_code in (200, 204):
                return {"status": "disabled"}
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def test_subscription(subscription_id: str) -> dict:
        """Send a mocked test notification payload to a subscription's destination.

        Args:
            subscription_id: The unique identifier of the subscription to test.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/subscription/{subscription_id}/test"
        try:
            resp = requests.post(url, headers=_headers(token), timeout=30)
            if resp.status_code in (200, 202):
                return resp.json() if resp.text else {"status": "test sent"}
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_subscription_filter(subscription_id: str, filter_schema: dict) -> dict:
        """Create a filter for a notification subscription.

        Filters allow only notifications matching the criteria to be sent to the destination.

        Args:
            subscription_id: The unique identifier of the subscription.
            filter_schema: A valid JSON Schema Core document (version 2020-12 or later)
                           describing the filter criteria.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/subscription/{subscription_id}/filter"
        payload = {"filterSchema": filter_schema}
        try:
            resp = requests.post(url, headers=_json_headers(token), json=payload, timeout=30)
            if resp.status_code in (200, 201):
                result = resp.json() if resp.text else {}
                result["location"] = resp.headers.get("Location", "")
                return result
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_subscription_filter(subscription_id: str, filter_id: str) -> dict:
        """Retrieve details for a specific subscription filter.

        Args:
            subscription_id: The unique identifier of the subscription.
            filter_id: The unique identifier of the subscription filter.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = (f"{get_base_url()}/commerce/notification/v1/subscription"
               f"/{subscription_id}/filter/{filter_id}")
        try:
            resp = requests.get(url, headers=_headers(token), timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_subscription_filter(subscription_id: str, filter_id: str) -> dict:
        """Disable the active filter on a notification subscription.

        Args:
            subscription_id: The unique identifier of the subscription.
            filter_id: The unique identifier of the subscription filter to delete.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = (f"{get_base_url()}/commerce/notification/v1/subscription"
               f"/{subscription_id}/filter/{filter_id}")
        try:
            resp = requests.delete(url, headers=_headers(token), timeout=30)
            if resp.status_code in (200, 204):
                return {"status": "deleted"}
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    # ── Public Key ─────────────────────────────────────────────────────────────

    @mcp.tool()
    def get_notification_public_key(public_key_id: str) -> dict:
        """Retrieve a public key for validating eBay push notification payloads.

        Args:
            public_key_id: The unique key ID from the X-EBAY-SIGNATURE notification header.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/notification/v1/public_key/{public_key_id}"
        try:
            resp = requests.get(url, headers=_headers(token), timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}
