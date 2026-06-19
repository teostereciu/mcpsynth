from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payment_method(
    type: str,
    *,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    allow_redisplay: Optional[str] = None,
    card: Optional[Dict[str, Any]] = None,
    us_bank_account: Optional[Dict[str, Any]] = None,
    sepa_debit: Optional[Dict[str, Any]] = None,
    bacs_debit: Optional[Dict[str, Any]] = None,
    au_becs_debit: Optional[Dict[str, Any]] = None,
    link: Optional[Dict[str, Any]] = None,
    paypal: Optional[Dict[str, Any]] = None,
    cashapp: Optional[Dict[str, Any]] = None,
    ideal: Optional[Dict[str, Any]] = None,
    klarna: Optional[Dict[str, Any]] = None,
    affirm: Optional[Dict[str, Any]] = None,
    afterpay_clearpay: Optional[Dict[str, Any]] = None,
    alipay: Optional[Dict[str, Any]] = None,
    wechat_pay: Optional[Dict[str, Any]] = None,
    revolut_pay: Optional[Dict[str, Any]] = None,
    bancontact: Optional[Dict[str, Any]] = None,
    eps: Optional[Dict[str, Any]] = None,
    giropay: Optional[Dict[str, Any]] = None,
    p24: Optional[Dict[str, Any]] = None,
    sofort: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_methods

    Doc: docs/payment_methods.md (Create a PaymentMethod)
    """
    params: Dict[str, Any] = {
        "type": type,
        "billing_details": billing_details,
        "metadata": metadata,
        "allow_redisplay": allow_redisplay,
        "card": card,
        "us_bank_account": us_bank_account,
        "sepa_debit": sepa_debit,
        "bacs_debit": bacs_debit,
        "au_becs_debit": au_becs_debit,
        "link": link,
        "paypal": paypal,
        "cashapp": cashapp,
        "ideal": ideal,
        "klarna": klarna,
        "affirm": affirm,
        "afterpay_clearpay": afterpay_clearpay,
        "alipay": alipay,
        "wechat_pay": wechat_pay,
        "revolut_pay": revolut_pay,
        "bancontact": bancontact,
        "eps": eps,
        "giropay": giropay,
        "p24": p24,
        "sofort": sofort,
    }
    return stripe_request(
        "POST",
        "/v1/payment_methods",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payment_method(
    payment_method_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payment_methods/{payment_method_id}

    Doc: docs/payment_methods.md (Retrieve a PaymentMethod)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/payment_methods/{payment_method_id}",
        params,
        stripe_account=stripe_account,
    )


def update_payment_method(
    payment_method_id: str,
    *,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    allow_redisplay: Optional[str] = None,
    card: Optional[Dict[str, Any]] = None,
    payto: Optional[Dict[str, Any]] = None,
    us_bank_account: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_methods/{payment_method_id}

    Doc: docs/payment_methods.md (Update a PaymentMethod)
    """
    params: Dict[str, Any] = {
        "billing_details": billing_details,
        "metadata": metadata,
        "allow_redisplay": allow_redisplay,
        "card": card,
        "payto": payto,
        "us_bank_account": us_bank_account,
    }
    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}",
        params,
        stripe_account=stripe_account,
    )


def attach_payment_method(
    payment_method_id: str,
    customer: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_methods/{payment_method_id}/attach

    Doc: docs/payment_methods.md (Attach a PaymentMethod to a Customer)
    """
    params: Dict[str, Any] = {"customer": customer}
    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}/attach",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def detach_payment_method(
    payment_method_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_methods/{payment_method_id}/detach

    Doc: docs/payment_methods.md (Detach a PaymentMethod from a Customer)
    """
    return stripe_request(
        "POST",
        f"/v1/payment_methods/{payment_method_id}/detach",
        None,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payment_methods(
    customer: str,
    *,
    type: str = "card",
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/customers/{customer}/payment_methods

    Doc: docs/payment_methods.md (List a Customer's PaymentMethods)
    """
    params: Dict[str, Any] = {
        "type": type,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
    }
    return stripe_request(
        "GET",
        f"/v1/customers/{customer}/payment_methods",
        params,
        stripe_account=stripe_account,
    )


def retrieve_customer_payment_method(
    customer: str,
    payment_method_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/customers/{customer}/payment_methods/{payment_method_id}

    Doc: docs/payment_methods.md (Retrieve a Customer's PaymentMethod)
    """
    return stripe_request(
        "GET",
        f"/v1/customers/{customer}/payment_methods/{payment_method_id}",
        None,
        stripe_account=stripe_account,
    )
