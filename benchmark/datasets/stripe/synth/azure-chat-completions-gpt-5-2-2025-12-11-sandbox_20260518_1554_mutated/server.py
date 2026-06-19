import json
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.accounts import (
    create_account,
    delete_account,
    list_accounts,
    retrieve_account,
    update_account,
)
from generated_tools.charges import create_charge, list_charges, retrieve_charge, update_charge
from generated_tools.checkout_sessions import (
    create_checkout_session,
    expire_checkout_session,
    list_checkout_sessions,
    retrieve_checkout_session,
)
from generated_tools.coupons import (
    create_coupon,
    delete_coupon,
    list_coupons,
    retrieve_coupon,
    update_coupon,
)
from generated_tools.customers import (
    create_customer,
    delete_customer,
    list_customers,
    retrieve_customer,
    update_customer,
)
from generated_tools.invoices import (
    create_invoice,
    create_preview_invoice,
    delete_draft_invoice,
    finalize_invoice,
    list_invoices,
    pay_invoice,
    retrieve_invoice,
    update_invoice,
    void_invoice,
)
from generated_tools.payment_intents import (
    cancel_payment_intent,
    capture_payment_intent,
    confirm_payment_intent,
    create_payment_intent,
    list_payment_intents,
    retrieve_payment_intent,
    update_payment_intent,
)
from generated_tools.payment_links import (
    create_payment_link,
    list_payment_links,
    retrieve_payment_link,
    retrieve_payment_link_line_items,
    update_payment_link,
)
from generated_tools.payouts import (
    cancel_payout,
    create_payout,
    list_payouts,
    retrieve_payout,
    reverse_payout,
    update_payout,
)
from generated_tools.prices import create_price, list_prices, retrieve_price, update_price
from generated_tools.promotion_codes import (
    create_promotion_code,
    list_promotion_codes,
    retrieve_promotion_code,
    update_promotion_code,
)
from generated_tools.products import (
    create_product,
    delete_product,
    list_products,
    retrieve_product,
    update_product,
)
from generated_tools.refunds import create_refund, list_refunds, retrieve_refund, update_refund
from generated_tools.setup_intents import (
    cancel_setup_intent,
    confirm_setup_intent,
    create_setup_intent,
    list_setup_intents,
    retrieve_setup_intent,
    update_setup_intent,
)
from generated_tools.subscriptions import (
    cancel_subscription,
    create_subscription,
    list_subscriptions,
    retrieve_subscription,
    update_subscription,
)
from generated_tools.transfers import create_transfer, list_transfers, retrieve_transfer, update_transfer


mcp = FastMCP("stripe")


def _jsonable(x: Any) -> Any:
    try:
        json.dumps(x)
        return x
    except TypeError:
        return json.loads(json.dumps(x, default=str))


