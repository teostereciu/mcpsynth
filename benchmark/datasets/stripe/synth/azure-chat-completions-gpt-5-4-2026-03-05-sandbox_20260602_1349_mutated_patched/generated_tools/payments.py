from typing import Any, Dict, Optional

from generated_tools.common import stripe_request


def create_payment_intent(amount: int, currency: str, **kwargs: Any) -> Dict[str, Any]:
    data = {"amount": amount, "currency": currency, **kwargs}
    return stripe_request("POST", "/v1/payment_intents", data=data)


def update_payment_intent(payment_intent: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent}", data=kwargs)


def retrieve_payment_intent(payment_intent: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_intents/{payment_intent}", query=query)


def create_charge(amount: int, currency: str, source: Optional[str] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"amount": amount, "currency": currency, **kwargs}
    if source is not None:
        data["source"] = source
    return stripe_request("POST", "/v1/charges", data=data)


def update_charge(charge: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/charges/{charge}", data=kwargs)


def retrieve_charge(charge: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/charges/{charge}", query=query)


def create_refund(**kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/refunds", data=kwargs)


def update_refund(refund: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/refunds/{refund}", data=kwargs)


def retrieve_refund(refund: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/refunds/{refund}", query=query)


def create_payout(amount: int, currency: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/payouts", data={"amount": amount, "currency": currency, **kwargs})


def update_payout(payout: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/payouts/{payout}", data=kwargs)


def retrieve_payout(payout: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payouts/{payout}", query=query)


def create_setup_intent(**kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/setup_intents", data=kwargs)


def update_setup_intent(setup_intent: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/setup_intents/{setup_intent}", data=kwargs)


def retrieve_setup_intent(setup_intent: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/setup_intents/{setup_intent}", query=query)
