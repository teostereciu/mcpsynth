from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def accounts_create(**kwargs) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/accounts", kwargs)


def accounts_retrieve(account_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/accounts/{account_id}", kwargs or None)


def accounts_update(account_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/accounts/{account_id}", kwargs)


def accounts_delete(account_id: str) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/accounts/{account_id}")


def accounts_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/accounts", params)


def transfers_create(amount: int, currency: str, destination: str, **kwargs) -> Dict[str, Any]:
    params = {"amount": amount, "currency": currency, "destination": destination}
    params.update(kwargs)
    return stripe_request("POST", "/v1/transfers", params)


def transfers_retrieve(transfer_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/transfers/{transfer_id}", kwargs or None)


def transfers_update(transfer_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/transfers/{transfer_id}", kwargs)


def transfers_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/transfers", params)


def payouts_create(amount: int, currency: str, **kwargs) -> Dict[str, Any]:
    params = {"amount": amount, "currency": currency}
    params.update(kwargs)
    return stripe_request("POST", "/v1/payouts", params)


def payouts_retrieve(payout_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payouts/{payout_id}", kwargs or None)


def payouts_update(payout_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/payouts/{payout_id}", kwargs)


def payouts_cancel(payout_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/payouts/{payout_id}/cancel", kwargs)


def payouts_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/payouts", params)
