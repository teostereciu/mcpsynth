from typing import Any, Dict

from generated_tools.common import stripe_request


def create_checkout_session(mode: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/checkout/sessions", data={"mode": mode, **kwargs})


def update_checkout_session(session: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/checkout/sessions/{session}", data=kwargs)


def retrieve_checkout_session(session: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/checkout/sessions/{session}", query=query)


def create_payment_link(line_items: list[dict], **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/payment_links", data={"line_items": line_items, **kwargs})


def update_payment_link(payment_link: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/payment_links/{payment_link}", data=kwargs)


def list_payment_link_line_items(payment_link: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_links/{payment_link}/line_items", query=query)
