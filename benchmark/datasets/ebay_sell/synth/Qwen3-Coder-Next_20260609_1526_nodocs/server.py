#!/usr/bin/env python3
"""
eBay Sell API MCP Server

Implements comprehensive coverage of the eBay Sell API for use by autonomous agents.
"""

import os
import json
import requests
from typing import Optional, Dict, Any, List
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("ebay-sell")

# Configuration
EBAY_APP_ID = os.getenv("EBAY_APP_ID")
EBAY_CERT_ID = os.getenv("EBAY_CERT_ID")
EBAY_REFRESH_TOKEN = os.getenv("EBAY_REFRESH_TOKEN")
EBAY_ENVIRONMENT = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()

# Base URLs
BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com"
}

BASE_URL = BASE_URLS.get(EBAY_ENVIRONMENT, BASE_URLS["SANDBOX"])

# OAuth 2.0 endpoints
TOKEN_ENDPOINT = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
if EBAY_ENVIRONMENT == "PRODUCTION":
    TOKEN_ENDPOINT = "https://api.ebay.com/identity/v1/oauth2/token"


def get_access_token() -> Optional[str]:
    """Get OAuth 2.0 access token using refresh token."""
    if not all([EBAY_APP_ID, EBAY_CERT_ID, EBAY_REFRESH_TOKEN]):
        return None
    
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": EBAY_REFRESH_TOKEN,
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    
    auth = (EBAY_APP_ID, EBAY_CERT_ID)
    
    try:
        response = requests.post(TOKEN_ENDPOINT, data=payload, auth=auth)
        response.raise_for_status()
        return response.json().get("access_token")
    except Exception as e:
        return None


def make_request(method: str, path: str, params: Dict = None, data: Dict = None) -> Dict[str, Any]:
    """Make authenticated request to eBay API."""
    access_token = get_access_token()
    
    if not access_token:
        return {"error": "Failed to authenticate with eBay API"}
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    url = f"{BASE_URL}{path}"
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, params=params, json=data)
        elif method == "PUT":
            response = requests.put(url, headers=headers, params=params, json=data)
        elif method == "PATCH":
            response = requests.patch(url, headers=headers, params=params, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, params=params)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            error_data = response.json()
            return {"error": error_data}
        except:
            return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


# ========== INVENTORY API ==========
# Item (Listings) Management

@mcp.tool()
def get_item(item_id: str) -> Dict[str, Any]:
    """Get a single item by ID."""
    return make_request("GET", f"/sell/inventory/v1/item/{item_id}")


