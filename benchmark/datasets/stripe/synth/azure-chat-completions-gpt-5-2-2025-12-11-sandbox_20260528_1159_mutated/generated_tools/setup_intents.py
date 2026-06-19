from typing import Any, Dict, Optional

from .http import stripe_request


def create_setup_intent(
    *,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    attach_to_self: Optional[bool] = None,
    confirmation_token: Optional[str] = None,
    excluded_payment_method_types: Optional[list[str]] = None,
    flow_directions: Optional[list[str]] = None,
    mandate_data: Optional[Dict[str, Any]] = None,
    on_behalf_of: Optional[str] = None,
    payment_method_configuration: Optional[str] = None,
    payment_method_data: Optional[Dict[str, Any]] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    return_url: Optional[str] = None,
    single_use: Optional[Dict[str, Any]] = None,
    use_stripe_sdk: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "automatic_payment_methods": automatic_payment_methods,
        "confirm": confirm,
        "customer": customer,
        "customer_account": customer_account,
        "description": description,
        "metadata": metadata,
        "payment_method": payment_method,
        "usage": usage,
        "attach_to_self": attach_to_self,
        "confirmation_token": confirmation_token,
        "excluded_payment_method_types": excluded_payment_method_types,
        "flow_directions": flow_directions,
        "mandate_data": mandate_data,
        "on_behalf_of": on_behalf_of,
        "payment_method_configuration": payment_method_configuration,
        "payment_method_data": payment_method_data,
        "payment_method_options": payment_method_options,
        "payment_method_types": payment_method_types,
        "return_url": return_url,
        "single_use": single_use,
        "use_stripe_sdk": use_stripe_sdk,
    }
    return stripe_request(
        "POST",
        "/v1/setup_intents",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_setup_intent(
    setup_intent_id: str,
    *,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    attach_to_self: Optional[bool] = None,
    excluded_payment_method_types: Optional[list[str]] = None,
    flow_directions: Optional[list[str]] = None,
    payment_method_configuration: Optional[str] = None,
    payment_method_data: Optional[Dict[str, Any]] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "customer_account": customer_account,
        "description": description,
        "metadata": metadata,
        "payment_method": payment_method,
        "attach_to_self": attach_to_self,
        "excluded_payment_method_types": excluded_payment_method_types,
        "flow_directions": flow_directions,
        "payment_method_configuration": payment_method_configuration,
        "payment_method_data": payment_method_data,
        "payment_method_options": payment_method_options,
        "payment_method_types": payment_method_types,
    }
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_setup_intent(
    setup_intent_id: str,
    *,
    client_secret: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params = {"client_secret": client_secret} if client_secret else None
    return stripe_request(
        "GET",
        f"/v1/setup_intents/{setup_intent_id}",
        params=params,
        stripe_account=stripe_account,
    )
