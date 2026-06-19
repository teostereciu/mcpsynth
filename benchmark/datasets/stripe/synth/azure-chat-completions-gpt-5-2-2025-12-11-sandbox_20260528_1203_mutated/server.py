from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.charges import create_charge, retrieve_charge, update_charge
from generated_tools.payment_intents import (
    create_payment_intent,
    retrieve_payment_intent,
    update_payment_intent,
)

mcp = FastMCP("stripe")


@mcp.tool()
def stripe_create_payment_intent(
    amount: int,
    currency: str,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_payment_intent(
        amount,
        currency,
        confirm=confirm,
        customer=customer,
        payment_method=payment_method,
        description=description,
        receipt_email=receipt_email,
        setup_future_usage=setup_future_usage,
        automatic_payment_methods=automatic_payment_methods,
        metadata=metadata,
        shipping=shipping,
        statement_descriptor=statement_descriptor,
        statement_descriptor_suffix=statement_descriptor_suffix,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_payment_intent(
    payment_intent_id: str,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return retrieve_payment_intent(payment_intent_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_payment_intent(
    payment_intent_id: str,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return update_payment_intent(
        payment_intent_id,
        amount=amount,
        currency=currency,
        customer=customer,
        payment_method=payment_method,
        description=description,
        receipt_email=receipt_email,
        setup_future_usage=setup_future_usage,
        automatic_payment_methods=automatic_payment_methods,
        metadata=metadata,
        shipping=shipping,
        statement_descriptor=statement_descriptor,
        statement_descriptor_suffix=statement_descriptor_suffix,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_create_charge(
    amount: int,
    currency: str,
    source: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    capture: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_charge(
        amount,
        currency,
        source=source,
        customer=customer,
        description=description,
        receipt_email=receipt_email,
        metadata=metadata,
        shipping=shipping,
        statement_descriptor=statement_descriptor,
        statement_descriptor_suffix=statement_descriptor_suffix,
        capture=capture,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_charge(
    charge_id: str,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return retrieve_charge(charge_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_charge(
    charge_id: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    fraud_details: Optional[Dict[str, Any]] = None,
    transfer_group: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return update_charge(
        charge_id,
        customer=customer,
        description=description,
        receipt_email=receipt_email,
        metadata=metadata,
        shipping=shipping,
        fraud_details=fraud_details,
        transfer_group=transfer_group,
        stripe_account=stripe_account,
    )


if __name__ == "__main__":
    mcp.run()
