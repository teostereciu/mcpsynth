from typing import Any, Dict, Optional

from .http import stripe_request


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
        "source_type": source_type,
        "transfer_group": transfer_group,
    }
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
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"description": description, "metadata": metadata}
    return stripe_request(
        "POST",
        f"/v1/transfers/{transfer_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_transfer(
    transfer_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "GET",
        f"/v1/transfers/{transfer_id}",
        params=None,
        stripe_account=stripe_account,
    )
