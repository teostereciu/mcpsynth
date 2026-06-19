from typing import Any, Dict

from generated_tools.common import stripe_request


def create_account(**kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/accounts", data=kwargs)


def update_account(account: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/accounts/{account}", data=kwargs)


def retrieve_account(account: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/accounts/{account}", query=query)


def create_transfer(amount: int, currency: str, destination: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/transfers", data={"amount": amount, "currency": currency, "destination": destination, **kwargs})


def update_transfer(transfer: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/transfers/{transfer}", data=kwargs)


def retrieve_transfer(transfer: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/transfers/{transfer}", query=query)
