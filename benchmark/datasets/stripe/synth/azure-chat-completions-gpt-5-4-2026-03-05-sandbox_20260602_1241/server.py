from mcp.server.fastmcp import FastMCP

from generated_tools import core

mcp = FastMCP("stripe")


@mcp.tool()
def create_customer(**params):
    return core.create_customer(**params)


@mcp.tool()
def update_customer(customer_id: str, **params):
    return core.update_customer(customer_id, **params)


@mcp.tool()
def retrieve_customer(customer_id: str):
    return core.retrieve_customer(customer_id)


@mcp.tool()
def list_customers(**params):
    return core.list_customers(**params)


@mcp.tool()
def delete_customer(customer_id: str):
    return core.delete_customer(customer_id)


@mcp.tool()
def create_payment_intent(**params):
    return core.create_payment_intent(**params)


@mcp.tool()
def update_payment_intent(payment_intent_id: str, **params):
    return core.update_payment_intent(payment_intent_id, **params)


@mcp.tool()
def retrieve_payment_intent(payment_intent_id: str):
    return core.retrieve_payment_intent(payment_intent_id)


@mcp.tool()
def list_payment_intents(**params):
    return core.list_payment_intents(**params)


@mcp.tool()
def confirm_payment_intent(payment_intent_id: str, **params):
    return core.confirm_payment_intent(payment_intent_id, **params)


@mcp.tool()
def capture_payment_intent(payment_intent_id: str, **params):
    return core.capture_payment_intent(payment_intent_id, **params)


@mcp.tool()
def cancel_payment_intent(payment_intent_id: str, **params):
    return core.cancel_payment_intent(payment_intent_id, **params)


@mcp.tool()
def create_charge(**params):
    return core.create_charge(**params)


@mcp.tool()
def update_charge(charge_id: str, **params):
    return core.update_charge(charge_id, **params)


@mcp.tool()
def retrieve_charge(charge_id: str):
    return core.retrieve_charge(charge_id)


@mcp.tool()
def list_charges(**params):
    return core.list_charges(**params)


@mcp.tool()
def create_refund(**params):
    return core.create_refund(**params)


@mcp.tool()
def update_refund(refund_id: str, **params):
    return core.update_refund(refund_id, **params)


@mcp.tool()
def retrieve_refund(refund_id: str):
    return core.retrieve_refund(refund_id)


@mcp.tool()
def list_refunds(**params):
    return core.list_refunds(**params)


@mcp.tool()
def create_product(**params):
    return core.create_product(**params)


@mcp.tool()
def update_product(product_id: str, **params):
    return core.update_product(product_id, **params)


@mcp.tool()
def retrieve_product(product_id: str):
    return core.retrieve_product(product_id)


@mcp.tool()
def list_products(**params):
    return core.list_products(**params)


@mcp.tool()
def delete_product(product_id: str):
    return core.delete_product(product_id)


@mcp.tool()
def create_price(**params):
    return core.create_price(**params)


@mcp.tool()
def update_price(price_id: str, **params):
    return core.update_price(price_id, **params)


@mcp.tool()
def retrieve_price(price_id: str):
    return core.retrieve_price(price_id)


@mcp.tool()
def list_prices(**params):
    return core.list_prices(**params)


@mcp.tool()
def create_subscription(**params):
    return core.create_subscription(**params)


@mcp.tool()
def update_subscription(subscription_id: str, **params):
    return core.update_subscription(subscription_id, **params)


@mcp.tool()
def retrieve_subscription(subscription_id: str):
    return core.retrieve_subscription(subscription_id)


@mcp.tool()
def list_subscriptions(**params):
    return core.list_subscriptions(**params)


@mcp.tool()
def cancel_subscription(subscription_id: str, **params):
    return core.cancel_subscription(subscription_id, **params)


@mcp.tool()
def create_invoice(**params):
    return core.create_invoice(**params)


@mcp.tool()
def create_preview_invoice(**params):
    return core.create_preview_invoice(**params)


@mcp.tool()
def update_invoice(invoice_id: str, **params):
    return core.update_invoice(invoice_id, **params)


@mcp.tool()
def retrieve_invoice(invoice_id: str):
    return core.retrieve_invoice(invoice_id)


@mcp.tool()
def list_invoices(**params):
    return core.list_invoices(**params)


@mcp.tool()
def finalize_invoice(invoice_id: str, **params):
    return core.finalize_invoice(invoice_id, **params)


