"""Shopify Admin REST API — Shop, Collects, Gift Cards, Fulfillment Requests tools."""
import os, requests
from typing import Optional, Any

BASE_URL = f"https://{os.environ.get('SHOPIFY_STORE_URL', '')}/admin/api/2026-01"

def _headers():
    return {
        "X-Shopify-Access-Token": os.environ.get("SHOPIFY_ACCESS_TOKEN", ""),
        "Content-Type": "application/json",
    }

def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _post(path, payload):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=payload, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, payload):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=payload, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _delete(path):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=_headers(), timeout=30)
        if r.status_code == 200:
            return r.json()
        return {"status": r.status_code}
    except Exception as e:
        return {"error": str(e)}


# ── Shop ──────────────────────────────────────────────────────────────────────

def get_shop(fields: Optional[str] = None) -> dict:
    """Retrieve the shop's configuration and settings."""
    params: dict[str, Any] = {}
    if fields: params["fields"] = fields
    return _get("/shop.json", params)


# ── Collects ──────────────────────────────────────────────────────────────────

def list_collects(collection_id: Optional[int] = None,
                  product_id: Optional[int] = None,
                  limit: int = 50) -> dict:
    """Retrieve a list of collects (product-collection links)."""
    params: dict[str, Any] = {"limit": limit}
    if collection_id: params["collection_id"] = collection_id
    if product_id: params["product_id"] = product_id
    return _get("/collects.json", params)

def count_collects(collection_id: Optional[int] = None,
                   product_id: Optional[int] = None) -> dict:
    """Retrieve a count of collects."""
    params: dict[str, Any] = {}
    if collection_id: params["collection_id"] = collection_id
    if product_id: params["product_id"] = product_id
    return _get("/collects/count.json", params)

def create_collect(product_id: int, collection_id: int) -> dict:
    """Add a product to a custom collection."""
    return _post("/collects.json", {
        "collect": {"product_id": product_id, "collection_id": collection_id}
    })

def delete_collect(collect_id: int) -> dict:
    """Remove a product from a collection (delete a collect)."""
    return _delete(f"/collects/{collect_id}.json")


# ── Gift Cards ────────────────────────────────────────────────────────────────

def list_gift_cards(status: Optional[str] = None, limit: int = 50) -> dict:
    """Retrieve a list of gift cards. status: enabled|disabled."""
    params: dict[str, Any] = {"limit": limit}
    if status: params["status"] = status
    return _get("/gift_cards.json", params)

def get_gift_card(gift_card_id: int) -> dict:
    """Retrieve a single gift card."""
    return _get(f"/gift_cards/{gift_card_id}.json")

def count_gift_cards(status: Optional[str] = None) -> dict:
    """Retrieve a count of gift cards."""
    params: dict[str, Any] = {}
    if status: params["status"] = status
    return _get("/gift_cards/count.json", params)

def search_gift_cards(query: str, limit: int = 50) -> dict:
    """Search for gift cards (e.g. query='last_characters:mnop')."""
    return _get("/gift_cards/search.json", {"query": query, "limit": limit})

def create_gift_card(initial_value: str, code: Optional[str] = None,
                     note: Optional[str] = None, expires_on: Optional[str] = None,
                     customer_id: Optional[int] = None,
                     template_suffix: Optional[str] = None) -> dict:
    """Create a gift card. initial_value is required (e.g. '25.00')."""
    gift_card: dict[str, Any] = {"initial_value": initial_value}
    if code: gift_card["code"] = code
    if note: gift_card["note"] = note
    if expires_on: gift_card["expires_on"] = expires_on
    if customer_id: gift_card["customer_id"] = customer_id
    if template_suffix: gift_card["template_suffix"] = template_suffix
    return _post("/gift_cards.json", {"gift_card": gift_card})

def update_gift_card(gift_card_id: int, note: Optional[str] = None,
                     expires_on: Optional[str] = None,
                     template_suffix: Optional[str] = None) -> dict:
    """Update an existing gift card (only note, expires_on, template_suffix can be changed)."""
    gift_card: dict[str, Any] = {"id": gift_card_id}
    if note is not None: gift_card["note"] = note
    if expires_on is not None: gift_card["expires_on"] = expires_on
    if template_suffix is not None: gift_card["template_suffix"] = template_suffix
    return _put(f"/gift_cards/{gift_card_id}.json", {"gift_card": gift_card})

def disable_gift_card(gift_card_id: int) -> dict:
    """Disable a gift card (this action cannot be undone)."""
    return _post(f"/gift_cards/{gift_card_id}/disable.json",
                 {"gift_card": {"id": gift_card_id}})


# ── Fulfillment Requests ──────────────────────────────────────────────────────

def send_fulfillment_request(fulfillment_order_id: int,
                             message: Optional[str] = None,
                             notify_customer: bool = False,
                             fulfillment_order_line_items: Optional[list] = None) -> dict:
    """Send a fulfillment request to the fulfillment service of a fulfillment order."""
    req: dict[str, Any] = {"notify_customer": notify_customer}
    if message: req["message"] = message
    if fulfillment_order_line_items: req["fulfillment_order_line_items"] = fulfillment_order_line_items
    return _post(f"/fulfillment_orders/{fulfillment_order_id}/fulfillment_request.json",
                 {"fulfillment_request": req})

def accept_fulfillment_request(fulfillment_order_id: int,
                               message: Optional[str] = None) -> dict:
    """Accept a fulfillment request (for fulfillment service apps)."""
    req: dict[str, Any] = {}
    if message: req["message"] = message
    return _post(f"/fulfillment_orders/{fulfillment_order_id}/fulfillment_request/accept.json",
                 {"fulfillment_request": req})

def reject_fulfillment_request(fulfillment_order_id: int,
                               message: Optional[str] = None) -> dict:
    """Reject a fulfillment request (for fulfillment service apps)."""
    req: dict[str, Any] = {}
    if message: req["message"] = message
    return _post(f"/fulfillment_orders/{fulfillment_order_id}/fulfillment_request/reject.json",
                 {"fulfillment_request": req})
