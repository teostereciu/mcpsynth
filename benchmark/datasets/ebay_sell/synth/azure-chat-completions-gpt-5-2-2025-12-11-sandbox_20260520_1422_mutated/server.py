import base64
import json
import os
import time
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("ebay-sell")


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


def _base_url() -> str:
    env = (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
    return "https://api.ebay.com" if env == "PRODUCTION" else "https://api.sandbox.ebay.com"


class EbayAuth:
    def __init__(self) -> None:
        self._token: Optional[str] = None
        self._exp: float = 0.0

    def get_access_token(self) -> str:
        now = time.time()
        if self._token and now < self._exp - 60:
            return self._token

        app_id = _env("EBAY_APP_ID")
        cert_id = _env("EBAY_CERT_ID")
        refresh = _env("EBAY_REFRESH_TOKEN")
        if not app_id or not cert_id or not refresh:
            raise RuntimeError(
                "Missing EBAY_APP_ID/EBAY_CERT_ID/EBAY_REFRESH_TOKEN environment variables"
            )

        basic = base64.b64encode(f"{app_id}:{cert_id}".encode("utf-8")).decode("ascii")
        url = f"{_base_url()}/identity/v1/oauth2/token"
        headers = {
            "Authorization": f"Basic {basic}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh,
        }
        resp = requests.post(url, headers=headers, data=data, timeout=60)
        if resp.status_code >= 400:
            try:
                payload = resp.json()
            except Exception:
                payload = {"message": resp.text}
            raise RuntimeError({"error": "token_request_failed", "status": resp.status_code, "details": payload})

        payload = resp.json()
        self._token = payload.get("access_token")
        expires_in = float(payload.get("expires_in", 7200))
        self._exp = now + expires_in
        if not self._token:
            raise RuntimeError({"error": "token_missing", "details": payload})
        return self._token


_auth = EbayAuth()


def _request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    url = f"{_base_url()}{path}"
    h = {
        "Authorization": f"Bearer {_auth.get_access_token()}",
        "Accept": "application/json",
    }
    if headers:
        h.update({k: v for k, v in headers.items() if v is not None})

    try:
        resp = requests.request(method, url, params=params, json=json_body, headers=h, timeout=90)
    except Exception as e:
        return {"error": "request_failed", "details": str(e), "method": method, "url": url}

    # Some endpoints return 204 with empty body
    if resp.status_code == 204:
        return {"status": 204}

    content_type = resp.headers.get("Content-Type", "")
    is_json = "json" in content_type.lower()
    payload: Any
    if is_json:
        try:
            payload = resp.json()
        except Exception:
            payload = {"raw": resp.text}
    else:
        payload = {"raw": resp.text}

    if resp.status_code >= 400:
        return {
            "error": "ebay_api_error",
            "status": resp.status_code,
            "method": method,
            "path": path,
            "details": payload,
        }

    # Include headers that are often useful (Location, etc.)
    useful_headers = {}
    for k in ["Location", "Content-Location", "X-EBAY-CORRELATION-ID"]:
        if k in resp.headers:
            useful_headers[k] = resp.headers[k]

    if useful_headers:
        return {"status": resp.status_code, "headers": useful_headers, "data": payload}
    return payload if isinstance(payload, (dict, list)) else {"data": payload}


# ---------------- Inventory API (Sell Inventory v1) ----------------

@mcp.tool()
def inventory_create_or_replace_inventory_item(
    seller_sku: str,
    inventory_item: Dict[str, Any],
    content_language: str = "en-US",
) -> Dict[str, Any]:
    """PUT /sell/inventory/v1/inventory_item/{seller_sku}"""
    return _request(
        "PUT",
        f"/sell/inventory/v1/inventory_item/{seller_sku}",
        json_body=inventory_item,
        headers={"Content-Type": "application/json", "Content-Language": content_language},
    )


@mcp.tool()
def inventory_get_inventory_item(seller_sku: str) -> Dict[str, Any]:
    """GET /sell/inventory/v1/inventory_item/{seller_sku}"""
    return _request("GET", f"/sell/inventory/v1/inventory_item/{seller_sku}")


@mcp.tool()
def inventory_delete_inventory_item(seller_sku: str) -> Dict[str, Any]:
    """DELETE /sell/inventory/v1/inventory_item/{seller_sku}"""
    return _request("DELETE", f"/sell/inventory/v1/inventory_item/{seller_sku}")


@mcp.tool()
def inventory_get_inventory_items(limit: int = 25, offset: int = 0) -> Dict[str, Any]:
    """GET /sell/inventory/v1/inventory_item"""
    return _request("GET", "/sell/inventory/v1/inventory_item", params={"limit": str(limit), "offset": str(offset)})


@mcp.tool()
def inventory_create_offer(offer: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/inventory/v1/offer"""
    return _request(
        "POST",
        "/sell/inventory/v1/offer",
        json_body=offer,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def inventory_get_offer(offer_id: str) -> Dict[str, Any]:
    """GET /sell/inventory/v1/offer/{offer_id}"""
    return _request("GET", f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def inventory_update_offer(offer_id: str, offer: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/inventory/v1/offer/{offer_id}"""
    return _request(
        "PUT",
        f"/sell/inventory/v1/offer/{offer_id}",
        json_body=offer,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def inventory_delete_offer(offer_id: str) -> Dict[str, Any]:
    """DELETE /sell/inventory/v1/offer/{offer_id}"""
    return _request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def inventory_get_offers(
    sku: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    format: Optional[str] = None,
    limit: int = 25,
    offset: int = 0,
) -> Dict[str, Any]:
    """GET /sell/inventory/v1/offer"""
    params: Dict[str, Any] = {"limit": str(limit), "offset": str(offset)}
    if sku:
        params["sku"] = sku
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    if format:
        params["format"] = format
    return _request("GET", "/sell/inventory/v1/offer", params=params)


@mcp.tool()
def inventory_publish_offer(offer_id: str) -> Dict[str, Any]:
    """POST /sell/inventory/v1/offer/{offer_id}/publish"""
    return _request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish", headers={"Content-Type": "application/json"})


@mcp.tool()
def inventory_withdraw_offer(offer_id: str) -> Dict[str, Any]:
    """POST /sell/inventory/v1/offer/{offer_id}/withdraw"""
    return _request("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw", headers={"Content-Type": "application/json"})


@mcp.tool()
def inventory_get_listing_fees(offer_id: str) -> Dict[str, Any]:
    """GET /sell/inventory/v1/offer/{offer_id}/listing_fees"""
    return _request("GET", f"/sell/inventory/v1/offer/{offer_id}/listing_fees")


@mcp.tool()
def inventory_create_inventory_location(merchant_location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/inventory/v1/location/{merchantLocationKey}"""
    return _request(
        "POST",
        f"/sell/inventory/v1/location/{merchant_location_key}",
        json_body=location,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def inventory_get_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    """GET /sell/inventory/v1/location/{merchantLocationKey}"""
    return _request("GET", f"/sell/inventory/v1/location/{merchant_location_key}")


@mcp.tool()
def inventory_update_inventory_location(merchant_location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/inventory/v1/location/{merchantLocationKey}"""
    return _request(
        "PUT",
        f"/sell/inventory/v1/location/{merchant_location_key}",
        json_body=location,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def inventory_delete_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    """DELETE /sell/inventory/v1/location/{merchantLocationKey}"""
    return _request("DELETE", f"/sell/inventory/v1/location/{merchant_location_key}")


@mcp.tool()
def inventory_get_inventory_locations(limit: int = 25, offset: int = 0) -> Dict[str, Any]:
    """GET /sell/inventory/v1/location"""
    return _request("GET", "/sell/inventory/v1/location", params={"limit": str(limit), "offset": str(offset)})


@mcp.tool()
def inventory_enable_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    """POST /sell/inventory/v1/location/{merchantLocationKey}/enable"""
    return _request("POST", f"/sell/inventory/v1/location/{merchant_location_key}/enable", headers={"Content-Type": "application/json"})


@mcp.tool()
def inventory_disable_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    """POST /sell/inventory/v1/location/{merchantLocationKey}/disable"""
    return _request("POST", f"/sell/inventory/v1/location/{merchant_location_key}/disable", headers={"Content-Type": "application/json"})


@mcp.tool()
def inventory_bulk_update_price_quantity(request_body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/inventory/v1/bulk_update_price_quantity"""
    return _request(
        "POST",
        "/sell/inventory/v1/bulk_update_price_quantity",
        json_body=request_body,
        headers={"Content-Type": "application/json"},
    )


# ---------------- Fulfillment API (Sell Fulfillment v1) ----------------

@mcp.tool()
def fulfillment_get_orders(
    filter: Optional[str] = None,
    order_ids: Optional[str] = None,
    field_groups: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
) -> Dict[str, Any]:
    """GET /sell/fulfillment/v1/order"""
    params: Dict[str, Any] = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    if order_ids:
        params["orderIds"] = order_ids
    if field_groups:
        params["fieldGroups"] = field_groups
    return _request("GET", "/sell/fulfillment/v1/order", params=params)


@mcp.tool()
def fulfillment_get_order(order_id: str, field_groups: Optional[str] = None) -> Dict[str, Any]:
    """GET /sell/fulfillment/v1/order/{orderId}"""
    params = {"fieldGroups": field_groups} if field_groups else None
    return _request("GET", f"/sell/fulfillment/v1/order/{order_id}", params=params)


@mcp.tool()
def fulfillment_get_activities(filter: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """GET /sell/fulfillment/v1/order_activity"""
    params: Dict[str, Any] = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    return _request("GET", "/sell/fulfillment/v1/order_activity", params=params)


@mcp.tool()
def fulfillment_create_shipping_fulfillment(order_id: str, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/fulfillment/v1/order/{orderId}/shipping_fulfillment"""
    return _request(
        "POST",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment",
        json_body=fulfillment,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def fulfillment_get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    """GET /sell/fulfillment/v1/order/{orderId}/shipping_fulfillment"""
    return _request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")


@mcp.tool()
def fulfillment_get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> Dict[str, Any]:
    """GET /sell/fulfillment/v1/order/{orderId}/shipping_fulfillment/{fulfillmentId}"""
    return _request(
        "GET",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}",
    )


@mcp.tool()
def fulfillment_issue_refund(order_id: str, refund: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/fulfillment/v1/order/{orderId}/issue_refund"""
    return _request(
        "POST",
        f"/sell/fulfillment/v1/order/{order_id}/issue_refund",
        json_body=refund,
        headers={"Content-Type": "application/json"},
    )


# ---------------- Account API (Sell Account v1) ----------------

@mcp.tool()
def account_get_fulfillment_policies(marketplace_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/fulfillment_policy?marketplace_id={marketplace_id}"""
    return _request("GET", "/sell/account/v1/fulfillment_policy", params={"marketplace_id": marketplace_id})


@mcp.tool()
def account_get_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/fulfillment_policy/{fulfillmentPolicyId}"""
    return _request("GET", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


@mcp.tool()
def account_create_fulfillment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/account/v1/fulfillment_policy/"""
    return _request(
        "POST",
        "/sell/account/v1/fulfillment_policy/",
        json_body=policy,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def account_update_fulfillment_policy(fulfillment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/account/v1/fulfillment_policy/{fulfillmentPolicyId}"""
    return _request(
        "PUT",
        f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}",
        json_body=policy,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def account_delete_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
    """DELETE /sell/account/v1/fulfillment_policy/{fulfillmentPolicyId}"""
    return _request("DELETE", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


@mcp.tool()
def account_get_payment_policies(marketplace_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/payment_policy?marketplace_id={marketplace_id}"""
    return _request("GET", "/sell/account/v1/payment_policy", params={"marketplace_id": marketplace_id})


@mcp.tool()
def account_get_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/payment_policy/{paymentPolicyId}"""
    return _request("GET", f"/sell/account/v1/payment_policy/{payment_policy_id}")


@mcp.tool()
def account_create_payment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/account/v1/payment_policy/"""
    return _request(
        "POST",
        "/sell/account/v1/payment_policy/",
        json_body=policy,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def account_update_payment_policy(payment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/account/v1/payment_policy/{paymentPolicyId}"""
    return _request(
        "PUT",
        f"/sell/account/v1/payment_policy/{payment_policy_id}",
        json_body=policy,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def account_delete_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    """DELETE /sell/account/v1/payment_policy/{paymentPolicyId}"""
    return _request("DELETE", f"/sell/account/v1/payment_policy/{payment_policy_id}")


@mcp.tool()
def account_get_return_policies(marketplace_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/return_policy?marketplace_id={marketplace_id}"""
    return _request("GET", "/sell/account/v1/return_policy", params={"marketplace_id": marketplace_id})


@mcp.tool()
def account_get_return_policy(return_policy_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/return_policy/{returnPolicyId}"""
    return _request("GET", f"/sell/account/v1/return_policy/{return_policy_id}")


@mcp.tool()
def account_create_return_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/account/v1/return_policy/"""
    return _request(
        "POST",
        "/sell/account/v1/return_policy/",
        json_body=policy,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def account_update_return_policy(return_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/account/v1/return_policy/{returnPolicyId}"""
    return _request(
        "PUT",
        f"/sell/account/v1/return_policy/{return_policy_id}",
        json_body=policy,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def account_delete_return_policy(return_policy_id: str) -> Dict[str, Any]:
    """DELETE /sell/account/v1/return_policy/{returnPolicyId}"""
    return _request("DELETE", f"/sell/account/v1/return_policy/{return_policy_id}")


@mcp.tool()
def account_get_sales_taxes(marketplace_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/sales_tax?marketplace_id={marketplace_id}"""
    return _request("GET", "/sell/account/v1/sales_tax", params={"marketplace_id": marketplace_id})


@mcp.tool()
def account_get_sales_tax(sales_tax_jurisdiction_id: str, marketplace_id: str) -> Dict[str, Any]:
    """GET /sell/account/v1/sales_tax/{salesTaxJurisdictionId}?marketplace_id={marketplace_id}"""
    return _request(
        "GET",
        f"/sell/account/v1/sales_tax/{sales_tax_jurisdiction_id}",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def account_create_or_replace_sales_tax(
    sales_tax_jurisdiction_id: str, marketplace_id: str, sales_tax: Dict[str, Any]
) -> Dict[str, Any]:
    """PUT /sell/account/v1/sales_tax/{salesTaxJurisdictionId}?marketplace_id={marketplace_id}"""
    return _request(
        "PUT",
        f"/sell/account/v1/sales_tax/{sales_tax_jurisdiction_id}",
        params={"marketplace_id": marketplace_id},
        json_body=sales_tax,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def account_delete_sales_tax(sales_tax_jurisdiction_id: str, marketplace_id: str) -> Dict[str, Any]:
    """DELETE /sell/account/v1/sales_tax/{salesTaxJurisdictionId}?marketplace_id={marketplace_id}"""
    return _request(
        "DELETE",
        f"/sell/account/v1/sales_tax/{sales_tax_jurisdiction_id}",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def account_get_privileges() -> Dict[str, Any]:
    """GET /sell/account/v1/privilege"""
    return _request("GET", "/sell/account/v1/privilege")


@mcp.tool()
def account_get_subscription() -> Dict[str, Any]:
    """GET /sell/account/v1/subscription"""
    return _request("GET", "/sell/account/v1/subscription")


# ---------------- Marketing API (Sell Marketing v1) ----------------

@mcp.tool()
def marketing_get_campaigns(
    campaign_title: Optional[str] = None,
    campaign_status: Optional[str] = None,
    channels: Optional[str] = None,
    funding_strategy: Optional[str] = None,
    start_date_range: Optional[str] = None,
    end_date_range: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
) -> Dict[str, Any]:
    """GET /sell/marketing/v1/ad_campaign"""
    params: Dict[str, Any] = {"limit": str(limit), "offset": str(offset)}
    if campaign_title:
        params["campaign_title"] = campaign_title
    if campaign_status:
        params["campaign_status"] = campaign_status
    if channels:
        params["channels"] = channels
    if funding_strategy:
        params["funding_strategy"] = funding_strategy
    if start_date_range:
        params["start_date_range"] = start_date_range
    if end_date_range:
        params["end_date_range"] = end_date_range
    return _request("GET", "/sell/marketing/v1/ad_campaign", params=params)


@mcp.tool()
def marketing_get_campaign(campaign_id: str) -> Dict[str, Any]:
    """GET /sell/marketing/v1/ad_campaign/{campaign_id}"""
    return _request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


@mcp.tool()
def marketing_clone_campaign(campaign_id: str, clone_request: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/marketing/v1/ad_campaign/{campaign_id}/clone"""
    return _request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/clone",
        json_body=clone_request,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def marketing_delete_campaign(campaign_id: str) -> Dict[str, Any]:
    """DELETE /sell/marketing/v1/ad_campaign/{campaign_id}"""
    return _request("DELETE", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


@mcp.tool()
def marketing_create_ad_group(campaign_id: str, ad_group: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/marketing/v1/ad_campaign/{campaign_id}/ad_group"""
    return _request(
        "POST",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group",
        json_body=ad_group,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def marketing_get_ad_groups(campaign_id: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    """GET /sell/marketing/v1/ad_campaign/{campaign_id}/ad_group"""
    return _request(
        "GET",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group",
        params={"limit": str(limit), "offset": str(offset)},
    )


@mcp.tool()
def marketing_get_ad_group(campaign_id: str, ad_group_id: str) -> Dict[str, Any]:
    """GET /sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}"""
    return _request(
        "GET",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}",
    )


@mcp.tool()
def marketing_update_ad_group(campaign_id: str, ad_group_id: str, ad_group: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}"""
    return _request(
        "PUT",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}",
        json_body=ad_group,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def marketing_get_ads(
    campaign_id: Optional[str] = None,
    ad_group_id: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
) -> Dict[str, Any]:
    """GET /sell/marketing/v1/ad"""
    params: Dict[str, Any] = {"limit": str(limit), "offset": str(offset)}
    if campaign_id:
        params["campaign_id"] = campaign_id
    if ad_group_id:
        params["ad_group_id"] = ad_group_id
    return _request("GET", "/sell/marketing/v1/ad", params=params)


@mcp.tool()
def marketing_get_ad(ad_id: str) -> Dict[str, Any]:
    """GET /sell/marketing/v1/ad/{ad_id}"""
    return _request("GET", f"/sell/marketing/v1/ad/{ad_id}")


@mcp.tool()
def marketing_create_ad_by_listing_id(ad: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/marketing/v1/ad"""
    return _request("POST", "/sell/marketing/v1/ad", json_body=ad, headers={"Content-Type": "application/json"})


@mcp.tool()
def marketing_delete_ad(ad_id: str) -> Dict[str, Any]:
    """DELETE /sell/marketing/v1/ad/{ad_id}"""
    return _request("DELETE", f"/sell/marketing/v1/ad/{ad_id}")


@mcp.tool()
def marketing_update_bid(ad_id: str, bid: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /sell/marketing/v1/ad/{ad_id}/bid"""
    return _request(
        "PUT",
        f"/sell/marketing/v1/ad/{ad_id}/bid",
        json_body=bid,
        headers={"Content-Type": "application/json"},
    )


# ---------------- Finances API (Sell Finances v1) ----------------

@mcp.tool()
def finances_get_transactions(
    filter: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /sell/finances/v1/transaction"""
    params: Dict[str, Any] = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return _request("GET", "/sell/finances/v1/transaction", params=params)


@mcp.tool()
def finances_get_transaction_summary(filter: Optional[str] = None) -> Dict[str, Any]:
    """GET /sell/finances/v1/transaction_summary"""
    params = {"filter": filter} if filter else None
    return _request("GET", "/sell/finances/v1/transaction_summary", params=params)


@mcp.tool()
def finances_get_payouts(filter: Optional[str] = None, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """GET /sell/finances/v1/payout"""
    params: Dict[str, Any] = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    return _request("GET", "/sell/finances/v1/payout", params=params)


@mcp.tool()
def finances_get_payout(payout_id: str) -> Dict[str, Any]:
    """GET /sell/finances/v1/payout/{payout_id}"""
    return _request("GET", f"/sell/finances/v1/payout/{payout_id}")


@mcp.tool()
def finances_get_payout_summary() -> Dict[str, Any]:
    """GET /sell/finances/v1/payout_summary"""
    return _request("GET", "/sell/finances/v1/payout_summary")


@mcp.tool()
def finances_get_billing_activities(filter: Optional[str] = None, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """GET /sell/finances/v1/billing_activity"""
    params: Dict[str, Any] = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    return _request("GET", "/sell/finances/v1/billing_activity", params=params)


# ---------------- Feed API (Sell Feed v1) ----------------

@mcp.tool()
def feed_create_task(
    marketplace_id: str,
    task: Dict[str, Any],
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /sell/feed/v1/task"""
    headers = {"Content-Type": "application/json", "X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if accept_language:
        headers["Accept-Language"] = accept_language
    return _request("POST", "/sell/feed/v1/task", json_body=task, headers=headers)


@mcp.tool()
def feed_get_task(task_id: str) -> Dict[str, Any]:
    """GET /sell/feed/v1/task/{task_id}"""
    return _request("GET", f"/sell/feed/v1/task/{task_id}")


@mcp.tool()
def feed_get_tasks(feed_type: Optional[str] = None, limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """GET /sell/feed/v1/task"""
    params: Dict[str, Any] = {"limit": str(limit), "offset": str(offset)}
    if feed_type:
        params["feed_type"] = feed_type
    return _request("GET", "/sell/feed/v1/task", params=params)


@mcp.tool()
def feed_get_input_file(task_id: str) -> Dict[str, Any]:
    """GET /sell/feed/v1/task/{task_id}/input_file"""
    return _request("GET", f"/sell/feed/v1/task/{task_id}/input_file")


@mcp.tool()
def feed_get_result_file(task_id: str) -> Dict[str, Any]:
    """GET /sell/feed/v1/task/{task_id}/result_file"""
    return _request("GET", f"/sell/feed/v1/task/{task_id}/result_file")


@mcp.tool()
def feed_get_latest_result_file(task_id: str) -> Dict[str, Any]:
    """GET /sell/feed/v1/task/{task_id}/latest_result_file"""
    return _request("GET", f"/sell/feed/v1/task/{task_id}/latest_result_file")


# ---------------- Metadata API (Sell Metadata v1) ----------------

@mcp.tool()
def metadata_get_currencies() -> Dict[str, Any]:
    """GET /sell/metadata/v1/currency"""
    return _request("GET", "/sell/metadata/v1/currency")


@mcp.tool()
def metadata_get_category_policies(marketplace_id: str, category_id: str) -> Dict[str, Any]:
    """GET /sell/metadata/v1/category_tree/{categoryTreeId}/get_category_policies"""
    # Docs in this workspace cover get-category-policies but not category tree discovery; accept categoryTreeId as marketplace_id for simplicity is wrong.
    # Instead, use the documented endpoint directly: /get_category_policies?marketplace_id&category_id
    return _request(
        "GET",
        "/sell/metadata/v1/category_tree/0/get_category_policies",
        params={"marketplace_id": marketplace_id, "category_id": category_id},
    )


# ---------------- Stores API (Sell Stores v1) ----------------

@mcp.tool()
def stores_get_store() -> Dict[str, Any]:
    """GET /sell/stores/v1/store"""
    return _request("GET", "/sell/stores/v1/store")


@mcp.tool()
def stores_get_store_categories() -> Dict[str, Any]:
    """GET /sell/stores/v1/store/category"""
    return _request("GET", "/sell/stores/v1/store/category")


@mcp.tool()
def stores_add_store_category(category: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/stores/v1/store/category"""
    return _request(
        "POST",
        "/sell/stores/v1/store/category",
        json_body=category,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def stores_delete_store_category(category_id: str) -> Dict[str, Any]:
    """DELETE /sell/stores/v1/store/category/{category_id}"""
    return _request("DELETE", f"/sell/stores/v1/store/category/{category_id}")


@mcp.tool()
def stores_rename_store_category(category_id: str, rename_request: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/stores/v1/store/category/{category_id}/rename"""
    return _request(
        "POST",
        f"/sell/stores/v1/store/category/{category_id}/rename",
        json_body=rename_request,
        headers={"Content-Type": "application/json"},
    )


@mcp.tool()
def stores_move_store_category(category_id: str, move_request: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/stores/v1/store/category/{category_id}/move"""
    return _request(
        "POST",
        f"/sell/stores/v1/store/category/{category_id}/move",
        json_body=move_request,
        headers={"Content-Type": "application/json"},
    )


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
