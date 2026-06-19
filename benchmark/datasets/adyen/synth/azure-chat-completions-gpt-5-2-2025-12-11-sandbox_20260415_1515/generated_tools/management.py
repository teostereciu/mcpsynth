from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import company_account, management_url, request_json


# Companies

def management_list_companies() -> Dict[str, Any]:
    """GET /companies (Management v3)"""
    return request_json("GET", management_url("/companies", "v3"))


def management_get_company(companyId: str) -> Dict[str, Any]:
    """GET /companies/{companyId} (Management v3)"""
    return request_json("GET", management_url(f"/companies/{companyId}", "v3"))


def management_list_company_merchants(companyId: Optional[str] = None) -> Dict[str, Any]:
    """GET /companies/{companyId}/merchants (Management v3)"""
    cid = companyId or company_account()
    if not cid:
        return {"error": "companyId is required (or set ADYEN_COMPANY_ACCOUNT)"}
    return request_json("GET", management_url(f"/companies/{cid}/merchants", "v3"))


# Merchants

def management_list_merchants() -> Dict[str, Any]:
    """GET /merchants (Management v3)"""
    return request_json("GET", management_url("/merchants", "v3"))


def management_get_merchant(merchantId: str) -> Dict[str, Any]:
    """GET /merchants/{merchantId} (Management v3)"""
    return request_json("GET", management_url(f"/merchants/{merchantId}", "v3"))


def management_create_merchant(body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /merchants (Management v3)"""
    return request_json("POST", management_url("/merchants", "v3"), json_body=body)


def management_activate_merchant(merchantId: str) -> Dict[str, Any]:
    """POST /merchants/{merchantId}/activate (Management v3)"""
    return request_json("POST", management_url(f"/merchants/{merchantId}/activate", "v3"), json_body={})


# Stores

def management_list_stores(*, merchantId: Optional[str] = None) -> Dict[str, Any]:
    """GET /stores or /merchants/{merchantId}/stores (Management v3)

    If merchantId is provided, uses the merchant-scoped endpoint.
    """
    if merchantId:
        return request_json("GET", management_url(f"/merchants/{merchantId}/stores", "v3"))
    return request_json("GET", management_url("/stores", "v3"))


def management_get_store(storeId: str) -> Dict[str, Any]:
    """GET /stores/{storeId} (Management v3)"""
    return request_json("GET", management_url(f"/stores/{storeId}", "v3"))


def management_create_store(body: Dict[str, Any], *, merchantId: str) -> Dict[str, Any]:
    """POST /merchants/{merchantId}/stores (Management v3)"""
    return request_json("POST", management_url(f"/merchants/{merchantId}/stores", "v3"), json_body=body)


def management_update_store(storeId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /stores/{storeId} (Management v3)"""
    return request_json("PATCH", management_url(f"/stores/{storeId}", "v3"), json_body=body)


# Webhooks (merchant-scoped)

def management_list_merchant_webhooks(merchantId: str) -> Dict[str, Any]:
    """GET /merchants/{merchantId}/webhooks (Management v3)"""
    return request_json("GET", management_url(f"/merchants/{merchantId}/webhooks", "v3"))


def management_get_merchant_webhook(merchantId: str, webhookId: str) -> Dict[str, Any]:
    """GET /merchants/{merchantId}/webhooks/{webhookId} (Management v3)"""
    return request_json("GET", management_url(f"/merchants/{merchantId}/webhooks/{webhookId}", "v3"))


def management_create_merchant_webhook(merchantId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /merchants/{merchantId}/webhooks (Management v3)"""
    return request_json("POST", management_url(f"/merchants/{merchantId}/webhooks", "v3"), json_body=body)


def management_update_merchant_webhook(merchantId: str, webhookId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /merchants/{merchantId}/webhooks/{webhookId} (Management v3)"""
    return request_json(
        "PATCH",
        management_url(f"/merchants/{merchantId}/webhooks/{webhookId}", "v3"),
        json_body=body,
    )


def management_delete_merchant_webhook(merchantId: str, webhookId: str) -> Dict[str, Any]:
    """DELETE /merchants/{merchantId}/webhooks/{webhookId} (Management v3)"""
    return request_json("DELETE", management_url(f"/merchants/{merchantId}/webhooks/{webhookId}", "v3"))


def management_test_merchant_webhook(merchantId: str, webhookId: str) -> Dict[str, Any]:
    """POST /merchants/{merchantId}/webhooks/{webhookId}/test (Management v3)"""
    return request_json(
        "POST",
        management_url(f"/merchants/{merchantId}/webhooks/{webhookId}/test", "v3"),
        json_body={},
    )


def management_generate_hmac_merchant_webhook(merchantId: str, webhookId: str) -> Dict[str, Any]:
    """POST /merchants/{merchantId}/webhooks/{webhookId}/generateHmac (Management v3)"""
    return request_json(
        "POST",
        management_url(f"/merchants/{merchantId}/webhooks/{webhookId}/generateHmac", "v3"),
        json_body={},
    )


# API credentials (merchant-scoped)

def management_list_merchant_api_credentials(merchantId: str) -> Dict[str, Any]:
    """GET /merchants/{merchantId}/apiCredentials (Management v3)"""
    return request_json("GET", management_url(f"/merchants/{merchantId}/apiCredentials", "v3"))


def management_get_merchant_api_credential(merchantId: str, apiCredentialId: str) -> Dict[str, Any]:
    """GET /merchants/{merchantId}/apiCredentials/{apiCredentialId} (Management v3)"""
    return request_json(
        "GET",
        management_url(f"/merchants/{merchantId}/apiCredentials/{apiCredentialId}", "v3"),
    )


def management_create_merchant_api_credential(merchantId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /merchants/{merchantId}/apiCredentials (Management v3)"""
    return request_json(
        "POST",
        management_url(f"/merchants/{merchantId}/apiCredentials", "v3"),
        json_body=body,
    )


def management_update_merchant_api_credential(merchantId: str, apiCredentialId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /merchants/{merchantId}/apiCredentials/{apiCredentialId} (Management v3)"""
    return request_json(
        "PATCH",
        management_url(f"/merchants/{merchantId}/apiCredentials/{apiCredentialId}", "v3"),
        json_body=body,
    )


def management_generate_api_key_for_merchant_credential(merchantId: str, apiCredentialId: str) -> Dict[str, Any]:
    """POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey (Management v3)"""
    return request_json(
        "POST",
        management_url(f"/merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey", "v3"),
        json_body={},
    )


def management_generate_client_key_for_merchant_credential(merchantId: str, apiCredentialId: str) -> Dict[str, Any]:
    """POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateClientKey (Management v3)"""
    return request_json(
        "POST",
        management_url(f"/merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateClientKey", "v3"),
        json_body={},
    )
