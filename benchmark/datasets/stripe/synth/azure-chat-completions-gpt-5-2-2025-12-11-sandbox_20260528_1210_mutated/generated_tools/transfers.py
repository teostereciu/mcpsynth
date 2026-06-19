from typing import Any, Dict, Optional

from .http_client import stripe_request_with_retries


def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
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
    }
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if source_transaction is not None:
        params["source_transaction"] = source_transaction
    if source_type is not None:
        params["source_type"] = source_type
    if transfer_group is not None:
        params["transfer_group"] = transfer_group

    return stripe_request_with_retries(
        "POST",
        "/v1/transfers",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_transfer(transfer_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request_with_retries(
        "GET",
        f"/v1/transfers/{transfer_id}",
        stripe_account=stripe_account,
    )


def update_transfer(
    transfer_id: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request_with_retries(
        "POST",
        f"/v1/transfers/{transfer_id}",
        params=params,
        stripe_account=stripe_account,
    )


def list_transfers(
    *,
    destination: Optional[str] = None,
    transfer_group: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if destination is not None:
        params["destination"] = destination
    if transfer_group is not None:
        params["transfer_group"] = transfer_group
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if created is not None:
        params["created"] = created

    return stripe_request_with_retries(
        "GET",
        "/v1/transfers",
        params=params,
        stripe_account=stripe_account,
    )
