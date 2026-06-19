from typing import Any, Dict, Optional

from .http_client import adyen_base_urls, request_json


def management_me() -> Dict[str, Any]:
    """Management API: GET /me (v3)"""
    base = adyen_base_urls()["management"]
    return request_json("GET", f"{base}/me")


def management_list_companies(page_number: int = 1, page_size: int = 10) -> Dict[str, Any]:
    """Management API: GET /companies"""
    base = adyen_base_urls()["management"]
    return request_json("GET", f"{base}/companies", params={"pageNumber": page_number, "pageSize": page_size})


def management_get_company(company_id: str) -> Dict[str, Any]:
    """Management API: GET /companies/{companyId}"""
    base = adyen_base_urls()["management"]
    return request_json("GET", f"{base}/companies/{company_id}")


def management_list_merchants(page_number: int = 1, page_size: int = 10) -> Dict[str, Any]:
    """Management API: GET /merchants"""
    base = adyen_base_urls()["management"]
    return request_json("GET", f"{base}/merchants", params={"pageNumber": page_number, "pageSize": page_size})


def management_get_merchant(merchant_id: str) -> Dict[str, Any]:
    """Management API: GET /merchants/{merchantId}"""
    base = adyen_base_urls()["management"]
    return request_json("GET", f"{base}/merchants/{merchant_id}")


def management_list_stores(page_number: int = 1, page_size: int = 10, merchant_id: Optional[str] = None) -> Dict[str, Any]:
    """Management API: GET /stores

    If merchant_id is provided, uses /merchants/{merchantId}/stores.
    """
    base = adyen_base_urls()["management"]
    if merchant_id:
        return request_json(
            "GET",
            f"{base}/merchants/{merchant_id}/stores",
            params={"pageNumber": page_number, "pageSize": page_size},
        )
    return request_json("GET", f"{base}/stores", params={"pageNumber": page_number, "pageSize": page_size})


def management_get_store(store_id: str) -> Dict[str, Any]:
    """Management API: GET /stores/{storeId}"""
    base = adyen_base_urls()["management"]
    return request_json("GET", f"{base}/stores/{store_id}")


def management_create_store(merchant_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Management API: POST /merchants/{merchantId}/stores"""
    base = adyen_base_urls()["management"]
    return request_json("POST", f"{base}/merchants/{merchant_id}/stores", json_body=payload)


def management_update_store(store_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Management API: PATCH /stores/{storeId}"""
    base = adyen_base_urls()["management"]
    return request_json("PATCH", f"{base}/stores/{store_id}", json_body=payload)


def management_list_webhooks(merchant_id: str, page_number: int = 1, page_size: int = 10) -> Dict[str, Any]:
    """Management API: GET /merchants/{merchantId}/webhooks"""
    base = adyen_base_urls()["management"]
    return request_json(
        "GET",
        f"{base}/merchants/{merchant_id}/webhooks",
        params={"pageNumber": page_number, "pageSize": page_size},
    )


def management_get_webhook(merchant_id: str, webhook_id: str) -> Dict[str, Any]:
    """Management API: GET /merchants/{merchantId}/webhooks/{webhookId}"""
    base = adyen_base_urls()["management"]
    return request_json("GET", f"{base}/merchants/{merchant_id}/webhooks/{webhook_id}")


def management_create_webhook(merchant_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Management API: POST /merchants/{merchantId}/webhooks"""
    base = adyen_base_urls()["management"]
    return request_json("POST", f"{base}/merchants/{merchant_id}/webhooks", json_body=payload)


def management_update_webhook(merchant_id: str, webhook_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Management API: PATCH /merchants/{merchantId}/webhooks/{webhookId}"""
    base = adyen_base_urls()["management"]
    return request_json("PATCH", f"{base}/merchants/{merchant_id}/webhooks/{webhook_id}", json_body=payload)


def management_delete_webhook(merchant_id: str, webhook_id: str) -> Dict[str, Any]:
    """Management API: DELETE /merchants/{merchantId}/webhooks/{webhookId}"""
    base = adyen_base_urls()["management"]
    return request_json("DELETE", f"{base}/merchants/{merchant_id}/webhooks/{webhook_id}")


def management_list_api_credentials(merchant_id: str) -> Dict[str, Any]:
    """Management API: GET /merchants/{merchantId}/apiCredentials"""
    base = adyen_base_urls()["management"]
    return request_json("GET", f"{base}/merchants/{merchant_id}/apiCredentials")


def management_get_api_credential(merchant_id: str, api_credential_id: str) -> Dict[str, Any]:
    """Management API: GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}"""
    base = adyen_base_urls()["management"]
    return request_json("GET", f"{base}/merchants/{merchant_id}/apiCredentials/{api_credential_id}")


def management_generate_api_key(merchant_id: str, api_credential_id: str) -> Dict[str, Any]:
    """Management API: POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey"""
    base = adyen_base_urls()["management"]
    return request_json("POST", f"{base}/merchants/{merchant_id}/apiCredentials/{api_credential_id}/generateApiKey")


def management_generate_client_key(merchant_id: str, api_credential_id: str) -> Dict[str, Any]:
    """Management API: POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateClientKey"""
    base = adyen_base_urls()["management"]
    return request_json(
        "POST", f"{base}/merchants/{merchant_id}/apiCredentials/{api_credential_id}/generateClientKey"
    )
