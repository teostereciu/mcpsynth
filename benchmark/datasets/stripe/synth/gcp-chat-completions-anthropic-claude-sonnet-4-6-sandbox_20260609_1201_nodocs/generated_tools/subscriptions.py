"""
Stripe Subscriptions tools.
Endpoints covered:
  POST   /v1/subscriptions
  GET    /v1/subscriptions/{id}
  POST   /v1/subscriptions/{id}
  DELETE /v1/subscriptions/{id}
  GET    /v1/subscriptions
  POST   /v1/subscriptions/{id}/resume
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_subscription(
        customer: str,
        items: list,
        default_payment_method: str = None,
        trial_period_days: int = None,
        trial_end: int = None,
        cancel_at_period_end: bool = None,
        cancel_at: int = None,
        billing_cycle_anchor: int = None,
        proration_behavior: str = None,
        coupon: str = None,
        promotion_code: str = None,
        collection_method: str = None,
        days_until_due: int = None,
        metadata: dict = None,
        payment_behavior: str = None,
        off_session: bool = None,
    ) -> dict:
        """
        Create a Subscription.
        items: list of dicts with keys 'price' (required) and optionally 'quantity'.
        proration_behavior: create_prorations | none | always_invoice
        collection_method: charge_automatically | send_invoice
        """
        data = {"customer": customer}
        for i, item in enumerate(items):
            if "price" in item:
                data[f"items[{i}][price]"] = item["price"]
            if "quantity" in item:
                data[f"items[{i}][quantity]"] = item["quantity"]
        if default_payment_method:
            data["default_payment_method"] = default_payment_method
        if trial_period_days is not None:
            data["trial_period_days"] = trial_period_days
        if trial_end is not None:
            data["trial_end"] = trial_end
        if cancel_at_period_end is not None:
            data["cancel_at_period_end"] = str(cancel_at_period_end).lower()
        if cancel_at is not None:
            data["cancel_at"] = cancel_at
        if billing_cycle_anchor is not None:
            data["billing_cycle_anchor"] = billing_cycle_anchor
        if proration_behavior:
            data["proration_behavior"] = proration_behavior
        if coupon:
            data["coupon"] = coupon
        if promotion_code:
            data["promotion_code"] = promotion_code
        if collection_method:
            data["collection_method"] = collection_method
        if days_until_due is not None:
            data["days_until_due"] = days_until_due
        if payment_behavior:
            data["payment_behavior"] = payment_behavior
        if off_session is not None:
            data["off_session"] = str(off_session).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/subscriptions", data=data)

    @mcp.tool()
    def get_subscription(subscription_id: str) -> dict:
        """Retrieve a Subscription by ID."""
        return stripe_request("GET", f"/v1/subscriptions/{subscription_id}")

    @mcp.tool()
    def update_subscription(
        subscription_id: str,
        items: list = None,
        default_payment_method: str = None,
        cancel_at_period_end: bool = None,
        cancel_at: int = None,
        proration_behavior: str = None,
        coupon: str = None,
        promotion_code: str = None,
        trial_end: int = None,
        billing_cycle_anchor: str = None,
        collection_method: str = None,
        days_until_due: int = None,
        metadata: dict = None,
        pause_collection_behavior: str = None,
    ) -> dict:
        """Update a Subscription. billing_cycle_anchor can be 'now' or a timestamp."""
        data = {}
        if items:
            for i, item in enumerate(items):
                if "id" in item:
                    data[f"items[{i}][id]"] = item["id"]
                if "price" in item:
                    data[f"items[{i}][price]"] = item["price"]
                if "quantity" in item:
                    data[f"items[{i}][quantity]"] = item["quantity"]
                if item.get("deleted"):
                    data[f"items[{i}][deleted]"] = "true"
        if default_payment_method:
            data["default_payment_method"] = default_payment_method
        if cancel_at_period_end is not None:
            data["cancel_at_period_end"] = str(cancel_at_period_end).lower()
        if cancel_at is not None:
            data["cancel_at"] = cancel_at
        if proration_behavior:
            data["proration_behavior"] = proration_behavior
        if coupon:
            data["coupon"] = coupon
        if promotion_code:
            data["promotion_code"] = promotion_code
        if trial_end is not None:
            data["trial_end"] = trial_end
        if billing_cycle_anchor:
            data["billing_cycle_anchor"] = billing_cycle_anchor
        if collection_method:
            data["collection_method"] = collection_method
        if days_until_due is not None:
            data["days_until_due"] = days_until_due
        if pause_collection_behavior:
            data["pause_collection[behavior]"] = pause_collection_behavior
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/subscriptions/{subscription_id}", data=data)

    @mcp.tool()
    def cancel_subscription(
        subscription_id: str,
        invoice_now: bool = None,
        prorate: bool = None,
    ) -> dict:
        """Cancel a Subscription immediately."""
        data = {}
        if invoice_now is not None:
            data["invoice_now"] = str(invoice_now).lower()
        if prorate is not None:
            data["prorate"] = str(prorate).lower()
        return stripe_request("DELETE", f"/v1/subscriptions/{subscription_id}", data=data)

    @mcp.tool()
    def list_subscriptions(
        customer: str = None,
        price: str = None,
        status: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        current_period_end_gte: int = None,
        current_period_end_lte: int = None,
    ) -> dict:
        """
        List Subscriptions.
        status: active | past_due | unpaid | canceled | incomplete | incomplete_expired | trialing | all | ended
        """
        params = {}
        if customer:
            params["customer"] = customer
        if price:
            params["price"] = price
        if status:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        if current_period_end_gte is not None:
            params["current_period_end[gte]"] = current_period_end_gte
        if current_period_end_lte is not None:
            params["current_period_end[lte]"] = current_period_end_lte
        return stripe_request("GET", "/v1/subscriptions", params=params)

    @mcp.tool()
    def resume_subscription(
        subscription_id: str,
        billing_cycle_anchor: str = None,
        proration_behavior: str = None,
    ) -> dict:
        """Resume a paused Subscription."""
        data = {}
        if billing_cycle_anchor:
            data["billing_cycle_anchor"] = billing_cycle_anchor
        if proration_behavior:
            data["proration_behavior"] = proration_behavior
        return stripe_request("POST", f"/v1/subscriptions/{subscription_id}/resume", data=data)
