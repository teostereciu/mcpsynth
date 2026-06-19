"""
Stripe Connect tools — Accounts, Transfers, Payouts.
Endpoints covered:
  POST   /v1/accounts
  GET    /v1/accounts/{id}
  POST   /v1/accounts/{id}
  DELETE /v1/accounts/{id}
  GET    /v1/accounts
  POST   /v1/accounts/{id}/reject
  POST   /v1/transfers
  GET    /v1/transfers/{id}
  POST   /v1/transfers/{id}
  GET    /v1/transfers
  POST   /v1/transfers/{id}/reversals
  GET    /v1/transfers/{id}/reversals/{reversal_id}
  GET    /v1/transfers/{id}/reversals
  POST   /v1/payouts
  GET    /v1/payouts/{id}
  POST   /v1/payouts/{id}
  POST   /v1/payouts/{id}/cancel
  POST   /v1/payouts/{id}/reverse
  GET    /v1/payouts
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    # ── Accounts ───────────────────────────────────────────────────────────────

    @mcp.tool()
    def create_account(
        type: str = None,
        country: str = None,
        email: str = None,
        capabilities: dict = None,
        business_type: str = None,
        company_name: str = None,
        individual_first_name: str = None,
        individual_last_name: str = None,
        individual_email: str = None,
        metadata: dict = None,
        tos_acceptance_date: int = None,
        tos_acceptance_ip: str = None,
    ) -> dict:
        """
        Create a connected Account.
        type: custom | express | standard
        business_type: individual | company | non_profit | government_entity
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
        if company_name:
            data["company[name]"] = company_name
        if individual_first_name:
            data["individual[first_name]"] = individual_first_name
        if individual_last_name:
            data["individual[last_name]"] = individual_last_name
        if individual_email:
            data["individual[email]"] = individual_email
        if tos_acceptance_date is not None:
            data["tos_acceptance[date]"] = tos_acceptance_date
        if tos_acceptance_ip:
            data["tos_acceptance[ip]"] = tos_acceptance_ip
        if capabilities:
            for cap, cap_data in capabilities.items():
                if isinstance(cap_data, dict):
                    for k, v in cap_data.items():
                        data[f"capabilities[{cap}][{k}]"] = str(v).lower()
                else:
                    data[f"capabilities[{cap}]"] = str(cap_data).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/accounts", data=data)

    @mcp.tool()
    def get_account(account_id: str) -> dict:
        """Retrieve a connected Account by ID."""
        return stripe_request("GET", f"/v1/accounts/{account_id}")

    @mcp.tool()
    def update_account(
        account_id: str,
        email: str = None,
        business_type: str = None,
        company_name: str = None,
        individual_first_name: str = None,
        individual_last_name: str = None,
        individual_email: str = None,
        metadata: dict = None,
        tos_acceptance_date: int = None,
        tos_acceptance_ip: str = None,
    ) -> dict:
        """Update a connected Account."""
        data = {}
        if email:
            data["email"] = email
        if business_type:
            data["business_type"] = business_type
        if company_name:
            data["company[name]"] = company_name
        if individual_first_name:
            data["individual[first_name]"] = individual_first_name
        if individual_last_name:
            data["individual[last_name]"] = individual_last_name
        if individual_email:
            data["individual[email]"] = individual_email
        if tos_acceptance_date is not None:
            data["tos_acceptance[date]"] = tos_acceptance_date
        if tos_acceptance_ip:
            data["tos_acceptance[ip]"] = tos_acceptance_ip
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/accounts/{account_id}", data=data)

    @mcp.tool()
    def delete_account(account_id: str) -> dict:
        """Delete a connected Account."""
        return stripe_request("DELETE", f"/v1/accounts/{account_id}")

    @mcp.tool()
    def list_accounts(
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
    ) -> dict:
        """List connected Accounts."""
        params = {}
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        if created_gte is not None:
            params["created[gte]"] = created_gte
        if created_lte is not None:
            params["created[lte]"] = created_lte
        return stripe_request("GET", "/v1/accounts", params=params)

    @mcp.tool()
    def reject_account(account_id: str, reason: str) -> dict:
        """Reject a connected Account. reason: fraud | terms_of_service | other"""
        return stripe_request("POST", f"/v1/accounts/{account_id}/reject", data={"reason": reason})

    # ── Transfers ──────────────────────────────────────────────────────────────

    @mcp.tool()
    def create_transfer(
        amount: int,
        currency: str,
        destination: str,
        description: str = None,
        source_transaction: str = None,
        transfer_group: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Transfer to a connected account."""
        data = {
            "amount": amount,
            "currency": currency,
            "destination": destination,
        }
        if description:
            data["description"] = description
        if source_transaction:
            data["source_transaction"] = source_transaction
        if transfer_group:
            data["transfer_group"] = transfer_group
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/transfers", data=data)

    @mcp.tool()
    def get_transfer(transfer_id: str) -> dict:
        """Retrieve a Transfer by ID."""
        return stripe_request("GET", f"/v1/transfers/{transfer_id}")

    @mcp.tool()
    def update_transfer(
        transfer_id: str,
        description: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Transfer's description or metadata."""
        data = {}
        if description:
            data["description"] = description
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/transfers/{transfer_id}", data=data)

    @mcp.tool()
    def list_transfers(
        destination: str = None,
        transfer_group: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
    ) -> dict:
        """List Transfers."""
        params = {}
        if destination:
            params["destination"] = destination
        if transfer_group:
            params["transfer_group"] = transfer_group
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        if created_gte is not None:
            params["created[gte]"] = created_gte
        if created_lte is not None:
            params["created[lte]"] = created_lte
        return stripe_request("GET", "/v1/transfers", params=params)

    @mcp.tool()
    def create_transfer_reversal(
        transfer_id: str,
        amount: int = None,
        description: str = None,
        refund_application_fee: bool = None,
        metadata: dict = None,
    ) -> dict:
        """Reverse a Transfer (create a Transfer Reversal)."""
        data = {}
        if amount is not None:
            data["amount"] = amount
        if description:
            data["description"] = description
        if refund_application_fee is not None:
            data["refund_application_fee"] = str(refund_application_fee).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/transfers/{transfer_id}/reversals", data=data)

    @mcp.tool()
    def get_transfer_reversal(transfer_id: str, reversal_id: str) -> dict:
        """Retrieve a Transfer Reversal."""
        return stripe_request("GET", f"/v1/transfers/{transfer_id}/reversals/{reversal_id}")

    @mcp.tool()
    def list_transfer_reversals(
        transfer_id: str,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List reversals for a Transfer."""
        params = {}
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", f"/v1/transfers/{transfer_id}/reversals", params=params)

    # ── Payouts ────────────────────────────────────────────────────────────────

    @mcp.tool()
    def create_payout(
        amount: int,
        currency: str,
        description: str = None,
        destination: str = None,
        method: str = None,
        source_type: str = None,
        statement_descriptor: str = None,
        metadata: dict = None,
    ) -> dict:
        """
        Create a Payout to a bank account or debit card.
        method: standard | instant
        source_type: bank_account | fpx | card
        """
        data = {"amount": amount, "currency": currency}
        if description:
            data["description"] = description
        if destination:
            data["destination"] = destination
        if method:
            data["method"] = method
        if source_type:
            data["source_type"] = source_type
        if statement_descriptor:
            data["statement_descriptor"] = statement_descriptor
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/payouts", data=data)

    @mcp.tool()
    def get_payout(payout_id: str) -> dict:
        """Retrieve a Payout by ID."""
        return stripe_request("GET", f"/v1/payouts/{payout_id}")

    @mcp.tool()
    def update_payout(payout_id: str, metadata: dict = None) -> dict:
        """Update a Payout's metadata."""
        data = {}
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/payouts/{payout_id}", data=data)

    @mcp.tool()
    def cancel_payout(payout_id: str) -> dict:
        """Cancel a Payout (only while status=pending)."""
        return stripe_request("POST", f"/v1/payouts/{payout_id}/cancel")

    @mcp.tool()
    def reverse_payout(payout_id: str, metadata: dict = None) -> dict:
        """Reverse a Payout."""
        data = {}
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/payouts/{payout_id}/reverse", data=data)

    @mcp.tool()
    def list_payouts(
        destination: str = None,
        status: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        arrival_date_gte: int = None,
        arrival_date_lte: int = None,
    ) -> dict:
        """List Payouts. status: pending | paid | failed | canceled"""
        params = {}
        if destination:
            params["destination"] = destination
        if status:
            params["status"] = status
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        if arrival_date_gte is not None:
            params["arrival_date[gte]"] = arrival_date_gte
        if arrival_date_lte is not None:
            params["arrival_date[lte]"] = arrival_date_lte
        return stripe_request("GET", "/v1/payouts", params=params)
