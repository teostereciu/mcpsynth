import os
import requests
from fastmcp import tool

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

@tool("create_subscription")
def create_subscription(customer: str, items: list, automatic_tax: dict = None, currency: str = None, customer_account: str = None, default_payment_method: str = None, description: str = None, metadata: dict = None, payment_behavior: str = None, add_invoice_items: list = None, application_fee_percent: float = None, backdate_start_date: int = None, billing_cycle_anchor: int = None, billing_cycle_anchor_config: dict = None, billing_mode: dict = None, billing_thresholds: dict = None, cancel_at: str = None, cancel_at_period_end: bool = None, collection_method: str = None, days_until_due: int = None, default_source: str = None, default_tax_rates: list = None, discounts: list = None, invoice_settings: dict = None, off_session: bool = None, on_behalf_of: str = None, payment_settings: dict = None, pending_invoice_item_interval: dict = None, proration_behavior: str = None, transfer_data: dict = None, trial_end: str = None, trial_from_plan: bool = None, trial_period_days: int = None, trial_settings: dict = None):
    """
    Create a Subscription object.
    """
    data = {
        "customer": customer,
    }
    if items:
        for i, item in enumerate(items):
            for k, v in item.items():
                data[f"items[{i}][{k}]"] = v
    if automatic_tax:
        for k, v in automatic_tax.items():
            data[f"automatic_tax[{k}]"] = v
    if currency:
        data["currency"] = currency
    if customer_account:
        data["customer_account"] = customer_account
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if payment_behavior:
        data["payment_behavior"] = payment_behavior
    if add_invoice_items:
        for i, item in enumerate(add_invoice_items):
            for k, v in item.items():
                data[f"add_invoice_items[{i}][{k}]"] = v
    if application_fee_percent is not None:
        data["application_fee_percent"] = application_fee_percent
    if backdate_start_date:
        data["backdate_start_date"] = backdate_start_date
    if billing_cycle_anchor:
        data["billing_cycle_anchor"] = billing_cycle_anchor
    if billing_cycle_anchor_config:
        for k, v in billing_cycle_anchor_config.items():
            data[f"billing_cycle_anchor_config[{k}]"] = v
    if billing_mode:
        for k, v in billing_mode.items():
            data[f"billing_mode[{k}]"] = v
    if billing_thresholds:
        for k, v in billing_thresholds.items():
            data[f"billing_thresholds[{k}]"] = v
    if cancel_at:
        data["cancel_at"] = cancel_at
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = "true" if cancel_at_period_end else "false"
    if collection_method:
        data["collection_method"] = collection_method
    if days_until_due:
        data["days_until_due"] = days_until_due
    if default_source:
        data["default_source"] = default_source
    if default_tax_rates:
        for i, rate in enumerate(default_tax_rates):
            data[f"default_tax_rates[{i}]"] = rate
    if discounts:
        for i, discount in enumerate(discounts):
            for k, v in discount.items():
                data[f"discounts[{i}][{k}]"] = v
    if invoice_settings:
        for k, v in invoice_settings.items():
            data[f"invoice_settings[{k}]"] = v
    if off_session is not None:
        data["off_session"] = "true" if off_session else "false"
    if on_behalf_of:
        data["on_behalf_of"] = on_behalf_of
    if payment_settings:
        for k, v in payment_settings.items():
            data[f"payment_settings[{k}]"] = v
    if pending_invoice_item_interval:
        for k, v in pending_invoice_item_interval.items():
            data[f"pending_invoice_item_interval[{k}]"] = v
    if proration_behavior:
        data["proration_behavior"] = proration_behavior
    if transfer_data:
        for k, v in transfer_data.items():
            data[f"transfer_data[{k}]"] = v
    if trial_end:
        data["trial_end"] = trial_end
    if trial_from_plan is not None:
        data["trial_from_plan"] = "true" if trial_from_plan else "false"
    if trial_period_days:
        data["trial_period_days"] = trial_period_days
    if trial_settings:
        for k, v in trial_settings.items():
            data[f"trial_settings[{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/subscriptions", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("retrieve_subscription")
def retrieve_subscription(subscription_id: str):
    """
    Retrieve a Subscription object.
    """
    try:
        resp = requests.get(f"{BASE_URL}/subscriptions/{subscription_id}", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("update_subscription")
def update_subscription(subscription_id: str, metadata: dict = None, description: str = None, default_payment_method: str = None, invoice_settings: dict = None, items: list = None):
    """
    Update a Subscription object.
    """
    data = {}
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if description:
        data["description"] = description
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if invoice_settings:
        for k, v in invoice_settings.items():
            data[f"invoice_settings[{k}]"] = v
    if items:
        for i, item in enumerate(items):
            for k, v in item.items():
                data[f"items[{i}][{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/subscriptions/{subscription_id}", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}
