from typing import Any, Dict, Optional

from .http import stripe_request


# Accounts (Connect)

def create_account(type: str = "express", country: Optional[str] = None, email: Optional[str] = None, capabilities: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"type": type}
    if country:
        data["country"] = country
    if email:
        data["email"] = email
    if capabilities is not None:
        data["capabilities"] = capabilities
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/accounts", data=data)
    return err or res  # type: ignore


def get_account(account_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/accounts/{account_id}")
    return err or res  # type: ignore


def update_account(account_id: str, **kwargs: Any) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/accounts/{account_id}", data=kwargs)
    return err or res  # type: ignore


def list_accounts(limit: int = 10, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/accounts", params=params)
    return err or res  # type: ignore


# Transfers

def create_transfer(amount: int, currency: str, destination: str, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"amount": amount, "currency": currency, "destination": destination}
    if description:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/transfers", data=data)
    return err or res  # type: ignore


def get_transfer(transfer_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/transfers/{transfer_id}")
    return err or res  # type: ignore


def list_transfers(limit: int = 10, destination: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if destination:
        params["destination"] = destination
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/transfers", params=params)
    return err or res  # type: ignore


# Payouts

def create_payout(amount: int, currency: str = "usd", description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"amount": amount, "currency": currency}
    if description:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/payouts", data=data)
    return err or res  # type: ignore


def get_payout(payout_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/payouts/{payout_id}")
    return err or res  # type: ignore


def cancel_payout(payout_id: str) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/payouts/{payout_id}/cancel")
    return err or res  # type: ignore


def list_payouts(limit: int = 10, status: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if status:
        params["status"] = status
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/payouts", params=params)
    return err or res  # type: ignore
