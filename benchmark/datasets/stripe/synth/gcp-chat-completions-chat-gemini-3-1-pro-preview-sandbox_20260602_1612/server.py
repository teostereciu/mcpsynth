import os
import requests
from typing import Any, Dict, Optional, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Stripe")
BASE_URL = "https://api.stripe.com/v1"

def get_headers() -> Dict[str, str]:
    api_key = os.environ.get("STRIPE_API_KEY")
    if not api_key:
        raise ValueError("STRIPE_API_KEY environment variable is not set")
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

def make_request(method: str, path: str, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{BASE_URL}{path}"
    headers = get_headers()
    
    if data:
        data = {k: v for k, v in data.items() if v is not None}
    if params:
        params = {k: v for k, v in params.items() if v is not None}
        
    try:
        response = requests.request(method, url, headers=headers, data=data, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        if e.response is not None:
            try:
                return e.response.json()
            except ValueError:
                return {"error": str(e), "status_code": e.response.status_code}
        return {"error": str(e)}

# Payment Intents
@mcp.tool()
def create_payment_intent(amount: int, currency: str, customer: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/payment_intents", data={"amount": amount, "currency": currency, "customer": customer, "description": description})

@mcp.tool()
def retrieve_payment_intent(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/payment_intents/{id}")

@mcp.tool()
def update_payment_intent(id: str, amount: Optional[int] = None, currency: Optional[str] = None, customer: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/payment_intents/{id}", data={"amount": amount, "currency": currency, "customer": customer, "description": description})

@mcp.tool()
def cancel_payment_intent(id: str, cancellation_reason: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/payment_intents/{id}/cancel", data={"cancellation_reason": cancellation_reason})

@mcp.tool()
def capture_payment_intent(id: str, amount_to_capture: Optional[int] = None) -> Dict[str, Any]:
    return make_request("POST", f"/payment_intents/{id}/capture", data={"amount_to_capture": amount_to_capture})

@mcp.tool()
def list_payment_intents(customer: Optional[str] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/payment_intents", params={"customer": customer, "limit": limit})

# Charges
@mcp.tool()
def retrieve_charge(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/charges/{id}")

@mcp.tool()
def update_charge(id: str, description: Optional[str] = None, receipt_email: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/charges/{id}", data={"description": description, "receipt_email": receipt_email})

@mcp.tool()
def capture_charge(id: str, amount: Optional[int] = None) -> Dict[str, Any]:
    return make_request("POST", f"/charges/{id}/capture", data={"amount": amount})

@mcp.tool()
def list_charges(customer: Optional[str] = None, payment_intent: Optional[str] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/charges", params={"customer": customer, "payment_intent": payment_intent, "limit": limit})

# Refunds
@mcp.tool()
def create_refund(charge: Optional[str] = None, payment_intent: Optional[str] = None, amount: Optional[int] = None, reason: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/refunds", data={"charge": charge, "payment_intent": payment_intent, "amount": amount, "reason": reason})

@mcp.tool()
def retrieve_refund(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/refunds/{id}")

@mcp.tool()
def update_refund(id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    return make_request("POST", f"/refunds/{id}", data={"metadata": metadata})

@mcp.tool()
def list_refunds(charge: Optional[str] = None, payment_intent: Optional[str] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/refunds", params={"charge": charge, "payment_intent": payment_intent, "limit": limit})

# Customers
@mcp.tool()
def create_customer(email: Optional[str] = None, name: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/customers", data={"email": email, "name": name, "description": description})

@mcp.tool()
def retrieve_customer(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/customers/{id}")

@mcp.tool()
def update_customer(id: str, email: Optional[str] = None, name: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/customers/{id}", data={"email": email, "name": name, "description": description})

@mcp.tool()
def delete_customer(id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/customers/{id}")

@mcp.tool()
def list_customers(email: Optional[str] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/customers", params={"email": email, "limit": limit})

# Products
@mcp.tool()
def create_product(name: str, description: Optional[str] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", "/products", data={"name": name, "description": description, "active": active})

@mcp.tool()
def retrieve_product(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/products/{id}")

@mcp.tool()
def update_product(id: str, name: Optional[str] = None, description: Optional[str] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/products/{id}", data={"name": name, "description": description, "active": active})

@mcp.tool()
def delete_product(id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/products/{id}")

@mcp.tool()
def list_products(active: Optional[bool] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/products", params={"active": active, "limit": limit})

# Prices
@mcp.tool()
def create_price(currency: str, product: str, unit_amount: Optional[int] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", "/prices", data={"currency": currency, "product": product, "unit_amount": unit_amount, "active": active})

@mcp.tool()
def retrieve_price(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/prices/{id}")

@mcp.tool()
def update_price(id: str, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/prices/{id}", data={"active": active})

@mcp.tool()
def list_prices(product: Optional[str] = None, active: Optional[bool] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/prices", params={"product": product, "active": active, "limit": limit})

# Subscriptions
@mcp.tool()
def create_subscription(customer: str, items: List[Dict[str, Any]], description: Optional[str] = None) -> Dict[str, Any]:
    # Note: items is a list of dicts, e.g. [{"price": "price_123"}]
    # Stripe expects items[0][price]=price_123 in form data
    data = {"customer": customer, "description": description}
    for i, item in enumerate(items):
        for k, v in item.items():
            data[f"items[{i}][{k}]"] = v
    return make_request("POST", "/subscriptions", data=data)

@mcp.tool()
def retrieve_subscription(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/subscriptions/{id}")

@mcp.tool()
def update_subscription(id: str, description: Optional[str] = None, cancel_at_period_end: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/subscriptions/{id}", data={"description": description, "cancel_at_period_end": cancel_at_period_end})

@mcp.tool()
def cancel_subscription(id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/subscriptions/{id}")

@mcp.tool()
def list_subscriptions(customer: Optional[str] = None, status: Optional[str] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/subscriptions", params={"customer": customer, "status": status, "limit": limit})

# Invoices
@mcp.tool()
def create_invoice(customer: str, description: Optional[str] = None, auto_advance: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", "/invoices", data={"customer": customer, "description": description, "auto_advance": auto_advance})

@mcp.tool()
def retrieve_invoice(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/invoices/{id}")

@mcp.tool()
def update_invoice(id: str, description: Optional[str] = None, auto_advance: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/invoices/{id}", data={"description": description, "auto_advance": auto_advance})

@mcp.tool()
def delete_invoice(id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/invoices/{id}")

@mcp.tool()
def finalize_invoice(id: str, auto_advance: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/invoices/{id}/finalize", data={"auto_advance": auto_advance})

@mcp.tool()
def pay_invoice(id: str, paid_out_of_band: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/invoices/{id}/pay", data={"paid_out_of_band": paid_out_of_band})

@mcp.tool()
def list_invoices(customer: Optional[str] = None, status: Optional[str] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/invoices", params={"customer": customer, "status": status, "limit": limit})

# Checkout Sessions
@mcp.tool()
def create_checkout_session(success_url: str, cancel_url: Optional[str] = None, mode: Optional[str] = "payment", customer: Optional[str] = None, line_items: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    data = {"success_url": success_url, "cancel_url": cancel_url, "mode": mode, "customer": customer}
    if line_items:
        for i, item in enumerate(line_items):
            for k, v in item.items():
                data[f"line_items[{i}][{k}]"] = v
    return make_request("POST", "/checkout/sessions", data=data)

@mcp.tool()
def retrieve_checkout_session(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/checkout/sessions/{id}")

@mcp.tool()
def expire_checkout_session(id: str) -> Dict[str, Any]:
    return make_request("POST", f"/checkout/sessions/{id}/expire")

@mcp.tool()
def list_checkout_sessions(customer: Optional[str] = None, payment_intent: Optional[str] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/checkout/sessions", params={"customer": customer, "payment_intent": payment_intent, "limit": limit})

# Payment Links
@mcp.tool()
def create_payment_link(line_items: List[Dict[str, Any]], active: Optional[bool] = None) -> Dict[str, Any]:
    data = {"active": active}
    for i, item in enumerate(line_items):
        for k, v in item.items():
            data[f"line_items[{i}][{k}]"] = v
    return make_request("POST", "/payment_links", data=data)

@mcp.tool()
def retrieve_payment_link(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/payment_links/{id}")

@mcp.tool()
def update_payment_link(id: str, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/payment_links/{id}", data={"active": active})

@mcp.tool()
def list_payment_links(active: Optional[bool] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/payment_links", params={"active": active, "limit": limit})

# Connect Accounts
@mcp.tool()
def create_account(type: str, country: Optional[str] = None, email: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/accounts", data={"type": type, "country": country, "email": email})

@mcp.tool()
def retrieve_account(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/accounts/{id}")

@mcp.tool()
def update_account(id: str, email: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/accounts/{id}", data={"email": email})

@mcp.tool()
def delete_account(id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/accounts/{id}")

@mcp.tool()
def list_accounts(limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/accounts", params={"limit": limit})

# Transfers
@mcp.tool()
def create_transfer(amount: int, currency: str, destination: str, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/transfers", data={"amount": amount, "currency": currency, "destination": destination, "description": description})

@mcp.tool()
def retrieve_transfer(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/transfers/{id}")

@mcp.tool()
def update_transfer(id: str, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/transfers/{id}", data={"description": description})

@mcp.tool()
def list_transfers(destination: Optional[str] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/transfers", params={"destination": destination, "limit": limit})

# Payouts
@mcp.tool()
def create_payout(amount: int, currency: str, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/payouts", data={"amount": amount, "currency": currency, "description": description})

@mcp.tool()
def retrieve_payout(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/payouts/{id}")

@mcp.tool()
def update_payout(id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    return make_request("POST", f"/payouts/{id}", data={"metadata": metadata})

@mcp.tool()
def cancel_payout(id: str) -> Dict[str, Any]:
    return make_request("POST", f"/payouts/{id}/cancel")

@mcp.tool()
def list_payouts(status: Optional[str] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/payouts", params={"status": status, "limit": limit})

# Setup Intents
@mcp.tool()
def create_setup_intent(customer: Optional[str] = None, description: Optional[str] = None, usage: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/setup_intents", data={"customer": customer, "description": description, "usage": usage})

@mcp.tool()
def retrieve_setup_intent(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/setup_intents/{id}")

@mcp.tool()
def update_setup_intent(id: str, customer: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/setup_intents/{id}", data={"customer": customer, "description": description})

@mcp.tool()
def cancel_setup_intent(id: str, cancellation_reason: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/setup_intents/{id}/cancel", data={"cancellation_reason": cancellation_reason})

@mcp.tool()
def list_setup_intents(customer: Optional[str] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/setup_intents", params={"customer": customer, "limit": limit})

# Coupons
@mcp.tool()
def create_coupon(duration: str, amount_off: Optional[int] = None, currency: Optional[str] = None, percent_off: Optional[float] = None, name: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", "/coupons", data={"duration": duration, "amount_off": amount_off, "currency": currency, "percent_off": percent_off, "name": name})

@mcp.tool()
def retrieve_coupon(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/coupons/{id}")

@mcp.tool()
def update_coupon(id: str, name: Optional[str] = None) -> Dict[str, Any]:
    return make_request("POST", f"/coupons/{id}", data={"name": name})

@mcp.tool()
def delete_coupon(id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/coupons/{id}")

@mcp.tool()
def list_coupons(limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/coupons", params={"limit": limit})

# Promotion Codes
@mcp.tool()
def create_promotion_code(coupon: str, code: Optional[str] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", "/promotion_codes", data={"coupon": coupon, "code": code, "active": active})

@mcp.tool()
def retrieve_promotion_code(id: str) -> Dict[str, Any]:
    return make_request("GET", f"/promotion_codes/{id}")

@mcp.tool()
def update_promotion_code(id: str, active: Optional[bool] = None) -> Dict[str, Any]:
    return make_request("POST", f"/promotion_codes/{id}", data={"active": active})

@mcp.tool()
def list_promotion_codes(coupon: Optional[str] = None, active: Optional[bool] = None, limit: Optional[int] = 10) -> Dict[str, Any]:
    return make_request("GET", "/promotion_codes", params={"coupon": coupon, "active": active, "limit": limit})

if __name__ == "__main__":
    mcp.run()
