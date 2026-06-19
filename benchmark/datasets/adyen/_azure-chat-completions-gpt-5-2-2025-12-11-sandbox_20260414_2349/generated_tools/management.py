"""Adyen Management API (v3) tools."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

from fastmcp import FastMCP

from .http import adyen_request

mcp = FastMCP("adyen")


def _default_company_id(company_id: Optional[str]) -> Optional[str]:
    return company_id or os.environ.get("ADYEN_COMPANY_ACCOUNT")


def _default_merchant_id(merchant_id: Optional[str]) -> Optional[str]:
    return merchant_id or os.environ.get("ADYEN_MERCHANT_ACCOUNT")


@mcp.tool()
def management_get_company(company_id: Optional[str] = None) -> Dict[str, Any]:
    """Get a company account.

    GET /companies/{companyId}
    """

    cid = _default_company_id(company_id)
    if not cid:
        return {"error": {"message": "company_id is required (or set ADYEN_COMPANY_ACCOUNT)"}}
    return adyen_request("management", "GET", f"/companies/{cid}")


@mcp.tool()
def management_list_companies(page_number: int = 1, page_size: int = 10) -> Dict[str, Any]:
    """List company accounts accessible by the API credential.

    GET /companies
    """

    params = {"pageNumber": page_number, "pageSize": page_size}
    return adyen_request("management", "GET", "/companies", params=params)


@mcp.tool()
def management_get_merchant(merchant_id: Optional[str] = None) -> Dict[str, Any]:
    """Get a merchant account.

    GET /merchants/{merchantId}
    """

    mid = _default_merchant_id(merchant_id)
    if not mid:
        return {"error": {"message": "merchant_id is required (or set ADYEN_MERCHANT_ACCOUNT)"}}
    return adyen_request("management", "GET", f"/merchants/{mid}")


@mcp.tool()
def management_list_company_merchants(
    company_id: Optional[str] = None,
    page_number: int = 1,
    page_size: int = 10,
) -> Dict[str, Any]:
    """List merchant accounts under a company.

    GET /companies/{companyId}/merchants
    """

    cid = _default_company_id(company_id)
    if not cid:
        return {"error": {"message": "company_id is required (or set ADYEN_COMPANY_ACCOUNT)"}}

    params = {"pageNumber": page_number, "pageSize": page_size}
    return adyen_request("management", "GET", f"/companies/{cid}/merchants", params=params)


@mcp.tool()
def management_list_merchant_stores(
    merchant_id: Optional[str] = None,
    page_number: int = 1,
    page_size: int = 10,
    reference: Optional[str] = None,
) -> Dict[str, Any]:
    """List stores for a merchant.

    GET /merchants/{merchantId}/stores
    """

    mid = _default_merchant_id(merchant_id)
    if not mid:
        return {"error": {"message": "merchant_id is required (or set ADYEN_MERCHANT_ACCOUNT)"}}

    params: Dict[str, Any] = {"pageNumber": page_number, "pageSize": page_size}
    if reference:
        params["reference"] = reference

    return adyen_request("management", "GET", f"/merchants/{mid}/stores", params=params)


@mcp.tool()
def management_get_store(store_id: str) -> Dict[str, Any]:
    """Get store details.

    GET /stores/{storeId}
    """

    return adyen_request("management", "GET", f"/stores/{store_id}")


@mcp.tool()
def management_list_merchant_webhooks(
    merchant_id: Optional[str] = None,
    page_number: int = 1,
    page_size: int = 10,
) -> Dict[str, Any]:
    """List webhooks for a merchant.

    GET /merchants/{merchantId}/webhooks
    """

    mid = _default_merchant_id(merchant_id)
    if not mid:
        return {"error": {"message": "merchant_id is required (or set ADYEN_MERCHANT_ACCOUNT)"}}

    params = {"pageNumber": page_number, "pageSize": page_size}
    return adyen_request("management", "GET", f"/merchants/{mid}/webhooks", params=params)


@mcp.tool()
def management_get_merchant_webhook(merchant_id: Optional[str], webhook_id: str) -> Dict[str, Any]:
    """Get a merchant webhook configuration.

    GET /merchants/{merchantId}/webhooks/{webhookId}
    """

    mid = _default_merchant_id(merchant_id)
    if not mid:
        return {"error": {"message": "merchant_id is required (or set ADYEN_MERCHANT_ACCOUNT)"}}

    return adyen_request("management", "GET", f"/merchants/{mid}/webhooks/{webhook_id}")