@mcp.tool()
def list_items(limit: int = 10, offset: int = 0, filter: str = None, order: str = None) -> Dict[str, Any]:
    """List items with pagination."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if order:
        params["order"] = order
    return make_request("GET", "/sell/inventory/v1/item", params=params)


@mcp.tool()
def create_item(title: str, description: str, category_id: str, price: float,
                quantity: int = 1, condition: str = "NEW", sku: str = None,
                brand: str = None, mpn: str = None, images: List[str] = None,
                subtitle: str = None) -> Dict[str, Any]:
    """Create a new item listing."""
    item = {
        "title": title,
        "description": description,
        "category_id": category_id,
        "price": {"value": str(price), "currency": "USD"},
        "quantity": quantity,
        "condition": condition
    }
    if sku:
        item["sku"] = sku
    if brand:
        item["brand"] = brand
    if mpn:
        item["mpn"] = mpn
    if images:
        item["images"] = [{"url": img} for img in images]
    if subtitle:
        item["subtitle"] = subtitle
    return make_request("POST", "/sell/inventory/v1/item", data=item)


@mcp.tool()
def update_item(item_id: str, title: str = None, description: str = None,
                price: float = None, quantity: int = None, condition: str = None,
                sku: str = None, brand: str = None, mpn: str = None,
                images: List[str] = None, subtitle: str = None) -> Dict[str, Any]:
    """Update an existing item listing."""
    updates = {}
    if title:
        updates["title"] = title
    if description:
        updates["description"] = description
    if price is not None:
        updates["price"] = {"value": str(price), "currency": "USD"}
    if quantity is not None:
        updates["quantity"] = quantity
    if condition:
        updates["condition"] = condition
    if sku:
        updates["sku"] = sku
    if brand:
        updates["brand"] = brand
    if mpn:
        updates["mpn"] = mpn
    if images:
        updates["images"] = [{"url": img} for img in images]
    if subtitle:
        updates["subtitle"] = subtitle
    return make_request("PATCH", f"/sell/inventory/v1/item/{item_id}", data=updates)


@mcp.tool()
def delete_item(item_id: str) -> Dict[str, Any]:
    """Delete an item listing."""
    return make_request("DELETE", f"/sell/inventory/v1/item/{item_id}")


@mcp.tool()
def revise_item_quantity(item_id: str, quantity: int, fulfillment_action: str = "SHIP") -> Dict[str, Any]:
    """Revise the quantity of an item listing."""
    data = {
        "availability": {
            "shipToLocationAvailability": {"quantity": quantity},
            "fulfillmentAction": fulfillment_action
        }
    }
    return make_request("PATCH", f"/sell/inventory/v1/item/{item_id}", data=data)


@mcp.tool()
def revise_item_price(item_id: str, price: float) -> Dict[str, Any]:
    """Revise the price of an item listing."""
    data = {"price": {"value": str(price), "currency": "USD"}}
    return make_request("PATCH", f"/sell/inventory/v1/item/{item_id}", data=data)


# Inventory Location Management

@mcp.tool()
def get_inventory_location(location_id: str) -> Dict[str, Any]:
    """Get an inventory location by ID."""
    return make_request("GET", f"/sell/inventory/v1/inventory_location/{location_id}")


@mcp.tool()
def list_inventory_locations(limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """List inventory locations with pagination."""
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/sell/inventory/v1/inventory_location", params=params)


@mcp.tool()
def create_inventory_location(name: str, address: Dict, phone: str = None,
                               hours: Dict = None, geocode: Dict = None,
                               display_location: str = "PRIVATE") -> Dict[str, Any]:
    """Create a new inventory location."""
    data = {
        "location": {
            "name": name,
            "address": address
        },
        "displayLocation": display_location
    }
    if phone:
        data["location"]["phone"] = phone
    if hours:
        data["location"]["hours"] = hours
    if geocode:
        data["location"]["geocode"] = geocode
    return make_request("POST", "/sell/inventory/v1/inventory_location", data=data)


@mcp.tool()
def update_inventory_location(location_id: str, name: str = None, address: Dict = None,
                               phone: str = None, hours: Dict = None) -> Dict[str, Any]:
    """Update an existing inventory location."""
    updates = {}
    if name:
        updates["name"] = name
    if address:
        updates["address"] = address
    if phone:
        updates["phone"] = phone
    if hours:
        updates["hours"] = hours
    return make_request("PATCH", f"/sell/inventory/v1/inventory_location/{location_id}", data=updates)


# Offer Management

@mcp.tool()
def get_offer(offer_id: str) -> Dict[str, Any]:
    """Get a single offer by ID."""
    return make_request("GET", f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def list_offers(limit: int = 10, offset: int = 0, filter: str = None) -> Dict[str, Any]:
    """List offers with pagination."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return make_request("GET", "/sell/inventory/v1/offer", params=params)


@mcp.tool()
def create_offer(name: str, description: str, sku: str, price: float,
                 quantity: int = 1, condition: str = "NEW",
                 category_id: str = None, availability: Dict = None) -> Dict[str, Any]:
    """Create a new offer."""
    data = {
        "name": name,
        "description": description,
        "sku": sku,
        "price": {"value": str(price), "currency": "USD"},
        "quantity": quantity,
        "condition": condition
    }
    if category_id:
        data["category_id"] = category_id
    if availability:
        data["availability"] = availability
    return make_request("POST", "/sell/inventory/v1/offer", data=data)


