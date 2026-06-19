"""Management API (v3) tools."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

from fastmcp import FastMCP

from ._http import adyen_base_urls, adyen_request

mcp = FastMCP("adyen")


def _merchant_account(merchant_account: Optional[str] = None) -> Optional[str]:
    return merchant_account or os.environ.get("ADYEN_MERCHANT_ACCOUNT")


def _company_account(company_id: Optional[str] = None) -> Optional[str]:
    return company_id or os.environ.get("ADYEN_COMPANY_ACCOUNT")


@mcp.tool
def management_companies_list(*, page_number: Optional[int] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /companies - list company accounts."""
    params: Dict[str, Any] = {}
    if page_number is not None:
        params["pageNumber"] = page_number
    if page_size is not None:
        params["pageSize"] = page_size
    return adyen_request(method="GET", base_url=adyen_base_urls()["management"], path="/companies", params=params or None)


@mcp.tool
def management_companies_get(*, company_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /companies/{companyId} - retrieve company account."""
    cid = _company_account(company_id)
    if not cid:
        return {"error": "Missing company_id (or ADYEN_COMPANY_ACCOUNT env var)"}
    return adyen_request(method="GET", base_url=adyen_base_urls()["management"], path=f"/companies/{cid}")


@mcp.tool
def management_merchants_list(*, company_id: Optional[str] = None, page_number: Optional[int] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /companies/{companyId}/merchants - list merchant accounts under a company."""
    cid = _company_account(company_id)
    if not cid:
        return {"error": "Missing company_id (or ADYEN_COMPANY_ACCOUNT env var)"}
    params: Dict[str, Any] = {}
    if page_number is not None:
        params["pageNumber"] = page_number
    if page_size is not None:
        params["pageSize"] = page_size
    return adyen_request(
        method="GET",
        base_url=adyen_base_urls()["management"],
        path=f"/companies/{cid}/merchants",
        params=params or None,
    )


@mcp.tool
def management_merchants_get(*, merchant_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /merchants/{merchantId} - retrieve merchant account."""
    mid = _merchant_account(merchant_id)
    if not mid:
        return {"error": "Missing merchant_id (or ADYEN_MERCHANT_ACCOUNT env var)"}
    return adyen_request(method="GET", base_url=adyen_base_urls()["management"], path=f"/merchants/{mid}")


@mcp.tool
def management_stores_list(*, merchant_id: Optional[str] = None, page_number: Optional[int] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /merchants/{merchantId}/stores - list stores."""
    mid = _merchant_account(merchant_id)
    if not mid:
        return {"error": "Missing merchant_id (or ADYEN_MERCHANT_ACCOUNT env var)"}
    params: Dict[str, Any] = {}
    if page_number is not None:
        params["pageNumber"] = page_number
    if page_size is not None:
        params["pageSize"] = page_size
    return adyen_request(
        method="GET",
        base_url=adyen_base_urls()["management"],
        path=f"/merchants/{mid}/stores",
        params=params or None,
    )


@mcp.tool
def management_stores_get(*, store_id: str) -> Dict[str, Any]:
    """GET /stores/{storeId} - retrieve store details."""
    return adyen_request(method="GET", base_url=adyen_base_urls()["management"], path=f"/stores/{store_id}")


@mcp.tool
def management_webhooks_list(*, merchant_id: Optional[str] = None, company_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /merchants/{merchantId}/webhooks or /companies/{companyId}/webhooks."""
    if merchant_id or os.environ.get("ADYEN_MERCHANT_ACCOUNT"):
        mid = _merchant_account(merchant_id)
        if not mid:
            return {"error": "Missing merchant_id"}
        return adyen_request(method="GET", base_url=adyen_base_urls()["management"], path=f"/merchants/{mid}/webhooks")

    cid = _company_account(company_id)
    if not cid:
        return {"error": "Missing company_id (or ADYEN_COMPANY_ACCOUNT env var)"}
    return adyen_request(method="GET", base_url=adyen_base_urls()["management"], path=f"/companies/{cid}/webhooks")


@mcp.tool
def management_webhooks_get(*, webhook_id: str, merchant_id: Optional[str] = None, company_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /merchants/{merchantId}/webhooks/{webhookId} or /companies/{companyId}/webhooks/{webhookId}."""
    if merchant_id or os.environ.get("ADYEN_MERCHANT_ACCOUNT"):
        mid = _merchant_account(merchant_id)
        if not mid:
            return {"error": "Missing merchant_id"}
        return adyen_request(
            method="GET", base_url=adyen_base_urls()["management"], path=f"/merchants/{mid}/webhooks/{webhook_id}"
        )

    cid = _company_account(company_id)
    if not cid:
        return {"error": "Missing company_id (or ADYEN_COMPANY_ACCOUNT env var)"}
    return adyen_request(method="GET", base_url=adyen_base_urls()["management"], path=f"/companies/{cid}/webhooks/{webhook_id}")
