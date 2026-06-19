#!/usr/bin/env python3
"""
MCP Server for eBay Sell API
Provides tools for managing eBay listings, inventory, orders, and more.
"""

import os
import json
import requests
from typing import Any, Dict, Optional
from datetime import datetime, timedelta
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
server = FastMCP("ebay-sell-api")

# Configuration from environment
EBAY_APP_ID = os.getenv("EBAY_APP_ID", "")
EBAY_CERT_ID = os.getenv("EBAY_CERT_ID", "")
EBAY_REFRESH_TOKEN = os.getenv("EBAY_REFRESH_TOKEN", "")
EBAY_ENVIRONMENT = os.getenv("EBAY_ENVIRONMENT", "SANDBOX")

# Base URLs
BASE_URL = (
    "https://api.sandbox.ebay.com"
    if EBAY_ENVIRONMENT == "SANDBOX"
    else "https://api.ebay.com"
)

# Token cache
_token_cache: Dict[str, Any] = {}


def get_access_token() -> str:
    """Get a valid access token, using cache if available."""
    # Check if cached token is still valid
    if _token_cache.get("access_token") and _token_cache.get("expires_at"):
        if datetime.now() < _token_cache["expires_at"]:
            return _token_cache["access_token"]

    # Request new token
    token_url = f"{BASE_URL}/identity/v1/oauth2/token"
    auth = (EBAY_APP_ID, EBAY_CERT_ID)
    data = {
        "grant_type": "refresh_token",
        "refresh_token": EBAY_REFRESH_TOKEN,
    }

    try:
        response = requests.post(token_url, auth=auth, data=data, timeout=10)
        response.raise_for_status()
        token_data = response.json()

        # Cache the token
        _token_cache["access_token"] = token_data["access_token"]
        expires_in = token_data.get("expires_in", 3600)
        _token_cache["expires_at"] = datetime.now() + timedelta(seconds=expires_in - 60)

        return token_data["access_token"]
    except Exception as e:
        return f"Error getting token: {str(e)}"


def make_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    json_data: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Make an authenticated request to the eBay API."""
    token = get_access_token()
    if isinstance(token, str) and token.startswith("Error"):
        return {"error": token}

    url = f"{BASE_URL}{endpoint}"
    auth_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    if headers:
        auth_headers.update(headers)

    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=json_data,
            headers=auth_headers,
            timeout=30,
        )

        # Handle different status codes
        if response.status_code in [200, 201, 202, 204]:
            if response.text:
                return response.json()
            return {"success": True}
        elif response.status_code == 400:
            try:
                return {"error": response.json()}
            except:
                return {"error": response.text}
        elif response.status_code == 401:
            return {"error": "Unauthorized - check credentials"}
        elif response.status_code == 404:
            return {"error": "Not found"}
        elif response.status_code == 429:
            return {"error": "Rate limited - try again later"}
        else:
            try:
                return {"error": response.json()}
            except:
                return {"error": f"HTTP {response.status_code}: {response.text}"}
    except requests.exceptions.Timeout:
        return {"error": "Request timeout"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# ============================================================================
# INVENTORY MANAGEMENT TOOLS
# ============================================================================


@server.tool()
def create_inventory_item(
    sku: str,
    title: str,
    description: str,
    price: float,
    quantity: int,
    category_id: str,
    condition: str = "NEW",
    item_type: str = "FIXED_PRICE",
) -> Dict[str, Any]:
    """
    Create a new inventory item in your eBay inventory.
    
    Args:
        sku: Stock keeping unit (unique identifier)
        title: Item title
        description: Item description
        price: Item price
        quantity: Available quantity
        category_id: eBay category ID
        condition: Item condition (NEW, LIKE_NEW, GOOD, ACCEPTABLE)
        item_type: Listing type (FIXED_PRICE, AUCTION)
    
    Returns:
        Created inventory item details
    """
    endpoint = "/sell/inventory/v1/inventory_item"
    payload = {
        "sku": sku,
        "title": title,
        "description": description,
        "price": {"currency": "USD", "value": str(price)},
        "quantity": quantity,
        "categoryId": category_id,
        "condition": condition,
        "itemType": item_type,
    }
    return make_request("POST", endpoint, json_data=payload)


@server.tool()
def get_inventory_item(sku: str) -> Dict[str, Any]:
    """
    Get details of an inventory item by SKU.
    
    Args:
        sku: Stock keeping unit
    
    Returns:
        Inventory item details
    """
    endpoint = f"/sell/inventory/v1/inventory_item/{sku}"
    return make_request("GET", endpoint)


@server.tool()
def update_inventory_item(
    sku: str,
    title: Optional[str] = None,
    description: Optional[str] = None,
    price: Optional[float] = None,
    quantity: Optional[int] = None,
    condition: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update an existing inventory item.
    
    Args:
        sku: Stock keeping unit
        title: New title (optional)
        description: New description (optional)
        price: New price (optional)
        quantity: New quantity (optional)
        condition: New condition (optional)
    
    Returns:
        Update result
    """
    endpoint = f"/sell/inventory/v1/inventory_item/{sku}"
    payload = {}
    if title:
        payload["title"] = title
    if description:
        payload["description"] = description
    if price is not None:
        payload["price"] = {"currency": "USD", "value": str(price)}
    if quantity is not None:
        payload["quantity"] = quantity
    if condition:
        payload["condition"] = condition

    return make_request("PUT", endpoint, json_data=payload)


