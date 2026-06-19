"""
Stripe Balance & Balance Transactions tools.
Endpoints covered:
  GET    /v1/balance
  GET    /v1/balance_transactions/{id}
  GET    /v1/balance_transactions
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def get_balance() -> dict:
        """Retrieve the current account balance."""
        return stripe_request("GET", "/v1/balance")

    @mcp.tool()
    def get_balance_transaction(balance_transaction_id: str) -> dict:
        """Retrieve a Balance Transaction by ID."""
        return stripe_request("GET", f"/v1/balance_transactions/{balance_transaction_id}")

    @mcp.tool()
    def list_balance_transactions(
        type: str = None,
        source: str = None,
        payout: str = None,
        currency: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
        available_on_gte: int = None,
        available_on_lte: int = None,
    ) -> dict:
        """
        List Balance Transactions.
        type: charge | refund | adjustment | application_fee | application_fee_refund |
              transfer | payment | payout | payout_failure | stripe_fee | network_cost
        """
        params = {}
        if type:
            params["type"] = type
        if source:
            params["source"] = source
        if payout:
            params["payout"] = payout
        if currency:
            params["currency"] = currency
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
        if available_on_gte is not None:
            params["available_on[gte]"] = available_on_gte
        if available_on_lte is not None:
            params["available_on[lte]"] = available_on_lte
        return stripe_request("GET", "/v1/balance_transactions", params=params)
