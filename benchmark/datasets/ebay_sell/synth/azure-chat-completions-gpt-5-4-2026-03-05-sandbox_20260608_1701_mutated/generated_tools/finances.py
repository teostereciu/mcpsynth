from typing import Any, Optional

from generated_tools.common import client, compact_kwargs


API_BASE = "/sell/finances/v1"


def get_transactions(marketplace_id: str, filter: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, sort_by: Optional[str] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", "/transaction", params=compact_kwargs(filter=filter, limit=limit, offset=offset, sort_by=sort_by), headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id})
    except Exception as e:
        return {"error": str(e)}


def get_transaction_summary(marketplace_id: str, filter: Optional[str] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", "/transaction_summary", params=compact_kwargs(filter=filter), headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id})
    except Exception as e:
        return {"error": str(e)}


def get_payouts(filter: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", "/payout", params=compact_kwargs(filter=filter, limit=limit, offset=offset))
    except Exception as e:
        return {"error": str(e)}


def get_payout(payout_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/payout/{payout_id}")
    except Exception as e:
        return {"error": str(e)}


def get_payout_summary() -> Any:
    try:
        return client.request(API_BASE, "GET", "/payout_summary")
    except Exception as e:
        return {"error": str(e)}


def get_transfer(transfer_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/transfer/{transfer_id}")
    except Exception as e:
        return {"error": str(e)}


def get_seller_funds_summary() -> Any:
    try:
        return client.request(API_BASE, "GET", "/seller_funds_summary")
    except Exception as e:
        return {"error": str(e)}


def get_billing_activities(filter: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", "/billing_activity", params=compact_kwargs(filter=filter, limit=limit, offset=offset))
    except Exception as e:
        return {"error": str(e)}