@server.tool()
def delete_inventory_item(sku: str) -> Dict[str, Any]:
    """
    Delete an inventory item by SKU.
    
    Args:
        sku: Stock keeping unit
    
    Returns:
        Deletion result
    """
    endpoint = f"/sell/inventory/v1/inventory_item/{sku}"
    return make_request("DELETE", endpoint)


@server.tool()
def get_inventory_items(limit: int = 25, offset: int = 0) -> Dict[str, Any]:
    """
    Get a list of inventory items.
    
    Args:
        limit: Maximum number of items to return (1-25)
        offset: Number of items to skip
    
    Returns:
        List of inventory items
    """
    endpoint = "/sell/inventory/v1/inventory_item"
    params = {"limit": min(limit, 25), "offset": offset}
    return make_request("GET", endpoint, params=params)


# ============================================================================
# LISTING MANAGEMENT TOOLS
# ============================================================================


@server.tool()
def create_listing(
    sku: str,
    listing_type: str = "FIXED_PRICE",
    quantity_available: int = 1,
    duration_in_days: int = 30,
) -> Dict[str, Any]:
    """
    Create a new listing from an inventory item.
    
    Args:
        sku: Stock keeping unit of the inventory item
        listing_type: FIXED_PRICE or AUCTION
        quantity_available: Quantity to list
        duration_in_days: How long to list (1-365)
    
    Returns:
        Created listing details
    """
    endpoint = "/sell/inventory/v1/offer"
    payload = {
        "sku": sku,
        "listingType": listing_type,
        "quantityLimitPerBuyer": 1,
        "availableQuantity": quantity_available,
        "durationInDays": min(duration_in_days, 365),
    }
    return make_request("POST", endpoint, json_data=payload)


@server.tool()
def get_listing(offer_id: str) -> Dict[str, Any]:
    """
    Get details of a specific listing.
    
    Args:
        offer_id: The offer/listing ID
    
    Returns:
        Listing details
    """
    endpoint = f"/sell/inventory/v1/offer/{offer_id}"
    return make_request("GET", endpoint)