@mcp.tool()
def update_offer(offer_id: str, name: str = None, description: str = None,
                 price: float = None, quantity: int = None) -> Dict[str, Any]:
    """Update an existing offer."""
    updates = {}
    if name:
        updates["name"] = name
    if description:
        updates["description"] = description
    if price is not None:
        updates["price"] = {"value": str(price), "currency": "USD"}
    if quantity is not None:
        updates["quantity"] = quantity
    return make_request("PATCH", f"/sell/inventory/v1/offer/{offer_id}", data=updates)


@mcp.tool()
def delete_offer(offer_id: str) -> Dict[str, Any]:
    """Delete an offer."""
    return make_request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")


# ========== ORDER FULFILLMENT API ==========

@mcp.tool()
def get_order(order_id: str) -> Dict[str, Any]:
    """Get a single order by ID."""
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}")


@mcp.tool()
def list_orders(limit: int = 10, offset: int = 0, filter: str = None,
                order_by: str = None, status: str = None) -> Dict[str, Any]:
    """List orders with pagination."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if order_by:
        params["orderBy"] = order_by
    if status:
        params["status"] = status
    return make_request("GET", "/sell/fulfillment/v1/order", params=params)


@mcp.tool()
def create_order(line_items: List[Dict], shipping_address: Dict,
                 payment_method: str = "PAYPAL") -> Dict[str, Any]:
    """Create a new order."""
    data = {
        "lineItems": line_items,
        "shippingAddress": shipping_address,
        "paymentMethod": payment_method
    }
    return make_request("POST", "/sell/fulfillment/v1/order", data=data)


@mcp.tool()
def update_order(order_id: str, shipping_address: Dict = None,
                 shipping_costs: List[Dict] = None) -> Dict[str, Any]:
    """Update an existing order."""
    updates = {}
    if shipping_address:
        updates["shippingAddress"] = shipping_address
    if shipping_costs:
        updates["shippingCosts"] = shipping_costs
    return make_request("PATCH", f"/sell/fulfillment/v1/order/{order_id}", data=updates)


# Order Fulfillment Actions

@mcp.tool()
def complete_order(order_id: str, shipment_details: Dict = None) -> Dict[str, Any]:
    """Mark an order as completed."""
    data = {}
    if shipment_details:
        data["shipmentDetails"] = shipment_details
    return make_request("POST", f"/sell/fulfillment/v1/order/{order_id}/completeOrder", data=data)


@mcp.tool()
def cancel_order(order_id: str, reason: str = "Buyer Cancellation") -> Dict[str, Any]:
    """Cancel an order."""
    data = {"cancellationReason": reason}
    return make_request("POST", f"/sell/fulfillment/v1/order/{order_id}/cancelOrder", data=data)


@mcp.tool()
def refund_order(order_id: str, refund_amount: float, reason: str = "Return") -> Dict[str, Any]:
    """Refund an order."""
    data = {
        "refundAmount": {"value": str(refund_amount), "currency": "USD"},
        "reason": reason
    }
    return make_request("POST", f"/sell/fulfillment/v1/order/{order_id}/refund", data=data)


# ========== SHIPPING API ==========

@mcp.tool()
def get_shipping_carrier(carrier_id: str) -> Dict[str, Any]:
    """Get shipping carrier details."""
    return make_request("GET", f"/sell/fulfillment/v1/shipping_carrier/{carrier_id}")


@mcp.tool()
def list_shipping_carriers() -> Dict[str, Any]:
    """List available shipping carriers."""
    return make_request("GET", "/sell/fulfillment/v1/shipping_carrier")


@mcp.tool()
def get_shipping_service(carrier_id: str, service_id: str) -> Dict[str, Any]:
    """Get shipping service details."""
    return make_request("GET", f"/sell/fulfillment/v1/shipping_carrier/{carrier_id}/service/{service_id}")


@mcp.tool()
def calculate_shipping(order_id: str, carrier_id: str, service_id: str) -> Dict[str, Any]:
    """Calculate shipping cost for an order."""
    data = {"carrierId": carrier_id, "serviceId": service_id}
    return make_request("POST", f"/sell/fulfillment/v1/order/{order_id}/calculate_shipping", data=data)


@mcp.tool()
def create_shipment(order_id: str, carrier_id: str, service_id: str,
                    tracking_number: str = None, shipment_date: str = None) -> Dict[str, Any]:
    """Create a shipment for an order."""
    data = {"carrierId": carrier_id, "serviceId": service_id}
    if tracking_number:
        data["trackingNumber"] = tracking_number
    if shipment_date:
        data["shipmentDate"] = shipment_date
    return make_request("POST", f"/sell/fulfillment/v1/order/{order_id}/create_shipment", data=data)


@mcp.tool()
def get_shipment(order_id: str, shipment_id: str) -> Dict[str, Any]:
    """Get shipment details."""
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipment/{shipment_id}")


@mcp.tool()
def list_shipments(order_id: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """List shipments for an order."""
    params = {"limit": limit, "offset": offset}
    return make_request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipment", params=params)


# ========== ACCOUNT API - POLICIES ==========

@mcp.tool()
def get_selling_policy(policy_type: str, policy_id: str) -> Dict[str, Any]:
    """Get a selling policy by ID."""
    return make_request("GET", f"/sell/account/v1/policy/{policy_type}/{policy_id}")


@mcp.tool()
def list_selling_policies(policy_type: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """List selling policies of a specific type."""
    params = {"limit": limit, "offset": offset}
    return make_request("GET", f"/sell/account/v1/policy/{policy_type}", params=params)


@mcp.tool()
def create_selling_policy(policy_type: str, name: str, description: str = None,
                          **policy_details) -> Dict[str, Any]:
    """Create a new selling policy."""
    data = {"name": name}
    if description:
        data["description"] = description
    data.update(policy_details)
    return make_request("POST", f"/sell/account/v1/policy/{policy_type}", data=data)


@mcp.tool()
def update_selling_policy(policy_type: str, policy_id: str,
                          name: str = None, description: str = None,
                          **policy_details) -> Dict[str, Any]:
    """Update an existing selling policy."""
    updates = {}
    if name:
        updates["name"] = name
    if description:
        updates["description"] = description
    updates.update(policy_details)
    return make_request("PATCH", f"/sell/account/v1/policy/{policy_type}/{policy_id}", data=updates)


@mcp.tool()
def delete_selling_policy(policy_type: str, policy_id: str) -> Dict[str, Any]:
    """Delete a selling policy."""
    return make_request("DELETE", f"/sell/account/v1/policy/{policy_type}/{policy_id}")


# Payment Policies

@mcp.tool()
def create_payment_policy(name: str, description: str = None,
                          payment_instructions: str = None,
                          payment_methods: List[Dict] = None) -> Dict[str, Any]:
    """Create a new payment policy."""
    data = {"name": name}
    if description:
        data["description"] = description
    if payment_instructions:
        data["paymentInstructions"] = payment_instructions
    if payment_methods:
        data["paymentMethods"] = payment_methods
    return create_selling_policy("payment", name, description, **data)


@mcp.tool()
def get_payment_policy(policy_id: str) -> Dict[str, Any]:
    """Get payment policy by ID."""
    return get_selling_policy("payment", policy_id)


@mcp.tool()
def list_payment_policies(limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """List payment policies."""
    return list_selling_policies("payment", limit, offset)


# Shipping Policies

@mcp.tool()
def create_shipping_policy(name: str, description: str = None,
                           shipping_cost_calculations: List[Dict] = None,
                           international_shipping_cost_calculations: List[Dict] = None,
                           shipping_package_details: Dict = None) -> Dict[str, Any]:
    """Create a new shipping policy."""
    data = {"name": name}
    if description:
        data["description"] = description
    if shipping_cost_calculations:
        data["shippingCostCalculations"] = shipping_cost_calculations
    if international_shipping_cost_calculations:
        data["internationalShippingCostCalculations"] = international_shipping_cost_calculations
    if shipping_package_details:
        data["shippingPackageDetails"] = shipping_package_details
    return create_selling_policy("shipping", name, description, **data)


@mcp.tool()
def get_shipping_policy(policy_id: str) -> Dict[str, Any]:
    """Get shipping policy by ID."""
    return get_selling_policy("shipping", policy_id)


@mcp.tool()
def list_shipping_policies(limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """List shipping policies."""
    return list_selling_policies("shipping", limit, offset)


# Return Policies

@mcp.tool()
def create_return_policy(name: str, description: str = None,
                         refund_method: str = "MONEY_BACK",
                         return_shipping_cost_payer: str = "SELLER",
                         restocking_fee: Dict = None,
                         return_instructions: str = None,
                         returns_accepted: bool = True,
                         return_period: Dict = None) -> Dict[str, Any]:
    """Create a new return policy."""
    data = {"name": name, "refund": refund_method,
            "returnShippingCostPayer": return_shipping_cost_payer,
            "returnsAccepted": returns_accepted}
    if description:
        data["description"] = description
    if restocking_fee:
        data["restockingFee"] = restocking_fee
    if return_instructions:
        data["returnInstructions"] = return_instructions
    if return_period:
        data["returnPeriod"] = return_period
    return create_selling_policy("return", name, description, **data)


@mcp.tool()
def get_return_policy(policy_id: str) -> Dict[str, Any]:
    """Get return policy by ID."""
    return get_selling_policy("return", policy_id)


@mcp.tool()
def list_return_policies(limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """List return policies."""
    return list_selling_policies("return", limit, offset)


# ========== ACCOUNT API - PROGRAMS ==========

@mcp.tool()
def get_program(program_type: str, program_id: str) -> Dict[str, Any]:
    """Get a program by ID."""
    return make_request("GET", f"/sell/account/v1/program/{program_type}/{program_id}")


@mcp.tool()
def list_programs(program_type: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """List programs of a specific type."""
    params = {"limit": limit, "offset": offset}
    return make_request("GET", f"/sell/account/v1/program/{program_type}", params=params)


@mcp.tool()
def create_program(program_type: str, name: str, description: str = None,
                   **program_details) -> Dict[str, Any]:
    """Create a new program."""
    data = {"name": name}
    if description:
        data["description"] = description
    data.update(program_details)
    return make_request("POST", f"/sell/account/v1/program/{program_type}", data=data)


@mcp.tool()
def update_program(program_type: str, program_id: str,
                   name: str = None, description: str = None,
                   **program_details) -> Dict[str, Any]:
    """Update an existing program."""
    updates = {}
    if name:
        updates["name"] = name
    if description:
        updates["description"] = description
    updates.update(program_details)
    return make_request("PATCH", f"/sell/account/v1/program/{program_type}/{program_id}", data=updates)


@mcp.tool()
def delete_program(program_type: str, program_id: str) -> Dict[str, Any]:
    """Delete a program."""
    return make_request("DELETE", f"/sell/account/v1/program/{program_type}/{program_id}")


# ========== MARKETING API - PROMOTIONS ==========

@mcp.tool()
def get_promotion(promotion_id: str) -> Dict[str, Any]:
    """Get a single promotion by ID."""
    return make_request("GET", f"/sell/marketing/v1/promotion/{promotion_id}")


@mcp.tool()
def list_promotions(limit: int = 10, offset: int = 0, filter: str = None) -> Dict[str, Any]:
    """List promotions with pagination."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return make_request("GET", "/sell/marketing/v1/promotion", params=params)


