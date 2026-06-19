from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    *,
    description: Optional[str] = None,
    transfer_group: Optional[str] = None,
    source_transaction: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
        "description": description,
        "transfer_group": transfer_group,
        "source_transaction": source_transaction,
        "metadata": metadata,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        "/v1/transfers",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_transfer(
    transfer_id: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/transfers/{transfer_id}",
        {"description": description, "metadata": metadata},
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
        None,
        stripe_account=stripe_account,
    )
