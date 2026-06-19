from typing import Any, Dict, Optional

from generated_tools.stripe_common import stripe_request


def create_account(type: str = "express", country: Optional[str] = None, email: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", "/v1/accounts", {"type": type, "country": country, "email": email, "metadata": metadata})


def retrieve_account(account_id: str) -> Any:
    return stripe_request("GET", f"/v1/accounts/{account_id}")


def update_account(account_id: str, email: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", f"/v1/accounts/{account_id}", {"email": email, "metadata": metadata})


def list_accounts(limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/accounts", {"limit": limit})


def create_transfer(amount: int, currency: str, destination: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", "/v1/transfers", {"amount": amount, "currency": currency, "destination": destination, "description": description, "metadata": metadata})


def retrieve_transfer(transfer_id: str) -> Any:
    return stripe_request("GET", f"/v1/transfers/{transfer_id}")


def list_transfers(destination: Optional[str] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/transfers", {"destination": destination, "limit": limit})


def create_payout(amount: int, currency: str, method: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", "/v1/payouts", {"amount": amount, "currency": currency, "method": method, "description": description, "metadata": metadata})


def retrieve_payout(payout_id: str) -> Any:
    return stripe_request("GET", f"/v1/payouts/{payout_id}")


def list_payouts(status: Optional[str] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/payouts", {"status": status, "limit": limit})
