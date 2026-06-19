import os
import requests
from fastmcp import tool

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

@tool("retrieve_invoice")
def retrieve_invoice(invoice_id: str):
    """
    Retrieve an Invoice object.
    """
    try:
        resp = requests.get(f"{BASE_URL}/invoices/{invoice_id}", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("create_invoice_preview")
def create_invoice_preview(customer: str = None, customer_account: str = None, subscription: str = None, automatic_tax: dict = None, currency: str = None, customer_details: dict = None, discounts: list = None, invoice_items: list = None, issuer: dict = None, on_behalf_of: str = None, preview_mode: str = None, schedule: str = None, schedule_details: dict = None, subscription_details: dict = None):
    """
    Create a preview invoice for a customer or subscription.
    """
    data = {}
    if customer:
        data["customer"] = customer
    if customer_account:
        data["customer_account"] = customer_account
    if subscription:
        data["subscription"] = subscription
    if automatic_tax:
        for k, v in automatic_tax.items():
            data[f"automatic_tax[{k}]"] = v
    if currency:
        data["currency"] = currency
    if customer_details:
        for k, v in customer_details.items():
            data[f"customer_details[{k}]"] = v
    if discounts:
        for i, discount in enumerate(discounts):
            for k, v in discount.items():
                data[f"discounts[{i}][{k}]"] = v
    if invoice_items:
        for i, item in enumerate(invoice_items):
            for k, v in item.items():
                data[f"invoice_items[{i}][{k}]"] = v
    if issuer:
        for k, v in issuer.items():
            data[f"issuer[{k}]"] = v
    if on_behalf_of:
        data["on_behalf_of"] = on_behalf_of
    if preview_mode:
        data["preview_mode"] = preview_mode
    if schedule:
        data["schedule"] = schedule
    if schedule_details:
        for k, v in schedule_details.items():
            data[f"schedule_details[{k}]"] = v
    if subscription_details:
        for k, v in subscription_details.items():
            data[f"subscription_details[{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/invoices/create_preview", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}
