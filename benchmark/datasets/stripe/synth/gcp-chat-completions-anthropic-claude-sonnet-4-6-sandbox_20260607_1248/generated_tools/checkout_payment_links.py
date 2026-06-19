"""Tools for Stripe Checkout Sessions and Payment Links APIs."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.stripe.com"

def _get_headers():
    api_key = os.environ.get("STRIPE_API_KEY", "")
    return {"Authorization": f"Bearer {api_key}"}

def _req(method, path, params=None, data=None):
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(
            method, url,
            headers=_get_headers(),
            params=params,
            data=data,
            timeout=30,
        )
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def register_checkout_payment_link_tools(mcp: FastMCP):

    # ── Checkout Sessions ──────────────────────────────────────────────────

    @mcp.tool()
    def create_checkout_session(
        mode: str,
        success_url: str = None,
        cancel_url: str = None,
        return_url: str = None,
        customer: str = None,
        customer_email: str = None,
        line_items: list = None,
        currency: str = None,
        client_reference_id: str = None,
        ui_mode: str = None,
        allow_promotion_codes: bool = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Checkout Session for one-time payments or subscriptions.

        Args:
            mode: 'payment', 'subscription', or 'setup'.
            success_url: URL to redirect after successful payment (required for hosted mode).
            cancel_url: URL to redirect if customer cancels.
            return_url: URL to redirect after auth (required for embedded/custom mode).
            customer: ID of an existing customer.
            customer_email: Email to prefill for the customer.
            line_items: List of dicts with 'price' and 'quantity' keys.
                        e.g. [{"price": "price_xxx", "quantity": 1}]
            currency: Three-letter ISO currency code.
            client_reference_id: Unique string to reference this session.
            ui_mode: 'hosted', 'embedded', or 'custom'.
            allow_promotion_codes: Allow customers to enter promotion codes.
            metadata: Key-value pairs to attach.
        """
        data = {"mode": mode}
        if success_url: data["success_url"] = success_url
        if cancel_url: data["cancel_url"] = cancel_url
        if return_url: data["return_url"] = return_url
        if customer: data["customer"] = customer
        if customer_email: data["customer_email"] = customer_email
        if currency: data["currency"] = currency
        if client_reference_id: data["client_reference_id"] = client_reference_id
        if ui_mode: data["ui_mode"] = ui_mode
        if allow_promotion_codes is not None: data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
        if line_items:
            for i, item in enumerate(line_items):
                for k, v in item.items():
                    data[f"line_items[{i}][{k}]"] = v
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/checkout/sessions", data=data)

    @mcp.tool()
    def retrieve_checkout_session(session_id: str) -> dict:
        """Retrieve a Checkout Session by ID.

        Args:
            session_id: The ID of the checkout session to retrieve.
        """
        return _req("GET", f"/v1/checkout/sessions/{session_id}")

    @mcp.tool()
    def expire_checkout_session(session_id: str) -> dict:
        """Expire a Checkout Session, preventing further payments.

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
        if customer: params["customer"] = customer
        if payment_intent: params["payment_intent"] = payment_intent
        if subscription: params["subscription"] = subscription
        if status: params["status"] = status
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/checkout/sessions", params=params)

    # ── Payment Links ──────────────────────────────────────────────────────

    @mcp.tool()
    def create_payment_link(
        line_items: list,
        allow_promotion_codes: bool = None,
        currency: str = None,
        customer_creation: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a shareable Payment Link.

        Args:
            line_items: List of dicts with 'price' and 'quantity' keys.
                        e.g. [{"price": "price_xxx", "quantity": 1}]
            allow_promotion_codes: Allow customers to enter promotion codes.
            currency: Three-letter ISO currency code.
            customer_creation: 'always' or 'if_required'.
            metadata: Key-value pairs to attach.
        """
        data = {}
        for i, item in enumerate(line_items):
            for k, v in item.items():
                data[f"line_items[{i}][{k}]"] = v
        if allow_promotion_codes is not None: data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
        if currency: data["currency"] = currency
        if customer_creation: data["customer_creation"] = customer_creation
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/payment_links", data=data)

    @mcp.tool()
    def retrieve_payment_link(payment_link_id: str) -> dict:
        """Retrieve a Payment Link by ID.

        Args:
            payment_link_id: The ID of the payment link to retrieve.
        """
        return _req("GET", f"/v1/payment_links/{payment_link_id}")

    @mcp.tool()
    def update_payment_link(
        payment_link_id: str,
        active: bool = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Payment Link.

        Args:
            payment_link_id: The ID of the payment link to update.
            active: Whether the payment link URL is active.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if active is not None: data["active"] = str(active).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/payment_links/{payment_link_id}", data=data)

    @mcp.tool()
    def list_payment_links(
        active: bool = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Payment Links.

        Args:
            active: Filter by active status.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if active is not None: params["active"] = str(active).lower()
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/payment_links", params=params)

    @mcp.tool()
    def list_payment_link_line_items(
        payment_link_id: str,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List line items for a Payment Link.

        Args:
            payment_link_id: The ID of the payment link.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", f"/v1/payment_links/{payment_link_id}/line_items", params=params)
