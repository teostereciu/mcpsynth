import os
import time
import json
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("ebay-sell")


class EbaySellClient:
    def __init__(self):
        self.app_id = os.getenv("EBAY_APP_ID")
        self.cert_id = os.getenv("EBAY_CERT_ID")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
        self.environment = (os.getenv("EBAY_ENVIRONMENT") or "SANDBOX").upper()

        if self.environment not in {"SANDBOX", "PRODUCTION"}:
            self.environment = "SANDBOX"

        self.base_url = (
            "https://api.sandbox.ebay.com" if self.environment == "SANDBOX" else "https://api.ebay.com"
        )
        self._access_token: Optional[str] = None
        self._access_token_exp: float = 0.0

    def _token_url(self) -> str:
        return f"{self.base_url}/identity/v1/oauth2/token"

    def _get_access_token(self) -> str:
        now = time.time()
        if self._access_token and now < (self._access_token_exp - 30):
            return self._access_token

        if not (self.app_id and self.cert_id and self.refresh_token):
            raise RuntimeError(
                "Missing EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN environment variables"
            )

        auth = requests.auth.HTTPBasicAuth(self.app_id, self.cert_id)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            # Scope is optional for refresh token exchange; eBay may require it.
            # We omit to avoid incorrect scope; if needed, set EBAY_OAUTH_SCOPE.
        }
        scope = os.getenv("EBAY_OAUTH_SCOPE")
        if scope:
            data["scope"] = scope

        resp = requests.post(self._token_url(), headers=headers, data=data, auth=auth, timeout=30)
        if resp.status_code >= 400:
            raise RuntimeError(f"Token request failed: {resp.status_code} {resp.text}")
        payload = resp.json()
        self._access_token = payload.get("access_token")
        expires_in = payload.get("expires_in", 7200)
        self._access_token_exp = now + float(expires_in)
        if not self._access_token:
            raise RuntimeError(f"Token response missing access_token: {payload}")
        return self._access_token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        accept: str = "application/json",
        content_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        try:
            token = self._get_access_token()
        except Exception as e:
            return {"error": str(e)}

        h = {
            "Authorization": f"Bearer {token}",
            "Accept": accept,
        }
        if content_type:
            h["Content-Type"] = content_type
        if headers:
            h.update(headers)

        try:
            resp = requests.request(
                method,
                url,
                params=params,
                json=json_body,
                headers=h,
                timeout=60,
            )
        except Exception as e:
            return {"error": f"Request failed: {e}"}

        # eBay often returns empty body for 204
        if resp.status_code == 204:
            return {"status": 204}

        content_type_resp = resp.headers.get("Content-Type", "")
        body: Any
        if "application/json" in content_type_resp:
            try:
                body = resp.json()
            except Exception:
                body = {"raw": resp.text}
        else:
            body = {"raw": resp.text}

        if resp.status_code >= 400:
            return {
                "error": "HTTP error",
                "status": resp.status_code,
                "body": body,
            }
        return body if isinstance(body, (dict, list)) else {"result": body}


client = EbaySellClient()


# Inventory API
@mcp.tool()
def inventory_get_inventory_item(sku: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/inventory_item/{sku}")


@mcp.tool()
def inventory_create_or_replace_inventory_item(sku: str, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "PUT",
        f"/sell/inventory/v1/inventory_item/{sku}",
        json_body=inventory_item,
        content_type="application/json",
    )


@mcp.tool()
def inventory_delete_inventory_item(sku: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")


@mcp.tool()
def inventory_bulk_create_or_replace_inventory_item(request_body: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/sell/inventory/v1/bulk_create_or_replace_inventory_item",
        json_body=request_body,
        content_type="application/json",
    )


@mcp.tool()
def inventory_get_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def inventory_create_offer(offer: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/sell/inventory/v1/offer",
        json_body=offer,
        content_type="application/json",
    )


@mcp.tool()
def inventory_update_offer(offer_id: str, offer_patch: Dict[str, Any]) -> Dict[str, Any]:
    # eBay uses JSON Patch for PATCH offer
    return client.request(
        "PATCH",
        f"/sell/inventory/v1/offer/{offer_id}",
        json_body=offer_patch,
        content_type="application/json",
    )


@mcp.tool()
def inventory_publish_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")


@mcp.tool()
def inventory_withdraw_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw")


@mcp.tool()
def inventory_delete_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")


@mcp.tool()
def inventory_get_location(location_key: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/location/{location_key}")


@mcp.tool()
def inventory_create_inventory_location(location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/sell/inventory/v1/location/{location_key}",
        json_body=location,
        content_type="application/json",
    )


@mcp.tool()
def inventory_update_inventory_location(location_key: str, location_patch: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "PUT",
        f"/sell/inventory/v1/location/{location_key}",
        json_body=location_patch,
        content_type="application/json",
    )


@mcp.tool()
def inventory_disable_inventory_location(location_key: str) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/location/{location_key}/disable")


@mcp.tool()
def inventory_enable_inventory_location(location_key: str) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/location/{location_key}/enable")


# Fulfillment API
@mcp.tool()
def fulfillment_get_order(order_id: str, field_groups: Optional[str] = None) -> Dict[str, Any]:
    params = {}
    if field_groups:
        params["fieldGroups"] = field_groups
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}", params=params or None)


@mcp.tool()
def fulfillment_get_orders(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    filter: Optional[str] = None,
    field_groups: Optional[str] = None,
    order_ids: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if filter:
        params["filter"] = filter
    if field_groups:
        params["fieldGroups"] = field_groups
    if order_ids:
        params["orderIds"] = order_ids
    if sort:
        params["sort"] = sort
    return client.request("GET", "/sell/fulfillment/v1/order", params=params or None)


@mcp.tool()
def fulfillment_create_shipping_fulfillment(order_id: str, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "POST",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment",
        json_body=fulfillment,
        content_type="application/json",
    )


@mcp.tool()
def fulfillment_get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment",
    )


@mcp.tool()
def fulfillment_get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}",
    )