@mcp.tool()
def pay_invoice(invoice_id: str, **params):
    return core.pay_invoice(invoice_id, **params)


@mcp.tool()
def void_invoice(invoice_id: str):
    return core.void_invoice(invoice_id)


@mcp.tool()
def create_checkout_session(**params):
    return core.create_checkout_session(**params)


@mcp.tool()
def retrieve_checkout_session(session_id: str):
    return core.retrieve_checkout_session(session_id)


@mcp.tool()
def list_checkout_sessions(**params):
    return core.list_checkout_sessions(**params)


@mcp.tool()
def expire_checkout_session(session_id: str):
    return core.expire_checkout_session(session_id)


@mcp.tool()
def create_payment_link(**params):
    return core.create_payment_link(**params)


@mcp.tool()
def update_payment_link(payment_link_id: str, **params):
    return core.update_payment_link(payment_link_id, **params)


@mcp.tool()
def retrieve_payment_link(payment_link_id: str):
    return core.retrieve_payment_link(payment_link_id)


@mcp.tool()
def list_payment_links(**params):
    return core.list_payment_links(**params)


@mcp.tool()
def list_payment_link_line_items(payment_link_id: str, **params):
    return core.list_payment_link_line_items(payment_link_id, **params)


@mcp.tool()
def create_account(**params):
    return core.create_account(**params)


@mcp.tool()
def update_account(account_id: str, **params):
    return core.update_account(account_id, **params)


@mcp.tool()
def retrieve_account(account_id: str):
    return core.retrieve_account(account_id)


@mcp.tool()
def list_accounts(**params):
    return core.list_accounts(**params)


@mcp.tool()
def create_transfer(**params):
    return core.create_transfer(**params)


@mcp.tool()
def update_transfer(transfer_id: str, **params):
    return core.update_transfer(transfer_id, **params)


@mcp.tool()
def retrieve_transfer(transfer_id: str):
    return core.retrieve_transfer(transfer_id)


@mcp.tool()
def list_transfers(**params):
    return core.list_transfers(**params)


@mcp.tool()
def create_payout(**params):
    return core.create_payout(**params)


@mcp.tool()
def update_payout(payout_id: str, **params):
    return core.update_payout(payout_id, **params)


@mcp.tool()
def retrieve_payout(payout_id: str):
    return core.retrieve_payout(payout_id)


@mcp.tool()
def list_payouts(**params):
    return core.list_payouts(**params)


@mcp.tool()
def cancel_payout(payout_id: str):
    return core.cancel_payout(payout_id)


@mcp.tool()
def create_setup_intent(**params):
    return core.create_setup_intent(**params)


@mcp.tool()
def update_setup_intent(setup_intent_id: str, **params):
    return core.update_setup_intent(setup_intent_id, **params)


@mcp.tool()
def retrieve_setup_intent(setup_intent_id: str, **params):
    return core.retrieve_setup_intent(setup_intent_id, **params)


@mcp.tool()
def list_setup_intents(**params):
    return core.list_setup_intents(**params)


@mcp.tool()
def confirm_setup_intent(setup_intent_id: str, **params):
    return core.confirm_setup_intent(setup_intent_id, **params)


@mcp.tool()
def cancel_setup_intent(setup_intent_id: str, **params):
    return core.cancel_setup_intent(setup_intent_id, **params)


@mcp.tool()
def create_coupon(**params):
    return core.create_coupon(**params)


@mcp.tool()
def update_coupon(coupon_id: str, **params):
    return core.update_coupon(coupon_id, **params)


@mcp.tool()
def retrieve_coupon(coupon_id: str):
    return core.retrieve_coupon(coupon_id)


@mcp.tool()
def list_coupons(**params):
    return core.list_coupons(**params)


@mcp.tool()
def delete_coupon(coupon_id: str):
    return core.delete_coupon(coupon_id)


@mcp.tool()
def create_promotion_code(**params):
    return core.create_promotion_code(**params)


@mcp.tool()
def update_promotion_code(promotion_code_id: str, **params):
    return core.update_promotion_code(promotion_code_id, **params)


@mcp.tool()
def retrieve_promotion_code(promotion_code_id: str):
    return core.retrieve_promotion_code(promotion_code_id)


@mcp.tool()
def list_promotion_codes(**params):
    return core.list_promotion_codes(**params)


if __name__ == "__main__":
    mcp.run()
