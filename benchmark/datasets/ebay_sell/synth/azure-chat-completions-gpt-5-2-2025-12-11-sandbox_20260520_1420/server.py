import os
import json
import re
from typing import Any, Dict, Optional

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("ebay-sell")

DEFAULT_BASE_URL = os.getenv("EBAY_SELL_BASE_URL", "https://api.ebay.com/sell")


def _clean_none(d: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if v is not None}


def _parse_headers(headers_json: Optional[str]) -> Dict[str, str]:
    if not headers_json:
        return {}
    if isinstance(headers_json, dict):
        return {str(k): str(v) for k, v in headers_json.items()}
    try:
        obj = json.loads(headers_json)
        if isinstance(obj, dict):
            return {str(k): str(v) for k, v in obj.items()}
    except Exception:
        pass
    raise ValueError("headers_json must be a JSON object string")


def _parse_query(query_json: Optional[str]) -> Dict[str, Any]:
    if not query_json:
        return {}
    if isinstance(query_json, dict):
        return query_json
    try:
        obj = json.loads(query_json)
        if isinstance(obj, dict):
            return obj
    except Exception:
        pass
    raise ValueError("query_json must be a JSON object string")


def _parse_body(body_json: Optional[str]) -> Any:
    if body_json is None or body_json == "":
        return None
    if isinstance(body_json, (dict, list)):
        return body_json
    try:
        return json.loads(body_json)
    except Exception:
        # allow raw string bodies
        return body_json


def _token_from_env() -> str:
    token = os.getenv("EBAY_OAUTH_TOKEN") or os.getenv("EBAY_ACCESS_TOKEN")
    if not token:
        raise ValueError(
            "Missing OAuth token. Set EBAY_OAUTH_TOKEN (or EBAY_ACCESS_TOKEN) env var."
        )
    return token


def _base_url_for_api(api: str) -> str:
    api = api.strip().lower()
    # docs show endpoints like /inventory_item (Inventory API v1), /order/... (Fulfillment), etc.
    # Use /sell/{api}/v1 as base.
    return f"{DEFAULT_BASE_URL}/{api}/v1"


async def _request(
    api: str,
    method: str,
    path: str,
    *,
    query: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    body: Any = None,
    timeout_s: float = 60.0,
) -> Dict[str, Any]:
    token = _token_from_env()
    base = _base_url_for_api(api)
    if not path.startswith("/"):
        path = "/" + path
    url = base + path

    req_headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if headers:
        req_headers.update({k: str(v) for k, v in headers.items()})

    # If body is dict/list and content-type not set, set JSON
    json_body = None
    data_body = None
    files = None

    ct = None
    for k, v in req_headers.items():
        if k.lower() == "content-type":
            ct = v
            break

    if body is not None:
        if isinstance(body, (dict, list)):
            if not ct:
                req_headers["Content-Type"] = "application/json"
            if req_headers.get("Content-Type", "").startswith("application/json"):
                json_body = body
            else:
                data_body = json.dumps(body)
        else:
            # raw string/bytes
            data_body = body

    async with httpx.AsyncClient(timeout=timeout_s) as client:
        resp = await client.request(
            method.upper(),
            url,
            params=query or None,
            headers=req_headers,
            json=json_body,
            content=data_body,
            files=files,
        )

    content_type = resp.headers.get("content-type", "")
    parsed: Any
    if "application/json" in content_type:
        try:
            parsed = resp.json()
        except Exception:
            parsed = resp.text
    else:
        parsed = resp.text

    return {
        "url": str(resp.request.url),
        "status_code": resp.status_code,
        "headers": dict(resp.headers),
        "body": parsed,
    }


@mcp.tool()
async def ebay_sell_request(
    api: str,
    method: str,
    path: str,
    query_json: str = "",
    headers_json: str = "",
    body_json: str = "",
    timeout_s: float = 60.0,
) -> Dict[str, Any]:
    """Generic eBay Sell API request tool.

    Parameters:
      api: One of: account, inventory, fulfillment, feed, marketing, finances, metadata, logistics
      method: HTTP method (GET, POST, PUT, DELETE)
      path: Path starting with '/', e.g. '/inventory_item' or '/order/{orderId}/shipping_fulfillment'
      query_json: JSON object string of query params
      headers_json: JSON object string of extra headers (e.g. Content-Language, X-EBAY-C-MARKETPLACE-ID)
      body_json: JSON string for request body (or raw string)
      timeout_s: request timeout

    Auth:
      Uses EBAY_OAUTH_TOKEN env var.
    """
    query = _parse_query(query_json)
    headers = _parse_headers(headers_json)
    body = _parse_body(body_json)
    return await _request(api, method, path, query=query, headers=headers, body=body, timeout_s=timeout_s)


# --- Convenience tools for common flows (based on docs) ---