@mcp.tool()
def stripe_create_payment_intent(
    amount: int,
    currency: str,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    off_session: Optional[Any] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_payment_intent(
            amount,
            currency,
            confirm=confirm,
            customer=customer,
            description=description,
            payment_method=payment_method,
            receipt_email=receipt_email,
            setup_future_usage=setup_future_usage,
            automatic_payment_methods=automatic_payment_methods,
            metadata=metadata,
            shipping=shipping,
            statement_descriptor=statement_descriptor,
            statement_descriptor_suffix=statement_descriptor_suffix,
            off_session=off_session,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_payment_intent(payment_intent_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_payment_intent(payment_intent_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_payment_intent(
    payment_intent_id: str,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        update_payment_intent(
            payment_intent_id,
            amount=amount,
            currency=currency,
            customer=customer,
            description=description,
            metadata=metadata,
            payment_method=payment_method,
            receipt_email=receipt_email,
            shipping=shipping,
            statement_descriptor=statement_descriptor,
            statement_descriptor_suffix=statement_descriptor_suffix,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_confirm_payment_intent(
    payment_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    off_session: Optional[Any] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        confirm_payment_intent(
            payment_intent_id,
            payment_method=payment_method,
            return_url=return_url,
            off_session=off_session,
            receipt_email=receipt_email,
            setup_future_usage=setup_future_usage,
            metadata=metadata,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_capture_payment_intent(payment_intent_id: str, amount_to_capture: Optional[int] = None, metadata: Optional[Dict[str, str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(capture_payment_intent(payment_intent_id, amount_to_capture=amount_to_capture, metadata=metadata, stripe_account=stripe_account))


@mcp.tool()
def stripe_cancel_payment_intent(payment_intent_id: str, cancellation_reason: Optional[str] = None, stripe_account: Optional[str] = None):
    return _jsonable(cancel_payment_intent(payment_intent_id, cancellation_reason=cancellation_reason, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_payment_intents(
    customer: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        list_payment_intents(
            customer=customer,
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            created=created,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_create_refund(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_refund(
            charge=charge,
            payment_intent=payment_intent,
            amount=amount,
            reason=reason,
            metadata=metadata,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_refund(refund_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_refund(refund_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_refund(refund_id: str, metadata: Optional[Dict[str, str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(update_refund(refund_id, metadata=metadata, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_refunds(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        list_refunds(
            charge=charge,
            payment_intent=payment_intent,
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_create_customer(
    name: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_customer(
            name=name,
            email=email,
            phone=phone,
            description=description,
            address=address,
            shipping=shipping,
            metadata=metadata,
            payment_method=payment_method,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_customer(customer_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_customer(customer_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_customer(
    customer_id: str,
    name: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        update_customer(
            customer_id,
            name=name,
            email=email,
            phone=phone,
            description=description,
            address=address,
            shipping=shipping,
            metadata=metadata,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_delete_customer(customer_id: str, stripe_account: Optional[str] = None):
    return _jsonable(delete_customer(customer_id, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_customers(
    email: Optional[str] = None,
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        list_customers(
            email=email,
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
            created=created,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_create_product(
    name: str,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    product_id: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_code: Optional[str] = None,
    default_price_data: Optional[Dict[str, Any]] = None,
    images: Optional[list[str]] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_product(
            name,
            active=active,
            description=description,
            product_id=product_id,
            metadata=metadata,
            tax_code=tax_code,
            default_price_data=default_price_data,
            images=images,
            statement_descriptor=statement_descriptor,
            unit_label=unit_label,
            url=url,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_product(product_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_product(product_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_product(
    product_id: str,
    name: Optional[str] = None,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    default_price: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_code: Optional[str] = None,
    images: Optional[list[str]] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        update_product(
            product_id,
            name=name,
            active=active,
            description=description,
            default_price=default_price,
            metadata=metadata,
            tax_code=tax_code,
            images=images,
            statement_descriptor=statement_descriptor,
            unit_label=unit_label,
            url=url,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_delete_product(product_id: str, stripe_account: Optional[str] = None):
    return _jsonable(delete_product(product_id, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_products(active: Optional[bool] = None, limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, stripe_account: Optional[str] = None):
    return _jsonable(list_products(active=active, limit=limit, starting_after=starting_after, ending_before=ending_before, stripe_account=stripe_account))


@mcp.tool()
def stripe_create_price(
    currency: str,
    unit_amount: Optional[int] = None,
    product: Optional[str] = None,
    product_data: Optional[Dict[str, Any]] = None,
    recurring: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_behavior: Optional[str] = None,
    billing_scheme: Optional[str] = None,
    lookup_key: Optional[str] = None,
    unit_amount_decimal: Optional[str] = None,
    custom_unit_amount: Optional[Dict[str, Any]] = None,
    tiers: Optional[list[Dict[str, Any]]] = None,
    tiers_mode: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_price(
            currency,
            unit_amount=unit_amount,
            product=product,
            product_data=product_data,
            recurring=recurring,
            active=active,
            nickname=nickname,
            metadata=metadata,
            tax_behavior=tax_behavior,
            billing_scheme=billing_scheme,
            lookup_key=lookup_key,
            unit_amount_decimal=unit_amount_decimal,
            custom_unit_amount=custom_unit_amount,
            tiers=tiers,
            tiers_mode=tiers_mode,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_price(price_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_price(price_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_price(price_id: str, active: Optional[bool] = None, nickname: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, tax_behavior: Optional[str] = None, lookup_key: Optional[str] = None, stripe_account: Optional[str] = None):
    return _jsonable(update_price(price_id, active=active, nickname=nickname, metadata=metadata, tax_behavior=tax_behavior, lookup_key=lookup_key, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_prices(product: Optional[str] = None, active: Optional[bool] = None, currency: Optional[str] = None, limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, stripe_account: Optional[str] = None):
    return _jsonable(list_prices(product=product, active=active, currency=currency, limit=limit, starting_after=starting_after, ending_before=ending_before, stripe_account=stripe_account))


@mcp.tool()
def stripe_create_subscription(
    customer: str,
    items: list[Dict[str, Any]],
    currency: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_behavior: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    trial_end: Optional[Any] = None,
    trial_period_days: Optional[int] = None,
    cancel_at_period_end: Optional[bool] = None,
    cancel_at: Optional[Any] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    off_session: Optional[bool] = None,
    proration_behavior: Optional[str] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_subscription(
            customer,
            items,
            currency=currency,
            default_payment_method=default_payment_method,
            description=description,
            metadata=metadata,
            payment_behavior=payment_behavior,
            collection_method=collection_method,
            days_until_due=days_until_due,
            trial_end=trial_end,
            trial_period_days=trial_period_days,
            cancel_at_period_end=cancel_at_period_end,
            cancel_at=cancel_at,
            automatic_tax=automatic_tax,
            discounts=discounts,
            off_session=off_session,
            proration_behavior=proration_behavior,
            payment_settings=payment_settings,
            invoice_settings=invoice_settings,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_subscription(subscription_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_subscription(subscription_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_subscription(
    subscription_id: str,
    items: Optional[list[Dict[str, Any]]] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    cancel_at_period_end: Optional[bool] = None,
    cancel_at: Optional[Any] = None,
    proration_behavior: Optional[str] = None,
    payment_behavior: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    trial_end: Optional[Any] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    pause_collection: Optional[Dict[str, Any]] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        update_subscription(
            subscription_id,
            items=items,
            default_payment_method=default_payment_method,
            description=description,
            metadata=metadata,
            cancel_at_period_end=cancel_at_period_end,
            cancel_at=cancel_at,
            proration_behavior=proration_behavior,
            payment_behavior=payment_behavior,
            collection_method=collection_method,
            days_until_due=days_until_due,
            trial_end=trial_end,
            automatic_tax=automatic_tax,
            discounts=discounts,
            pause_collection=pause_collection,
            payment_settings=payment_settings,
            invoice_settings=invoice_settings,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_cancel_subscription(subscription_id: str, invoice_now: Optional[bool] = None, prorate: Optional[bool] = None, stripe_account: Optional[str] = None):
    return _jsonable(cancel_subscription(subscription_id, invoice_now=invoice_now, prorate=prorate, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_subscriptions(customer: Optional[str] = None, price: Optional[str] = None, status: Optional[str] = None, limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, stripe_account: Optional[str] = None):
    return _jsonable(list_subscriptions(customer=customer, price=price, status=status, limit=limit, starting_after=starting_after, ending_before=ending_before, stripe_account=stripe_account))


@mcp.tool()
def stripe_create_invoice(
    customer: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    footer: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_invoice(
            customer,
            description=description,
            metadata=metadata,
            auto_advance=auto_advance,
            collection_method=collection_method,
            days_until_due=days_until_due,
            default_payment_method=default_payment_method,
            discounts=discounts,
            automatic_tax=automatic_tax,
            statement_descriptor=statement_descriptor,
            footer=footer,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_invoice(invoice_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_invoice(invoice_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_invoice(
    invoice_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    footer: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        update_invoice(
            invoice_id,
            description=description,
            metadata=metadata,
            auto_advance=auto_advance,
            collection_method=collection_method,
            days_until_due=days_until_due,
            default_payment_method=default_payment_method,
            discounts=discounts,
            automatic_tax=automatic_tax,
            footer=footer,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_finalize_invoice(invoice_id: str, auto_advance: Optional[bool] = None, stripe_account: Optional[str] = None):
    return _jsonable(finalize_invoice(invoice_id, auto_advance=auto_advance, stripe_account=stripe_account))


@mcp.tool()
def stripe_pay_invoice(invoice_id: str, payment_method: Optional[str] = None, paid_out_of_band: Optional[bool] = None, stripe_account: Optional[str] = None):
    return _jsonable(pay_invoice(invoice_id, payment_method=payment_method, paid_out_of_band=paid_out_of_band, stripe_account=stripe_account))


@mcp.tool()
def stripe_void_invoice(invoice_id: str, stripe_account: Optional[str] = None):
    return _jsonable(void_invoice(invoice_id, stripe_account=stripe_account))


@mcp.tool()
def stripe_delete_draft_invoice(invoice_id: str, stripe_account: Optional[str] = None):
    return _jsonable(delete_draft_invoice(invoice_id, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_invoices(customer: Optional[str] = None, subscription: Optional[str] = None, status: Optional[str] = None, limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, stripe_account: Optional[str] = None):
    return _jsonable(list_invoices(customer=customer, subscription=subscription, status=status, limit=limit, starting_after=starting_after, ending_before=ending_before, stripe_account=stripe_account))


@mcp.tool()
def stripe_create_preview_invoice(
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    currency: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    invoice_items: Optional[list[Dict[str, Any]]] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    schedule: Optional[str] = None,
    schedule_details: Optional[Dict[str, Any]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_preview_invoice(
            customer=customer,
            subscription=subscription,
            currency=currency,
            discounts=discounts,
            invoice_items=invoice_items,
            subscription_details=subscription_details,
            schedule=schedule,
            schedule_details=schedule_details,
            automatic_tax=automatic_tax,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_create_checkout_session(
    mode: str,
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    return_url: Optional[str] = None,
    ui_mode: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    line_items: Optional[list[Dict[str, Any]]] = None,
    currency: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    allow_promotion_codes: Optional[bool] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    payment_method_collection: Optional[str] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[list[Dict[str, Any]]] = None,
    expires_at: Optional[int] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_checkout_session(
            mode,
            success_url=success_url,
            cancel_url=cancel_url,
            return_url=return_url,
            ui_mode=ui_mode,
            customer=customer,
            customer_email=customer_email,
            client_reference_id=client_reference_id,
            line_items=line_items,
            currency=currency,
            metadata=metadata,
            allow_promotion_codes=allow_promotion_codes,
            discounts=discounts,
            automatic_tax=automatic_tax,
            invoice_creation=invoice_creation,
            payment_intent_data=payment_intent_data,
            subscription_data=subscription_data,
            payment_method_types=payment_method_types,
            payment_method_collection=payment_method_collection,
            shipping_address_collection=shipping_address_collection,
            shipping_options=shipping_options,
            expires_at=expires_at,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_checkout_session(session_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_checkout_session(session_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_expire_checkout_session(session_id: str, stripe_account: Optional[str] = None):
    return _jsonable(expire_checkout_session(session_id, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_checkout_sessions(customer: Optional[str] = None, payment_intent: Optional[str] = None, subscription: Optional[str] = None, limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, stripe_account: Optional[str] = None):
    return _jsonable(list_checkout_sessions(customer=customer, payment_intent=payment_intent, subscription=subscription, limit=limit, starting_after=starting_after, ending_before=ending_before, stripe_account=stripe_account))


@mcp.tool()
def stripe_create_payment_link(
    line_items: list[Dict[str, Any]],
    metadata: Optional[Dict[str, str]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    currency: Optional[str] = None,
    customer_creation: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    payment_method_collection: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    phone_number_collection: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    shipping_options: Optional[list[Dict[str, Any]]] = None,
    submit_type: Optional[str] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_payment_link(
            line_items,
            metadata=metadata,
            after_completion=after_completion,
            allow_promotion_codes=allow_promotion_codes,
            automatic_tax=automatic_tax,
            billing_address_collection=billing_address_collection,
            currency=currency,
            customer_creation=customer_creation,
            invoice_creation=invoice_creation,
            payment_intent_data=payment_intent_data,
            payment_method_collection=payment_method_collection,
            payment_method_types=payment_method_types,
            phone_number_collection=phone_number_collection,
            shipping_address_collection=shipping_address_collection,
            shipping_options=shipping_options,
            submit_type=submit_type,
            subscription_data=subscription_data,
            tax_id_collection=tax_id_collection,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_payment_link(payment_link_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_payment_link(payment_link_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_payment_link(
    payment_link_id: str,
    active: Optional[bool] = None,
    line_items: Optional[list[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, str]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    customer_creation: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    payment_method_collection: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    phone_number_collection: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    submit_type: Optional[str] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    tax_id_collection: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        update_payment_link(
            payment_link_id,
            active=active,
            line_items=line_items,
            metadata=metadata,
            after_completion=after_completion,
            allow_promotion_codes=allow_promotion_codes,
            automatic_tax=automatic_tax,
            billing_address_collection=billing_address_collection,
            customer_creation=customer_creation,
            invoice_creation=invoice_creation,
            payment_intent_data=payment_intent_data,
            payment_method_collection=payment_method_collection,
            payment_method_types=payment_method_types,
            phone_number_collection=phone_number_collection,
            shipping_address_collection=shipping_address_collection,
            submit_type=submit_type,
            subscription_data=subscription_data,
            tax_id_collection=tax_id_collection,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_list_payment_links(active: Optional[bool] = None, limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, stripe_account: Optional[str] = None):
    return _jsonable(list_payment_links(active=active, limit=limit, starting_after=starting_after, ending_before=ending_before, stripe_account=stripe_account))


@mcp.tool()
def stripe_retrieve_payment_link_line_items(payment_link_id: str, limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_payment_link_line_items(payment_link_id, limit=limit, starting_after=starting_after, ending_before=ending_before, stripe_account=stripe_account))


@mcp.tool()
def stripe_create_coupon(
    duration: str,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    duration_in_months: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    redeem_by: Optional[int] = None,
    coupon_id: Optional[str] = None,
    applies_to: Optional[Dict[str, Any]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_coupon(
            duration,
            percent_off=percent_off,
            amount_off=amount_off,
            currency=currency,
            name=name,
            metadata=metadata,
            duration_in_months=duration_in_months,
            max_redemptions=max_redemptions,
            redeem_by=redeem_by,
            coupon_id=coupon_id,
            applies_to=applies_to,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_coupon(coupon_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_coupon(coupon_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_coupon(coupon_id: str, name: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(update_coupon(coupon_id, name=name, metadata=metadata, stripe_account=stripe_account))


@mcp.tool()
def stripe_delete_coupon(coupon_id: str, stripe_account: Optional[str] = None):
    return _jsonable(delete_coupon(coupon_id, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_coupons(limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, stripe_account: Optional[str] = None):
    return _jsonable(list_coupons(limit=limit, starting_after=starting_after, ending_before=ending_before, stripe_account=stripe_account))


@mcp.tool()
def stripe_create_promotion_code(
    promotion: Dict[str, Any],
    code: Optional[str] = None,
    active: Optional[bool] = None,
    customer: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_promotion_code(
            promotion,
            code=code,
            active=active,
            customer=customer,
            expires_at=expires_at,
            max_redemptions=max_redemptions,
            restrictions=restrictions,
            metadata=metadata,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_promotion_code(promotion_code_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_promotion_code(promotion_code_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_promotion_code(promotion_code_id: str, active: Optional[bool] = None, restrictions: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(update_promotion_code(promotion_code_id, active=active, restrictions=restrictions, metadata=metadata, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_promotion_codes(code: Optional[str] = None, coupon: Optional[str] = None, customer: Optional[str] = None, active: Optional[bool] = None, limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, stripe_account: Optional[str] = None):
    return _jsonable(list_promotion_codes(code=code, coupon=coupon, customer=customer, active=active, limit=limit, starting_after=starting_after, ending_before=ending_before, stripe_account=stripe_account))


@mcp.tool()
def stripe_create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    source_transaction: Optional[str] = None,
    source_type: Optional[str] = None,
    transfer_group: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_transfer(
            amount,
            currency,
            destination,
            description=description,
            metadata=metadata,
            source_transaction=source_transaction,
            source_type=source_type,
            transfer_group=transfer_group,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_transfer(transfer_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_transfer(transfer_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_transfer(transfer_id: str, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(update_transfer(transfer_id, description=description, metadata=metadata, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_transfers(destination: Optional[str] = None, transfer_group: Optional[str] = None, limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None):
    return _jsonable(list_transfers(destination=destination, transfer_group=transfer_group, limit=limit, starting_after=starting_after, ending_before=ending_before, created=created, stripe_account=stripe_account))


@mcp.tool()
def stripe_create_payout(
    amount: int,
    currency: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
    destination: Optional[str] = None,
    method: Optional[str] = None,
    source_type: Optional[str] = None,
    payout_method: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_payout(
            amount,
            currency,
            description=description,
            metadata=metadata,
            statement_descriptor=statement_descriptor,
            destination=destination,
            method=method,
            source_type=source_type,
            payout_method=payout_method,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_payout(payout_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_payout(payout_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_payout(payout_id: str, metadata: Optional[Dict[str, str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(update_payout(payout_id, metadata=metadata, stripe_account=stripe_account))


@mcp.tool()
def stripe_cancel_payout(payout_id: str, stripe_account: Optional[str] = None):
    return _jsonable(cancel_payout(payout_id, stripe_account=stripe_account))


@mcp.tool()
def stripe_reverse_payout(payout_id: str, metadata: Optional[Dict[str, str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(reverse_payout(payout_id, metadata=metadata, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_payouts(status: Optional[str] = None, destination: Optional[str] = None, limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None):
    return _jsonable(list_payouts(status=status, destination=destination, limit=limit, starting_after=starting_after, ending_before=ending_before, created=created, stripe_account=stripe_account))


@mcp.tool()
def stripe_create_setup_intent(
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    mandate_data: Optional[Dict[str, Any]] = None,
    use_stripe_sdk: Optional[bool] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_setup_intent(
            customer=customer,
            description=description,
            metadata=metadata,
            payment_method=payment_method,
            usage=usage,
            confirm=confirm,
            return_url=return_url,
            automatic_payment_methods=automatic_payment_methods,
            payment_method_types=payment_method_types,
            payment_method_options=payment_method_options,
            mandate_data=mandate_data,
            use_stripe_sdk=use_stripe_sdk,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_setup_intent(setup_intent_id: str, client_secret: Optional[str] = None, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_setup_intent(setup_intent_id, client_secret=client_secret, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_setup_intent(
    setup_intent_id: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    payment_method_options: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        update_setup_intent(
            setup_intent_id,
            customer=customer,
            description=description,
            metadata=metadata,
            payment_method=payment_method,
            payment_method_types=payment_method_types,
            payment_method_options=payment_method_options,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_confirm_setup_intent(setup_intent_id: str, payment_method: Optional[str] = None, return_url: Optional[str] = None, use_stripe_sdk: Optional[bool] = None, mandate_data: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None):
    return _jsonable(confirm_setup_intent(setup_intent_id, payment_method=payment_method, return_url=return_url, use_stripe_sdk=use_stripe_sdk, mandate_data=mandate_data, stripe_account=stripe_account))


@mcp.tool()
def stripe_cancel_setup_intent(setup_intent_id: str, cancellation_reason: Optional[str] = None, stripe_account: Optional[str] = None):
    return _jsonable(cancel_setup_intent(setup_intent_id, cancellation_reason=cancellation_reason, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_setup_intents(customer: Optional[str] = None, payment_method: Optional[str] = None, limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None):
    return _jsonable(list_setup_intents(customer=customer, payment_method=payment_method, limit=limit, starting_after=starting_after, ending_before=ending_before, created=created, stripe_account=stripe_account))


@mcp.tool()
def stripe_create_charge(
    amount: int,
    currency: str,
    source: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    stripe_account: Optional[str] = None,
):
    return _jsonable(
        create_charge(
            amount,
            currency,
            source=source,
            customer=customer,
            description=description,
            metadata=metadata,
            receipt_email=receipt_email,
            shipping=shipping,
            statement_descriptor=statement_descriptor,
            statement_descriptor_suffix=statement_descriptor_suffix,
            idempotency_key=idempotency_key,
            stripe_account=stripe_account,
        )
    )


@mcp.tool()
def stripe_retrieve_charge(charge_id: str, expand: Optional[list[str]] = None, stripe_account: Optional[str] = None):
    return _jsonable(retrieve_charge(charge_id, expand=expand, stripe_account=stripe_account))


@mcp.tool()
def stripe_update_charge(charge_id: str, customer: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, receipt_email: Optional[str] = None, shipping: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None):
    return _jsonable(update_charge(charge_id, customer=customer, description=description, metadata=metadata, receipt_email=receipt_email, shipping=shipping, stripe_account=stripe_account))


@mcp.tool()
def stripe_list_charges(customer: Optional[str] = None, payment_intent: Optional[str] = None, limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None, created: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None):
    return _jsonable(list_charges(customer=customer, payment_intent=payment_intent, limit=limit, starting_after=starting_after, ending_before=ending_before, created=created, stripe_account=stripe_account))


@mcp.tool()
def stripe_create_account(
    type: Optional[str] = None,
    country: Optional[str] = None,
    email: Optional[str] = None,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    controller: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    external_account: Optional[str] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    account_token: Optional[str] = None,
    default_currency: Optional[str] = None,
    idempotency_key: Optional[str] = None,
):
    return _jsonable(
        create_account(
            type=type,
            country=country,
            email=email,
            business_type=business_type,
            capabilities=capabilities,
            company=company,
            individual=individual,
            controller=controller,
            tos_acceptance=tos_acceptance,
            metadata=metadata,
            external_account=external_account,
            business_profile=business_profile,
            settings=settings,
            account_token=account_token,
            default_currency=default_currency,
            idempotency_key=idempotency_key,
        )
    )


@mcp.tool()
def stripe_retrieve_account(account_id: str, expand: Optional[list[str]] = None):
    return _jsonable(retrieve_account(account_id, expand=expand))


@mcp.tool()
def stripe_update_account(
    account_id: str,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    business_profile: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
):
    return _jsonable(
        update_account(
            account_id,
            business_type=business_type,
            capabilities=capabilities,
            company=company,
            individual=individual,
            tos_acceptance=tos_acceptance,
            metadata=metadata,
            business_profile=business_profile,
            settings=settings,
        )
    )


@mcp.tool()
def stripe_delete_account(account_id: str):
    return _jsonable(delete_account(account_id))


@mcp.tool()
def stripe_list_accounts(limit: Optional[int] = 10, starting_after: Optional[str] = None, ending_before: Optional[str] = None):
    return _jsonable(list_accounts(limit=limit, starting_after=starting_after, ending_before=ending_before))


if __name__ == "__main__":
    mcp.run()
