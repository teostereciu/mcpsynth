from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    source_transaction: Optional[str] = None,
    source_type: Optional[str] = None,
    transfer_group: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
        "description": description,
        "metadata": metadata,
        "source_transaction": source_transaction,
        "source_type": source_type,
        "transfer_group": transfer_group,
    }
    return stripe_request(
        "POST",
        "/v1/transfers",
        params=params,
        idempotency_key=idempotency_key,
        stripe_account=stripe_account,
    )


def retrieve_transfer(
    transfer_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return stripe_request(
        "GET",
        f"/v1/transfers/{transfer_id}",
        params=params or None,
        stripe_account=stripe_account,
    )


def update_transfer(
    transfer_id: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"description": description, "metadata": metadata}
    return stripe_request(
        "POST",
        f"/v1/transfers/{transfer_id}",
        params=params,
        stripe_account=stripe_account,
    )


def list_transfers(
    *,
    destination: Optional[str] = None,
    transfer_group: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "destination": destination,
        "transfer_group": transfer_group,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    return stripe_request(
        "GET",
        "/v1/transfers",
        params=params,
        stripe_account=stripe_account,
    )
