from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    source_transaction: Optional[str] = None,
    transfer_group: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
        "description": description,
        "metadata": metadata,
        "source_transaction": source_transaction,
        "transfer_group": transfer_group,
    }
    _, data = stripe_request(
        "POST",
        "/v1/transfers",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return data


def retrieve_transfer(
    transfer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    _, data = stripe_request(
        "GET",
        f"/v1/transfers/{transfer_id}",
        stripe_account=stripe_account,
    )
    return data


def update_transfer(
    transfer_id: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"description": description, "metadata": metadata}
    _, data = stripe_request(
        "POST",
        f"/v1/transfers/{transfer_id}",
        params=params,
        stripe_account=stripe_account,
    )
    return data


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
    params: Dict[str, Any] = {
        "destination": destination,
        "transfer_group": transfer_group,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
        "created": created,
    }
    _, data = stripe_request(
        "GET",
        "/v1/transfers",
        params=params,
        stripe_account=stripe_account,
    )
    return data
