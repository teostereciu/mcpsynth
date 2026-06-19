#!/usr/bin/env python3
"""
eBay Buy API MCP Server

This server provides access to eBay Buy API operations through MCP (Model Context Protocol).
It supports operations across Browse, Deal, Feed, Marketing, Offer, and Order namespaces.
"""

import os
import base64
import json
from typing import Any
import requests

from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("ebay-buy")

# Configuration
EBAY_APP_ID = os.environ.get("EBAY_APP_ID")
EBAY_CERT_ID = os.environ.get("EBAY_CERT_ID")
EBAY_ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs based on environment
BASE_URLS = {
    "SANDBOX": {
        "browse": "https://api.sandbox.ebay.com/buy/browse/v1",
        "deal": "https://api.sandbox.ebay.com/buy/deal/v1",
        "feed": "https://api.sandbox.ebay.com/buy/feed/v1",
        "marketing": "https://api.sandbox.ebay.com/buy/marketing/v1_beta",
        "offer": "https://api.sandbox.ebay.com/buy/offer/v1_beta",
        "order": "https://apix.sandbox.ebay.com/buy/order/v2",
    },
    "PRODUCTION": {
        "browse": "https://api.ebay.com/buy/browse/v1",
        "deal": "https://api.ebay.com/buy/deal/v1",
        "feed": "https://api.ebay.com/buy/feed/v1",
        "marketing": "https://api.ebay.com/buy/marketing/v1_beta",
        "offer": "https://api.ebay.com/buy/offer/v1_beta",
        "order": "https://apix.ebay.com/buy/order/v2",
    },
}

MARKETPLACE_IDS = {
    "US": "EBAY_US",
    "GB": "EBAY_GB",
    "CA": "EBAY_CA",
    "DE": "EBAY_DE",
    "FR": "EBAY_FR",
    "IT": "EBAY_IT",
    "ES": "EBAY_ES",
    "AU": "EBAY_AU",
    "IN": "EBAY_IN",
    "HK": "EBAY_HK",
    "MY": "EBAY_MY",
    "PH": "EBAY_PH",
    "PL": "EBAY_PL",
    "SG": "EBAY_SG",
}

def get_base_url(namespace: str) -> str:
    """Get the base URL for a given API namespace."""
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return BASE_URLS[env].get(namespace, BASE_URLS["SANDBOX"][namespace])

def get_marketplace_id() -> str:
    """Get the marketplace ID from environment or default to US."""
    return os.environ.get("EBAY_MARKETPLACE_ID", "EBAY_US")

def get_auth_headers() -> dict:
    """Get authentication headers using OAuth 2.0 Client Credentials."""
    if not EBAY_APP_ID or not EBAY_CERT_ID:
        raise ValueError("EBAY_APP_ID and EBAY_CERT_ID environment variables must be set")
    
    # For Client Credentials flow, we need to get an access token first
    # In production, you'd cache this token
    token_url = "https://api.ebay.com/oauth/api_scope"
    
    auth = requests.auth.HTTPBasicAuth(EBAY_APP_ID, EBAY_CERT_ID)
    response = requests.post(
        "https://api.ebay.com/oauth/api_scope",
        auth=auth,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"grant_type": "client_credentials", "scope": "https://api.ebay.com/oauth/api_scope"}
    )
    
    if response.status_code != 200:
        raise ValueError(f"Failed to get OAuth token: {response.text}")
    
    access_token = response.json().get("access_token", "")
    
    return {
        "Authorization": f"Bearer {access_token}",
        "X-EBAY-C-MARKETPLACE-ID": get_marketplace_id(),
    }

