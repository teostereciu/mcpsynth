from typing import Any, Dict

from generated_tools.common import stripe_request


def create_product(name: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/products", data={"name": name, **kwargs})


def update_product(product: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/products/{product}", data=kwargs)


def retrieve_product(product: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/products/{product}", query=query)


def create_price(currency: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/prices", data={"currency": currency, **kwargs})


def update_price(price: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/prices/{price}", data=kwargs)


def retrieve_price(price: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/prices/{price}", query=query)
