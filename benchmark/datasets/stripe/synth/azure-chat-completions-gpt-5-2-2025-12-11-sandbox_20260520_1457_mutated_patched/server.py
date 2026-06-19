from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools import (
    account_links,
    accounts,
    charges,
    checkout_sessions,
    coupons,
    customers,
    invoices,
    payment_intents,
    payment_links,
    payouts,
    prices,
    promotion_codes,
    refunds,
    setup_intents,
    subscriptions,
    transfers,
)

mcp = FastMCP("stripe")


# Payment Intents
@mcp.tool()
def stripe_create_payment_intent(
    amount: int,
    currency: str,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    setup_future_usage: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return payment_intents.create_payment_intent(
        amount,
        currency,
        confirm=confirm,
        customer=customer,
        payment_method=payment_method,
        receipt_email=receipt_email,
        description=description,
        metadata=metadata,
        automatic_payment_methods=automatic_payment_methods,
        setup_future_usage=setup_future_usage,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_payment_intent(
    payment_intent_id: str,
    client_secret: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return payment_intents.retrieve_payment_intent(
        payment_intent_id, client_secret=client_secret, stripe_account=stripe_account
    )


@mcp.tool()
def stripe_update_payment_intent(
    payment_intent_id: str,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    setup_future_usage: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return payment_intents.update_payment_intent(
        payment_intent_id,
        amount=amount,
        currency=currency,
        customer=customer,
        payment_method=payment_method,
        receipt_email=receipt_email,
        description=description,
        metadata=metadata,
        automatic_payment_methods=automatic_payment_methods,
        setup_future_usage=setup_future_usage,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_confirm_payment_intent(
    payment_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    off_session: Optional[Any] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return payment_intents.confirm_payment_intent(
        payment_intent_id,
        payment_method=payment_method,
        return_url=return_url,
        off_session=off_session,
        receipt_email=receipt_email,
        setup_future_usage=setup_future_usage,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_capture_payment_intent(
    payment_intent_id: str,
    amount_to_capture: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return payment_intents.capture_payment_intent(
        payment_intent_id,
        amount_to_capture=amount_to_capture,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_cancel_payment_intent(
    payment_intent_id: str,
    cancellation_reason: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return payment_intents.cancel_payment_intent(
        payment_intent_id,
        cancellation_reason=cancellation_reason,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_list_payment_intents(
    customer: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return payment_intents.list_payment_intents(
        customer=customer,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        created=created,
        stripe_account=stripe_account,
    )


# Charges
@mcp.tool()
def stripe_retrieve_charge(charge_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return charges.retrieve_charge(charge_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_charge(
    charge_id: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return charges.update_charge(
        charge_id,
        customer=customer,
        description=description,
        metadata=metadata,
        receipt_email=receipt_email,
        shipping=shipping,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_list_charges(
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return charges.list_charges(
        customer=customer,
        payment_intent=payment_intent,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        created=created,
        stripe_account=stripe_account,
    )


# Refunds
@mcp.tool()
def stripe_create_refund(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return refunds.create_refund(
        charge=charge,
        payment_intent=payment_intent,
        amount=amount,
        reason=reason,
        metadata=metadata,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_refund(refund_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return refunds.retrieve_refund(refund_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_refund(
    refund_id: str,
    metadata: Dict[str, Any],
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return refunds.update_refund(refund_id, metadata=metadata, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_refunds(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return refunds.list_refunds(
        charge=charge,
        payment_intent=payment_intent,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        created=created,
        stripe_account=stripe_account,
    )


# Customers
@mcp.tool()
def stripe_create_customer(
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_method: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return customers.create_customer(
        email=email,
        name=name,
        phone=phone,
        description=description,
        address=address,
        shipping=shipping,
        metadata=metadata,
        payment_method=payment_method,
        invoice_settings=invoice_settings,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_customer(customer_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return customers.retrieve_customer(customer_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_customer(
    customer_id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    default_source: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return customers.update_customer(
        customer_id,
        email=email,
        name=name,
        phone=phone,
        description=description,
        address=address,
        shipping=shipping,
        metadata=metadata,
        default_source=default_source,
        invoice_settings=invoice_settings,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_delete_customer(customer_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return customers.delete_customer(customer_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_customers(
    email: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return customers.list_customers(
        email=email,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        created=created,
        stripe_account=stripe_account,
    )


# Products
@mcp.tool()
def stripe_create_product(
    name: str,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    product_id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_code: Optional[str] = None,
    default_price_data: Optional[Dict[str, Any]] = None,
    images: Optional[list[str]] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    from generated_tools import products

    return products.create_product(
        name,
        active=active,
        description=description,
        product_id=product_id,
        metadata=metadata,
        tax_code=tax_code,
        default_price_data=default_price_data,
        images=images,
        url=url,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_product(product_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    from generated_tools import products

    return products.retrieve_product(product_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_product(
    product_id: str,
    name: Optional[str] = None,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    default_price: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_code: Optional[str] = None,
    images: Optional[list[str]] = None,
    url: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    from generated_tools import products

    return products.update_product(
        product_id,
        name=name,
        active=active,
        description=description,
        default_price=default_price,
        metadata=metadata,
        tax_code=tax_code,
        images=images,
        url=url,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_delete_product(product_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    from generated_tools import products

    return products.delete_product(product_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_products(
    active: Optional[bool] = None,
    ids: Optional[list[str]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    from generated_tools import products

    return products.list_products(
        active=active,
        ids=ids,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        stripe_account=stripe_account,
    )


# Prices
@mcp.tool()
def stripe_create_price(
    currency: str,
    product: Optional[str] = None,
    unit_amount: Optional[int] = None,
    unit_amount_decimal: Optional[str] = None,
    recurring: Optional[Dict[str, Any]] = None,
    product_data: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_behavior: Optional[str] = None,
    lookup_key: Optional[str] = None,
    billing_scheme: Optional[str] = None,
    tiers: Optional[list[Dict[str, Any]]] = None,
    tiers_mode: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return prices.create_price(
        currency,
        product=product,
        unit_amount=unit_amount,
        unit_amount_decimal=unit_amount_decimal,
        recurring=recurring,
        product_data=product_data,
        active=active,
        nickname=nickname,
        metadata=metadata,
        tax_behavior=tax_behavior,
        lookup_key=lookup_key,
        billing_scheme=billing_scheme,
        tiers=tiers,
        tiers_mode=tiers_mode,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_price(price_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return prices.retrieve_price(price_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_price(
    price_id: str,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    tax_behavior: Optional[str] = None,
    lookup_key: Optional[str] = None,
    transfer_lookup_key: Optional[bool] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return prices.update_price(
        price_id,
        active=active,
        nickname=nickname,
        metadata=metadata,
        tax_behavior=tax_behavior,
        lookup_key=lookup_key,
        transfer_lookup_key=transfer_lookup_key,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_list_prices(
    active: Optional[bool] = None,
    product: Optional[str] = None,
    lookup_keys: Optional[list[str]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return prices.list_prices(
        active=active,
        product=product,
        lookup_keys=lookup_keys,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        stripe_account=stripe_account,
    )


# Subscriptions
@mcp.tool()
def stripe_create_subscription(
    customer: str,
    items: list[Dict[str, Any]],
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    payment_behavior: Optional[str] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    trial_end: Optional[Any] = None,
    trial_period_days: Optional[int] = None,
    cancel_at_period_end: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return subscriptions.create_subscription(
        customer,
        items,
        default_payment_method=default_payment_method,
        description=description,
        metadata=metadata,
        payment_behavior=payment_behavior,
        collection_method=collection_method,
        days_until_due=days_until_due,
        trial_end=trial_end,
        trial_period_days=trial_period_days,
        cancel_at_period_end=cancel_at_period_end,
        automatic_tax=automatic_tax,
        coupon=coupon,
        promotion_code=promotion_code,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_subscription(subscription_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return subscriptions.retrieve_subscription(subscription_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_subscription(
    subscription_id: str,
    items: Optional[list[Dict[str, Any]]] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    cancel_at_period_end: Optional[bool] = None,
    proration_behavior: Optional[str] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return subscriptions.update_subscription(
        subscription_id,
        items=items,
        default_payment_method=default_payment_method,
        description=description,
        metadata=metadata,
        cancel_at_period_end=cancel_at_period_end,
        proration_behavior=proration_behavior,
        coupon=coupon,
        promotion_code=promotion_code,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_cancel_subscription(
    subscription_id: str,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return subscriptions.cancel_subscription(
        subscription_id,
        invoice_now=invoice_now,
        prorate=prorate,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_list_subscriptions(
    customer: Optional[str] = None,
    price: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return subscriptions.list_subscriptions(
        customer=customer,
        price=price,
        status=status,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        stripe_account=stripe_account,
    )


# Invoices
@mcp.tool()
def stripe_create_invoice(
    customer: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    subscription: Optional[str] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return invoices.create_invoice(
        customer,
        auto_advance=auto_advance,
        collection_method=collection_method,
        days_until_due=days_until_due,
        description=description,
        metadata=metadata,
        subscription=subscription,
        discounts=discounts,
        automatic_tax=automatic_tax,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_invoice(invoice_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return invoices.retrieve_invoice(invoice_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_invoice(
    invoice_id: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return invoices.update_invoice(
        invoice_id,
        auto_advance=auto_advance,
        collection_method=collection_method,
        days_until_due=days_until_due,
        description=description,
        metadata=metadata,
        discounts=discounts,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_finalize_invoice(
    invoice_id: str,
    auto_advance: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return invoices.finalize_invoice(
        invoice_id,
        auto_advance=auto_advance,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_pay_invoice(
    invoice_id: str,
    payment_method: Optional[str] = None,
    source: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return invoices.pay_invoice(
        invoice_id,
        payment_method=payment_method,
        source=source,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_void_invoice(
    invoice_id: str,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return invoices.void_invoice(
        invoice_id,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_list_invoices(
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return invoices.list_invoices(
        customer=customer,
        subscription=subscription,
        status=status,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_create_preview_invoice(
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    subscription_details: Optional[Dict[str, Any]] = None,
    invoice_items: Optional[list[Dict[str, Any]]] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return invoices.create_preview_invoice(
        customer=customer,
        subscription=subscription,
        subscription_details=subscription_details,
        invoice_items=invoice_items,
        discounts=discounts,
        automatic_tax=automatic_tax,
        stripe_account=stripe_account,
    )


# Checkout Sessions
@mcp.tool()
def stripe_create_checkout_session(
    mode: str,
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    return_url: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    client_reference_id: Optional[str] = None,
    line_items: Optional[list[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    ui_mode: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return checkout_sessions.create_checkout_session(
        mode,
        success_url=success_url,
        cancel_url=cancel_url,
        return_url=return_url,
        customer=customer,
        customer_email=customer_email,
        client_reference_id=client_reference_id,
        line_items=line_items,
        metadata=metadata,
        allow_promotion_codes=allow_promotion_codes,
        discounts=discounts,
        subscription_data=subscription_data,
        payment_intent_data=payment_intent_data,
        invoice_creation=invoice_creation,
        automatic_tax=automatic_tax,
        ui_mode=ui_mode,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_checkout_session(
    session_id: str,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return checkout_sessions.retrieve_checkout_session(
        session_id, expand=expand, stripe_account=stripe_account
    )


@mcp.tool()
def stripe_expire_checkout_session(
    session_id: str,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return checkout_sessions.expire_checkout_session(
        session_id, stripe_account=stripe_account, idempotency_key=idempotency_key
    )


@mcp.tool()
def stripe_list_checkout_sessions(
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return checkout_sessions.list_checkout_sessions(
        customer=customer,
        payment_intent=payment_intent,
        subscription=subscription,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        stripe_account=stripe_account,
    )


# Payment Links
@mcp.tool()
def stripe_create_payment_link(
    line_items: list[Dict[str, Any]],
    metadata: Optional[Dict[str, Any]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    currency: Optional[str] = None,
    customer_creation: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return payment_links.create_payment_link(
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
        subscription_data=subscription_data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_payment_link(
    payment_link_id: str,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return payment_links.retrieve_payment_link(payment_link_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_payment_link(
    payment_link_id: str,
    active: Optional[bool] = None,
    line_items: Optional[list[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    customer_creation: Optional[str] = None,
    invoice_creation: Optional[Dict[str, Any]] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return payment_links.update_payment_link(
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
        subscription_data=subscription_data,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_list_payment_links(
    active: Optional[bool] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return payment_links.list_payment_links(
        active=active,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_list_payment_link_line_items(
    payment_link_id: str,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return payment_links.list_payment_link_line_items(
        payment_link_id,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        stripe_account=stripe_account,
    )


# Setup Intents
@mcp.tool()
def stripe_create_setup_intent(
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    payment_method_types: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return setup_intents.create_setup_intent(
        customer=customer,
        payment_method=payment_method,
        usage=usage,
        description=description,
        metadata=metadata,
        confirm=confirm,
        return_url=return_url,
        automatic_payment_methods=automatic_payment_methods,
        payment_method_types=payment_method_types,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_setup_intent(
    setup_intent_id: str,
    client_secret: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return setup_intents.retrieve_setup_intent(
        setup_intent_id, client_secret=client_secret, stripe_account=stripe_account
    )


@mcp.tool()
def stripe_update_setup_intent(
    setup_intent_id: str,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return setup_intents.update_setup_intent(
        setup_intent_id,
        customer=customer,
        payment_method=payment_method,
        description=description,
        metadata=metadata,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_confirm_setup_intent(
    setup_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    use_stripe_sdk: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return setup_intents.confirm_setup_intent(
        setup_intent_id,
        payment_method=payment_method,
        return_url=return_url,
        use_stripe_sdk=use_stripe_sdk,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_cancel_setup_intent(
    setup_intent_id: str,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return setup_intents.cancel_setup_intent(setup_intent_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_setup_intents(
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return setup_intents.list_setup_intents(
        customer=customer,
        payment_method=payment_method,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        stripe_account=stripe_account,
    )


# Coupons
@mcp.tool()
def stripe_create_coupon(
    duration: str,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    duration_in_months: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    redeem_by: Optional[int] = None,
    coupon_id: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return coupons.create_coupon(
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
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_coupon(coupon_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return coupons.retrieve_coupon(coupon_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_coupon(
    coupon_id: str,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return coupons.update_coupon(coupon_id, name=name, metadata=metadata, stripe_account=stripe_account)


@mcp.tool()
def stripe_delete_coupon(coupon_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return coupons.delete_coupon(coupon_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_coupons(
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return coupons.list_coupons(
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        stripe_account=stripe_account,
    )


# Promotion Codes
@mcp.tool()
def stripe_create_promotion_code(
    promotion: Dict[str, Any],
    code: Optional[str] = None,
    active: Optional[bool] = None,
    customer: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return promotion_codes.create_promotion_code(
        promotion,
        code=code,
        active=active,
        customer=customer,
        expires_at=expires_at,
        max_redemptions=max_redemptions,
        restrictions=restrictions,
        metadata=metadata,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_promotion_code(
    promotion_code_id: str,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return promotion_codes.retrieve_promotion_code(
        promotion_code_id, stripe_account=stripe_account
    )


@mcp.tool()
def stripe_update_promotion_code(
    promotion_code_id: str,
    active: Optional[bool] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return promotion_codes.update_promotion_code(
        promotion_code_id,
        active=active,
        restrictions=restrictions,
        metadata=metadata,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_list_promotion_codes(
    code: Optional[str] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    active: Optional[bool] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return promotion_codes.list_promotion_codes(
        code=code,
        coupon=coupon,
        customer=customer,
        active=active,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        stripe_account=stripe_account,
    )


# Transfers
@mcp.tool()
def stripe_create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    source_transaction: Optional[str] = None,
    transfer_group: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return transfers.create_transfer(
        amount,
        currency,
        destination,
        description=description,
        metadata=metadata,
        source_transaction=source_transaction,
        transfer_group=transfer_group,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_transfer(transfer_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return transfers.retrieve_transfer(transfer_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_transfer(
    transfer_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return transfers.update_transfer(
        transfer_id,
        description=description,
        metadata=metadata,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_list_transfers(
    destination: Optional[str] = None,
    transfer_group: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return transfers.list_transfers(
        destination=destination,
        transfer_group=transfer_group,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        created=created,
        stripe_account=stripe_account,
    )


# Payouts
@mcp.tool()
def stripe_create_payout(
    amount: int,
    currency: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    destination: Optional[str] = None,
    method: Optional[str] = None,
    source_type: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return payouts.create_payout(
        amount,
        currency,
        description=description,
        metadata=metadata,
        statement_descriptor=statement_descriptor,
        destination=destination,
        method=method,
        source_type=source_type,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_payout(payout_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return payouts.retrieve_payout(payout_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_payout(
    payout_id: str,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return payouts.update_payout(payout_id, metadata=metadata, stripe_account=stripe_account)


@mcp.tool()
def stripe_cancel_payout(
    payout_id: str,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return payouts.cancel_payout(payout_id, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_reverse_payout(
    payout_id: str,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return payouts.reverse_payout(payout_id, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_list_payouts(
    status: Optional[str] = None,
    destination: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return payouts.list_payouts(
        status=status,
        destination=destination,
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        created=created,
        stripe_account=stripe_account,
    )


# Accounts + Account Links
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
    metadata: Optional[Dict[str, Any]] = None,
    external_account: Optional[str] = None,
    default_currency: Optional[str] = None,
    settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return accounts.create_account(
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
        default_currency=default_currency,
        settings=settings,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_retrieve_account(account_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return accounts.retrieve_account(account_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_account(
    account_id: str,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    controller: Optional[Dict[str, Any]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    settings: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return accounts.update_account(
        account_id,
        business_type=business_type,
        capabilities=capabilities,
        company=company,
        individual=individual,
        controller=controller,
        tos_acceptance=tos_acceptance,
        metadata=metadata,
        settings=settings,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_delete_account(account_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return accounts.delete_account(account_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_accounts(
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return accounts.list_accounts(
        limit=limit,
        starting_after=starting_after,
        ending_before=ending_before,
        stripe_account=stripe_account,
    )


@mcp.tool()
def stripe_create_account_link(
    account: str,
    type: str,
    refresh_url: str,
    return_url: str,
    collection_options: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return account_links.create_account_link(
        account,
        type,
        refresh_url,
        return_url,
        collection_options=collection_options,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


if __name__ == "__main__":
    mcp.run()
