from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.payment_intents import (
    cancel_payment_intent,
    capture_payment_intent,
    confirm_payment_intent,
    create_payment_intent,
    list_payment_intents,
    retrieve_payment_intent,
    update_payment_intent,
)
from generated_tools.charges import create_charge, list_charges, retrieve_charge, update_charge
from generated_tools.refunds import create_refund, list_refunds, retrieve_refund, update_refund
from generated_tools.customers import (
    create_customer,
    delete_customer,
    list_customers,
    retrieve_customer,
    search_customers,
    update_customer,
)
from generated_tools.products import (
    create_product,
    delete_product,
    list_products,
    retrieve_product,
    search_products,
    update_product,
)
from generated_tools.prices import create_price, list_prices, retrieve_price, search_prices, update_price
from generated_tools.subscriptions import (
    cancel_subscription,
    create_subscription,
    list_subscriptions,
    retrieve_subscription,
    search_subscriptions,
    update_subscription,
)
from generated_tools.invoices import (
    create_invoice,
    create_preview_invoice,
    finalize_invoice,
    list_invoices,
    pay_invoice,
    retrieve_invoice,
    search_invoices,
    update_invoice,
    void_invoice,
)
from generated_tools.checkout_sessions import (
    create_checkout_session,
    expire_checkout_session,
    list_checkout_sessions,
    retrieve_checkout_session,
)
from generated_tools.payment_links import (
    create_payment_link,
    list_payment_link_line_items,
    list_payment_links,
    retrieve_payment_link,
    update_payment_link,
)
from generated_tools.accounts import create_account, delete_account, list_accounts, retrieve_account, update_account
from generated_tools.transfers import create_transfer, list_transfers, retrieve_transfer, update_transfer
from generated_tools.payouts import (
    cancel_payout,
    create_payout,
    list_payouts,
    retrieve_payout,
    reverse_payout,
    update_payout,
)
from generated_tools.setup_intents import (
    cancel_setup_intent,
    confirm_setup_intent,
    create_setup_intent,
    list_setup_intents,
    retrieve_setup_intent,
    update_setup_intent,
)
from generated_tools.coupons import create_coupon, delete_coupon, list_coupons, retrieve_coupon, update_coupon
from generated_tools.promotion_codes import (
    create_promotion_code,
    list_promotion_codes,
    retrieve_promotion_code,
    update_promotion_code,
)

mcp = FastMCP("stripe")