def make_request(
    method: str,
    endpoint: str,
    params: dict | None = None,
    payload: dict | None = None,
    headers: dict | None = None,
) -> dict:
    """Make an API request and return the response as a dictionary."""
    try:
        full_url = endpoint if endpoint.startswith("http") else endpoint
        request_headers = get_auth_headers()
        if headers:
            request_headers.update(headers)
        
        response = requests.request(
            method=method,
            url=full_url,
            params=params,
            json=payload,
            headers=request_headers,
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            try:
                return response.json()
            except json.JSONDecodeError:
                return {"raw_response": response.text}
        else:
            try:
                error_data = response.json()
                return {"error": error_data}
            except json.JSONDecodeError:
                return {"error": response.text}
                
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Browse API - Item Operations
@mcp.tool()
def get_item(item_id: str, fieldgroups: str | None = None) -> dict:
    """
    Retrieve the details of a specific item.
    
    Args:
        item_id: The unique RESTful identifier of the item (e.g., v1|2**********6|5**********4)
        fieldgroups: Optional field groups to include (COMPACT, PRODUCT, ADDITIONAL_SELLER_DETAILS, CHARITY_DETAILS)
    
    Returns:
        Item details including price, condition, shipping options, etc.
    """
    endpoint = f"{get_base_url('browse')}/item/{item_id}"
    params = {}
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    
    return make_request("GET", endpoint, params=params)

@mcp.tool()
def get_items(item_ids: str | list[str], fieldgroups: str | None = None) -> dict:
    """
    Retrieve details about multiple items.
    
    Args:
        item_ids: A pipe-separated list of item IDs or a list of item IDs
        fieldgroups: Optional field groups to include
    
    Returns:
        A list of item details.
    """
    if isinstance(item_ids, list):
        item_ids = "|".join(item_ids)
    
    endpoint = f"{get_base_url('browse')}/items"
    params = {"item_id": item_ids}
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    
    return make_request("GET", endpoint, params=params)

@mcp.tool()
def get_item_by_legacy_id(legacy_id: str) -> dict:
    """
    Retrieve item details using a legacy item ID.
    
    Args:
        legacy_id: The traditional/legacy eBay item ID (e.g., 123456789012)
    
    Returns:
        Item details.
    """
    endpoint = f"{get_base_url('browse')}/item_by_legacy_id/{legacy_id}"
    return make_request("GET", endpoint)

@mcp.tool()
def get_items_by_item_group(item_group_id: str) -> dict:
    """
    Retrieve items that belong to an item group (variations).
    
    Args:
        item_group_id: The unique RESTful identifier of the item group
    
    Returns:
        Items in the group with variation details.
    """
    endpoint = f"{get_base_url('browse')}/item_group/{item_group_id}/item"
    return make_request("GET", endpoint)

@mcp.tool()
def search_items(
    q: str | None = None,
    category_ids: str | None = None,
    filter: str | None = None,
    sort: str | None = None,
    max_results: int | None = 20,
    offset: int | None = 0,
    fieldgroups: str | None = None,
    aspect_filter: str | None = None,
    compatibility_filter: str | None = None,
) -> dict:
    """
    Search for eBay items by various query parameters.
    
    Args:
        q: Keyword search query
        category_ids: Category ID(s) to search in
        filter: Filter expressions (e.g., price:[10 TO 100], condition:New)
        sort: Sort order (e.g., price+asc, bestmatch)
        max_results: Maximum number of results (default: 20, max: 100)
        offset: Pagination offset
        fieldgroups: Field groups to include
        aspect_filter: Filter by aspect name/value pairs
        compatibility_filter: Filter by compatibility attributes
    
    Returns:
        Search results with item summaries.
    """
    endpoint = f"{get_base_url('browse')}/item_summary/search"
    params = {
        "q": q or "",
        "max_results": str(max_results),
        "skip": str(offset),
    }
    if category_ids:
        params["category_ids"] = category_ids
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    if compatibility_filter:
        params["compatibility_filter"] = compatibility_filter
    
    return make_request("GET", endpoint, params=params)

@mcp.tool()
def search_items_by_image(
    image_data: str,
    max_results: int | None = 20,
    category_ids: str | None = None,
    filter: str | None = None,
) -> dict:
    """
    Search for eBay items based on an image.
    
    Args:
        image_data: Base64-encoded image data
        max_results: Maximum number of results (default: 20)
        category_ids: Category ID(s) to search in
        filter: Filter expressions
    
    Returns:
        Search results with item summaries.
    """
    endpoint = f"{get_base_url('browse')}/item_summary/search_by_image"
    params = {"max_results": str(max_results)}
    if category_ids:
        params["category_ids"] = category_ids
    if filter:
        params["filter"] = filter
    
    payload = {"image_data": image_data}
    
    return make_request("POST", endpoint, params=params, payload=payload)

@mcp.tool()
def check_compatibility(item_id: str, compatibility_properties: list[dict]) -> dict:
    """
    Check if a product is compatible with a specific item (for motor vehicles).
    
    Args:
        item_id: The item ID of the part/piece
        compatibility_properties: List of name/value pairs defining the product (e.g., [{"name": "Year", "value": "2019"}])
    
    Returns:
        Compatibility status (COMPATIBLE, NOT_COMPATIBLE, or UNDETERMINED)
    """
    endpoint = f"{get_base_url('browse')}/item/{item_id}/check_compatibility"
    
    payload = {
        "compatibilityProperties": [
            {"name": prop["name"], "value": prop["value"]}
            for prop in compatibility_properties
        ]
    }
    
    return make_request("POST", endpoint, payload=payload)

# Deal API Operations
@mcp.tool()
def get_deal_items(
    category_ids: str | None = None,
    commissionable: str | None = None,
    delivery_country: str | None = None,
    max_results: int | None = 20,
    offset: int | None = 0,
) -> dict:
    """
    Retrieve a paginated set of deal items.
    
    Args:
        category_ids: Category ID(s) to filter by
        commissionable: Filter by commissionable items (true/false)
        delivery_country: Filter by delivery country (2-digit ISO code)
        max_results: Maximum number of results (default: 20, max: 100)
        offset: Pagination offset
    
    Returns:
        Deal items with pricing and shipping information.
    """
    endpoint = f"{get_base_url('deal')}/deal_item"
    params = {
        "max_results": str(max_results),
        "skip": str(offset),
    }
    if category_ids:
        params["category_ids"] = category_ids
    if commissionable:
        params["commissionable"] = commissionable
    if delivery_country:
        params["delivery_country"] = delivery_country
    
    return make_request("GET", endpoint, params=params)

@mcp.tool()
def get_event_items(
    event_ids: str | list[str],
    category_ids: str | None = None,
    delivery_country: str | None = None,
    max_results: int | None = 20,
    offset: int | None = 0,
) -> dict:
    """
    Retrieve a paginated set of event items.
    
    Args:
        event_ids: Event ID(s) to filter by (max 1)
        category_ids: Category ID(s) to filter by
        delivery_country: Filter by delivery country
        max_results: Maximum number of results (default: 20)
        offset: Pagination offset
    
    Returns:
        Event items with pricing and shipping information.
    """
    if isinstance(event_ids, list):
        event_ids = "|".join(event_ids)
    
    endpoint = f"{get_base_url('deal')}/event_item"
    params = {
        "event_ids": event_ids,
        "max_results": str(max_results),
        "skip": str(offset),
    }
    if category_ids:
        params["category_ids"] = category_ids
    if delivery_country:
        params["delivery_country"] = delivery_country
    
    return make_request("GET", endpoint, params=params)

@mcp.tool()
def get_events(
    max_results: int | None = 20,
    offset: int | None = 0,
) -> dict:
    """
    Retrieve a paginated set of eBay events.
    
    Args:
        max_results: Maximum number of results (default: 20, max: 100)
        offset: Pagination offset
    
    Returns:
        Events with descriptions, dates, and coupon information.
    """
    endpoint = f"{get_base_url('deal')}/event"
    params = {
        "max_results": str(max_results),
        "skip": str(offset),
    }
    
    return make_request("GET", endpoint, params=params)

@mcp.tool()
def get_event(event_id: str) -> dict:
    """
    Retrieve details about a specific event.
    
    Args:
        event_id: The unique identifier of the event
    
    Returns:
        Event details including title, description, dates, and coupons.
    """
    endpoint = f"{get_base_url('deal')}/event/{event_id}"
    return make_request("GET", endpoint)

# Feed API Operations
@mcp.tool()
def get_item_feed(
    category_id: str,
    feed_scope: str = "NEWLY_LISTED",
) -> dict:
    """
    Download a TSV_GZIP item feed file for a specific category.
    
    Args:
        category_id: The category ID to download items for
        feed_scope: Feed scope - "NEWLY_LISTED" or "ALL_ACTIVE"
    
    Returns:
        Binary feed file content as base64 string (use with caution for large files)
    """
    endpoint = f"{get_base_url('feed')}/item"
    params = {
        "category_id": category_id,
        "feed_scope": feed_scope,
    }
    
    # For feeds, we need to stream the binary content
    try:
        full_url = endpoint
        request_headers = get_auth_headers()
        request_headers["Accept"] = "application/gzip"
        
        response = requests.get(
            url=full_url,
            params=params,
            headers=request_headers,
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            # Return as base64 for large binary content
            return {
                "feed_data_base64": base64.b64encode(response.content).decode("utf-8"),
                "content_length": len(response.content),
                "content_type": response.headers.get("Content-Type", "application/gzip"),
            }
        else:
            try:
                error_data = response.json()
                return {"error": error_data}
            except json.JSONDecodeError:
                return {"error": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@mcp.tool()
def get_item_group_feed(
    category_id: str,
    feed_scope: str = "NEWLY_LISTED",
) -> dict:
    """
    Download a TSV_GZIP item group feed file for a specific category.
    
    Args:
        category_id: The category ID to download item groups for
        feed_scope: Feed scope - "NEWLY_LISTED" or "ALL_ACTIVE"
    
    Returns:
        Binary feed file content as base64 string
    """
    endpoint = f"{get_base_url('feed')}/item_group"
    params = {
        "category_id": category_id,
        "feed_scope": feed_scope,
    }
    
    try:
        full_url = endpoint
        request_headers = get_auth_headers()
        request_headers["Accept"] = "application/gzip"
        
        response = requests.get(
            url=full_url,
            params=params,
            headers=request_headers,
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            return {
                "feed_data_base64": base64.b64encode(response.content).decode("utf-8"),
                "content_length": len(response.content),
                "content_type": response.headers.get("Content-Type", "application/gzip"),
            }
        else:
            try:
                error_data = response.json()
                return {"error": error_data}
            except json.JSONDecodeError:
                return {"error": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@mcp.tool()
def get_item_priority_feed() -> dict:
    """
    Download a TSV_GZIP file containing items the seller has priority to sell.
    
    Returns:
        Binary feed file content as base64 string
    """
    endpoint = f"{get_base_url('feed')}/item_priority"
    
    try:
        full_url = endpoint
        request_headers = get_auth_headers()
        request_headers["Accept"] = "application/gzip"
        
        response = requests.get(
            url=full_url,
            headers=request_headers,
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            return {
                "feed_data_base64": base64.b64encode(response.content).decode("utf-8"),
                "content_length": len(response.content),
                "content_type": response.headers.get("Content-Type", "application/gzip"),
            }
        else:
            try:
                error_data = response.json()
                return {"error": error_data}
            except json.JSONDecodeError:
                return {"error": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@mcp.tool()
def get_item_snapshot_feed(
    category_id: str,
    snapshot_date: str | None = None,
) -> dict:
    """
    Download a TSV_GZIP file containing item snapshots.
    
    Args:
        category_id: The category ID to download snapshots for
        snapshot_date: Optional date for historical snapshots (YYYY-MM-DD)
    
    Returns:
        Binary feed file content as base64 string
    """
    endpoint = f"{get_base_url('feed')}/item_snapshot"
    params = {"category_id": category_id}
    if snapshot_date:
        params["snapshot_date"] = snapshot_date
    
    try:
        full_url = endpoint
        request_headers = get_auth_headers()
        request_headers["Accept"] = "application/gzip"
        
        response = requests.get(
            url=full_url,
            params=params,
            headers=request_headers,
        )
        
        if response.status_code >= 200 and response.status_code < 300:
            return {
                "feed_data_base64": base64.b64encode(response.content).decode("utf-8"),
                "content_length": len(response.content),
                "content_type": response.headers.get("Content-Type", "application/gzip"),
            }
        else:
            try:
                error_data = response.json()
                return {"error": error_data}
            except json.JSONDecodeError:
                return {"error": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Marketing API Operations
@mcp.tool()
def get_merchandised_products(
    category_id: str,
    metric_name: str = "BEST_SELLING",
    max_results: int | None = 8,
    aspect_filter: str | None = None,
) -> dict:
    """
    Retrieve products based on category and metric (e.g., best selling).
    
    Args:
        category_id: The category ID to search in
        metric_name: The metric to use (e.g., BEST_SELLING)
        max_results: Maximum number of products (default: 8, max: 100)
        aspect_filter: Filter by aspect name/value pairs (e.g., "Brand:Canon")
    
    Returns:
        Products with EPID, title, ratings, and market price details.
    """
    endpoint = f"{get_base_url('marketing')}/merchandised_product"
    params = {
        "category_id": category_id,
        "metric_name": metric_name,
        "max_results": str(max_results),
    }
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    
    return make_request("GET", endpoint, params=params)

# Offer API Operations
@mcp.tool()
def place_proxy_bid(
    listing_id: str,
    max_amount_value: float,
    max_amount_currency: str = "USD",
    user_consent: bool | None = None,
) -> dict:
    """
    Place a proxy bid on an auction item.
    
    Args:
        listing_id: The unique RESTful identifier of the auction item
        max_amount_value: Maximum bid amount
        max_amount_currency: Currency code (default: USD)
        user_consent: Consent to bid on adult-only items (default: false)
    
    Returns:
        Proxy bid ID if successful.
    """
    endpoint = f"{get_base_url('offer')}/bidding/{listing_id}/place_proxy_bid"
    
    payload = {
        "maxAmount": {
            "value": str(max_amount_value),
            "currency": max_amount_currency,
        }
    }
    
    if user_consent is not None:
        payload["userConsent"] = {
            "adultOnlyItem": user_consent
        }
    
    return make_request("POST", endpoint, payload=payload)

@mcp.tool()
def get_bidding(listing_id: str) -> dict:
    """
    Retrieve bidding information for an auction item.
    
    Args:
        listing_id: The unique RESTful identifier of the auction item
    
    Returns:
        Bidding information including current bid and bid count.
    """
    endpoint = f"{get_base_url('offer')}/bidding/{listing_id}"
    return make_request("GET", endpoint)

# Order API - Guest Checkout Operations
@mcp.tool()
def initiate_guest_checkout_session(
    contact_email: str,
    line_items: list[dict],
    shipping_address: dict,
    recipient: dict,
) -> dict:
    """
    Create a guest checkout session.
    
    Args:
        contact_email: Buyer's email address
        line_items: List of line items with itemId and quantity
        shipping_address: Shipping address with addressLine1, city, country, phoneNumber, recipient
        recipient: Recipient information with firstName and lastName
    
    Returns:
        Checkout session ID and line item details.
    """
    endpoint = f"{get_base_url('order')}/guest_checkout_session/initiate"
    
    payload = {
        "contactEmail": contact_email,
        "lineItemInputs": line_items,
        "shippingAddress": shipping_address,
        "recipient": recipient,
    }
    
    return make_request("POST", endpoint, payload=payload)

@mcp.tool()
def update_guest_checkout_session_quantity(
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
) -> dict:
    """
    Update the quantity of an item in a guest checkout session.
    
    Args:
        checkout_session_id: The checkout session ID
        line_item_id: The unique eBay-assigned ID of the line item
        quantity: New quantity for the line item
    
    Returns:
        Updated checkout session details.
    """
    endpoint = f"{get_base_url('order')}/guest_checkout_session/{checkout_session_id}/update_quantity"
    
    payload = {
        "lineItemId": line_item_id,
        "quantity": quantity,
    }
    
    return make_request("POST", endpoint, payload=payload)

@mcp.tool()
def update_guest_shipping_address(
    checkout_session_id: str,
    address_line_1: str,
    city: str,
    country: str,
    phone_number: str,
    recipient_first_name: str,
    recipient_last_name: str,
    address_line_2: str | None = None,
    county: str | None = None,
    postal_code: str | None = None,
    state_or_province: str | None = None,
) -> dict:
    """
    Update the shipping address in a guest checkout session.
    
    Args:
        checkout_session_id: The checkout session ID
        address_line_1: First line of street address
        city: City name
        country: Country code (2-letter ISO)
        phone_number: Phone number with country code
        recipient_first_name: Recipient's first name
        recipient_last_name: Recipient's last name
        address_line_2: Optional second line of address
        county: Optional county name
        postal_code: Optional postal code
        state_or_province: Optional state or province code
    
    Returns:
        Updated checkout session details.
    """
    endpoint = f"{get_base_url('order')}/guest_checkout_session/{checkout_session_id}/update_shipping_address"
    
    payload = {
        "addressLine1": address_line_1,
        "city": city,
        "country": country,
        "phoneNumber": phone_number,
        "recipient": {
            "firstName": recipient_first_name,
            "lastName": recipient_last_name,
        },
    }
    
    if address_line_2:
        payload["addressLine2"] = address_line_2
    if county:
        payload["county"] = county
    if postal_code:
        payload["postalCode"] = postal_code
    if state_or_province:
        payload["stateOrProvince"] = state_or_province
    
    return make_request("POST", endpoint, payload=payload)

@mcp.tool()
def update_guest_shipping_option(
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str,
) -> dict:
    """
    Update the shipping option for a line item in a guest checkout session.
    
    Args:
        checkout_session_id: The checkout session ID
        line_item_id: The unique eBay-assigned ID of the line item
        shipping_option_id: The unique identifier of the shipping option
    
    Returns:
        Updated checkout session details.
    """
    endpoint = f"{get_base_url('order')}/guest_checkout_session/{checkout_session_id}/update_shipping_option"
    
    payload = {
        "lineItemId": line_item_id,
        "shippingOptionId": shipping_option_id,
    }
    
    return make_request("POST", endpoint, payload=payload)

@mcp.tool()
def apply_guest_coupon(
    checkout_session_id: str,
    redemption_code: str,
) -> dict:
    """
    Apply a coupon to a guest checkout session.
    
    Args:
        checkout_session_id: The checkout session ID
        redemption_code: The coupon redemption code
    
    Returns:
        Updated checkout session with applied coupon details.
    """
    endpoint = f"{get_base_url('order')}/guest_checkout_session/{checkout_session_id}/apply_coupon"
    
    payload = {"redemptionCode": redemption_code}
    
    return make_request("POST", endpoint, payload=payload)

@mcp.tool()
def remove_guest_coupon(
    checkout_session_id: str,
    redemption_code: str,
) -> dict:
    """
    Remove a coupon from a guest checkout session.
    
    Args:
        checkout_session_id: The checkout session ID
        redemption_code: The coupon redemption code
    
    Returns:
        Updated checkout session details.
    """
    endpoint = f"{get_base_url('order')}/guest_checkout_session/{checkout_session_id}/remove_coupon"
    
    payload = {"redemptionCode": redemption_code}
    
    return make_request("POST", endpoint, payload=payload)

@mcp.tool()
def get_guest_checkout_session(checkout_session_id: str) -> dict:
    """
    Retrieve details of a guest checkout session.
    
    Args:
        checkout_session_id: The checkout session ID
    
    Returns:
        Checkout session details including line items, shipping, and costs.
    """
    endpoint = f"{get_base_url('order')}/guest_checkout_session/{checkout_session_id}"
    return make_request("GET", endpoint)

# Order API - Guest Purchase Order Operations
@mcp.tool()
def get_guest_purchase_order(purchase_order_id: str) -> dict:
    """
    Retrieve details of a guest purchase order.
    
    Args:
        purchase_order_id: The unique identifier of the purchase order
    
    Returns:
        Purchase order details including line items, status, and costs.
    """
    endpoint = f"{get_base_url('order')}/guest_purchase_order/{purchase_order_id}"
    return make_request("GET", endpoint)

if __name__ == "__main__":
    import asyncio
    # Run the MCP server
    mcp.run()
