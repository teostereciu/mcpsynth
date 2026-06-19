"""Tools for Stripe Checkout Sessions API."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.stripe.com"

def _get_headers():
    api_key = os.environ.get("STRIPE_API_KEY", "")
    return {"Authorization": f"Bearer {api_key}"}

def _req(method, path, **kwargs):
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", headers=_get_headers(), **kwargs)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def register_checkout_session_tools(mcp: FastMCP):

    @mcp.tool()
    def create_checkout_session(
        mode: str,
        success_url: str = None,
        cancel_url: str = None,
        line_items: list = None,
        customer: str = None,
        customer_email: str = None,
        currency: str = None,
        metadata: dict = None,
        return_url: str = None,
        ui_mode: str = None,
    ) -> dict:
        """Create a Checkout Session for one-time payments or subscriptions.

        Args:
            mode: 'payment', 'setup', or 'subscription'.
            success_url: URL to redirect after successful payment (for hosted mode).
            cancel_url: URL to redirect if customer cancels.
            line_items: List of dicts with 'price' and 'quantity' keys.
                        e.g. [{"price": "price_xxx", "quantity": 1}]
            customer: ID of an existing Customer.
            customer_email: Customer's email (prefills checkout form).
            currency: Three-letter ISO currency code.
            metadata: Key-value pairs to attach to the object.
            return_url: URL to redirect after auth (for embedded/custom mode).
            ui_mode: 'hosted', 'embedded', or 'custom'. Defaults to 'hosted'.
        """
        data = {"mode": mode}
        if success_url:
            data["success_url"] = success_url
        if cancel_url:
            data["cancel_url"] = cancel_url
        if line_items:
            for i, item in enumerate(line_items):
                for k, v in item.items():
                    data[f"line_items[{i}][{k}]"] = v
        if customer:
            data["customer"] = customer
        if customer_email:
            data["customer_email"] = customer_email
        if currency:
            data["currency"] = currency
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        if return_url:
            data["return_url"] = return_url
        if ui_mode:
            data["ui_mode"] = ui_mode
        return _req("POST", "/v1/checkout/sessions", data=data)

    @mcp.tool()
    def retrieve_checkout_session(session_id: str) -> dict:
        """Retrieve a Checkout Session by ID.

        Args:
            session_id: The ID of the checkout session (e.g. 'cs_...').
        """
        return _req("GET", f"/v1/checkout/sessions/{session_id}")

    @mcp.tool()
    def expire_checkout_session(session_id: str) -> dict:
        """Expire a Checkout Session, preventing further use.

        Args:
            session_id: The ID of the checkout session to expire.
        """
        return _req("POST", f"/v1/checkout/sessions/{session_id}/expire")

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
        """List all Checkout Sessions.

        Args:
            customer: Filter by customer ID.
            payment_intent: Filter by PaymentIntent ID.
            subscription: Filter by subscription ID.
            status: Filter by status: 'open', 'complete', or 'expired'.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
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
        return _req("GET", "/v1/checkout/sessions", params=params)
