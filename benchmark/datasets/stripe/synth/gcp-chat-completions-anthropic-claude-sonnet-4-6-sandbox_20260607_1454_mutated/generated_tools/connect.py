"""Tools for Stripe Connect API (Accounts, Transfers, Payouts)."""
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


def register_connect_tools(mcp: FastMCP):

    # ---- Accounts ----

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
            email: Email address of the account holder.
            business_type: 'individual', 'company', 'non_profit', or 'government_entity'.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if type:
            data["type"] = type
        if country:
            data["country"] = country
        if email:
            data["email"] = email
        if business_type:
            data["business_type"] = business_type
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/accounts", data=data)

    @mcp.tool()
    def retrieve_account(account_id: str = None) -> dict:
        """Retrieve a connected Account by ID (or the platform account if no ID given).

        Args:
            account_id: The ID of the account (e.g. 'acct_...'). Omit for own account.
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
            email: Email address of the account holder.
            business_type: 'individual', 'company', 'non_profit', or 'government_entity'.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if email:
            data["email"] = email
        if business_type:
            data["business_type"] = business_type
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
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/accounts", params=params)

    @mcp.tool()
    def create_account_link(
        account: str,
        refresh_url: str,
        return_url: str,
        type: str = "account_onboarding",
    ) -> dict:
        """Create an Account Link for Connect onboarding.

        Args:
            account: The ID of the account to create a link for.
            refresh_url: URL to redirect if the link expires.
            return_url: URL to redirect after onboarding.
            type: 'account_onboarding' or 'account_update'.
        """
        data = {
            "account": account,
            "refresh_url": refresh_url,
            "return_url": return_url,
            "type": type,
        }
        return _req("POST", "/v1/account_links", data=data)

    # ---- Transfers ----

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
            description: Arbitrary string attached to the object.
            transfer_group: Group identifier for related transfers.
            metadata: Key-value pairs to attach to the object.
        """
        data = {
            "amount": amount,
            "currency": currency,
            "destination": destination,
        }
        if description:
            data["description"] = description
        if transfer_group:
            data["transfer_group"] = transfer_group
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/transfers", data=data)

    @mcp.tool()
    def retrieve_transfer(transfer_id: str) -> dict:
        """Retrieve a Transfer by ID.

        Args:
            transfer_id: The ID of the transfer (e.g. 'tr_...').
        """
        return _req("GET", f"/v1/transfers/{transfer_id}")

    @mcp.tool()
    def update_transfer(
        transfer_id: str,
        description: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Transfer.

        Args:
            transfer_id: The ID of the transfer to update.
            description: Arbitrary string attached to the object.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if description:
            data["description"] = description
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
        if destination:
            params["destination"] = destination
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/transfers", params=params)

    # ---- Payouts ----

    @mcp.tool()
    def create_payout(
        amount: int,
        currency: str,
        description: str = None,
        statement_descriptor: str = None,
        method: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Payout to your bank account.

        Args:
            amount: Amount in smallest currency unit (e.g. cents).
            currency: Three-letter ISO currency code (e.g. 'usd').
            description: Arbitrary string attached to the object.
            statement_descriptor: Text on bank statement (max 22 chars).
            method: 'standard' or 'instant'.
            metadata: Key-value pairs to attach to the object.
        """
        data = {"amount": amount, "currency": currency}
        if description:
            data["description"] = description
        if statement_descriptor:
            data["statement_descriptor"] = statement_descriptor
        if method:
            data["method"] = method
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/payouts", data=data)

    @mcp.tool()
    def retrieve_payout(payout_id: str) -> dict:
        """Retrieve a Payout by ID.

        Args:
            payout_id: The ID of the payout (e.g. 'po_...').
        """
        return _req("GET", f"/v1/payouts/{payout_id}")

    @mcp.tool()
    def cancel_payout(payout_id: str) -> dict:
        """Cancel a pending Payout.

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
        if status:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/payouts", params=params)
