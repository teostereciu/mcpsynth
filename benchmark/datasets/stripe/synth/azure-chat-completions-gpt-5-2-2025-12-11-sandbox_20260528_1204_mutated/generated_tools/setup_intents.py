from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_setup_intent(
    *,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    payment_method: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    usage: Optional[str] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    confirmation_token: Optional[str] = None,
    mandate_data: Optional[Dict[str, Any]] = None,
    use_stripe_sdk: Optional[bool] = None,
    attach_to_self: Optional[bool] = None,
    excluded_payment_method_types: Optional[list[str]] = None,
    flow_directions: Optional[list[str]] = None,
    on_behalf_of: Optional[str] = None,
    payment_method_configuration: Optional[str] = None,
    payment_method_data: Optional[Dict[str, Any]] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    single_use: Optional[Dict[str, Any]] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents

    Doc: docs/setup_intents.md (Create a SetupIntent)
    """
    params: Dict[str, Any] = {
        "customer": customer,
        "customer_account": customer_account,
        "payment_method": payment_method,
        "payment_method_types": payment_method_types,
        "automatic_payment_methods": automatic_payment_methods,
        "description": description,
        "metadata": metadata,
        "usage": usage,
        "confirm": confirm,
        "return_url": return_url,
        "confirmation_token": confirmation_token,
        "mandate_data": mandate_data,
        "use_stripe_sdk": use_stripe_sdk,
        "attach_to_self": attach_to_self,
        "excluded_payment_method_types": excluded_payment_method_types,
        "flow_directions": flow_directions,
        "on_behalf_of": on_behalf_of,
        "payment_method_configuration": payment_method_configuration,
        "payment_method_data": payment_method_data,
        "payment_method_options": payment_method_options,
        "single_use": single_use,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        "/v1/setup_intents",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_setup_intent(
    setup_intent_id: str,
    *,
    client_secret: Optional[str] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/setup_intents/{setup_intent_id}

    Doc: docs/setup_intents.md (Retrieve a SetupIntent)
    """
    params: Dict[str, Any] = {"client_secret": client_secret, "expand": expand}
    return stripe_request(
        "GET",
        f"/v1/setup_intents/{setup_intent_id}",
        params,
        stripe_account=stripe_account,
    )


def update_setup_intent(
    setup_intent_id: str,
    *,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    attach_to_self: Optional[bool] = None,
    excluded_payment_method_types: Optional[list[str]] = None,
    flow_directions: Optional[list[str]] = None,
    payment_method_configuration: Optional[str] = None,
    payment_method_data: Optional[Dict[str, Any]] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents/{setup_intent_id}

    Doc: docs/setup_intents.md (Update a SetupIntent)
    """
    params: Dict[str, Any] = {
        "customer": customer,
        "customer_account": customer_account,
        "payment_method": payment_method,
        "description": description,
        "metadata": metadata,
        "attach_to_self": attach_to_self,
        "excluded_payment_method_types": excluded_payment_method_types,
        "flow_directions": flow_directions,
        "payment_method_configuration": payment_method_configuration,
        "payment_method_data": payment_method_data,
        "payment_method_options": payment_method_options,
        "payment_method_types": payment_method_types,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}",
        params,
        stripe_account=stripe_account,
    )


def confirm_setup_intent(
    setup_intent_id: str,
    *,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    mandate_data: Optional[Dict[str, Any]] = None,
    use_stripe_sdk: Optional[bool] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents/{setup_intent_id}/confirm

    Doc: docs/setup_intents.md (Confirm a SetupIntent)
    """
    params: Dict[str, Any] = {
        "payment_method": payment_method,
        "return_url": return_url,
        "mandate_data": mandate_data,
        "use_stripe_sdk": use_stripe_sdk,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/confirm",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_setup_intent(
    setup_intent_id: str,
    *,
    cancellation_reason: Optional[str] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/setup_intents/{setup_intent_id}/cancel

    Doc: docs/setup_intents.md (Cancel a SetupIntent)
    """
    params: Dict[str, Any] = {"cancellation_reason": cancellation_reason, "expand": expand}
    return stripe_request(
        "POST",
        f"/v1/setup_intents/{setup_intent_id}/cancel",
        params,
        stripe_account=stripe_account,
    )


def list_setup_intents(
    *,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/setup_intents

    Doc: docs/setup_intents.md (List all SetupIntents)
    """
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_method": payment_method,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request(
        "GET",
        "/v1/setup_intents",
        params,
        stripe_account=stripe_account,
    )
