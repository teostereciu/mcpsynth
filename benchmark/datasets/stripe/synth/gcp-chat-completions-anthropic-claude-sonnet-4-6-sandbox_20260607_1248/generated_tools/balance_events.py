"""Tools for Stripe Balance, Balance Transactions, and Events APIs."""
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


def register_balance_event_tools(mcp: FastMCP):

    # ── Balance ────────────────────────────────────────────────────────────

    @mcp.tool()
    def retrieve_balance() -> dict:
        """Retrieve the current Stripe account balance.

        Returns available and pending funds broken down by currency.
        """
        return _req("GET", "/v1/balance")

    @mcp.tool()
    def retrieve_balance_transaction(transaction_id: str) -> dict:
        """Retrieve a Balance Transaction by ID.

        Args:
            transaction_id: The ID of the balance transaction to retrieve.
        """
        return _req("GET", f"/v1/balance_transactions/{transaction_id}")

    @mcp.tool()
    def list_balance_transactions(
        type: str = None,
        source: str = None,
        currency: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Balance Transactions.

        Args:
            type: Filter by transaction type (e.g. 'charge', 'refund', 'payout').
            source: Filter by source object ID (e.g. charge ID).
            currency: Filter by currency code.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if type: params["type"] = type
        if source: params["source"] = source
        if currency: params["currency"] = currency
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/balance_transactions", params=params)

    # ── Events ─────────────────────────────────────────────────────────────

    @mcp.tool()
    def retrieve_event(event_id: str) -> dict:
        """Retrieve an Event by ID (events are available for 30 days).

        Args:
            event_id: The ID of the event to retrieve.
        """
        return _req("GET", f"/v1/events/{event_id}")

    @mcp.tool()
    def list_events(
        type: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Events (going back up to 30 days).

        Args:
            type: Filter by event type (e.g. 'charge.succeeded', 'customer.created').
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if type: params["type"] = type
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/events", params=params)