@mcp.tool()
def create_promotion(name: str, description: str = None, promotion_type: str = "PROMOTIONAL_DISCOUNT",
                     incentive_type: str = "PERCENT_OFF", incentive_value: float = None,
                     qualifying_items: List[Dict] = None, start_date: str = None,
                     end_date: str = None) -> Dict[str, Any]:
    """Create a new promotion."""
    data = {"name": name, "promotionType": promotion_type, "incentiveType": incentive_type}
    if description:
        data["description"] = description
    if incentive_value is not None:
        data["incentiveValue"] = str(incentive_value)
    if qualifying_items:
        data["qualifyingItems"] = qualifying_items
    if start_date:
        data["startDate"] = start_date
    if end_date:
        data["endDate"] = end_date
    return make_request("POST", "/sell/marketing/v1/promotion", data=data)


@mcp.tool()
def update_promotion(promotion_id: str, name: str = None, description: str = None,
                     incentive_value: float = None, start_date: str = None,
                     end_date: str = None) -> Dict[str, Any]:
    """Update an existing promotion."""
    updates = {}
    if name:
        updates["name"] = name
    if description:
        updates["description"] = description
    if incentive_value is not None:
        updates["incentiveValue"] = str(incentive_value)
    if start_date:
        updates["startDate"] = start_date
    if end_date:
        updates["endDate"] = end_date
    return make_request("PATCH", f"/sell/marketing/v1/promotion/{promotion_id}", data=updates)