@mcp.tool()
async def inventory_create_or_replace_inventory_item(
    sku: str,
    item_json: str,
) -> Dict[str, Any]:
    """Inventory API: createOrReplaceInventoryItem

    PUT /inventory_item/{sku}
    Body: InventoryItem
    """
    body = _parse_body(item_json)
    return await _request("inventory", "PUT", f"/inventory_item/{sku}", body=body)


@mcp.tool()
async def inventory_get_inventory_items(limit: int = 25, offset: int = 0) -> Dict[str, Any]:
    """Inventory API: getInventoryItems

    GET /inventory_item?limit=&offset=
    """
    return await _request(
        "inventory",
        "GET",
        "/inventory_item",
        query={"limit": str(limit), "offset": str(offset)},
    )


@mcp.tool()
async def inventory_create_offer(offer_json: str) -> Dict[str, Any]:
    """Inventory API: createOffer

    POST /offer
    Body: EbayOfferDetails
    """
    body = _parse_body(offer_json)
    return await _request("inventory", "POST", "/offer", body=body)


@mcp.tool()
async def inventory_update_offer(offer_id: str, offer_json: str, content_language: str = "en-US") -> Dict[str, Any]:
    """Inventory API: updateOffer

    PUT /offer/{offerId}
    Requires Content-Language header.
    """
    body = _parse_body(offer_json)
    return await _request(
        "inventory",
        "PUT",
        f"/offer/{offer_id}",
        headers={"Content-Language": content_language, "Content-Type": "application/json"},
        body=body,
    )


@mcp.tool()
async def inventory_publish_offer(offer_id: str) -> Dict[str, Any]:
    """Inventory API: publishOffer

    POST /offer/{offerId}/publish
    """
    return await _request("inventory", "POST", f"/offer/{offer_id}/publish")


@mcp.tool()
async def fulfillment_get_orders(filter: str = "", order_ids: str = "", limit: int = 50, offset: int = 0, field_groups: str = "") -> Dict[str, Any]:
    """Fulfillment API: getOrders

    GET /order
    Query params include filter, orderIds, limit, offset, fieldGroups.
    """
    q = _clean_none(
        {
            "filter": filter or None,
            "orderIds": order_ids or None,
            "limit": str(limit),
            "offset": str(offset),
            "fieldGroups": field_groups or None,
        }
    )
    return await _request("fulfillment", "GET", "/order", query=q)


@mcp.tool()
async def fulfillment_create_shipping_fulfillment(order_id: str, fulfillment_json: str) -> Dict[str, Any]:
    """Fulfillment API: createShippingFulfillment

    POST /order/{orderId}/shipping_fulfillment
    Body: ShippingFulfillmentDetails
    """
    body = _parse_body(fulfillment_json)
    return await _request(
        "fulfillment",
        "POST",
        f"/order/{order_id}/shipping_fulfillment",
        headers={"Content-Type": "application/json"},
        body=body,
    )


@mcp.tool()
async def account_get_fulfillment_policies(marketplace_id: str) -> Dict[str, Any]:
    """Account API: getFulfillmentPolicies

    GET /fulfillment_policy?marketplace_id=
    """
    return await _request("account", "GET", "/fulfillment_policy", query={"marketplace_id": marketplace_id})


@mcp.tool()
async def account_get_payment_policies(marketplace_id: str, content_language: str = "") -> Dict[str, Any]:
    """Account API: getPaymentPolicies

    GET /payment_policy?marketplace_id=
    Optional Content-Language header.
    """
    headers = {"Content-Language": content_language} if content_language else None
    return await _request("account", "GET", "/payment_policy", query={"marketplace_id": marketplace_id}, headers=headers)


@mcp.tool()
async def feed_create_task(task_json: str) -> Dict[str, Any]:
    """Feed API: createTask

    POST /task
    Body: CreateTaskRequest
    """
    body = _parse_body(task_json)
    return await _request("feed", "POST", "/task", headers={"Content-Type": "application/json"}, body=body)


@mcp.tool()
async def marketing_get_campaigns(filter: str = "", limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    """Marketing API: getCampaigns

    GET /ad_campaign
    Supports filter, limit, offset.
    """
    q = _clean_none({"filter": filter or None, "limit": str(limit), "offset": str(offset)})
    return await _request("marketing", "GET", "/ad_campaign", query=q)


@mcp.tool()
async def finances_get_payouts(filter: str = "", limit: int = 20, offset: int = 0, sort: str = "", marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """Finances API: getPayouts

    GET /payout
    Requires X-EBAY-C-MARKETPLACE-ID header (defaults EBAY_US per docs).
    """
    q = _clean_none({"filter": filter or None, "limit": str(limit), "offset": str(offset), "sort": sort or None})
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return await _request("finances", "GET", "/payout", query=q, headers=headers)


if __name__ == "__main__":
    mcp.run()
