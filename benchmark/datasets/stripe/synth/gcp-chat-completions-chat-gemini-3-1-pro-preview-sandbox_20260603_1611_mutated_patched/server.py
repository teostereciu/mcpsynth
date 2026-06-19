import os
import json
import requests
from typing import Any, Dict, List, Optional, Union
from fastmcp import FastMCP

mcp = FastMCP("stripe")

BASE_URL = "https://api.stripe.com/v1"

def get_api_key() -> str:
    api_key = os.environ.get("STRIPE_API_KEY")
    if not api_key:
        raise ValueError("STRIPE_API_KEY environment variable is required")
    return api_key

def flatten_dict(d: Dict[str, Any], parent_key: str = '') -> Dict[str, Any]:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}[{k}]" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, f"{new_key}[{i}]").items())
                else:
                    items.append((f"{new_key}[{i}]", item))
        else:
            items.append((new_key, v))
    return dict(items)

def make_request(method: str, endpoint: str, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {get_api_key()}",
    }
    
    if data:
        data = flatten_dict(data)
        data = {k: v for k, v in data.items() if v is not None}
        
    if params:
        params = flatten_dict(params)
        params = {k: v for k, v in params.items() if v is not None}

    try:
        response = requests.request(method, url, headers=headers, params=params, data=data)
        if response.status_code == 204:
            return {"success": True}
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Payment Intents
@mcp.tool()
def list_payment_intents(limit: int = 10, customer: Optional[str] = None) -> Dict[str, Any]:
    return make_request("GET", "/payment_intents", params={"limit": limit, "customer": customer})

