"""
Stripe Disputes tools.
"""
import os
import requests

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"


def _auth():
    return (STRIPE_API_KEY, "")


def _handle(resp: requests.Response) -> dict:
    try:
        return resp.json()
    except Exception:
        return {"error": resp.text}


def get_dispute(dispute_id: str) -> dict:
    """Retrieve a Dispute by ID."""
    resp = requests.get(f"{BASE_URL}/disputes/{dispute_id}", auth=_auth())
    return _handle(resp)


def update_dispute(
    dispute_id: str,
    evidence_customer_email_address: str = None,
    evidence_customer_name: str = None,
    evidence_product_description: str = None,
    evidence_uncategorized_text: str = None,
    evidence_customer_purchase_ip: str = None,
    evidence_billing_address: str = None,
    evidence_customer_signature: str = None,
    evidence_receipt: str = None,
    evidence_refund_policy: str = None,
    evidence_service_documentation: str = None,
    evidence_shipping_documentation: str = None,
    submit: bool = None,
    metadata: dict = None,
) -> dict:
    """Update a Dispute with evidence."""
    data = {}
    if evidence_customer_email_address:
        data["evidence[customer_email_address]"] = evidence_customer_email_address
    if evidence_customer_name:
        data["evidence[customer_name]"] = evidence_customer_name
    if evidence_product_description:
        data["evidence[product_description]"] = evidence_product_description
    if evidence_uncategorized_text:
        data["evidence[uncategorized_text]"] = evidence_uncategorized_text
    if evidence_customer_purchase_ip:
        data["evidence[customer_purchase_ip]"] = evidence_customer_purchase_ip
    if evidence_billing_address:
        data["evidence[billing_address]"] = evidence_billing_address
    if evidence_customer_signature:
        data["evidence[customer_signature]"] = evidence_customer_signature
    if evidence_receipt:
        data["evidence[receipt]"] = evidence_receipt
    if evidence_refund_policy:
        data["evidence[refund_policy]"] = evidence_refund_policy
    if evidence_service_documentation:
        data["evidence[service_documentation]"] = evidence_service_documentation
    if evidence_shipping_documentation:
        data["evidence[shipping_documentation]"] = evidence_shipping_documentation
    if submit is not None:
        data["submit"] = str(submit).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/disputes/{dispute_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def close_dispute(dispute_id: str) -> dict:
    """Close a Dispute (accept it)."""
    resp = requests.post(
        f"{BASE_URL}/disputes/{dispute_id}/close", data={}, auth=_auth()
    )
    return _handle(resp)


def list_disputes(
    charge: str = None,
    payment_intent: str = None,
    status: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
) -> dict:
    """List Disputes."""
    params = {}
    if charge:
        params["charge"] = charge
    if payment_intent:
        params["payment_intent"] = payment_intent
    if status:
        params["status"] = status
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if created_gte is not None:
        params["created[gte]"] = created_gte
    if created_lte is not None:
        params["created[lte]"] = created_lte
    resp = requests.get(f"{BASE_URL}/disputes", params=params, auth=_auth())
    return _handle(resp)