@server.tool()
def update_listing(
    offer_id: str,
    quantity_available: Optional[int] = None,
    price: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Update an active listing.
    
    Args:
        offer_id: The offer/listing ID
        quantity_available: New available quantity (optional)
        price: New price (optional)
    
    Returns:
        Update result
    """
    endpoint = f"/sell/inventory/v1/offer/{offer_id}"
    payload = {}
    if quantity_available is not None:
        payload["availableQuantity"] = quantity_available
    if price is not None:
        payload["price"] = {"currency": "USD", "value": str(price)}

    return make_request("PUT", endpoint, json_data=payload)


@server.tool()
def publish_listing(sku: str) -> Dict[str, Any]:
    """
    Publish a listing from an inventory item.
    
    Args:
        sku: Stock keeping unit
    
    Returns:
        Published listing details
    """
    endpoint = "/sell/inventory/v1/offer"
    payload = {"sku": sku}
    return make_request("POST", endpoint, json_data=payload)


@server.tool()
def withdraw_listing(offer_id: str) -> Dict[str, Any]:
    """
    Withdraw (end) an active listing.
    
    Args:
        offer_id: The offer/listing ID
    
    Returns:
        Withdrawal result
    """
    endpoint = f"/sell/inventory/v1/offer/{offer_id}/withdraw"
    return make_request("POST", endpoint)


@server.tool()
def get_listings(
    limit: int = 25,
    offset: int = 0,
    filter_status: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get a list of your listings.
    
    Args:
        limit: Maximum number of listings to return (1-25)
        offset: Number of listings to skip
        filter_status: Filter by status (ACTIVE, INACTIVE, SOLD, ENDED)
    
    Returns:
        List of listings
    """
    endpoint = "/sell/inventory/v1/offer"
    params = {"limit": min(limit, 25), "offset": offset}
    if filter_status:
        params["filter"] = f"status:{filter_status}"
    return make_request("GET", endpoint, params=params)


# ============================================================================
# ORDER MANAGEMENT TOOLS
# ============================================================================


@server.tool()
def get_orders(
    limit: int = 25,
    offset: int = 0,
    order_status: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get a list of orders.
    
    Args:
        limit: Maximum number of orders to return (1-25)
        offset: Number of orders to skip
        order_status: Filter by status (ACTIVE, COMPLETED, CANCELLED, ALL)
    
    Returns:
        List of orders
    """
    endpoint = "/sell/fulfillment/v1/order"
    params = {"limit": min(limit, 25), "offset": offset}
    if order_status:
        params["filter"] = f"orderfulfillmentstatus:{order_status}"
    return make_request("GET", endpoint, params=params)


@server.tool()
def get_order(order_id: str) -> Dict[str, Any]:
    """
    Get details of a specific order.
    
    Args:
        order_id: The order ID
    
    Returns:
        Order details including items, buyer, and shipping info
    """
    endpoint = f"/sell/fulfillment/v1/order/{order_id}"
    return make_request("GET", endpoint)


@server.tool()
def get_order_by_reference_id(reference_id: str) -> Dict[str, Any]:
    """
    Get an order by its reference ID.
    
    Args:
        reference_id: The reference ID (e.g., from external system)
    
    Returns:
        Order details
    """
    endpoint = "/sell/fulfillment/v1/order"
    params = {"filter": f"legacyOrderId:{reference_id}"}
    return make_request("GET", endpoint, params=params)


@server.tool()
def issue_refund(
    order_id: str,
    item_id: str,
    reason_for_refund: str,
    refund_amount: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Issue a refund for an order item.
    
    Args:
        order_id: The order ID
        item_id: The line item ID
        reason_for_refund: Reason (BUYER_REMORSE, ITEM_NOT_AS_DESCRIBED, etc.)
        refund_amount: Amount to refund (optional, defaults to full item price)
    
    Returns:
        Refund result
    """
    endpoint = f"/sell/fulfillment/v1/order/{order_id}/issue_refund"
    payload = {
        "lineItemId": item_id,
        "reasonForRefund": reason_for_refund,
    }
    if refund_amount is not None:
        payload["refundAmount"] = {
            "currency": "USD",
            "value": str(refund_amount),
        }
    return make_request("POST", endpoint, json_data=payload)


@server.tool()
def create_shipment(
    order_id: str,
    carrier_name: str,
    tracking_number: str,
    ship_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a shipment for an order.
    
    Args:
        order_id: The order ID
        carrier_name: Carrier name (USPS, UPS, FedEx, etc.)
        tracking_number: Tracking number
        ship_date: Ship date in ISO format (optional)
    
    Returns:
        Shipment creation result
    """
    endpoint = f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment"
    payload = {
        "lineItems": [{"lineItemId": "*"}],  # All items
        "shippingCarrierCode": carrier_name,
        "trackingNumber": tracking_number,
    }
    if ship_date:
        payload["shippedDate"] = ship_date
    return make_request("POST", endpoint, json_data=payload)


@server.tool()
def get_shipments(order_id: str) -> Dict[str, Any]:
    """
    Get all shipments for an order.
    
    Args:
        order_id: The order ID
    
    Returns:
        List of shipments
    """
    endpoint = f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment"
    return make_request("GET", endpoint)


# ============================================================================
# ACCOUNT & POLICIES TOOLS
# ============================================================================


@server.tool()
def get_account_profile() -> Dict[str, Any]:
    """
    Get your eBay account profile information.
    
    Returns:
        Account profile details
    """
    endpoint = "/sell/account/v1/account_profile"
    return make_request("GET", endpoint)


@server.tool()
def get_return_policies() -> Dict[str, Any]:
    """
    Get all return policies for your account.
    
    Returns:
        List of return policies
    """
    endpoint = "/sell/account/v1/return_policy"
    return make_request("GET", endpoint)


@server.tool()
def create_return_policy(
    name: str,
    description: str,
    returns_accepted: bool = True,
    return_period_days: int = 30,
    refund_method: str = "MONEY_BACK",
) -> Dict[str, Any]:
    """
    Create a new return policy.
    
    Args:
        name: Policy name
        description: Policy description
        returns_accepted: Whether returns are accepted
        return_period_days: Number of days for returns
        refund_method: MONEY_BACK or EXCHANGE
    
    Returns:
        Created policy details
    """
    endpoint = "/sell/account/v1/return_policy"
    payload = {
        "name": name,
        "description": description,
        "returnsAccepted": returns_accepted,
        "returnPeriod": {"value": return_period_days, "unit": "DAY"},
        "refundMethod": refund_method,
    }
    return make_request("POST", endpoint, json_data=payload)


@server.tool()
def get_shipping_policies() -> Dict[str, Any]:
    """
    Get all shipping policies for your account.
    
    Returns:
        List of shipping policies
    """
    endpoint = "/sell/account/v1/shipping_policy"
    return make_request("GET", endpoint)


@server.tool()
def create_shipping_policy(
    name: str,
    description: str,
    domestic_shipping_cost: float,
    international_shipping_cost: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Create a new shipping policy.
    
    Args:
        name: Policy name
        description: Policy description
        domestic_shipping_cost: Cost for domestic shipping
        international_shipping_cost: Cost for international shipping (optional)
    
    Returns:
        Created policy details
    """
    endpoint = "/sell/account/v1/shipping_policy"
    payload = {
        "name": name,
        "description": description,
        "shippingOptions": [
            {
                "costType": "FLAT_RATE",
                "shippingServices": [
                    {
                        "shippingServiceCode": "USPS_GROUND_ADVANTAGE",
                        "shippingCost": {
                            "currency": "USD",
                            "value": str(domestic_shipping_cost),
                        },
                    }
                ],
            }
        ],
    }
    return make_request("POST", endpoint, json_data=payload)


@server.tool()
def get_payment_policies() -> Dict[str, Any]:
    """
    Get all payment policies for your account.
    
    Returns:
        List of payment policies
    """
    endpoint = "/sell/account/v1/payment_policy"
    return make_request("GET", endpoint)


# ============================================================================
# MARKETING & PROMOTIONS TOOLS
# ============================================================================


@server.tool()
def get_promotions(limit: int = 25, offset: int = 0) -> Dict[str, Any]:
    """
    Get a list of your promotions.
    
    Args:
        limit: Maximum number of promotions to return
        offset: Number of promotions to skip
    
    Returns:
        List of promotions
    """
    endpoint = "/sell/marketing/v1/promotion"
    params = {"limit": min(limit, 25), "offset": offset}
    return make_request("GET", endpoint, params=params)


@server.tool()
def get_promotion(promotion_id: str) -> Dict[str, Any]:
    """
    Get details of a specific promotion.
    
    Args:
        promotion_id: The promotion ID
    
    Returns:
        Promotion details
    """
    endpoint = f"/sell/marketing/v1/promotion/{promotion_id}"
    return make_request("GET", endpoint)


@server.tool()
def create_promotion(
    name: str,
    promotion_type: str,
    discount_percentage: Optional[float] = None,
    discount_amount: Optional[float] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a new promotion.
    
    Args:
        name: Promotion name
        promotion_type: Type (MARKDOWN_SALE, VOLUME_DISCOUNT, BUNDLE_PROMOTION)
        discount_percentage: Discount percentage (optional)
        discount_amount: Discount amount in dollars (optional)
        start_date: Start date in ISO format (optional)
        end_date: End date in ISO format (optional)
    
    Returns:
        Created promotion details
    """
    endpoint = "/sell/marketing/v1/promotion"
    payload = {
        "name": name,
        "promotionType": promotion_type,
    }
    if discount_percentage:
        payload["discountPercentage"] = discount_percentage
    if discount_amount:
        payload["discountAmount"] = {
            "currency": "USD",
            "value": str(discount_amount),
        }
    if start_date:
        payload["startDate"] = start_date
    if end_date:
        payload["endDate"] = end_date

    return make_request("POST", endpoint, json_data=payload)


@server.tool()
def get_campaigns(limit: int = 25, offset: int = 0) -> Dict[str, Any]:
    """
    Get a list of your advertising campaigns.
    
    Args:
        limit: Maximum number of campaigns to return
        offset: Number of campaigns to skip
    
    Returns:
        List of campaigns
    """
    endpoint = "/sell/marketing/v1/ad_campaign"
    params = {"limit": min(limit, 25), "offset": offset}
    return make_request("GET", endpoint, params=params)


@server.tool()
def get_campaign(campaign_id: str) -> Dict[str, Any]:
    """
    Get details of a specific advertising campaign.
    
    Args:
        campaign_id: The campaign ID
    
    Returns:
        Campaign details
    """
    endpoint = f"/sell/marketing/v1/ad_campaign/{campaign_id}"
    return make_request("GET", endpoint)


@server.tool()
def create_campaign(
    name: str,
    campaign_type: str = "PROMOTED_LISTINGS",
    daily_budget: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Create a new advertising campaign.
    
    Args:
        name: Campaign name
        campaign_type: Type (PROMOTED_LISTINGS, SPONSORED_PRODUCTS)
        daily_budget: Daily budget in dollars (optional)
    
    Returns:
        Created campaign details
    """
    endpoint = "/sell/marketing/v1/ad_campaign"
    payload = {
        "name": name,
        "campaignType": campaign_type,
    }
    if daily_budget:
        payload["dailyBudget"] = {
            "currency": "USD",
            "value": str(daily_budget),
        }
    return make_request("POST", endpoint, json_data=payload)


# ============================================================================
# FINANCES & PAYOUTS TOOLS
# ============================================================================


@server.tool()
def get_transactions(
    limit: int = 25,
    offset: int = 0,
    transaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get financial transactions.
    
    Args:
        limit: Maximum number of transactions to return
        offset: Number of transactions to skip
        transaction_type: Filter by type (SALE, REFUND, SHIPPING_LABEL, etc.)
    
    Returns:
        List of transactions
    """
    endpoint = "/sell/finances/v1/transaction"
    params = {"limit": min(limit, 25), "offset": offset}
    if transaction_type:
        params["filter"] = f"transactionType:{transaction_type}"
    return make_request("GET", endpoint, params=params)


@server.tool()
def get_payouts(limit: int = 25, offset: int = 0) -> Dict[str, Any]:
    """
    Get a list of payouts.
    
    Args:
        limit: Maximum number of payouts to return
        offset: Number of payouts to skip
    
    Returns:
        List of payouts
    """
    endpoint = "/sell/finances/v1/payout"
    params = {"limit": min(limit, 25), "offset": offset}
    return make_request("GET", endpoint, params=params)


@server.tool()
def get_payout(payout_id: str) -> Dict[str, Any]:
    """
    Get details of a specific payout.
    
    Args:
        payout_id: The payout ID
    
    Returns:
        Payout details
    """
    endpoint = f"/sell/finances/v1/payout/{payout_id}"
    return make_request("GET", endpoint)


@server.tool()
def get_seller_funds_summary() -> Dict[str, Any]:
    """
    Get a summary of your seller funds.
    
    Returns:
        Funds summary including available balance and pending amounts
    """
    endpoint = "/sell/finances/v1/seller_funds_summary"
    return make_request("GET", endpoint)


# ============================================================================
# FEED & BULK OPERATIONS TOOLS
# ============================================================================


@server.tool()
def create_inventory_feed(
    feed_type: str = "CSV_INVENTORY_FEED",
    file_path: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create an inventory feed for bulk operations.
    
    Args:
        feed_type: Type of feed (CSV_INVENTORY_FEED, XML_INVENTORY_FEED)
        file_path: Path to the feed file (optional)
    
    Returns:
        Created feed details
    """
    endpoint = "/sell/feed/v1/inventory_task"
    payload = {"feedType": feed_type}
    return make_request("POST", endpoint, json_data=payload)


@server.tool()
def get_feed_tasks(limit: int = 25, offset: int = 0) -> Dict[str, Any]:
    """
    Get a list of feed tasks.
    
    Args:
        limit: Maximum number of tasks to return
        offset: Number of tasks to skip
    
    Returns:
        List of feed tasks
    """
    endpoint = "/sell/feed/v1/inventory_task"
    params = {"limit": min(limit, 25), "offset": offset}
    return make_request("GET", endpoint, params=params)


@server.tool()
def get_feed_task(task_id: str) -> Dict[str, Any]:
    """
    Get details of a specific feed task.
    
    Args:
        task_id: The task ID
    
    Returns:
        Task details including status and results
    """
    endpoint = f"/sell/feed/v1/inventory_task/{task_id}"
    return make_request("GET", endpoint)


# ============================================================================
# ANALYTICS & INSIGHTS TOOLS
# ============================================================================


@server.tool()
def get_traffic_report(
    metric_type: str = "LISTING_IMPRESSION_CLICKS",
    date_range_days: int = 30,
) -> Dict[str, Any]:
    """
    Get traffic and performance metrics.
    
    Args:
        metric_type: Type of metric (LISTING_IMPRESSION_CLICKS, LISTING_VIEWS, etc.)
        date_range_days: Number of days to report on
    
    Returns:
        Traffic report data
    """
    endpoint = "/sell/analytics/v1/traffic_report"
    params = {
        "metric_type": metric_type,
        "date_range": f"LAST_{date_range_days}_DAYS",
    }
    return make_request("GET", endpoint, params=params)


@server.tool()
def get_sales_report(date_range_days: int = 30) -> Dict[str, Any]:
    """
    Get sales performance report.
    
    Args:
        date_range_days: Number of days to report on
    
    Returns:
        Sales report data
    """
    endpoint = "/sell/analytics/v1/sales_report"
    params = {"date_range": f"LAST_{date_range_days}_DAYS"}
    return make_request("GET", endpoint, params=params)


# ============================================================================
# LISTING QUALITY & RECOMMENDATIONS TOOLS
# ============================================================================


@server.tool()
def get_listing_quality_metrics(sku: str) -> Dict[str, Any]:
    """
    Get quality metrics for a listing.
    
    Args:
        sku: Stock keeping unit
    
    Returns:
        Quality metrics and recommendations
    """
    endpoint = f"/sell/quality/v1/listing_quality_metric/{sku}"
    return make_request("GET", endpoint)


@server.tool()
def get_quality_recommendations() -> Dict[str, Any]:
    """
    Get quality recommendations for your listings.
    
    Returns:
        List of recommendations to improve listings
    """
    endpoint = "/sell/quality/v1/recommendation"
    return make_request("GET", endpoint)


# ============================================================================
# COMPLIANCE & VIOLATIONS TOOLS
# ============================================================================


@server.tool()
def get_violations() -> Dict[str, Any]:
    """
    Get any policy violations on your account.
    
    Returns:
        List of violations if any
    """
    endpoint = "/sell/compliance/v1/violation"
    return make_request("GET", endpoint)


@server.tool()
def get_listings_with_violations() -> Dict[str, Any]:
    """
    Get listings that have policy violations.
    
    Returns:
        List of listings with violations
    """
    endpoint = "/sell/compliance/v1/listing_violation"
    return make_request("GET", endpoint)


if __name__ == "__main__":
    server.run()