@mcp.tool()
def delete_promotion(promotion_id: str) -> Dict[str, Any]:
    """Delete a promotion."""
    return make_request("DELETE", f"/sell/marketing/v1/promotion/{promotion_id}")


# ========== MARKETING API - CAMPAIGNS ==========

@mcp.tool()
def get_campaign(campaign_id: str) -> Dict[str, Any]:
    """Get a single campaign by ID."""
    return make_request("GET", f"/sell/marketing/v1/campaign/{campaign_id}")


@mcp.tool()
def list_campaigns(limit: int = 10, offset: int = 0, filter: str = None,
                   status: str = None) -> Dict[str, Any]:
    """List campaigns with pagination."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if status:
        params["status"] = status
    return make_request("GET", "/sell/marketing/v1/campaign", params=params)


@mcp.tool()
def create_campaign(name: str, description: str = None, campaign_type: str = "ADVERTISED_ITEMS",
                    active: bool = True, budget: Dict = None, targeting: Dict = None,
                    ad_format: str = "BANNER") -> Dict[str, Any]:
    """Create a new campaign."""
    data = {"name": name, "campaignType": campaign_type, "active": active, "adFormat": ad_format}
    if description:
        data["description"] = description
    if budget:
        data["budget"] = budget
    if targeting:
        data["targeting"] = targeting
    return make_request("POST", "/sell/marketing/v1/campaign", data=data)


@mcp.tool()
def update_campaign(campaign_id: str, name: str = None, description: str = None,
                    active: bool = None, budget: Dict = None) -> Dict[str, Any]:
    """Update an existing campaign."""
    updates = {}
    if name is not None:
        updates["name"] = name
    if description is not None:
        updates["description"] = description
    if active is not None:
        updates["active"] = active
    if budget:
        updates["budget"] = budget
    return make_request("PATCH", f"/sell/marketing/v1/campaign/{campaign_id}", data=updates)


@mcp.tool()
def delete_campaign(campaign_id: str) -> Dict[str, Any]:
    """Delete a campaign."""
    return make_request("DELETE", f"/sell/marketing/v1/campaign/{campaign_id}")


# ========== FINANCES API ==========

@mcp.tool()
def get_transaction(transaction_id: str) -> Dict[str, Any]:
    """Get a single transaction by ID."""
    return make_request("GET", f"/sell/finances/v1/transaction/{transaction_id}")


@mcp.tool()
def list_transactions(limit: int = 10, offset: int = 0, filter: str = None,
                      start_date: str = None, end_date: str = None) -> Dict[str, Any]:
    """List transactions with pagination."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if start_date:
        params["startDate"] = start_date
    if end_date:
        params["endDate"] = end_date
    return make_request("GET", "/sell/finances/v1/transaction", params=params)


