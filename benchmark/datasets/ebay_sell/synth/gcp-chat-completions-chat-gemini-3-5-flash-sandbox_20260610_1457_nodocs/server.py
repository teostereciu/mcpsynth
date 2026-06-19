import os
import time
import base64
import requests
from typing import Optional, Dict, Any
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("eBay Sell API MCP Server")

class EbayClient:
    def __init__(self):
        self.app_id = os.environ.get("EBAY_APP_ID")
        self.cert_id = os.environ.get("EBAY_CERT_ID")
        self.refresh_token = os.environ.get("EBAY_REFRESH_TOKEN")
        self.environment = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
        
        if self.environment == "PRODUCTION":
            self.base_url = "https://api.ebay.com"
        else:
            self.base_url = "https://api.sandbox.ebay.com"
            
        self._access_token = None
        self._token_expires_at = 0

    def get_access_token(self) -> str:
        # Check if token is still valid (with 1-minute buffer)
        if self._access_token and time.time() < self._token_expires_at - 60:
            return self._access_token

        if not self.app_id or not self.cert_id or not self.refresh_token:
            raise ValueError("Missing eBay credentials in environment variables (EBAY_APP_ID, EBAY_CERT_ID, EBAY_REFRESH_TOKEN)")

        url = f"{self.base_url}/identity/v1/oauth2/token"
        auth_str = f"{self.app_id}:{self.cert_id}"
        auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {auth_b64}"
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }
        
        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            raise Exception(f"Failed to refresh access token: {response.status_code} {response.text}")
            
        res_data = response.json()
        self._access_token = res_data["access_token"]
        self._token_expires_at = time.time() + res_data.get("expires_in", 7200)
        return self._access_token

    def request(self, method: str, path: str, params: Optional[Dict[str, Any]] = None, json_data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        try:
            token = self.get_access_token()
        except Exception as e:
            return {"error": f"Authentication failed: {str(e)}"}

        url = f"{self.base_url}{path}"
        req_headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        if headers:
            req_headers.update(headers)

        try:
            response = requests.request(method, url, params=params, json=json_data, headers=req_headers)
            if response.status_code == 204:
                return {"success": True, "status_code": 204}
            
            try:
                res_data = response.json()
            except ValueError:
                res_data = {"text": response.text}

            if response.status_code >= 400:
                return {
                    "error": f"HTTP {response.status_code}",
                    "details": res_data
                }
            return res_data
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}

# Instantiate the eBay client
client = EbayClient()


# ==========================================
# INVENTORY API
# ==========================================

@mcp.tool()
def get_inventory_item(sku: str) -> Dict[str, Any]:
    """
    Retrieve the details of an existing inventory item by SKU.
    
    :param sku: The seller-defined SKU of the inventory item.
    """
    return client.request("GET", f"/sell/inventory/v1/inventory_item/{sku}")


@mcp.tool()
def create_or_replace_inventory_item(sku: str, body: Dict[str, Any], content_language: str = "en-US") -> Dict[str, Any]:
    """
    Create a new inventory item or replace an existing inventory item.
    
    :param sku: The seller-defined SKU of the inventory item.
    :param body: The inventory item details (product, availability, condition, etc.).
    :param content_language: The language of the content (e.g., 'en-US', 'en-GB').
    """
    headers = {"Content-Language": content_language}
    return client.request("PUT", f"/sell/inventory/v1/inventory_item/{sku}", json_data=body, headers=headers)


@mcp.tool()
def delete_inventory_item(sku: str) -> Dict[str, Any]:
    """
    Delete an inventory item by SKU.
    
    :param sku: The seller-defined SKU of the inventory item.
    """
    return client.request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")


@mcp.tool()
def get_inventory_items(limit: int = 100, offset: int = 0) -> Dict[str, Any]:
    """
    Retrieve a list of inventory items.
    
    :param limit: The maximum number of items to return.
    :param offset: The number of items to skip.
    """
    params = {"limit": limit, "offset": offset}
    return client.request("GET", "/sell/inventory/v1/inventory_item", params=params)


