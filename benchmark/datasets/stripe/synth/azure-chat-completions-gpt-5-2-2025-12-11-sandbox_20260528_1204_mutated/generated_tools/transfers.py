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
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/transfers

    Doc: docs/transfers.md (Create a transfer)
    """
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
        "description": description,
        "metadata": metadata,
        "source_transaction": source_transaction,
        "source_type": source_type,
        "transfer_group": transfer_group,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        "/v1/transfers",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_transfer(
    transfer_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/transfers/{transfer_id}

    Doc: docs/transfers.md (Retrieve a transfer)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/transfers/{transfer_id}",
        params,
        stripe_account=stripe_account,
    )


def update_transfer(
    transfer_id: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/transfers/{transfer_id}

    Doc: docs/transfers.md (Update a transfer)
    """
    params: Dict[str, Any] = {"description": description, "metadata": metadata}
    return stripe_request(
        "POST",
        f"/v1/transfers/{transfer_id}",
        params,
        stripe_account=stripe_account,
    )


def list_transfers(
    *,
    destination: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    transfer_group: Optional[str] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/transfers

    Doc: docs/transfers.md (List all transfers)
    """
    params: Dict[str, Any] = {
        "destination": destination,
        "created": created,
        "transfer_group": transfer_group,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request(
        "GET",
        "/v1/transfers",
        params,
        stripe_account=stripe_account,
    )