# Account API
@mcp.tool()
def account_get_sales_tax(jurisdiction_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/account/v1/sales_tax/{jurisdiction_id}")


@mcp.tool()
def account_create_or_replace_sales_tax(jurisdiction_id: str, sales_tax: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "PUT",
        f"/sell/account/v1/sales_tax/{jurisdiction_id}",
        json_body=sales_tax,
        content_type="application/json",
    )


@mcp.tool()
def account_delete_sales_tax(jurisdiction_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/account/v1/sales_tax/{jurisdiction_id}")


@mcp.tool()
def account_get_fulfillment_policies(marketplace_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/sell/account/v1/fulfillment_policy",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def account_get_fulfillment_policy(policy_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/account/v1/fulfillment_policy/{policy_id}")


@mcp.tool()
def account_create_fulfillment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/sell/account/v1/fulfillment_policy",
        json_body=policy,
        content_type="application/json",
    )


@mcp.tool()
def account_update_fulfillment_policy(policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "PUT",
        f"/sell/account/v1/fulfillment_policy/{policy_id}",
        json_body=policy,
        content_type="application/json",
    )


@mcp.tool()
def account_delete_fulfillment_policy(policy_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/account/v1/fulfillment_policy/{policy_id}")


@mcp.tool()
def account_get_payment_policies(marketplace_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/sell/account/v1/payment_policy",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def account_get_payment_policy(policy_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/account/v1/payment_policy/{policy_id}")


@mcp.tool()
def account_create_payment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/sell/account/v1/payment_policy",
        json_body=policy,
        content_type="application/json",
    )


@mcp.tool()
def account_update_payment_policy(policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "PUT",
        f"/sell/account/v1/payment_policy/{policy_id}",
        json_body=policy,
        content_type="application/json",
    )


@mcp.tool()
def account_delete_payment_policy(policy_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/account/v1/payment_policy/{policy_id}")


@mcp.tool()
def account_get_return_policies(marketplace_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/sell/account/v1/return_policy",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def account_get_return_policy(policy_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/account/v1/return_policy/{policy_id}")


@mcp.tool()
def account_create_return_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/sell/account/v1/return_policy",
        json_body=policy,
        content_type="application/json",
    )


@mcp.tool()
def account_update_return_policy(policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "PUT",
        f"/sell/account/v1/return_policy/{policy_id}",
        json_body=policy,
        content_type="application/json",
    )


@mcp.tool()
def account_delete_return_policy(policy_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/account/v1/return_policy/{policy_id}")


# Marketing API
@mcp.tool()
def marketing_get_campaign(campaign_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


@mcp.tool()
def marketing_get_campaigns(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    campaign_name: Optional[str] = None,
    campaign_status: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if campaign_name:
        params["campaign_name"] = campaign_name
    if campaign_status:
        params["campaign_status"] = campaign_status
    return client.request("GET", "/sell/marketing/v1/ad_campaign", params=params or None)


@mcp.tool()
def marketing_create_campaign(campaign: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/sell/marketing/v1/ad_campaign",
        json_body=campaign,
        content_type="application/json",
    )


@mcp.tool()
def marketing_update_campaign(campaign_id: str, campaign: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "PUT",
        f"/sell/marketing/v1/ad_campaign/{campaign_id}",
        json_body=campaign,
        content_type="application/json",
    )


@mcp.tool()
def marketing_delete_campaign(campaign_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


@mcp.tool()
def marketing_create_item_promotion(promotion: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/sell/marketing/v1/item_promotion",
        json_body=promotion,
        content_type="application/json",
    )


@mcp.tool()
def marketing_get_item_promotion(promotion_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/marketing/v1/item_promotion/{promotion_id}")


@mcp.tool()
def marketing_update_item_promotion(promotion_id: str, promotion: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "PUT",
        f"/sell/marketing/v1/item_promotion/{promotion_id}",
        json_body=promotion,
        content_type="application/json",
    )


@mcp.tool()
def marketing_delete_item_promotion(promotion_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/marketing/v1/item_promotion/{promotion_id}")


# Finances API
@mcp.tool()
def finances_get_transactions(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return client.request("GET", "/sell/finances/v1/transaction", params=params or None)


@mcp.tool()
def finances_get_transaction(transaction_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/finances/v1/transaction/{transaction_id}")


@mcp.tool()
def finances_get_payouts(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    return client.request("GET", "/sell/finances/v1/payout", params=params or None)


@mcp.tool()
def finances_get_payout(payout_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/finances/v1/payout/{payout_id}")


# Feed API
@mcp.tool()
def feed_create_task(task: Dict[str, Any]) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/sell/feed/v1/task",
        json_body=task,
        content_type="application/json",
    )


@mcp.tool()
def feed_get_task(task_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/feed/v1/task/{task_id}")


@mcp.tool()
def feed_get_tasks(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    feed_type: Optional[str] = None,
    schedule_id: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if feed_type:
        params["feed_type"] = feed_type
    if schedule_id:
        params["schedule_id"] = schedule_id
    return client.request("GET", "/sell/feed/v1/task", params=params or None)


@mcp.tool()
def feed_get_result_file(file_id: str) -> Dict[str, Any]:
    # Result files are often binary; request as text and return raw.
    return client.request("GET", f"/sell/feed/v1/task/{file_id}/download", accept="application/octet-stream")


def main():
    mcp.run()


if __name__ == "__main__":
    main()
