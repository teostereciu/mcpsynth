"""
eBay Sell Finances API tools.
Covers: transactions, payouts, seller funds summary, fees, transfers.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post

mcp = FastMCP("ebay-finances")


# ── Transactions ─────────────────────────────────────────────────────────────

@mcp.tool()
def get_transactions(filter: str | None = None,
                     sort: str | None = None,
                     limit: int = 20,
                     offset: int = 0) -> dict:
    """
    Retrieve financial transactions for the seller account.

    Args:
        filter: Filter string, e.g. 'transactionType:{SALE}' or
                'transactionDate:[2024-01-01T00:00:00.000Z..]'.
        sort: Sort field (e.g. 'TRANSACTION_DATE', '-TRANSACTION_DATE').
        limit: Results per page (max 1000).
        offset: Pagination offset.
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return api_get("/sell/finances/v1/transaction", params=params)


@mcp.tool()
def get_transaction_summary(filter: str | None = None) -> dict:
    """
    Retrieve a summary of financial transactions.

    Args:
        filter: Filter string to scope the summary (same syntax as get_transactions).
    """
    params: dict = {}
    if filter:
        params["filter"] = filter
    return api_get("/sell/finances/v1/transaction_summary", params=params or None)


# ── Payouts ──────────────────────────────────────────────────────────────────

@mcp.tool()
def get_payouts(filter: str | None = None,
                sort: str | None = None,
                limit: int = 20,
                offset: int = 0) -> dict:
    """
    Retrieve payouts for the seller account.

    Args:
        filter: Filter string, e.g. 'payoutStatus:{SUCCEEDED}' or
                'payoutDate:[2024-01-01T00:00:00.000Z..]'.
        sort: Sort field (e.g. 'PAYOUT_DATE', '-PAYOUT_DATE').
        limit: Results per page (max 200).
        offset: Pagination offset.
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return api_get("/sell/finances/v1/payout", params=params)


@mcp.tool()
def get_payout(payout_id: str) -> dict:
    """
    Retrieve a single payout by ID.

    Args:
        payout_id: The payout ID.
    """
    return api_get(f"/sell/finances/v1/payout/{payout_id}")


@mcp.tool()
def get_payout_summary(filter: str | None = None) -> dict:
    """
    Retrieve a summary of payouts.

    Args:
        filter: Filter string to scope the summary.
    """
    params: dict = {}
    if filter:
        params["filter"] = filter
    return api_get("/sell/finances/v1/payout_summary", params=params or None)


@mcp.tool()
def get_transactions_for_payout(payout_id: str,
                                 limit: int = 20,
                                 offset: int = 0) -> dict:
    """
    Retrieve all transactions associated with a specific payout.

    Args:
        payout_id: The payout ID.
        limit: Results per page.
        offset: Pagination offset.
    """
    return api_get(f"/sell/finances/v1/payout/{payout_id}/transaction",
                   params={"limit": limit, "offset": offset})


# ── Seller Funds Summary ─────────────────────────────────────────────────────

@mcp.tool()
def get_seller_funds_summary() -> dict:
    """
    Retrieve a summary of the seller's available, processing, and on-hold funds.
    """
    return api_get("/sell/finances/v1/seller_funds_summary")


# ── Fees ─────────────────────────────────────────────────────────────────────

@mcp.tool()
def get_fees(filter: str | None = None,
             limit: int = 20,
             offset: int = 0) -> dict:
    """
    Retrieve fee transactions for the seller account.

    Args:
        filter: Filter string (e.g. by date range or fee type).
        limit: Results per page.
        offset: Pagination offset.
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return api_get("/sell/finances/v1/fee", params=params)


# ── Transfers ────────────────────────────────────────────────────────────────

@mcp.tool()
def get_transfer(transfer_id: str) -> dict:
    """
    Retrieve details of a funds transfer (e.g. a charge or debit).

    Args:
        transfer_id: The transfer ID.
    """
    return api_get(f"/sell/finances/v1/transfer/{transfer_id}")


# ── Buyer Payment Instrument ─────────────────────────────────────────────────

@mcp.tool()
def get_buyer_payment_instruments(order_id: str) -> dict:
    """
    Retrieve payment instrument details for a buyer's order.

    Args:
        order_id: The eBay order ID.
    """
    return api_get("/sell/finances/v1/buyer_payment_instrument",
                   params={"order_id": order_id})
