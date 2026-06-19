"""
eBay Sell Finances API tools.
Covers: transactions, payouts, seller funds summary, fees, tax reports.
"""

from mcp.server.fastmcp import FastMCP
from .auth import ebay_request

mcp = FastMCP("ebay-finances")

# ---------------------------------------------------------------------------
# Transactions
# ---------------------------------------------------------------------------

@mcp.tool()
def get_transactions(
    filter: str | None = None,
    sort: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Retrieve financial transactions for the seller.

    Args:
        filter: Filter string. Supported filters include:
                transactionDate, transactionType, transactionStatus,
                buyerUsername, salesRecordReference, orderId.
                Example: "transactionType:{SALE},transactionDate:[2024-01-01T00:00:00Z..]"
        sort: Sort field, e.g. 'TRANSACTION_DATE' or '-TRANSACTION_DATE'.
        limit: Number of transactions to return (default 20, max 1000).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return ebay_request("GET", "/sell/finances/v1/transaction", params=params)


@mcp.tool()
def get_transaction_summary(filter: str | None = None) -> dict:
    """
    Retrieve a summary of financial transactions (totals by type).

    Args:
        filter: Optional filter string (same syntax as get_transactions).
    """
    params: dict = {}
    if filter:
        params["filter"] = filter
    return ebay_request(
        "GET",
        "/sell/finances/v1/transaction_summary",
        params=params or None,
    )


# ---------------------------------------------------------------------------
# Payouts
# ---------------------------------------------------------------------------

@mcp.tool()
def get_payouts(
    filter: str | None = None,
    sort: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Retrieve payouts for the seller.

    Args:
        filter: Filter string. Supported filters: payoutDate, payoutStatus,
                lastAttemptedPayoutDate.
                Example: "payoutStatus:{SUCCEEDED},payoutDate:[2024-01-01T00:00:00Z..]"
        sort: Sort field, e.g. 'PAYOUT_DATE' or '-PAYOUT_DATE'.
        limit: Number of payouts to return (default 20, max 200).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return ebay_request("GET", "/sell/finances/v1/payout", params=params)


@mcp.tool()
def get_payout(payout_id: str) -> dict:
    """
    Retrieve a specific payout by its ID.

    Args:
        payout_id: The unique identifier of the payout.
    """
    return ebay_request("GET", f"/sell/finances/v1/payout/{payout_id}")


@mcp.tool()
def get_payout_summary(filter: str | None = None) -> dict:
    """
    Retrieve a summary of payouts (totals by status).

    Args:
        filter: Optional filter string (same syntax as get_payouts).
    """
    params: dict = {}
    if filter:
        params["filter"] = filter
    return ebay_request(
        "GET",
        "/sell/finances/v1/payout_summary",
        params=params or None,
    )


# ---------------------------------------------------------------------------
# Seller Funds Summary
# ---------------------------------------------------------------------------

@mcp.tool()
def get_seller_funds_summary() -> dict:
    """
    Retrieve a summary of the seller's available, processing, and on-hold funds.
    """
    return ebay_request("GET", "/sell/finances/v1/seller_funds_summary")


# ---------------------------------------------------------------------------
# Fees
# ---------------------------------------------------------------------------

@mcp.tool()
def get_fees(
    filter: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Retrieve fee transactions for the seller.

    Args:
        filter: Optional filter string (e.g. by feeType or transactionDate).
        limit: Number of fees to return (default 20).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return ebay_request("GET", "/sell/finances/v1/fee", params=params)


# ---------------------------------------------------------------------------
# Tax Reports
# ---------------------------------------------------------------------------

@mcp.tool()
def get_tax_report(
    year: int,
    marketplace_id: str,
) -> dict:
    """
    Retrieve a tax report for a given year and marketplace.

    Args:
        year: The tax year (e.g. 2023).
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
    """
    return ebay_request(
        "GET",
        "/sell/finances/v1/tax_report",
        params={"year": year, "marketplace_id": marketplace_id},
    )


# ---------------------------------------------------------------------------
# Transfers (buyer-initiated payment reversals)
# ---------------------------------------------------------------------------

@mcp.tool()
def get_transfer(transfer_id: str) -> dict:
    """
    Retrieve details of a specific transfer (payment reversal/chargeback debit).

    Args:
        transfer_id: The unique identifier of the transfer.
    """
    return ebay_request("GET", f"/sell/finances/v1/transfer/{transfer_id}")


@mcp.tool()
def get_transfers(
    filter: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Retrieve transfers (payment reversals) for the seller.

    Args:
        filter: Optional filter string (e.g. by transferDate or transferType).
        limit: Number of transfers to return (default 20).
        offset: Pagination offset (default 0).
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return ebay_request("GET", "/sell/finances/v1/transfer", params=params)
