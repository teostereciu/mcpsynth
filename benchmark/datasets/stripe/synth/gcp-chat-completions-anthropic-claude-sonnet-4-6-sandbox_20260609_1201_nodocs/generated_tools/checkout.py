"""
Stripe Checkout Sessions tools.
Endpoints covered:
  POST   /v1/checkout/sessions
  GET    /v1/checkout/sessions/{id}
  POST   /v1/checkout/sessions/{id}/expire
  GET    /v1/checkout/sessions/{id}/line_items
  GET    /v1/checkout/sessions
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_checkout_session(
        mode: str,
        success_url: str,
        cancel_url: str = None,
        line_items: list = None,
        customer: str = None,
        customer_email: str = None,
        currency: str = None,
        payment_method_types: list = None,
        allow_promotion_codes: bool = None,
        billing_address_collection: str = None,
        shipping_address_collection_allowed_countries: list = None,
        client_reference_id: str = None,
        subscription_data_trial_period_days: int = None,
        metadata: dict = None,
        expires_at: int = None,
        ui_mode: str = None,
        return_url: str = None,
        payment_intent_data_capture_method: str = None,
    ) -> dict:
        """
        Create a Checkout Session.
        mode: payment | setup | subscription
        line_items: list of dicts with keys 'price' and 'quantity'.
        """
        data = {"mode": mode, "success_url": success_url}
        if cancel_url:
            data["cancel_url"] = cancel_url
        if line_items:
            for i, item in enumerate(line_items):
                if "price" in item:
                    data[f"line_items[{i}][price]"] = item["price"]
                if "quantity" in item:
                    data[f"line_items[{i}][quantity]"] = item["quantity"]
                if "price_data" in item:
                    pd = item["price_data"]
                    if "currency" in pd:
                        data[f"line_items[{i}][price_data][currency]"] = pd["currency"]
                    if "unit_amount" in pd:
                        data[f"line_items[{i}][price_data][unit_amount]"] = pd["unit_amount"]
                    if "product" in pd:
                        data[f"line_items[{i}][price_data][product]"] = pd["product"]
                    if "product_data" in pd:
                        pdd = pd["product_data"]
                        if "name" in pdd:
                            data[f"line_items[{i}][price_data][product_data][name]"] = pdd["name"]
        if customer:
            data["customer"] = customer
        if customer_email:
            data["customer_email"] = customer_email
        if currency:
            data["currency"] = currency
        if payment_method_types:
            for i, pm in enumerate(payment_method_types):
                data[f"payment_method_types[{i}]"] = pm
        if allow_promotion_codes is not None:
            data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
        if billing_address_collection:
            data["billing_address_collection"] = billing_address_collection
        if shipping_address_collection_allowed_countries:
            for i, c in enumerate(shipping_address_collection_allowed_countries):
                data[f"shipping_address_collection[allowed_countries][{i}]"] = c
        if client_reference_id:
            data["client_reference_id"] = client_reference_id
        if subscription_data_trial_period_days is not None:
            data["subscription_data[trial_period_days]"] = subscription_data_trial_period_days
        if expires_at is not None:
            data["expires_at"] = expires_at
        if ui_mode:
            data["ui_mode"] = ui_mode
        if return_url:
            data["return_url"] = return_url
        if payment_intent_data_capture_method:
            data["payment_intent_data[capture_method]"] = payment_intent_data_capture_method
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/checkout/sessions", data=data)

    @mcp.tool()
    def get_checkout_session(session_id: str) -> dict:
        """Retrieve a Checkout Session by ID."""
        return stripe_request("GET", f"/v1/checkout/sessions/{session_id}")

    @mcp.tool()
    def expire_checkout_session(session_id: str) -> dict:
        """Expire an open Checkout Session."""
        return stripe_request("POST", f"/v1/checkout/sessions/{session_id}/expire")

    @mcp.tool()
    def list_checkout_session_line_items(
        session_id: str,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List line items for a Checkout Session."""
        params = {}
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", f"/v1/checkout/sessions/{session_id}/line_items", params=params)

    @mcp.tool()
    def list_checkout_sessions(
        customer: str = None,
        payment_intent: str = None,
        subscription: str = None,
        status: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List Checkout Sessions. status: open | complete | expired"""
        params = {}
        if customer:
            params["customer"] = customer
        if payment_intent:
            params["payment_intent"] = payment_intent
        if subscription:
            params["subscription"] = subscription
        if status:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", "/v1/checkout/sessions", params=params)