# PaymentIntents
@mcp.tool()
def stripe_create_payment_intent(
    amount: int,
    currency: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_payment_intent(amount, currency, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_update_payment_intent(
    payment_intent_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_payment_intent(payment_intent_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_payment_intent(
    payment_intent_id: str,
    expand: Optional[list] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return retrieve_payment_intent(payment_intent_id, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_payment_intents(
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return list_payment_intents(params=params, stripe_account=stripe_account)


@mcp.tool()
def stripe_confirm_payment_intent(
    payment_intent_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return confirm_payment_intent(payment_intent_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_capture_payment_intent(
    payment_intent_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return capture_payment_intent(payment_intent_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_cancel_payment_intent(
    payment_intent_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return cancel_payment_intent(payment_intent_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


# Charges
@mcp.tool()
def stripe_create_charge(
    amount: int,
    currency: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_charge(amount, currency, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_charge(charge_id: str, expand: Optional[list] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_charge(charge_id, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_charge(
    charge_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_charge(charge_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_list_charges(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_charges(params=params, stripe_account=stripe_account)


# Refunds
@mcp.tool()
def stripe_create_refund(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_refund(
        charge=charge,
        payment_intent=payment_intent,
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def stripe_update_refund(
    refund_id: str,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_refund(refund_id, metadata=metadata, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_refund(refund_id: str, expand: Optional[list] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_refund(refund_id, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_refunds(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_refunds(params=params, stripe_account=stripe_account)


# Customers
@mcp.tool()
def stripe_create_customer(
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_customer(params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_update_customer(
    customer_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_customer(customer_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_customer(customer_id: str, expand: Optional[list] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_customer(customer_id, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_delete_customer(customer_id: str, stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None) -> Dict[str, Any]:
    return delete_customer(customer_id, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_list_customers(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_customers(params=params, stripe_account=stripe_account)


@mcp.tool()
def stripe_search_customers(query: str, params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return search_customers(query, params=params, stripe_account=stripe_account)


# Products
@mcp.tool()
def stripe_create_product(
    name: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_product(name, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_update_product(
    product_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_product(product_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_product(product_id: str, expand: Optional[list] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_product(product_id, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_delete_product(product_id: str, stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None) -> Dict[str, Any]:
    return delete_product(product_id, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_list_products(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_products(params=params, stripe_account=stripe_account)


@mcp.tool()
def stripe_search_products(query: str, params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return search_products(query, params=params, stripe_account=stripe_account)


# Prices
@mcp.tool()
def stripe_create_price(
    currency: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_price(currency, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_update_price(
    price_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_price(price_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_price(price_id: str, expand: Optional[list] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_price(price_id, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_prices(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_prices(params=params, stripe_account=stripe_account)


@mcp.tool()
def stripe_search_prices(query: str, params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return search_prices(query, params=params, stripe_account=stripe_account)


# Subscriptions
@mcp.tool()
def stripe_create_subscription(
    customer: str,
    items: list,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_subscription(customer, items, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_update_subscription(
    subscription_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_subscription(subscription_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_subscription(subscription_id: str, expand: Optional[list] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_subscription(subscription_id, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_cancel_subscription(
    subscription_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return cancel_subscription(subscription_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_list_subscriptions(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_subscriptions(params=params, stripe_account=stripe_account)


@mcp.tool()
def stripe_search_subscriptions(query: str, params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return search_subscriptions(query, params=params, stripe_account=stripe_account)


# Invoices
@mcp.tool()
def stripe_create_invoice(
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_invoice(params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_create_preview_invoice(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return create_preview_invoice(params=params, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_invoice(
    invoice_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_invoice(invoice_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_invoice(invoice_id: str, expand: Optional[list] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_invoice(invoice_id, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_invoices(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_invoices(params=params, stripe_account=stripe_account)


@mcp.tool()
def stripe_finalize_invoice(
    invoice_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return finalize_invoice(invoice_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_pay_invoice(
    invoice_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return pay_invoice(invoice_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_void_invoice(
    invoice_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return void_invoice(invoice_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_search_invoices(query: str, params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return search_invoices(query, params=params, stripe_account=stripe_account)


# Checkout Sessions
@mcp.tool()
def stripe_create_checkout_session(
    mode: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_checkout_session(mode, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_checkout_session(session_id: str, expand: Optional[list] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_checkout_session(session_id, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_checkout_sessions(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_checkout_sessions(params=params, stripe_account=stripe_account)


@mcp.tool()
def stripe_expire_checkout_session(session_id: str, stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None) -> Dict[str, Any]:
    return expire_checkout_session(session_id, stripe_account=stripe_account, idempotency_key=idempotency_key)


# Payment Links
@mcp.tool()
def stripe_create_payment_link(
    line_items: list,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_payment_link(line_items, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_update_payment_link(
    payment_link_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_payment_link(payment_link_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_payment_link(payment_link_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_payment_link(payment_link_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_payment_links(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_payment_links(params=params, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_payment_link_line_items(
    payment_link_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return list_payment_link_line_items(payment_link_id, params=params, stripe_account=stripe_account)


# Connect Accounts
@mcp.tool()
def stripe_create_account(
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_account(params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_account(account_id: str, expand: Optional[list] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_account(account_id, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_update_account(
    account_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_account(account_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_delete_account(account_id: str, stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None) -> Dict[str, Any]:
    return delete_account(account_id, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_list_accounts(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_accounts(params=params, stripe_account=stripe_account)


# Transfers
@mcp.tool()
def stripe_create_transfer(
    amount: int,
    currency: str,
    destination: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_transfer(amount, currency, destination, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_update_transfer(
    transfer_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_transfer(transfer_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_transfer(transfer_id: str, expand: Optional[list] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_transfer(transfer_id, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_transfers(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_transfers(params=params, stripe_account=stripe_account)


# Payouts
@mcp.tool()
def stripe_create_payout(
    amount: int,
    currency: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_payout(amount, currency, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_update_payout(
    payout_id: str,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_payout(payout_id, metadata=metadata, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_payout(payout_id: str, expand: Optional[list] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_payout(payout_id, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_cancel_payout(payout_id: str, stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None) -> Dict[str, Any]:
    return cancel_payout(payout_id, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_reverse_payout(
    payout_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return reverse_payout(payout_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_list_payouts(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_payouts(params=params, stripe_account=stripe_account)


# SetupIntents
@mcp.tool()
def stripe_create_setup_intent(
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_setup_intent(params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_update_setup_intent(
    setup_intent_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_setup_intent(setup_intent_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_setup_intent(
    setup_intent_id: str,
    client_secret: Optional[str] = None,
    expand: Optional[list] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return retrieve_setup_intent(setup_intent_id, client_secret=client_secret, expand=expand, stripe_account=stripe_account)


@mcp.tool()
def stripe_confirm_setup_intent(
    setup_intent_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return confirm_setup_intent(setup_intent_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_cancel_setup_intent(
    setup_intent_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return cancel_setup_intent(setup_intent_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_list_setup_intents(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_setup_intents(params=params, stripe_account=stripe_account)


# Coupons
@mcp.tool()
def stripe_create_coupon(
    duration: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_coupon(duration, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_update_coupon(
    coupon_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_coupon(coupon_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_coupon(coupon_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_coupon(coupon_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_delete_coupon(coupon_id: str, stripe_account: Optional[str] = None, idempotency_key: Optional[str] = None) -> Dict[str, Any]:
    return delete_coupon(coupon_id, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_list_coupons(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_coupons(params=params, stripe_account=stripe_account)


# Promotion Codes
@mcp.tool()
def stripe_create_promotion_code(
    promotion: Dict[str, Any],
    code: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_promotion_code(promotion, code=code, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_update_promotion_code(
    promotion_code_id: str,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return update_promotion_code(promotion_code_id, params=params, stripe_account=stripe_account, idempotency_key=idempotency_key)


@mcp.tool()
def stripe_retrieve_promotion_code(promotion_code_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return retrieve_promotion_code(promotion_code_id, stripe_account=stripe_account)


@mcp.tool()
def stripe_list_promotion_codes(params: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return list_promotion_codes(params=params, stripe_account=stripe_account)


if __name__ == "__main__":
    mcp.run()
