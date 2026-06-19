from __future__ import annotations

from typing import Any, Dict, Optional

from .http import adyen_request, default_company_account, default_merchant_account


def management_list_companies() -> Dict[str, Any]:
    """GET /companies (Management v3)"""

    return adyen_request(service="management", method="GET", path="/companies")


def management_get_company(*, company_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /companies/{companyId} (Management v3)

    If company_id is omitted, uses ADYEN_COMPANY_ACCOUNT.
    """

    cid = default_company_account(company_id)
    if not cid:
        return {"error": "Missing company account. Provide company_id or set ADYEN_COMPANY_ACCOUNT."}
    return adyen_request(service="management", method="GET", path=f"/companies/{cid}")


def management_list_merchants(*, company_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /companies/{companyId}/merchants (Management v3)"""

    cid = default_company_account(company_id)
    if not cid:
        return {"error": "Missing company account. Provide company_id or set ADYEN_COMPANY_ACCOUNT."}
    return adyen_request(service="management", method="GET", path=f"/companies/{cid}/merchants")


def management_get_merchant(*, merchant_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /merchants/{merchantId} (Management v3)

    If merchant_id is omitted, uses ADYEN_MERCHANT_ACCOUNT.
    """

    mid = default_merchant_account(merchant_id)
    if not mid:
        return {"error": "Missing merchant account. Provide merchant_id or set ADYEN_MERCHANT_ACCOUNT."}
    return adyen_request(service="management", method="GET", path=f"/merchants/{mid}")


def management_list_stores(*, merchant_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /merchants/{merchantId}/stores (Management v3)"""

    mid = default_merchant_account(merchant_id)
    if not mid:
        return {"error": "Missing merchant account. Provide merchant_id or set ADYEN_MERCHANT_ACCOUNT."}
    return adyen_request(service="management", method="GET", path=f"/merchants/{mid}/stores")


def management_get_store(*, store_id: str) -> Dict[str, Any]:
    """GET /stores/{storeId} (Management v3)"""

    return adyen_request(service="management", method="GET", path=f"/stores/{store_id}")


def management_list_merchant_webhooks(*, merchant_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /merchants/{merchantId}/webhooks (Management v3)"""

    mid = default_merchant_account(merchant_id)
    if not mid:
        return {"error": "Missing merchant account. Provide merchant_id or set ADYEN_MERCHANT_ACCOUNT."}
    return adyen_request(service="management", method="GET", path=f"/merchants/{mid}/webhooks")


def management_get_merchant_webhook(*, merchant_id: Optional[str] = None, webhook_id: str) -> Dict[str, Any]:
    """GET /merchants/{merchantId}/webhooks/{webhookId} (Management v3)"""

    mid = default_merchant_account(merchant_id)
    if not mid:
        return {"error": "Missing merchant account. Provide merchant_id or set ADYEN_MERCHANT_ACCOUNT."}
    return adyen_request(service="management", method="GET", path=f"/merchants/{mid}/webhooks/{webhook_id}")


def management_list_company_webhooks(*, company_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /companies/{companyId}/webhooks (Management v3)"""

    cid = default_company_account(company_id)
    if not cid:
        return {"error": "Missing company account. Provide company_id or set ADYEN_COMPANY_ACCOUNT."}
    return adyen_request(service="management", method="GET", path=f"/companies/{cid}/webhooks")


def management_get_company_webhook(*, company_id: Optional[str] = None, webhook_id: str) -> Dict[str, Any]:
    """GET /companies/{companyId}/webhooks/{webhookId} (Management v3)"""

    cid = default_company_account(company_id)
    if not cid:
        return {"error": "Missing company account. Provide company_id or set ADYEN_COMPANY_ACCOUNT."}
    return adyen_request(service="management", method="GET", path=f"/companies/{cid}/webhooks/{webhook_id}")
