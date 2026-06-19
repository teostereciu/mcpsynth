from typing import Any, Dict

from generated_tools.common import stripe_request


def create_customer(**kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/customers", data=kwargs)


def update_customer(customer: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/customers/{customer}", data=kwargs)


def retrieve_customer(customer: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/customers/{customer}", query=query)
