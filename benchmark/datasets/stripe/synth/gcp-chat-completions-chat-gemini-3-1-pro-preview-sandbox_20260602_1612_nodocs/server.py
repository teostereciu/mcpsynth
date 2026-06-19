import os
import requests
from fastmcp import FastMCP
from typing import Optional, Dict, Any, List

mcp = FastMCP("Stripe")

def flatten_dict(d: Dict[str, Any], parent_key: str = '') -> Dict[str, Any]:
    items = []
    if d is None:
        return {}
    for k, v in d.items():
        if v is None:
            continue
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

def make_request(method: str, path: str, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    api_key = os.environ.get("STRIPE_API_KEY")
    if not api_key:
        return {"error": "STRIPE_API_KEY environment variable is not set"}
    
    url = f"https://api.stripe.com/v1{path}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    flat_data = flatten_dict(data) if data else None
    
    try:
        response = requests.request(method, url, headers=headers, data=flat_data, params=params)
        if response.status_code == 204:
            return {"success": True}
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# --- Customers ---

@mcp.tool()
def create_customer(email: Optional[str] = None, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe customer."""
    data = {"email": email, "name": name, "description": description, "metadata": metadata}
    return make_request("POST", "/customers", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_customer(customer_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe customer by ID."""
    return make_request("GET", f"/customers/{customer_id}")

@mcp.tool()
def update_customer(customer_id: str, email: Optional[str] = None, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe customer."""
    data = {"email": email, "name": name, "description": description, "metadata": metadata}
    return make_request("POST", f"/customers/{customer_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def delete_customer(customer_id: str) -> Dict[str, Any]:
    """Delete a Stripe customer."""
    return make_request("DELETE", f"/customers/{customer_id}")

@mcp.tool()
def list_customers(limit: Optional[int] = 10, email: Optional[str] = None) -> Dict[str, Any]:
    """List Stripe customers."""
    params = {"limit": limit}
    if email:
        params["email"] = email
    return make_request("GET", "/customers", params=params)

# --- Products ---

@mcp.tool()
def create_product(name: str, description: Optional[str] = None, active: Optional[bool] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe product."""
    data = {"name": name, "description": description, "active": active, "metadata": metadata}
    return make_request("POST", "/products", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_product(product_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe product by ID."""
    return make_request("GET", f"/products/{product_id}")

@mcp.tool()
def update_product(product_id: str, name: Optional[str] = None, description: Optional[str] = None, active: Optional[bool] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe product."""
    data = {"name": name, "description": description, "active": active, "metadata": metadata}
    return make_request("POST", f"/products/{product_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def delete_product(product_id: str) -> Dict[str, Any]:
    """Delete a Stripe product."""
    return make_request("DELETE", f"/products/{product_id}")

@mcp.tool()
def list_products(limit: Optional[int] = 10, active: Optional[bool] = None) -> Dict[str, Any]:
    """List Stripe products."""
    params = {"limit": limit}
    if active is not None:
        params["active"] = str(active).lower()
    return make_request("GET", "/products", params=params)

# --- Prices ---

@mcp.tool()
def create_price(product: str, currency: str, unit_amount: Optional[int] = None, recurring: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe price."""
    data = {"product": product, "currency": currency, "unit_amount": unit_amount, "recurring": recurring, "metadata": metadata}
    return make_request("POST", "/prices", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_price(price_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe price by ID."""
    return make_request("GET", f"/prices/{price_id}")

@mcp.tool()
def update_price(price_id: str, active: Optional[bool] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe price."""
    data = {"active": active, "metadata": metadata}
    return make_request("POST", f"/prices/{price_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def list_prices(limit: Optional[int] = 10, product: Optional[str] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    """List Stripe prices."""
    params = {"limit": limit}
    if product:
        params["product"] = product
    if active is not None:
        params["active"] = str(active).lower()
    return make_request("GET", "/prices", params=params)

# --- Payment Intents ---

@mcp.tool()
def create_payment_intent(amount: int, currency: str, customer: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe payment intent."""
    data = {"amount": amount, "currency": currency, "customer": customer, "description": description, "metadata": metadata}
    return make_request("POST", "/payment_intents", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_payment_intent(intent_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe payment intent by ID."""
    return make_request("GET", f"/payment_intents/{intent_id}")

@mcp.tool()
def update_payment_intent(intent_id: str, amount: Optional[int] = None, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe payment intent."""
    data = {"amount": amount, "description": description, "metadata": metadata}
    return make_request("POST", f"/payment_intents/{intent_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def cancel_payment_intent(intent_id: str) -> Dict[str, Any]:
    """Cancel a Stripe payment intent."""
    return make_request("POST", f"/payment_intents/{intent_id}/cancel")

@mcp.tool()
def capture_payment_intent(intent_id: str) -> Dict[str, Any]:
    """Capture a Stripe payment intent."""
    return make_request("POST", f"/payment_intents/{intent_id}/capture")

@mcp.tool()
def list_payment_intents(limit: Optional[int] = 10, customer: Optional[str] = None) -> Dict[str, Any]:
    """List Stripe payment intents."""
    params = {"limit": limit}
    if customer:
        params["customer"] = customer
    return make_request("GET", "/payment_intents", params=params)

# --- Subscriptions ---

@mcp.tool()
def create_subscription(customer: str, items: List[Dict[str, Any]], metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe subscription."""
    data = {"customer": customer, "items": items, "metadata": metadata}
    return make_request("POST", "/subscriptions", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe subscription by ID."""
    return make_request("GET", f"/subscriptions/{subscription_id}")

@mcp.tool()
def update_subscription(subscription_id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe subscription."""
    data = {"metadata": metadata}
    return make_request("POST", f"/subscriptions/{subscription_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def cancel_subscription(subscription_id: str) -> Dict[str, Any]:
    """Cancel a Stripe subscription."""
    return make_request("DELETE", f"/subscriptions/{subscription_id}")

@mcp.tool()
def list_subscriptions(limit: Optional[int] = 10, customer: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
    """List Stripe subscriptions."""
    params = {"limit": limit}
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    return make_request("GET", "/subscriptions", params=params)

# --- Invoices ---

@mcp.tool()
def create_invoice(customer: str, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe invoice."""
    data = {"customer": customer, "description": description, "metadata": metadata}
    return make_request("POST", "/invoices", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_invoice(invoice_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe invoice by ID."""
    return make_request("GET", f"/invoices/{invoice_id}")

@mcp.tool()
def update_invoice(invoice_id: str, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe invoice."""
    data = {"description": description, "metadata": metadata}
    return make_request("POST", f"/invoices/{invoice_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def delete_invoice(invoice_id: str) -> Dict[str, Any]:
    """Delete a Stripe invoice."""
    return make_request("DELETE", f"/invoices/{invoice_id}")

@mcp.tool()
def finalize_invoice(invoice_id: str) -> Dict[str, Any]:
    """Finalize a Stripe invoice."""
    return make_request("POST", f"/invoices/{invoice_id}/finalize")

@mcp.tool()
def pay_invoice(invoice_id: str) -> Dict[str, Any]:
    """Pay a Stripe invoice."""
    return make_request("POST", f"/invoices/{invoice_id}/pay")

@mcp.tool()
def list_invoices(limit: Optional[int] = 10, customer: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
    """List Stripe invoices."""
    params = {"limit": limit}
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    return make_request("GET", "/invoices", params=params)

# --- Checkout Sessions ---

@mcp.tool()
def create_checkout_session(success_url: str, cancel_url: Optional[str] = None, line_items: Optional[List[Dict[str, Any]]] = None, mode: Optional[str] = "payment", customer: Optional[str] = None) -> Dict[str, Any]:
    """Create a new Stripe checkout session."""
    data = {"success_url": success_url, "cancel_url": cancel_url, "line_items": line_items, "mode": mode, "customer": customer}
    return make_request("POST", "/checkout/sessions", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_checkout_session(session_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe checkout session by ID."""
    return make_request("GET", f"/checkout/sessions/{session_id}")

@mcp.tool()
def list_checkout_sessions(limit: Optional[int] = 10, customer: Optional[str] = None) -> Dict[str, Any]:
    """List Stripe checkout sessions."""
    params = {"limit": limit}
    if customer:
        params["customer"] = customer
    return make_request("GET", "/checkout/sessions", params=params)

# --- Payment Links ---

@mcp.tool()
def create_payment_link(line_items: List[Dict[str, Any]], metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe payment link."""
    data = {"line_items": line_items, "metadata": metadata}
    return make_request("POST", "/payment_links", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_payment_link(payment_link_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe payment link by ID."""
    return make_request("GET", f"/payment_links/{payment_link_id}")

@mcp.tool()
def update_payment_link(payment_link_id: str, active: Optional[bool] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe payment link."""
    data = {"active": active, "metadata": metadata}
    return make_request("POST", f"/payment_links/{payment_link_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def list_payment_links(limit: Optional[int] = 10, active: Optional[bool] = None) -> Dict[str, Any]:
    """List Stripe payment links."""
    params = {"limit": limit}
    if active is not None:
        params["active"] = str(active).lower()
    return make_request("GET", "/payment_links", params=params)

# --- Refunds ---

@mcp.tool()
def create_refund(payment_intent: Optional[str] = None, charge: Optional[str] = None, amount: Optional[int] = None, reason: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe refund."""
    data = {"payment_intent": payment_intent, "charge": charge, "amount": amount, "reason": reason, "metadata": metadata}
    return make_request("POST", "/refunds", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_refund(refund_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe refund by ID."""
    return make_request("GET", f"/refunds/{refund_id}")

@mcp.tool()
def update_refund(refund_id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe refund."""
    data = {"metadata": metadata}
    return make_request("POST", f"/refunds/{refund_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def list_refunds(limit: Optional[int] = 10, payment_intent: Optional[str] = None, charge: Optional[str] = None) -> Dict[str, Any]:
    """List Stripe refunds."""
    params = {"limit": limit}
    if payment_intent:
        params["payment_intent"] = payment_intent
    if charge:
        params["charge"] = charge
    return make_request("GET", "/refunds", params=params)

# --- Charges ---

@mcp.tool()
def get_charge(charge_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe charge by ID."""
    return make_request("GET", f"/charges/{charge_id}")

@mcp.tool()
def update_charge(charge_id: str, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe charge."""
    data = {"description": description, "metadata": metadata}
    return make_request("POST", f"/charges/{charge_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def list_charges(limit: Optional[int] = 10, customer: Optional[str] = None) -> Dict[str, Any]:
    """List Stripe charges."""
    params = {"limit": limit}
    if customer:
        params["customer"] = customer
    return make_request("GET", "/charges", params=params)

# --- Connect (Accounts) ---

@mcp.tool()
def create_account(type: str, country: Optional[str] = None, email: Optional[str] = None) -> Dict[str, Any]:
    """Create a new Stripe Connect account."""
    data = {"type": type, "country": country, "email": email}
    return make_request("POST", "/accounts", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_account(account_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe Connect account by ID."""
    return make_request("GET", f"/accounts/{account_id}")

@mcp.tool()
def update_account(account_id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe Connect account."""
    data = {"metadata": metadata}
    return make_request("POST", f"/accounts/{account_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def delete_account(account_id: str) -> Dict[str, Any]:
    """Delete a Stripe Connect account."""
    return make_request("DELETE", f"/accounts/{account_id}")

@mcp.tool()
def list_accounts(limit: Optional[int] = 10) -> Dict[str, Any]:
    """List Stripe Connect accounts."""
    params = {"limit": limit}
    return make_request("GET", "/accounts", params=params)

# --- Transfers ---

@mcp.tool()
def create_transfer(amount: int, currency: str, destination: str, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe transfer."""
    data = {"amount": amount, "currency": currency, "destination": destination, "description": description, "metadata": metadata}
    return make_request("POST", "/transfers", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_transfer(transfer_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe transfer by ID."""
    return make_request("GET", f"/transfers/{transfer_id}")

@mcp.tool()
def update_transfer(transfer_id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe transfer."""
    data = {"metadata": metadata}
    return make_request("POST", f"/transfers/{transfer_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def list_transfers(limit: Optional[int] = 10, destination: Optional[str] = None) -> Dict[str, Any]:
    """List Stripe transfers."""
    params = {"limit": limit}
    if destination:
        params["destination"] = destination
    return make_request("GET", "/transfers", params=params)

# --- Payouts ---

@mcp.tool()
def create_payout(amount: int, currency: str, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe payout."""
    data = {"amount": amount, "currency": currency, "description": description, "metadata": metadata}
    return make_request("POST", "/payouts", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_payout(payout_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe payout by ID."""
    return make_request("GET", f"/payouts/{payout_id}")

@mcp.tool()
def update_payout(payout_id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe payout."""
    data = {"metadata": metadata}
    return make_request("POST", f"/payouts/{payout_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def list_payouts(limit: Optional[int] = 10) -> Dict[str, Any]:
    """List Stripe payouts."""
    params = {"limit": limit}
    return make_request("GET", "/payouts", params=params)

# --- Setup Intents ---

@mcp.tool()
def create_setup_intent(customer: Optional[str] = None, payment_method_types: Optional[List[str]] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe setup intent."""
    data = {"customer": customer, "payment_method_types": payment_method_types, "metadata": metadata}
    return make_request("POST", "/setup_intents", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_setup_intent(intent_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe setup intent by ID."""
    return make_request("GET", f"/setup_intents/{intent_id}")

@mcp.tool()
def update_setup_intent(intent_id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe setup intent."""
    data = {"metadata": metadata}
    return make_request("POST", f"/setup_intents/{intent_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def cancel_setup_intent(intent_id: str) -> Dict[str, Any]:
    """Cancel a Stripe setup intent."""
    return make_request("POST", f"/setup_intents/{intent_id}/cancel")

@mcp.tool()
def list_setup_intents(limit: Optional[int] = 10, customer: Optional[str] = None) -> Dict[str, Any]:
    """List Stripe setup intents."""
    params = {"limit": limit}
    if customer:
        params["customer"] = customer
    return make_request("GET", "/setup_intents", params=params)

# --- Coupons ---

@mcp.tool()
def create_coupon(duration: str, amount_off: Optional[int] = None, currency: Optional[str] = None, percent_off: Optional[float] = None, name: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe coupon."""
    data = {"duration": duration, "amount_off": amount_off, "currency": currency, "percent_off": percent_off, "name": name, "metadata": metadata}
    return make_request("POST", "/coupons", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_coupon(coupon_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe coupon by ID."""
    return make_request("GET", f"/coupons/{coupon_id}")

@mcp.tool()
def update_coupon(coupon_id: str, name: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe coupon."""
    data = {"name": name, "metadata": metadata}
    return make_request("POST", f"/coupons/{coupon_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def delete_coupon(coupon_id: str) -> Dict[str, Any]:
    """Delete a Stripe coupon."""
    return make_request("DELETE", f"/coupons/{coupon_id}")

@mcp.tool()
def list_coupons(limit: Optional[int] = 10) -> Dict[str, Any]:
    """List Stripe coupons."""
    params = {"limit": limit}
    return make_request("GET", "/coupons", params=params)

# --- Promotion Codes ---

@mcp.tool()
def create_promotion_code(coupon: str, code: Optional[str] = None, active: Optional[bool] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Create a new Stripe promotion code."""
    data = {"coupon": coupon, "code": code, "active": active, "metadata": metadata}
    return make_request("POST", "/promotion_codes", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def get_promotion_code(promotion_code_id: str) -> Dict[str, Any]:
    """Retrieve a Stripe promotion code by ID."""
    return make_request("GET", f"/promotion_codes/{promotion_code_id}")

@mcp.tool()
def update_promotion_code(promotion_code_id: str, active: Optional[bool] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a Stripe promotion code."""
    data = {"active": active, "metadata": metadata}
    return make_request("POST", f"/promotion_codes/{promotion_code_id}", data={k: v for k, v in data.items() if v is not None})

@mcp.tool()
def list_promotion_codes(limit: Optional[int] = 10, coupon: Optional[str] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    """List Stripe promotion codes."""
    params = {"limit": limit}
    if coupon:
        params["coupon"] = coupon
    if active is not None:
        params["active"] = str(active).lower()
    return make_request("GET", "/promotion_codes", params=params)

if __name__ == "__main__":
    mcp.run()
