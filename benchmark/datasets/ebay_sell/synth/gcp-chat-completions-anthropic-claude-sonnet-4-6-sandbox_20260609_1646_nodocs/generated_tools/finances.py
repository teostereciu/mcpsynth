"""
eBay Sell Finances API tools.
Covers: transactions, payouts, seller funds summary, fees, charges.
"""

from typing import Optional
from auth import api_get, api_post


# ---------------------------------------------------------------------------
# Transactions
# ---------------------------------------------------------------------------

def get_transactions(
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Get a list of financial transactions.

    filter examples:
      "transactionDate:[2024-01-01T00:00:00.000Z..]"
      "transactionType:{SALE|REFUND|CREDIT|DISPUTE|NON_SALE_CHARGE}"
      "orderId:{12345}"
    sort: e.g. "TRANSACTION_DATE_DESC"
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return api_get("/sell/finances/v1/transaction", params=params)


def get_transaction_summary(filter: Optional[str] = None) -> dict:
    """
    Get a summary of financial transactions (totals by type).

    filter: same syntax as get_transactions filter.
    """
    params = {}
    if filter:
        params["filter"] = filter
    return api_get("/sell/finances/v1/transaction_summary", params=params or None)


# ---------------------------------------------------------------------------
# Payouts
# ---------------------------------------------------------------------------

def get_payouts(
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Get a list of payouts.

    filter examples:
      "payoutDate:[2024-01-01T00:00:00.000Z..]"
      "payoutStatus:{SUCCEEDED|INITIATED|RETRYABLE_FAILED|TERMINAL_FAILED}"
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return api_get("/sell/finances/v1/payout", params=params)


def get_payout(payout_id: str) -> dict:
    """Get a specific payout by ID."""
    return api_get(f"/sell/finances/v1/payout/{payout_id}")


def get_payout_summary(filter: Optional[str] = None) -> dict:
    """Get a summary of payouts (totals, counts by status)."""
    params = {}
    if filter:
        params["filter"] = filter
    return api_get("/sell/finances/v1/payout_summary", params=params or None)


def get_transactions_for_payout(payout_id: str, limit: int = 20, offset: int = 0) -> dict:
    """Get all transactions associated with a specific payout."""
    return api_get(f"/sell/finances/v1/payout/{payout_id}/transaction",
                   params={"limit": limit, "offset": offset})


# ---------------------------------------------------------------------------
# Seller Funds Summary
# ---------------------------------------------------------------------------

def get_seller_funds_summary() -> dict:
    """Get a summary of the seller's available, on-hold, and processing funds."""
    return api_get("/sell/finances/v1/seller_funds_summary")


# ---------------------------------------------------------------------------
# Fees / Charges
# ---------------------------------------------------------------------------

def get_fees(
    filter: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Get a list of seller fees/charges.

    filter: e.g. "transactionDate:[2024-01-01T00:00:00.000Z..]"
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return api_get("/sell/finances/v1/fee", params=params)


# ---------------------------------------------------------------------------
# Transfers
# ---------------------------------------------------------------------------

def get_transfer(transfer_id: str) -> dict:
    """Get details of a specific transfer (charge-back or debit)."""
    return api_get(f"/sell/finances/v1/transfer/{transfer_id}")


def get_transfers(
    filter: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Get a list of transfers.

    filter: e.g. "transferDate:[2024-01-01T00:00:00.000Z..]"
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return api_get("/sell/finances/v1/transfer", params=params)
