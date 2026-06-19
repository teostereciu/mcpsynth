"""Tools for Stripe miscellaneous APIs: Balance, Disputes, Events, Payment Methods, Setup Intents, Coupons, Promotion Codes, Payment Links."""
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


def register_misc_tools(mcp: FastMCP):

    # ---- Balance ----

    @mcp.tool()
    def retrieve_balance() -> dict:
        """Retrieve the current Stripe account balance.

        Returns available and pending funds by currency and source type.
        """
        return _req("GET", "/v1/balance")

    @mcp.tool()
    def list_balance_transactions(
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        type: str = None,
    ) -> dict:
        """List all Balance Transactions.

        Args:
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
            type: Filter by transaction type (e.g. 'charge', 'refund', 'payout').
        """
        params = {}
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        if type:
            params["type"] = type
        return _req("GET", "/v1/balance_transactions", params=params)

    @mcp.tool()
    def retrieve_balance_transaction(transaction_id: str) -> dict:
        """Retrieve a Balance Transaction by ID.

        Args:
            transaction_id: The ID of the balance transaction (e.g. 'txn_...').
        """
        return _req("GET", f"/v1/balance_transactions/{transaction_id}")

    # ---- Disputes ----

    @mcp.tool()
    def retrieve_dispute(dispute_id: str) -> dict:
        """Retrieve a Dispute by ID.

        Args:
            dispute_id: The ID of the dispute (e.g. 'du_...').
        """
        return _req("GET", f"/v1/disputes/{dispute_id}")

    @mcp.tool()
    def update_dispute(
        dispute_id: str,
        submit: bool = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Dispute with evidence.

        Args:
            dispute_id: The ID of the dispute to update.
            submit: If True, immediately submit evidence to the bank.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if submit is not None:
            data["submit"] = str(submit).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/disputes/{dispute_id}", data=data)

    @mcp.tool()
    def list_disputes(
        charge: str = None,
        payment_intent: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Disputes.

        Args:
            charge: Filter by charge ID.
            payment_intent: Filter by PaymentIntent ID.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if charge:
            params["charge"] = charge
        if payment_intent:
            params["payment_intent"] = payment_intent
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/disputes", params=params)

    # ---- Events ----

    @mcp.tool()
    def retrieve_event(event_id: str) -> dict:
        """Retrieve an Event by ID.

        Args:
            event_id: The ID of the event (e.g. 'evt_...').
        """
        return _req("GET", f"/v1/events/{event_id}")

    @mcp.tool()
    def list_events(
        type: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Events.

        Args:
            type: Filter by event type (e.g. 'payment_intent.succeeded').
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if type:
            params["type"] = type
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/events", params=params)

    # ---- Payment Methods ----

    @mcp.tool()
    def retrieve_payment_method(payment_method_id: str) -> dict:
        """Retrieve a PaymentMethod by ID.

        Args:
            payment_method_id: The ID of the payment method (e.g. 'pm_...').
        """
        return _req("GET", f"/v1/payment_methods/{payment_method_id}")

    @mcp.tool()
    def attach_payment_method(payment_method_id: str, customer: str) -> dict:
        """Attach a PaymentMethod to a Customer.

        Args:
            payment_method_id: The ID of the payment method to attach.
            customer: The ID of the customer to attach the payment method to.
        """
        return _req("POST", f"/v1/payment_methods/{payment_method_id}/attach",
                    data={"customer": customer})

    @mcp.tool()
    def detach_payment_method(payment_method_id: str) -> dict:
        """Detach a PaymentMethod from its Customer.

        Args:
            payment_method_id: The ID of the payment method to detach.
        """
        return _req("POST", f"/v1/payment_methods/{payment_method_id}/detach")

    @mcp.tool()
    def list_payment_methods(
        customer: str = None,
        type: str = None,
        limit: int = None,
    ) -> dict:
        """List PaymentMethods (optionally for a specific Customer).

        Args:
            customer: Filter by customer ID.
            type: Filter by type (e.g. 'card', 'us_bank_account').
            limit: Number of objects to return (1-100).
        """
        params = {}
        if customer:
            params["customer"] = customer
        if type:
            params["type"] = type
        if limit is not None:
            params["limit"] = limit
        return _req("GET", "/v1/payment_methods", params=params)

    # ---- Setup Intents ----

    @mcp.tool()
    def create_setup_intent(
        customer: str = None,
        payment_method: str = None,
        usage: str = None,
        description: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a SetupIntent to save a payment method for future use.

        Args:
            customer: ID of the Customer this SetupIntent belongs to.
            payment_method: ID of the payment method to attach.
            usage: 'off_session' or 'on_session'. Defaults to 'off_session'.
            description: Arbitrary string attached to the object.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if customer:
            data["customer"] = customer
        if payment_method:
            data["payment_method"] = payment_method
        if usage:
            data["usage"] = usage
        if description:
            data["description"] = description
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/setup_intents", data=data)

    @mcp.tool()
    def retrieve_setup_intent(setup_intent_id: str) -> dict:
        """Retrieve a SetupIntent by ID.

        Args:
            setup_intent_id: The ID of the SetupIntent (e.g. 'seti_...').
        """
        return _req("GET", f"/v1/setup_intents/{setup_intent_id}")

    @mcp.tool()
    def confirm_setup_intent(
        setup_intent_id: str,
        payment_method: str = None,
        return_url: str = None,
    ) -> dict:
        """Confirm a SetupIntent to complete setup.

        Args:
            setup_intent_id: The ID of the SetupIntent to confirm.
            payment_method: ID of the payment method to use.
            return_url: URL to redirect after authentication.
        """
        data = {}
        if payment_method:
            data["payment_method"] = payment_method
        if return_url:
            data["return_url"] = return_url
        return _req("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", data=data)

    @mcp.tool()
    def cancel_setup_intent(setup_intent_id: str) -> dict:
        """Cancel a SetupIntent.

        Args:
            setup_intent_id: The ID of the SetupIntent to cancel.
        """
        return _req("POST", f"/v1/setup_intents/{setup_intent_id}/cancel")

    @mcp.tool()
    def list_setup_intents(
        customer: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all SetupIntents.

        Args:
            customer: Filter by customer ID.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if customer:
            params["customer"] = customer
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/setup_intents", params=params)

    # ---- Coupons ----

    @mcp.tool()
    def create_coupon(
        duration: str,
        amount_off: int = None,
        currency: str = None,
        percent_off: float = None,
        name: str = None,
        duration_in_months: int = None,
        max_redemptions: int = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Coupon for discounts.

        Args:
            duration: 'forever', 'once', or 'repeating'.
            amount_off: Amount to subtract from invoice (requires currency).
            currency: Currency for amount_off (e.g. 'usd').
            percent_off: Percentage discount (0-100).
            name: Name displayed to customers.
            duration_in_months: Months for 'repeating' duration.
            max_redemptions: Maximum number of times coupon can be redeemed.
            metadata: Key-value pairs to attach to the object.
        """
        data = {"duration": duration}
        if amount_off is not None:
            data["amount_off"] = amount_off
        if currency:
            data["currency"] = currency
        if percent_off is not None:
            data["percent_off"] = percent_off
        if name:
            data["name"] = name
        if duration_in_months is not None:
            data["duration_in_months"] = duration_in_months
        if max_redemptions is not None:
            data["max_redemptions"] = max_redemptions
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/coupons", data=data)

    @mcp.tool()
    def retrieve_coupon(coupon_id: str) -> dict:
        """Retrieve a Coupon by ID.

        Args:
            coupon_id: The ID of the coupon.
        """
        return _req("GET", f"/v1/coupons/{coupon_id}")

    @mcp.tool()
    def update_coupon(
        coupon_id: str,
        name: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Coupon's name or metadata.

        Args:
            coupon_id: The ID of the coupon to update.
            name: Name displayed to customers.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if name:
            data["name"] = name
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/coupons/{coupon_id}", data=data)

    @mcp.tool()
    def delete_coupon(coupon_id: str) -> dict:
        """Delete a Coupon.

        Args:
            coupon_id: The ID of the coupon to delete.
        """
        return _req("DELETE", f"/v1/coupons/{coupon_id}")

    @mcp.tool()
    def list_coupons(limit: int = None, starting_after: str = None) -> dict:
        """List all Coupons.

        Args:
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
        """
        params = {}
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        return _req("GET", "/v1/coupons", params=params)

    # ---- Promotion Codes ----

    @mcp.tool()
    def create_promotion_code(
        coupon: str,
        code: str = None,
        customer: str = None,
        expires_at: int = None,
        max_redemptions: int = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Promotion Code for a Coupon.

        Args:
            coupon: The ID of the coupon this promotion code points to.
            code: Customer-facing code (auto-generated if not provided).
            customer: Restrict to a specific customer ID.
            expires_at: Unix timestamp when the code expires.
            max_redemptions: Maximum number of times the code can be redeemed.
            metadata: Key-value pairs to attach to the object.
        """
        data = {"promotion[type]": "coupon", "promotion[coupon]": coupon}
        if code:
            data["code"] = code
        if customer:
            data["customer"] = customer
        if expires_at is not None:
            data["expires_at"] = expires_at
        if max_redemptions is not None:
            data["max_redemptions"] = max_redemptions
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/promotion_codes", data=data)

    @mcp.tool()
    def retrieve_promotion_code(promotion_code_id: str) -> dict:
        """Retrieve a Promotion Code by ID.

        Args:
            promotion_code_id: The ID of the promotion code (e.g. 'promo_...').
        """
        return _req("GET", f"/v1/promotion_codes/{promotion_code_id}")

    @mcp.tool()
    def list_promotion_codes(
        code: str = None,
        coupon: str = None,
        active: bool = None,
        limit: int = None,
    ) -> dict:
        """List all Promotion Codes.

        Args:
            code: Filter by customer-facing code string.
            coupon: Filter by coupon ID.
            active: Filter by active status.
            limit: Number of objects to return (1-100).
        """
        params = {}
        if code:
            params["code"] = code
        if coupon:
            params["coupon"] = coupon
        if active is not None:
            params["active"] = str(active).lower()
        if limit is not None:
            params["limit"] = limit
        return _req("GET", "/v1/promotion_codes", params=params)

    # ---- Payment Links ----

    @mcp.tool()
    def create_payment_link(
        line_items: list,
        metadata: dict = None,
        allow_promotion_codes: bool = None,
    ) -> dict:
        """Create a Payment Link for sharing with customers.

        Args:
            line_items: List of dicts with 'price' and 'quantity' keys.
                        e.g. [{"price": "price_xxx", "quantity": 1}]
            metadata: Key-value pairs to attach to the object.
            allow_promotion_codes: Whether to allow promotion codes.
        """
        data = {}
        for i, item in enumerate(line_items):
            for k, v in item.items():
                data[f"line_items[{i}][{k}]"] = v
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        if allow_promotion_codes is not None:
            data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
        return _req("POST", "/v1/payment_links", data=data)

    @mcp.tool()
    def retrieve_payment_link(payment_link_id: str) -> dict:
        """Retrieve a Payment Link by ID.

        Args:
            payment_link_id: The ID of the payment link (e.g. 'plink_...').
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
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if active is not None:
            data["active"] = str(active).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/payment_links/{payment_link_id}", data=data)

    @mcp.tool()
    def list_payment_links(
        active: bool = None,
        limit: int = None,
        starting_after: str = None,
    ) -> dict:
        """List all Payment Links.

        Args:
            active: Filter by active status.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
        """
        params = {}
        if active is not None:
            params["active"] = str(active).lower()
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        return _req("GET", "/v1/payment_links", params=params)
