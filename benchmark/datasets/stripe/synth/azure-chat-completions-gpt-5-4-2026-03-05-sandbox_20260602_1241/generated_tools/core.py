from .common import compact_result, stripe_request


def create_customer(**params):
    return compact_result(stripe_request("POST", "/v1/customers", params))


def update_customer(customer_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/customers/{customer_id}", params))


def retrieve_customer(customer_id: str):
    return compact_result(stripe_request("GET", f"/v1/customers/{customer_id}"))


def list_customers(**params):
    return compact_result(stripe_request("GET", "/v1/customers", params))


def delete_customer(customer_id: str):
    return compact_result(stripe_request("DELETE", f"/v1/customers/{customer_id}"))


def create_payment_intent(**params):
    return compact_result(stripe_request("POST", "/v1/payment_intents", params))


def update_payment_intent(payment_intent_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}", params))


def retrieve_payment_intent(payment_intent_id: str):
    return compact_result(stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}"))


def list_payment_intents(**params):
    return compact_result(stripe_request("GET", "/v1/payment_intents", params))


def confirm_payment_intent(payment_intent_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", params))


def capture_payment_intent(payment_intent_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/capture", params))


def cancel_payment_intent(payment_intent_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/cancel", params))


def create_charge(**params):
    return compact_result(stripe_request("POST", "/v1/charges", params))


def update_charge(charge_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/charges/{charge_id}", params))


def retrieve_charge(charge_id: str):
    return compact_result(stripe_request("GET", f"/v1/charges/{charge_id}"))


def list_charges(**params):
    return compact_result(stripe_request("GET", "/v1/charges", params))


def create_refund(**params):
    return compact_result(stripe_request("POST", "/v1/refunds", params))


def update_refund(refund_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/refunds/{refund_id}", params))


def retrieve_refund(refund_id: str):
    return compact_result(stripe_request("GET", f"/v1/refunds/{refund_id}"))


def list_refunds(**params):
    return compact_result(stripe_request("GET", "/v1/refunds", params))


def create_product(**params):
    return compact_result(stripe_request("POST", "/v1/products", params))


def update_product(product_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/products/{product_id}", params))


def retrieve_product(product_id: str):
    return compact_result(stripe_request("GET", f"/v1/products/{product_id}"))


def list_products(**params):
    return compact_result(stripe_request("GET", "/v1/products", params))


def delete_product(product_id: str):
    return compact_result(stripe_request("DELETE", f"/v1/products/{product_id}"))


def create_price(**params):
    return compact_result(stripe_request("POST", "/v1/prices", params))


def update_price(price_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/prices/{price_id}", params))


def retrieve_price(price_id: str):
    return compact_result(stripe_request("GET", f"/v1/prices/{price_id}"))


def list_prices(**params):
    return compact_result(stripe_request("GET", "/v1/prices", params))


def create_subscription(**params):
    return compact_result(stripe_request("POST", "/v1/subscriptions", params))


def update_subscription(subscription_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/subscriptions/{subscription_id}", params))


def retrieve_subscription(subscription_id: str):
    return compact_result(stripe_request("GET", f"/v1/subscriptions/{subscription_id}"))


def list_subscriptions(**params):
    return compact_result(stripe_request("GET", "/v1/subscriptions", params))


def cancel_subscription(subscription_id: str, **params):
    return compact_result(stripe_request("DELETE", f"/v1/subscriptions/{subscription_id}", params))


def create_invoice(**params):
    return compact_result(stripe_request("POST", "/v1/invoices", params))


def create_preview_invoice(**params):
    return compact_result(stripe_request("POST", "/v1/invoices/create_preview", params))


def update_invoice(invoice_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/invoices/{invoice_id}", params))


def retrieve_invoice(invoice_id: str):
    return compact_result(stripe_request("GET", f"/v1/invoices/{invoice_id}"))


def list_invoices(**params):
    return compact_result(stripe_request("GET", "/v1/invoices", params))


def finalize_invoice(invoice_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/invoices/{invoice_id}/finalize", params))


def pay_invoice(invoice_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/invoices/{invoice_id}/pay", params))


def void_invoice(invoice_id: str):
    return compact_result(stripe_request("POST", f"/v1/invoices/{invoice_id}/void", {}))


def create_checkout_session(**params):
    return compact_result(stripe_request("POST", "/v1/checkout/sessions", params))


def retrieve_checkout_session(session_id: str):
    return compact_result(stripe_request("GET", f"/v1/checkout/sessions/{session_id}"))


def list_checkout_sessions(**params):
    return compact_result(stripe_request("GET", "/v1/checkout/sessions", params))


def expire_checkout_session(session_id: str):
    return compact_result(stripe_request("POST", f"/v1/checkout/sessions/{session_id}/expire", {}))


def create_payment_link(**params):
    return compact_result(stripe_request("POST", "/v1/payment_links", params))


def update_payment_link(payment_link_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/payment_links/{payment_link_id}", params))


def retrieve_payment_link(payment_link_id: str):
    return compact_result(stripe_request("GET", f"/v1/payment_links/{payment_link_id}"))


def list_payment_links(**params):
    return compact_result(stripe_request("GET", "/v1/payment_links", params))


def list_payment_link_line_items(payment_link_id: str, **params):
    return compact_result(stripe_request("GET", f"/v1/payment_links/{payment_link_id}/line_items", params))


def create_account(**params):
    return compact_result(stripe_request("POST", "/v1/accounts", params))


def update_account(account_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/accounts/{account_id}", params))


def retrieve_account(account_id: str):
    return compact_result(stripe_request("GET", f"/v1/accounts/{account_id}"))


def list_accounts(**params):
    return compact_result(stripe_request("GET", "/v1/accounts", params))


def create_transfer(**params):
    return compact_result(stripe_request("POST", "/v1/transfers", params))


def update_transfer(transfer_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/transfers/{transfer_id}", params))


def retrieve_transfer(transfer_id: str):
    return compact_result(stripe_request("GET", f"/v1/transfers/{transfer_id}"))


def list_transfers(**params):
    return compact_result(stripe_request("GET", "/v1/transfers", params))


def create_payout(**params):
    return compact_result(stripe_request("POST", "/v1/payouts", params))


def update_payout(payout_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/payouts/{payout_id}", params))


def retrieve_payout(payout_id: str):
    return compact_result(stripe_request("GET", f"/v1/payouts/{payout_id}"))


def list_payouts(**params):
    return compact_result(stripe_request("GET", "/v1/payouts", params))


def cancel_payout(payout_id: str):
    return compact_result(stripe_request("POST", f"/v1/payouts/{payout_id}/cancel", {}))


def create_setup_intent(**params):
    return compact_result(stripe_request("POST", "/v1/setup_intents", params))


def update_setup_intent(setup_intent_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}", params))


def retrieve_setup_intent(setup_intent_id: str, **params):
    return compact_result(stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}", params))


def list_setup_intents(**params):
    return compact_result(stripe_request("GET", "/v1/setup_intents", params))


def confirm_setup_intent(setup_intent_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", params))


def cancel_setup_intent(setup_intent_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/cancel", params))


def create_coupon(**params):
    return compact_result(stripe_request("POST", "/v1/coupons", params))


def update_coupon(coupon_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/coupons/{coupon_id}", params))


def retrieve_coupon(coupon_id: str):
    return compact_result(stripe_request("GET", f"/v1/coupons/{coupon_id}"))


def list_coupons(**params):
    return compact_result(stripe_request("GET", "/v1/coupons", params))


def delete_coupon(coupon_id: str):
    return compact_result(stripe_request("DELETE", f"/v1/coupons/{coupon_id}"))


def create_promotion_code(**params):
    return compact_result(stripe_request("POST", "/v1/promotion_codes", params))


def update_promotion_code(promotion_code_id: str, **params):
    return compact_result(stripe_request("POST", f"/v1/promotion_codes/{promotion_code_id}", params))


def retrieve_promotion_code(promotion_code_id: str):
    return compact_result(stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}"))


def list_promotion_codes(**params):
    return compact_result(stripe_request("GET", "/v1/promotion_codes", params))