@mcp.tool()
def get_payout(payout_id: str) -> Dict[str, Any]:
    """Get a single payout by ID."""
    return make_request("GET", f"/sell/finances/v1/payout/{payout_id}")


@mcp.tool()
def list_payouts(limit: int = 10, offset: int = 0, filter: str = None,
                 start_date: str = None, end_date: str = None) -> Dict[str, Any]:
    """List payouts with pagination."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if start_date:
        params["startDate"] = start_date
    if end_date:
        params["endDate"] = end_date
    return make_request("GET", "/sell/finances/v1/payout", params=params)


@mcp.tool()
def get_fee_invoice(invoice_id: str) -> Dict[str, Any]:
    """Get a fee invoice by ID."""
    return make_request("GET", f"/sell/finances/v1/fee_invoice/{invoice_id}")


@mcp.tool()
def list_fee_invoices(limit: int = 10, offset: int = 0, filter: str = None,
                      start_date: str = None, end_date: str = None) -> Dict[str, Any]:
    """List fee invoices with pagination."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if start_date:
        params["startDate"] = start_date
    if end_date:
        params["endDate"] = end_date
    return make_request("GET", "/sell/finances/v1/fee_invoice", params=params)


# ========== FEED API ==========

@mcp.tool()
def get_feed(feed_type: str, feed_id: str) -> Dict[str, Any]:
    """Get a feed job by ID."""
    return make_request("GET", f"/sell/feed/v1/feed/{feed_type}/{feed_id}")