@mcp.tool()
def create_payment_intent(amount: int, currency: str, customer: Optional[str] = None, payment_method: Optional[str] = None, confirm: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", "/payment_intents", data={"amount": amount, "currency": currency, "customer": customer, "payment_method": payment_method, "confirm": confirm})

@mcp.tool()
def retrieve_payment_intent(intent_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/payment_intents/{intent_id}")

@mcp.tool()
def update_payment_intent(intent_id: str, amount: Optional[int] = None, currency: Optional[str] = None, customer: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/payment_intents/{intent_id}", data={"amount": amount, "currency": currency, "customer": customer})

@mcp.tool()
def cancel_payment_intent(intent_id: str) -> Dict[str, Any]:
    return make_request("POST", f"/payment_intents/{intent_id}/cancel")

# Charges
@mcp.tool()
def list_charges(limit: int = 10, customer: Optional[str] = None) -> Dict[str, Any]:
    return make_request("GET", "/charges", params={"limit": limit, "customer": customer})

@mcp.tool()
def create_charge(amount: int, currency: str, source: Optional[str] = None, customer: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/charges", data={"amount": amount, "currency": currency, "source": source, "customer": customer, "description": description})

@mcp.tool()
def retrieve_charge(charge_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/charges/{charge_id}")

@mcp.tool()
def update_charge(charge_id: str, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    return make_request("POST", f"/charges/{charge_id}", data={"description": description, "metadata": metadata})

# Refunds
@mcp.tool()
def list_refunds(limit: int = 10, charge: Optional[str] = None, payment_intent: Optional[str] = None) -> Dict[str, Any]:
    return make_request("GET", "/refunds", params={"limit": limit, "charge": charge, "payment_intent": payment_intent})

@mcp.tool()
def create_refund(charge: Optional[str] = None, payment_intent: Optional[str] = None, amount: Optional[int] = None, reason: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/refunds", data={"charge": charge, "payment_intent": payment_intent, "amount": amount, "reason": reason})

@mcp.tool()
def retrieve_refund(refund_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/refunds/{refund_id}")

@mcp.tool()
def update_refund(refund_id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    return make_request("POST", f"/refunds/{refund_id}", data={"metadata": metadata})

# Customers
@mcp.tool()
def list_customers(limit: int = 10, email: Optional[str] = None) -> Dict[str, Any]:
    return make_request("GET", "/customers", params={"limit": limit, "email": email})

@mcp.tool()
def create_customer(email: Optional[str] = None, name: Optional[str] = None, phone: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/customers", data={"email": email, "name": name, "phone": phone, "description": description})

@mcp.tool()
def retrieve_customer(customer_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/customers/{customer_id}")

@mcp.tool()
def update_customer(customer_id: str, email: Optional[str] = None, name: Optional[str] = None, phone: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/customers/{customer_id}", data={"email": email, "name": name, "phone": phone, "description": description})

@mcp.tool()
def delete_customer(customer_id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/customers/{customer_id}")

# Products
@mcp.tool()
def list_products(limit: int = 10, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("GET", "/products", params={"limit": limit, "active": active})

@mcp.tool()
def create_product(name: str, description: Optional[str] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", "/products", data={"name": name, "description": description, "active": active})

@mcp.tool()
def retrieve_product(product_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/products/{product_id}")

@mcp.tool()
def update_product(product_id: str, name: Optional[str] = None, description: Optional[str] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/products/{product_id}", data={"name": name, "description": description, "active": active})

@mcp.tool()
def delete_product(product_id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/products/{product_id}")

# Prices
@mcp.tool()
def list_prices(limit: int = 10, product: Optional[str] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("GET", "/prices", params={"limit": limit, "product": product, "active": active})

@mcp.tool()
def create_price(currency: str, product: str, unit_amount: Optional[int] = None, recurring: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return make_request("POST", "/prices", data={"currency": currency, "product": product, "unit_amount": unit_amount, "recurring": recurring})

@mcp.tool()
def retrieve_price(price_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/prices/{price_id}")

@mcp.tool()
def update_price(price_id: str, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/prices/{price_id}", data={"active": active})

# Subscriptions
@mcp.tool()
def list_subscriptions(limit: int = 10, customer: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
    return make_request("GET", "/subscriptions", params={"limit": limit, "customer": customer, "status": status})

@mcp.tool()
def create_subscription(customer: str, items: List[Dict[str, Any]]) -> Dict[str, Any]:
    return make_request("POST", "/subscriptions", data={"customer": customer, "items": items})

@mcp.tool()
def retrieve_subscription(subscription_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/subscriptions/{subscription_id}")

@mcp.tool()
def update_subscription(subscription_id: str, items: Optional[List[Dict[str, Any]]] = None, cancel_at_period_end: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/subscriptions/{subscription_id}", data={"items": items, "cancel_at_period_end": cancel_at_period_end})

@mcp.tool()
def cancel_subscription(subscription_id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/subscriptions/{subscription_id}")

# Invoices
@mcp.tool()
def list_invoices(limit: int = 10, customer: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
    return make_request("GET", "/invoices", params={"limit": limit, "customer": customer, "status": status})

@mcp.tool()
def create_invoice(customer: str, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/invoices", data={"customer": customer, "description": description})

@mcp.tool()
def retrieve_invoice(invoice_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/invoices/{invoice_id}")

@mcp.tool()
def update_invoice(invoice_id: str, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/invoices/{invoice_id}", data={"description": description})

@mcp.tool()
def delete_invoice(invoice_id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/invoices/{invoice_id}")

@mcp.tool()
def finalize_invoice(invoice_id: str) -> Dict[str, Any]:
    return make_request("POST", f"/invoices/{invoice_id}/finalize")

@mcp.tool()
def pay_invoice(invoice_id: str) -> Dict[str, Any]:
    return make_request("POST", f"/invoices/{invoice_id}/pay")

# Checkout Sessions
@mcp.tool()
def list_checkout_sessions(limit: int = 10, payment_intent: Optional[str] = None, subscription: Optional[str] = None) -> Dict[str, Any]:
    return make_request("GET", "/checkout/sessions", params={"limit": limit, "payment_intent": payment_intent, "subscription": subscription})

@mcp.tool()
def create_checkout_session(success_url: str, cancel_url: str, line_items: List[Dict[str, Any]], mode: str = "payment", customer: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/checkout/sessions", data={"success_url": success_url, "cancel_url": cancel_url, "line_items": line_items, "mode": mode, "customer": customer})

@mcp.tool()
def retrieve_checkout_session(session_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/checkout/sessions/{session_id}")

@mcp.tool()
def expire_checkout_session(session_id: str) -> Dict[str, Any]:
    return make_request("POST", f"/checkout/sessions/{session_id}/expire")

# Payment Links
@mcp.tool()
def list_payment_links(limit: int = 10, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("GET", "/payment_links", params={"limit": limit, "active": active})

@mcp.tool()
def create_payment_link(line_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    return make_request("POST", "/payment_links", data={"line_items": line_items})

@mcp.tool()
def retrieve_payment_link(payment_link_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/payment_links/{payment_link_id}")

@mcp.tool()
def update_payment_link(payment_link_id: str, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/payment_links/{payment_link_id}", data={"active": active})

# Accounts (Connect)
@mcp.tool()
def list_accounts(limit: int = 10) -> Dict[str, Any]:
    return make_request("GET", "/accounts", params={"limit": limit})

@mcp.tool()
def create_account(type: str, country: Optional[str] = None, email: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/accounts", data={"type": type, "country": country, "email": email})

@mcp.tool()
def retrieve_account(account_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/accounts/{account_id}")

@mcp.tool()
def update_account(account_id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    return make_request("POST", f"/accounts/{account_id}", data={"metadata": metadata})

@mcp.tool()
def delete_account(account_id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/accounts/{account_id}")

# Transfers (Connect)
@mcp.tool()
def list_transfers(limit: int = 10, destination: Optional[str] = None) -> Dict[str, Any]:
    return make_request("GET", "/transfers", params={"limit": limit, "destination": destination})

@mcp.tool()
def create_transfer(amount: int, currency: str, destination: str, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/transfers", data={"amount": amount, "currency": currency, "destination": destination, "description": description})

@mcp.tool()
def retrieve_transfer(transfer_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/transfers/{transfer_id}")

@mcp.tool()
def update_transfer(transfer_id: str, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/transfers/{transfer_id}", data={"description": description})

# Payouts (Connect)
@mcp.tool()
def list_payouts(limit: int = 10, destination: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
    return make_request("GET", "/payouts", params={"limit": limit, "destination": destination, "status": status})

@mcp.tool()
def create_payout(amount: int, currency: str, destination: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/payouts", data={"amount": amount, "currency": currency, "destination": destination, "description": description})

@mcp.tool()
def retrieve_payout(payout_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/payouts/{payout_id}")

@mcp.tool()
def update_payout(payout_id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    return make_request("POST", f"/payouts/{payout_id}", data={"metadata": metadata})

@mcp.tool()
def cancel_payout(payout_id: str) -> Dict[str, Any]:
    return make_request("POST", f"/payouts/{payout_id}/cancel")

# Setup Intents
@mcp.tool()
def list_setup_intents(limit: int = 10, customer: Optional[str] = None, payment_method: Optional[str] = None) -> Dict[str, Any]:
    return make_request("GET", "/setup_intents", params={"limit": limit, "customer": customer, "payment_method": payment_method})

@mcp.tool()
def create_setup_intent(customer: Optional[str] = None, payment_method: Optional[str] = None, usage: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/setup_intents", data={"customer": customer, "payment_method": payment_method, "usage": usage})

@mcp.tool()
def retrieve_setup_intent(intent_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/setup_intents/{intent_id}")

@mcp.tool()
def update_setup_intent(intent_id: str, customer: Optional[str] = None, payment_method: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/setup_intents/{intent_id}", data={"customer": customer, "payment_method": payment_method})

@mcp.tool()
def cancel_setup_intent(intent_id: str) -> Dict[str, Any]:
    return make_request("POST", f"/setup_intents/{intent_id}/cancel")

# Coupons
@mcp.tool()
def list_coupons(limit: int = 10) -> Dict[str, Any]:
    return make_request("GET", "/coupons", params={"limit": limit})

@mcp.tool()
def create_coupon(duration: str, amount_off: Optional[int] = None, currency: Optional[str] = None, percent_off: Optional[float] = None, name: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/coupons", data={"duration": duration, "amount_off": amount_off, "currency": currency, "percent_off": percent_off, "name": name})

@mcp.tool()
def retrieve_coupon(coupon_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/coupons/{coupon_id}")

@mcp.tool()
def update_coupon(coupon_id: str, name: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/coupons/{coupon_id}", data={"name": name})

@mcp.tool()
def delete_coupon(coupon_id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/coupons/{coupon_id}")

# Promotion Codes
@mcp.tool()
def list_promotion_codes(limit: int = 10, coupon: Optional[str] = None, customer: Optional[str] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("GET", "/promotion_codes", params={"limit": limit, "coupon": coupon, "customer": customer, "active": active})

@mcp.tool()
def create_promotion_code(coupon: str, code: Optional[str] = None, customer: Optional[str] = None, max_redemptions: Optional[int] = None) -> Dict[str, Any]:
    return make_request("POST", "/promotion_codes", data={"coupon": coupon, "code": code, "customer": customer, "max_redemptions": max_redemptions})

@mcp.tool()
def retrieve_promotion_code(promotion_code_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/promotion_codes/{promotion_code_id}")

@mcp.tool()
def update_promotion_code(promotion_code_id: str, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/promotion_codes/{promotion_code_id}", data={"active": active})

if __name__ == "__main__":
    mcp.run()
