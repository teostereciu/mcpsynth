from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_transfer(
    *,
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    source_transaction: Optional[str] = None,
    source_type: Optional[str] = None,
    transfer_group: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"amount": amount, "currency": currency, "destination": destination}
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
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        "/v1/transfers",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_transfer(
    transfer_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    description: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if metadata is not None:
        params["metadata"] = metadata
    if description is not None:
        params["description"] = description
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/transfers/{transfer_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_transfer(transfer_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/transfers/{transfer_id}", stripe_account=stripe_account)


def list_transfers(
    *,
    destination: Optional[str] = None,
    transfer_group: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if destination is not None:
        params["destination"] = destination
    if transfer_group is not None:
        params["transfer_group"] = transfer_group
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if extra_params:
        params.update(extra_params)

    return stripe_request("GET", "/v1/transfers", params=params, stripe_account=stripe_account)