@mcp.tool()
def list_feeds(feed_type: str, limit: int = 10, offset: int = 0,
               filter: str = None, status: str = None) -> Dict[str, Any]:
    """List feed jobs with pagination."""
    params = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if status:
        params["status"] = status
    return make_request("GET", f"/sell/feed/v1/feed/{feed_type}", params=params)


@mcp.tool()
def create_inventory_feed(inventory_items: List[Dict] = None) -> Dict[str, Any]:
    """Create an inventory feed for bulk upload."""
    data = {"feedType": "INVENTORY", "inventoryItems": inventory_items or []}
    return make_request("POST", "/sell/feed/v1/feed/INVENTORY", data=data)


@mcp.tool()
def create_order_feed() -> Dict[str, Any]:
    """Create an order feed for bulk download."""
    data = {"feedType": "ORDER"}
    return make_request("POST", "/sell/feed/v1/feed/ORDER", data=data)


# ========== CATEGORY API ==========

@mcp.tool()
def get_category(category_id: str) -> Dict[str, Any]:
    """Get a single category by ID."""
    return make_request("GET", f"/sell/account/v1/category/{category_id}")


@mcp.tool()
def get_category_tree(tree_id: str = "1") -> Dict[str, Any]:
    """Get a category tree."""
    return make_request("GET", f"/sell/account/v1/category_tree/{tree_id}")


@mcp.tool()
def get_category_suggestions(query: str, category_tree_id: str = "1") -> Dict[str, Any]:
    """Get category suggestions for a query."""
    params = {"q": query, "category_tree_id": category_tree_id}
    return make_request("GET", "/sell/account/v1/category_suggestion", params=params)


@mcp.tool()
def get_requirements_for_category(category_id: str, action: str = "CREATE_ITEM") -> Dict[str, Any]:
    """Get requirements for a category."""
    params = {"action": action}
    return make_request("GET", f"/sell/account/v1/category/{category_id}/requirement", params=params)


# ========== TOOL LISTING ==========

