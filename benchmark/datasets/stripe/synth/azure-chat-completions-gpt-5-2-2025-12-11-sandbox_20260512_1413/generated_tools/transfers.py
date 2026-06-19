from typing import Any, Dict, Optional

from .stripe_client import stripe_list_all, stripe_request


def transfers_create(
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
    return stripe_request("POST", "/v1/transfers", params, stripe_account=stripe_account, idempotency_key=idempotency_key)


def transfers_retrieve(transfer_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/transfers/{transfer_id}", None, stripe_account=stripe_account)


def transfers_update(
    transfer_id: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"description": description, "metadata": metadata}
    return stripe_request("POST", f"/v1/transfers/{transfer_id}", params, stripe_account=stripe_account)


def transfers_list(
    *,
    destination: Optional[str] = None,
    transfer_group: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "destination": destination,
        "transfer_group": transfer_group,
        "created": created,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/transfers", params, stripe_account=stripe_account)


def transfers_list_all(
    *,
    destination: Optional[str] = None,
    transfer_group: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    limit: int = 100,
    max_pages: int = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"destination": destination, "transfer_group": transfer_group, "created": created}
    return stripe_list_all("/v1/transfers", params, stripe_account=stripe_account, limit=limit, max_pages=max_pages)
