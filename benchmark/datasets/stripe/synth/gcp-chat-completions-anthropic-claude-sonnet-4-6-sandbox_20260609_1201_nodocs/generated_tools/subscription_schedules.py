"""
Stripe Subscription Schedules tools.
Endpoints covered:
  POST   /v1/subscription_schedules
  GET    /v1/subscription_schedules/{id}
  POST   /v1/subscription_schedules/{id}
  POST   /v1/subscription_schedules/{id}/cancel
  POST   /v1/subscription_schedules/{id}/release
  GET    /v1/subscription_schedules
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_subscription_schedule(
        customer: str = None,
        from_subscription: str = None,
        start_date: int = None,
        end_behavior: str = None,
        phases: list = None,
        metadata: dict = None,
    ) -> dict:
        """
        Create a Subscription Schedule.
        end_behavior: release | cancel
        phases: list of phase dicts with keys: items (list of {price, quantity}),
                iterations, trial, trial_end, coupon, default_payment_method.
        """
        data = {}
        if customer:
            data["customer"] = customer
        if from_subscription:
            data["from_subscription"] = from_subscription
        if start_date is not None:
            data["start_date"] = start_date
        if end_behavior:
            data["end_behavior"] = end_behavior
        if phases:
            for i, phase in enumerate(phases):
                if "items" in phase:
                    for j, item in enumerate(phase["items"]):
                        if "price" in item:
                            data[f"phases[{i}][items][{j}][price]"] = item["price"]
                        if "quantity" in item:
                            data[f"phases[{i}][items][{j}][quantity]"] = item["quantity"]
                if "iterations" in phase:
                    data[f"phases[{i}][iterations]"] = phase["iterations"]
                if "trial" in phase:
                    data[f"phases[{i}][trial]"] = str(phase["trial"]).lower()
                if "coupon" in phase:
                    data[f"phases[{i}][coupon]"] = phase["coupon"]
                if "default_payment_method" in phase:
                    data[f"phases[{i}][default_payment_method]"] = phase["default_payment_method"]
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/subscription_schedules", data=data)

    @mcp.tool()
    def get_subscription_schedule(subscription_schedule_id: str) -> dict:
        """Retrieve a Subscription Schedule by ID."""
        return stripe_request("GET", f"/v1/subscription_schedules/{subscription_schedule_id}")

    @mcp.tool()
    def update_subscription_schedule(
        subscription_schedule_id: str,
        end_behavior: str = None,
        phases: list = None,
        metadata: dict = None,
        proration_behavior: str = None,
    ) -> dict:
        """Update a Subscription Schedule."""
        data = {}
        if end_behavior:
            data["end_behavior"] = end_behavior
        if proration_behavior:
            data["proration_behavior"] = proration_behavior
        if phases:
            for i, phase in enumerate(phases):
                if "items" in phase:
                    for j, item in enumerate(phase["items"]):
                        if "price" in item:
                            data[f"phases[{i}][items][{j}][price]"] = item["price"]
                        if "quantity" in item:
                            data[f"phases[{i}][items][{j}][quantity]"] = item["quantity"]
                if "iterations" in phase:
                    data[f"phases[{i}][iterations]"] = phase["iterations"]
                if "coupon" in phase:
                    data[f"phases[{i}][coupon]"] = phase["coupon"]
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/subscription_schedules/{subscription_schedule_id}", data=data)

    @mcp.tool()
    def cancel_subscription_schedule(
        subscription_schedule_id: str,
        invoice_now: bool = None,
        prorate: bool = None,
    ) -> dict:
        """Cancel a Subscription Schedule."""
        data = {}
        if invoice_now is not None:
            data["invoice_now"] = str(invoice_now).lower()
        if prorate is not None:
            data["prorate"] = str(prorate).lower()
        return stripe_request(
            "POST",
            f"/v1/subscription_schedules/{subscription_schedule_id}/cancel",
            data=data,
        )

    @mcp.tool()
    def release_subscription_schedule(
        subscription_schedule_id: str,
        preserve_cancel_date: bool = None,
    ) -> dict:
        """Release a Subscription Schedule, converting it to a regular Subscription."""
        data = {}
        if preserve_cancel_date is not None:
            data["preserve_cancel_date"] = str(preserve_cancel_date).lower()
        return stripe_request(
            "POST",
            f"/v1/subscription_schedules/{subscription_schedule_id}/release",
            data=data,
        )

    @mcp.tool()
    def list_subscription_schedules(
        customer: str = None,
        scheduled: bool = None,
        canceled_at_gte: int = None,
        canceled_at_lte: int = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List Subscription Schedules."""
        params = {}
        if customer:
            params["customer"] = customer
        if scheduled is not None:
            params["scheduled"] = str(scheduled).lower()
        if canceled_at_gte is not None:
            params["canceled_at[gte]"] = canceled_at_gte
        if canceled_at_lte is not None:
            params["canceled_at[lte]"] = canceled_at_lte
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", "/v1/subscription_schedules", params=params)