@mcp.tool()
def list_tools() -> List[Dict[str, str]]:
    """List all available tools."""
    return [
        {"name": "get_item", "description": "Get a single item by ID"},
        {"name": "list_items", "description": "List items with pagination"},
        {"name": "create_item", "description": "Create a new item listing"},
        {"name": "update_item", "description": "Update an existing item listing"},
        {"name": "delete_item", "description": "Delete an item listing"},
        {"name": "revise_item_quantity", "description": "Revise item quantity"},
        {"name": "revise_item_price", "description": "Revise item price"},
        {"name": "get_inventory_location", "description": "Get inventory location by ID"},
        {"name": "list_inventory_locations", "description": "List inventory locations"},
        {"name": "create_inventory_location", "description": "Create inventory location"},
        {"name": "update_inventory_location", "description": "Update inventory location"},
        {"name": "get_offer", "description": "Get offer by ID"},
        {"name": "list_offers", "description": "List offers"},
        {"name": "create_offer", "description": "Create new offer"},
        {"name": "update_offer", "description": "Update offer"},
        {"name": "delete_offer", "description": "Delete offer"},
        {"name": "get_order", "description": "Get order by ID"},
        {"name": "list_orders", "description": "List orders"},
        {"name": "create_order", "description": "Create new order"},
        {"name": "update_order", "description": "Update order"},
        {"name": "complete_order", "description": "Mark order as completed"},
        {"name": "cancel_order", "description": "Cancel order"},
        {"name": "refund_order", "description": "Refund order"},
        {"name": "get_shipping_carrier", "description": "Get shipping carrier"},
        {"name": "list_shipping_carriers", "description": "List shipping carriers"},
        {"name": "get_shipping_service", "description": "Get shipping service"},
        {"name": "calculate_shipping", "description": "Calculate shipping cost"},
        {"name": "create_shipment", "description": "Create shipment"},
        {"name": "get_shipment", "description": "Get shipment details"},
        {"name": "list_shipments", "description": "List shipments"},
        {"name": "get_selling_policy", "description": "Get selling policy"},
        {"name": "list_selling_policies", "description": "List selling policies"},
        {"name": "create_selling_policy", "description": "Create selling policy"},
        {"name": "update_selling_policy", "description": "Update selling policy"},
        {"name": "delete_selling_policy", "description": "Delete selling policy"},
        {"name": "create_payment_policy", "description": "Create payment policy"},
        {"name": "get_payment_policy", "description": "Get payment policy"},
        {"name": "list_payment_policies", "description": "List payment policies"},
        {"name": "create_shipping_policy", "description": "Create shipping policy"},
        {"name": "get_shipping_policy", "description": "Get shipping policy"},
        {"name": "list_shipping_policies", "description": "List shipping policies"},
        {"name": "create_return_policy", "description": "Create return policy"},
        {"name": "get_return_policy", "description": "Get return policy"},
        {"name": "list_return_policies", "description": "List return policies"},
        {"name": "get_program", "description": "Get program by ID"},
        {"name": "list_programs", "description": "List programs"},
        {"name": "create_program", "description": "Create program"},
        {"name": "update_program", "description": "Update program"},
        {"name": "delete_program", "description": "Delete program"},
        {"name": "get_promotion", "description": "Get promotion by ID"},
        {"name": "list_promotions", "description": "List promotions"},
        {"name": "create_promotion", "description": "Create promotion"},
        {"name": "update_promotion", "description": "Update promotion"},
        {"name": "delete_promotion", "description": "Delete promotion"},
        {"name": "get_campaign", "description": "Get campaign by ID"},
        {"name": "list_campaigns", "description": "List campaigns"},
        {"name": "create_campaign", "description": "Create campaign"},
        {"name": "update_campaign", "description": "Update campaign"},
        {"name": "delete_campaign", "description": "Delete campaign"},
        {"name": "get_transaction", "description": "Get transaction by ID"},
        {"name": "list_transactions", "description": "List transactions"},
        {"name": "get_payout", "description": "Get payout by ID"},
        {"name": "list_payouts", "description": "List payouts"},
        {"name": "get_fee_invoice", "description": "Get fee invoice"},
        {"name": "list_fee_invoices", "description": "List fee invoices"},
        {"name": "get_feed", "description": "Get feed by ID"},
        {"name": "list_feeds", "description": "List feeds"},
        {"name": "create_inventory_feed", "description": "Create inventory feed"},
        {"name": "create_order_feed", "description": "Create order feed"},
        {"name": "get_category", "description": "Get category by ID"},
        {"name": "get_category_tree", "description": "Get category tree"},
        {"name": "get_category_suggestions", "description": "Get category suggestions"},
        {"name": "get_requirements_for_category", "description": "Get category requirements"},
        {"name": "list_tools", "description": "List all available tools"}
    ]


# Run the server
if __name__ == "__main__":
    mcp.run()