@mcp.tool()
def get_inventory_item_group(inventory_item_group_key: str) -> Dict[str, Any]:
    """
    Retrieve the details of an existing inventory item group (variation group).
    
    :param inventory_item_group_key: The seller-defined key of the inventory item group.
    """
    return client.request("GET", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")


@mcp.tool()
def create_or_replace_inventory_item_group(inventory_item_group_key: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create or replace an inventory item group (variation group).
    
    :param inventory_item_group_key: The seller-defined key of the inventory item group.
    :param body: The inventory item group details (title, description, aspect brands, etc.).
    """
    return client.request("PUT", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}", json_data=body)


@mcp.tool()
def delete_inventory_item_group(inventory_item_group_key: str) -> Dict[str, Any]:
    """
    Delete an inventory item group.
    
    :param inventory_item_group_key: The seller-defined key of the inventory item group.
    """
    return client.request("DELETE", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")


@mcp.tool()
def get_offers(sku: Optional[str] = None, limit: int = 100, offset: int = 0, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Retrieve a list of offers.
    
    :param sku: Filter offers by SKU.
    :param limit: The maximum number of offers to return.
    :param offset: The number of offers to skip.
    :param marketplace_id: Filter offers by eBay marketplace ID (e.g., 'EBAY_US').
    """
    params = {"limit": limit, "offset": offset}
    if sku:
        params["sku"] = sku
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    return client.request("GET", "/sell/inventory/v1/offer", params=params)


@mcp.tool()
def get_offer(offer_id: str) -> Dict[str, Any]:
    """
    Retrieve the details of an existing offer.
    
    :param offer_id: The unique identifier of the offer.
    """
    return client.request("GET", f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def create_offer(body: Dict[str, Any], content_language: str = "en-US") -> Dict[str, Any]:
    """
    Create a new offer for a specific SKU.
    
    :param body: The offer details (sku, marketplaceId, format, pricing, listingPolicies, etc.).
    :param content_language: The language of the content (e.g., 'en-US').
    """
    headers = {"Content-Language": content_language}
    return client.request("POST", "/sell/inventory/v1/offer", json_data=body, headers=headers)


@mcp.tool()
def update_offer(offer_id: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """
    Update an existing offer.
    
    :param offer_id: The unique identifier of the offer.
    :param body: The updated offer details.
    """
    return client.request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json_data=body)


@mcp.tool()
def delete_offer(offer_id: str) -> Dict[str, Any]:
    """
    Delete an existing offer.
    
    :param offer_id: The unique identifier of the offer.
    """
    return client.request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def publish_offer(offer_id: str) -> Dict[str, Any]:
    """
    Publish an existing offer to make it an active listing on eBay.
    
    :param offer_id: The unique identifier of the offer.
    """
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")


@mcp.tool()
def get_locations(limit: int = 100, offset: int = 0) -> Dict[str, Any]:
    """
    Retrieve a list of inventory locations.
    
    :param limit: The maximum number of locations to return.
    :param offset: The number of locations to skip.
    """
    params = {"limit": limit, "offset": offset}
    return client.request("GET", "/sell/inventory/v1/location", params=params)


@mcp.tool()
def get_location(merchant_location_key: str) -> Dict[str, Any]:
    """
    Retrieve details of a specific inventory location.
    
    :param merchant_location_key: The seller-defined key of the location.
    """
    return client.request("GET", f"/sell/inventory/v1/location/{merchant_location_key}")


@mcp.tool()
def create_or_replace_location(merchant_location_key: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create or replace an inventory location.
    
    :param merchant_location_key: The seller-defined key of the location.
    :param body: The location details (name, address, locationWebUrl, etc.).
    """
    return client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}", json_data=body)


@mcp.tool()
def delete_location(merchant_location_key: str) -> Dict[str, Any]:
    """
    Delete an inventory location.
    
    :param merchant_location_key: The seller-defined key of the location.
    """
    return client.request("DELETE", f"/sell/inventory/v1/location/{merchant_location_key}")


# ==========================================
# FULFILLMENT API
# ==========================================

@mcp.tool()
def get_orders(order_ids: Optional[str] = None, filter_query: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """
    Retrieve details of orders.
    
    :param order_ids: A comma-separated list of order IDs.
    :param filter_query: Filter criteria (e.g., 'creationdate:[2023-01-01T00:00:00Z..]').
    :param limit: The maximum number of orders to return.
    :param offset: The number of orders to skip.
    """
    params = {"limit": limit, "offset": offset}
    if order_ids:
        params["orderIds"] = order_ids
    if filter_query:
        params["filter"] = filter_query
    return client.request("GET", "/sell/fulfillment/v1/order", params=params)


@mcp.tool()
def get_order(order_id: str) -> Dict[str, Any]:
    """
    Retrieve details of a specific order.
    
    :param order_id: The unique identifier of the order.
    """
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}")


@mcp.tool()
def create_shipping_fulfillment(order_id: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a shipping fulfillment (shipment) for an order.
    
    :param order_id: The unique identifier of the order.
    :param body: Fulfillment details (trackingNumber, shippingCarrierCode, lineItems, etc.).
    """
    return client.request("POST", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment", json_data=body)


@mcp.tool()
def get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    """
    Retrieve shipping fulfillments for an order.
    
    :param order_id: The unique identifier of the order.
    """
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")


# ==========================================
# ACCOUNT API
# ==========================================

@mcp.tool()
def get_fulfillment_policies(marketplace_id: str, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
    """
    Retrieve fulfillment policies for a marketplace.
    
    :param marketplace_id: The eBay marketplace ID (e.g., 'EBAY_US').
    :param limit: The maximum number of policies to return.
    :param offset: The number of policies to skip.
    """
    params = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    return client.request("GET", "/sell/account/v1/fulfillment_policy", params=params)


@mcp.tool()
def get_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    """
    Retrieve details of a specific fulfillment policy.
    
    :param fulfillment_policy_id: The unique identifier of the fulfillment policy.
    """
    return client.request("GET", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


@mcp.tool()
def get_payment_policies(marketplace_id: str, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
    """
    Retrieve payment policies for a marketplace.
    
    :param marketplace_id: The eBay marketplace ID (e.g., 'EBAY_US').
    :param limit: The maximum number of policies to return.
    :param offset: The number of policies to skip.
    """
    params = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    return client.request("GET", "/sell/account/v1/payment_policy", params=params)


@mcp.tool()
def get_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    """
    Retrieve details of a specific payment policy.
    
    :param payment_policy_id: The unique identifier of the payment policy.
    """
    return client.request("GET", f"/sell/account/v1/payment_policy/{payment_policy_id}")


@mcp.tool()
def get_return_policies(marketplace_id: str, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
    """
    Retrieve return policies for a marketplace.
    
    :param marketplace_id: The eBay marketplace ID (e.g., 'EBAY_US').
    :param limit: The maximum number of policies to return.
    :param offset: The number of policies to skip.
    """
    params = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    return client.request("GET", "/sell/account/v1/return_policy", params=params)


@mcp.tool()
def get_return_policy(return_policy_id: str) -> Dict[str, Any]:
    """
    Retrieve details of a specific return policy.
    
    :param return_policy_id: The unique identifier of the return policy.
    """
    return client.request("GET", f"/sell/account/v1/return_policy/{return_policy_id}")


@mcp.tool()
def get_sales_taxes(country_code: str) -> Dict[str, Any]:
    """
    Retrieve sales tax tables for a country.
    
    :param country_code: The two-letter ISO 3166 country code (e.g., 'US').
    """
    params = {"country_code": country_code}
    return client.request("GET", "/sell/account/v1/sales_tax", params=params)


@mcp.tool()
def get_sales_tax(country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
    """
    Retrieve details of a sales tax configuration for a jurisdiction.
    
    :param country_code: The two-letter ISO 3166 country code (e.g., 'US').
    :param jurisdiction_id: The unique identifier of the tax jurisdiction.
    """
    return client.request("GET", f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")


@mcp.tool()
def create_or_replace_sales_tax(country_code: str, jurisdiction_id: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create or replace a sales tax configuration for a jurisdiction.
    
    :param country_code: The two-letter ISO 3166 country code (e.g., 'US').
    :param jurisdiction_id: The unique identifier of the tax jurisdiction.
    :param body: Sales tax details (salesTaxPercentage, shippingAndHandlingTaxed, etc.).
    """
    return client.request("PUT", f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}", json_data=body)


@mcp.tool()
def delete_sales_tax(country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
    """
    Delete a sales tax configuration for a jurisdiction.
    
    :param country_code: The two-letter ISO 3166 country code (e.g., 'US').
    :param jurisdiction_id: The unique identifier of the tax jurisdiction.
    """
    return client.request("DELETE", f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")


# ==========================================
# MARKETING API
# ==========================================

@mcp.tool()
def get_campaigns(marketplace_id: Optional[str] = None, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
    """
    Retrieve details of marketing campaigns.
    
    :param marketplace_id: Filter campaigns by eBay marketplace ID (e.g., 'EBAY_US').
    :param limit: The maximum number of campaigns to return.
    :param offset: The number of campaigns to skip.
    """
    params = {"limit": limit, "offset": offset}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    return client.request("GET", "/sell/marketing/v1/campaign", params=params)


@mcp.tool()
def get_campaign(campaign_id: str) -> Dict[str, Any]:
    """
    Retrieve details of a specific marketing campaign.
    
    :param campaign_id: The unique identifier of the campaign.
    """
    return client.request("GET", f"/sell/marketing/v1/campaign/{campaign_id}")


@mcp.tool()
def create_campaign(body: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a marketing campaign.
    
    :param body: Campaign details (campaignName, startDate, endDate, marketplaceId, fundingStrategy, etc.).
    """
    return client.request("POST", "/sell/marketing/v1/campaign", json_data=body)


@mcp.tool()
def get_promotions(marketplace_id: str, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
    """
    Retrieve details of promotions for a marketplace.
    
    :param marketplace_id: The eBay marketplace ID (e.g., 'EBAY_US').
    :param limit: The maximum number of promotions to return.
    :param offset: The number of promotions to skip.
    """
    params = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    return client.request("GET", "/sell/marketing/v1/promotion", params=params)


@mcp.tool()
def get_promotion(promotion_id: str) -> Dict[str, Any]:
    """
    Retrieve details of a specific promotion.
    
    :param promotion_id: The unique identifier of the promotion.
    """
    return client.request("GET", f"/sell/marketing/v1/promotion/{promotion_id}")


# ==========================================
# FINANCES API
# ==========================================

@mcp.tool()
def get_transactions(limit: int = 100, offset: int = 0, filter_query: Optional[str] = None) -> Dict[str, Any]:
    """
    Retrieve details of financial transactions.
    
    :param limit: The maximum number of transactions to return.
    :param offset: The number of transactions to skip.
    :param filter_query: Filter criteria (e.g., 'transactionDate:[2023-01-01T00:00:00Z..]').
    """
    params = {"limit": limit, "offset": offset}
    if filter_query:
        params["filter"] = filter_query
    return client.request("GET", "/sell/finances/v1/transaction", params=params)


@mcp.tool()
def get_payouts(limit: int = 100, offset: int = 0, filter_query: Optional[str] = None) -> Dict[str, Any]:
    """
    Retrieve details of payouts.
    
    :param limit: The maximum number of payouts to return.
    :param offset: The number of payouts to skip.
    :param filter_query: Filter criteria (e.g., 'payoutStatus:{INITIATED|SUCCEEDED}').
    """
    params = {"limit": limit, "offset": offset}
    if filter_query:
        params["filter"] = filter_query
    return client.request("GET", "/sell/finances/v1/payout", params=params)


@mcp.tool()
def get_payout(payout_id: str) -> Dict[str, Any]:
    """
    Retrieve details of a specific payout.
    
    :param payout_id: The unique identifier of the payout.
    """
    return client.request("GET", f"/sell/finances/v1/payout/{payout_id}")


# ==========================================
# FEED API
# ==========================================

@mcp.tool()
def get_feed_tasks(limit: int = 100, offset: int = 0, filter_query: Optional[str] = None) -> Dict[str, Any]:
    """
    Retrieve details of feed tasks.
    
    :param limit: The maximum number of tasks to return.
    :param offset: The number of tasks to skip.
    :param filter_query: Filter criteria (e.g., 'feedType:{LMS_ACTIVE_INVENTORY_REPORT}').
    """
    params = {"limit": limit, "offset": offset}
    if filter_query:
        params["filter"] = filter_query
    return client.request("GET", "/sell/feed/v1/task", params=params)


@mcp.tool()
def get_feed_task(task_id: str) -> Dict[str, Any]:
    """
    Retrieve details of a specific feed task.
    
    :param task_id: The unique identifier of the feed task.
    """
    return client.request("GET", f"/sell/feed/v1/task/{task_id}")


@mcp.tool()
def create_feed_task(body: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a new feed task.
    
    :param body: Feed task details (feedType, schemaVersion, marketplaceId, etc.).
    """
    return client.request("POST", "/sell/feed/v1/task", json_data=body)


if __name__ == "__main__":
    mcp.run()
