"""eBay Sell Finances API tools."""
from typing import Optional
from .client import get_client


def get_transactions(filter: Optional[str] = None, limit: Optional[str] = None,
                     offset: Optional[str] = None, sort_by: Optional[str] = None,
                     marketplace_id: str = "EBAY_US") -> dict:
    """Retrieve information about one or more monetary transactions."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    if sort_by:
        params["sort_by"] = sort_by
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/finances/v1/transaction", params=params, extra_headers=headers)


def get_transaction_summary(filter: str, marketplace_id: str = "EBAY_US") -> dict:
    """Retrieve cumulative information for monetary transactions."""
    client = get_client()
    params = {"filter": filter}
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/finances/v1/transaction_summary", params=params, extra_headers=headers)


def get_payouts(filter: Optional[str] = None, limit: Optional[str] = None,
                offset: Optional[str] = None, sort_by: Optional[str] = None,
                marketplace_id: str = "EBAY_US") -> dict:
    """Retrieve details of one or more seller payouts."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    if sort_by:
        params["sort_by"] = sort_by
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/finances/v1/payout", params=params, extra_headers=headers)


def get_payout(payout_id: str, marketplace_id: str = "EBAY_US") -> dict:
    """Retrieve details on a specific seller payout by ID."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", f"/sell/finances/v1/payout/{payout_id}", extra_headers=headers)


def get_payout_summary(filter: Optional[str] = None, marketplace_id: str = "EBAY_US") -> dict:
    """Retrieve cumulative values for payouts in a particular state or all states."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/finances/v1/payout_summary", params=params, extra_headers=headers)


def get_seller_funds_summary(marketplace_id: str = "EBAY_US") -> dict:
    """Retrieve all pending funds that have not yet been distributed through a seller payout."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/finances/v1/seller_funds_summary", extra_headers=headers)


def get_transfer(transfer_id: str, marketplace_id: str = "EBAY_US") -> dict:
    """Retrieve detailed information regarding a TRANSFER transaction type."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", f"/sell/finances/v1/transfer/{transfer_id}", extra_headers=headers)


def get_billing_activities(filter: str, limit: Optional[str] = None,
                           offset: Optional[str] = None, sort_by: Optional[str] = None) -> dict:
    """Retrieve filtered billing activities of the seller."""
    client = get_client()
    params = {"filter": filter}
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    if sort_by:
        params["sort_by"] = sort_by
    return client.request("GET", "/sell/finances/v1/billing_activity", params=params)
