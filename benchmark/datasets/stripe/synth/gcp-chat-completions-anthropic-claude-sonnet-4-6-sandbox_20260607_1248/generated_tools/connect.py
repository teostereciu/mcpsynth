"""Tools for Stripe Connect APIs: Accounts, Transfers, Payouts, Setup Intents."""
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


def register_connect_tools(mcp: FastMCP):

    # ── Accounts ───────────────────────────────────────────────────────────

    @mcp.tool()
    def create_account(
        type: str = None,
        country: str = None,
        email: str = None,
        business_type: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a connected Stripe Account.

        Args:
            type: Account type: 'standard', 'express', or 'custom'.
            country: ISO 3166-1 alpha-2 country code (e.g. 'US').
            email: Email address associated with the account.
            business_type: 'individual', 'company', 'non_profit', or 'government_entity'.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if type: data["type"] = type
        if country: data["country"] = country
        if email: data["email"] = email
        if business_type: data["business_type"] = business_type
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/accounts", data=data)

    @mcp.tool()
    def retrieve_account(account_id: str = None) -> dict:
        """Retrieve a connected Account by ID, or the platform account if no ID given.

        Args:
            account_id: The ID of the account to retrieve. Omit for the platform account.
        """
        if account_id:
            return _req("GET", f"/v1/accounts/{account_id}")
        return _req("GET", "/v1/account")

    @mcp.tool()
    def update_account(
        account_id: str,
        email: str = None,
        business_type: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a connected Account.

        Args:
            account_id: The ID of the account to update.
            email: New email address.
            business_type: New business type.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if email: data["email"] = email
        if business_type: data["business_type"] = business_type
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/accounts/{account_id}", data=data)

    @mcp.tool()
    def delete_account(account_id: str) -> dict:
        """Delete a connected Account.

        Args:
            account_id: The ID of the account to delete.
        """
        return _req("DELETE", f"/v1/accounts/{account_id}")

    @mcp.tool()
    def list_accounts(
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all connected Accounts.

        Args:
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/accounts", params=params)

    @mcp.tool()
    def create_account_link(
        account: str,
        refresh_url: str,
        return_url: str,
        type: str,
    ) -> dict:
        """Create an Account Link for Connect onboarding.

        Args:
            account: The ID of the account to create a link for.
            refresh_url: URL to redirect if the link expires.
            return_url: URL to redirect after the user completes onboarding.
            type: 'account_onboarding' or 'account_update'.
        """
        data = {
            "account": account,
            "refresh_url": refresh_url,
            "return_url": return_url,
            "type": type,
        }
        return _req("POST", "/v1/account_links", data=data)

    # ── Transfers ──────────────────────────────────────────────────────────

    @mcp.tool()
    def create_transfer(
        amount: int,
        currency: str,
        destination: str,
        description: str = None,
        transfer_group: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Transfer to a connected Stripe account.

        Args:
            amount: Amount in smallest currency unit (e.g. cents).
            currency: Three-letter ISO currency code (e.g. 'usd').
            destination: ID of the connected Stripe account to transfer to.
            description: Arbitrary string attached to the transfer.
            transfer_group: Group identifier for related transfers.
            metadata: Key-value pairs to attach.
        """
        data = {
            "amount": amount,
            "currency": currency,
            "destination": destination,
        }
        if description: data["description"] = description
        if transfer_group: data["transfer_group"] = transfer_group
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/transfers", data=data)

    @mcp.tool()
    def retrieve_transfer(transfer_id: str) -> dict:
        """Retrieve a Transfer by ID.

        Args:
            transfer_id: The ID of the transfer to retrieve.
        """
        return _req("GET", f"/v1/transfers/{transfer_id}")

    @mcp.tool()
    def update_transfer(
        transfer_id: str,
        description: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Transfer's metadata or description.

        Args:
            transfer_id: The ID of the transfer to update.
            description: New description.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if description: data["description"] = description
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/transfers/{transfer_id}", data=data)

    @mcp.tool()
    def list_transfers(
        destination: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Transfers.

        Args:
            destination: Filter by destination account ID.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if destination: params["destination"] = destination
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/transfers", params=params)

    # ── Payouts ────────────────────────────────────────────────────────────

    @mcp.tool()
    def create_payout(
        amount: int,
        currency: str,
        description: str = None,
        statement_descriptor: str = None,
        method: str = None,
        destination: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Payout to your bank account.

        Args:
            amount: Amount in smallest currency unit (e.g. cents).
            currency: Three-letter ISO currency code (e.g. 'usd').
            description: Arbitrary string attached to the payout.
            statement_descriptor: Text on the bank statement (up to 22 chars).
            method: 'standard' or 'instant'.
            destination: ID of the bank account or card to payout to.
            metadata: Key-value pairs to attach.
        """
        data = {"amount": amount, "currency": currency}
        if description: data["description"] = description
        if statement_descriptor: data["statement_descriptor"] = statement_descriptor
        if method: data["method"] = method
        if destination: data["destination"] = destination
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/payouts", data=data)

    @mcp.tool()
    def retrieve_payout(payout_id: str) -> dict:
        """Retrieve a Payout by ID.

        Args:
            payout_id: The ID of the payout to retrieve.
        """
        return _req("GET", f"/v1/payouts/{payout_id}")

    @mcp.tool()
    def update_payout(
        payout_id: str,
        metadata: dict = None,
    ) -> dict:
        """Update a Payout's metadata.

        Args:
            payout_id: The ID of the payout to update.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/payouts/{payout_id}", data=data)

    @mcp.tool()
    def cancel_payout(payout_id: str) -> dict:
        """Cancel a Payout that is still pending.

        Args:
            payout_id: The ID of the payout to cancel.
        """
        return _req("POST", f"/v1/payouts/{payout_id}/cancel")

    @mcp.tool()
    def list_payouts(
        status: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Payouts.

        Args:
            status: Filter by status: 'pending', 'paid', 'failed', 'canceled'.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if status: params["status"] = status
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/payouts", params=params)

    # ── Setup Intents ──────────────────────────────────────────────────────

    @mcp.tool()
    def create_setup_intent(
        customer: str = None,
        payment_method: str = None,
        payment_method_types: list = None,
        usage: str = None,
        description: str = None,
        confirm: bool = None,
        metadata: dict = None,
    ) -> dict:
        """Create a SetupIntent to save a payment method for future use.

        Args:
            customer: ID of the Customer this SetupIntent belongs to.
            payment_method: ID of the payment method to attach.
            payment_method_types: List of payment method types (e.g. ['card']).
            usage: 'off_session' or 'on_session'.
            description: Arbitrary string attached to the object.
            confirm: Set True to confirm immediately.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if customer: data["customer"] = customer
        if payment_method: data["payment_method"] = payment_method
        if payment_method_types:
            for i, pmt in enumerate(payment_method_types):
                data[f"payment_method_types[{i}]"] = pmt
        if usage: data["usage"] = usage
        if description: data["description"] = description
        if confirm is not None: data["confirm"] = str(confirm).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/setup_intents", data=data)

    @mcp.tool()
    def retrieve_setup_intent(setup_intent_id: str) -> dict:
        """Retrieve a SetupIntent by ID.

        Args:
            setup_intent_id: The ID of the SetupIntent to retrieve.
        """
        return _req("GET", f"/v1/setup_intents/{setup_intent_id}")

    @mcp.tool()
    def update_setup_intent(
        setup_intent_id: str,
        customer: str = None,
        payment_method: str = None,
        description: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a SetupIntent.

        Args:
            setup_intent_id: The ID of the SetupIntent to update.
            customer: New customer ID.
            payment_method: New payment method ID.
            description: New description.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if customer: data["customer"] = customer
        if payment_method: data["payment_method"] = payment_method
        if description: data["description"] = description
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/setup_intents/{setup_intent_id}", data=data)

    @mcp.tool()
    def confirm_setup_intent(
        setup_intent_id: str,
        payment_method: str = None,
        return_url: str = None,
    ) -> dict:
        """Confirm a SetupIntent to complete payment method setup.

        Args:
            setup_intent_id: The ID of the SetupIntent to confirm.
            payment_method: ID of the payment method to use.
            return_url: URL to redirect after confirmation.
        """
        data = {}
        if payment_method: data["payment_method"] = payment_method
        if return_url: data["return_url"] = return_url
        return _req("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", data=data)

    @mcp.tool()
    def cancel_setup_intent(
        setup_intent_id: str,
        cancellation_reason: str = None,
    ) -> dict:
        """Cancel a SetupIntent.

        Args:
            setup_intent_id: The ID of the SetupIntent to cancel.
            cancellation_reason: Reason: 'abandoned', 'requested_by_customer', or 'duplicate'.
        """
        data = {}
        if cancellation_reason: data["cancellation_reason"] = cancellation_reason
        return _req("POST", f"/v1/setup_intents/{setup_intent_id}/cancel", data=data)

    @mcp.tool()
    def list_setup_intents(
        customer: str = None,
        payment_method: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all SetupIntents.

        Args:
            customer: Filter by customer ID.
            payment_method: Filter by payment method ID.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if customer: params["customer"] = customer
        if payment_method: params["payment_method"] = payment_method
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/setup_intents", params=params)
