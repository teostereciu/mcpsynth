from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/transfers"""
    body: Dict[str, Any] = {"amount": amount, "currency": currency, "destination": destination}
    if params:
        body.update(params)
    return stripe_request("POST", "/v1/transfers", body, idempotency_key=idempotency_key)


def retrieve_transfer(
    transfer_id: str,
) -> Dict[str, Any]:
    """GET /v1/transfers/{id}"""
    return stripe_request("GET", f"/v1/transfers/{transfer_id}", None)


def update_transfer(
    transfer_id: str,
    *,
    params: Dict[str, Any],
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/transfers/{id}"""
    return stripe_request("POST", f"/v1/transfers/{transfer_id}", params, idempotency_key=idempotency_key)


def list_transfers(
    *,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """GET /v1/transfers"""
    return stripe_request("GET", "/v1/transfers", params)
