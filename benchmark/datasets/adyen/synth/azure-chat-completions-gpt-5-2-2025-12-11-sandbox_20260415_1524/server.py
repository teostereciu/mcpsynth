import json
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.checkout import (
    checkout_create_session,
    checkout_get_session,
    checkout_payment_links_create,
    checkout_payment_links_get,
    checkout_payment_links_update,
    checkout_payment_methods,
    checkout_payments,
    checkout_payments_cancel,
    checkout_payments_capture,
    checkout_payments_details,
    checkout_payments_refund,
    checkout_stored_payment_method_delete,
    checkout_stored_payment_methods_list,
)
from generated_tools.management import (
    management_create_store,
    management_create_webhook,
    management_delete_webhook,
    management_generate_api_key,
    management_generate_client_key,
    management_get_api_credential,
    management_get_company,
    management_get_merchant,
    management_get_store,
    management_get_webhook,
    management_list_api_credentials,
    management_list_companies,
    management_list_merchants,
    management_list_stores,
    management_list_webhooks,
    management_me,
    management_update_store,
    management_update_webhook,
)
from generated_tools.payment import (
    payment_adjust_authorisation,
    payment_authorise,
    payment_cancel,
    payment_cancel_or_refund,
    payment_capture,
    payment_refund,
    payment_technical_cancel,
)

mcp = FastMCP("adyen-mcp")


@mcp.tool()
def adyen_checkout_create_session(payload: Dict[str, Any]) -> Dict[str, Any]:
    return checkout_create_session(payload)


@mcp.tool()
def adyen_checkout_get_session(session_id: str) -> Dict[str, Any]:
    return checkout_get_session(session_id)


@mcp.tool()
def adyen_checkout_payment_methods(payload: Dict[str, Any]) -> Dict[str, Any]:
    return checkout_payment_methods(payload)


@mcp.tool()
def adyen_checkout_payments(payload: Dict[str, Any]) -> Dict[str, Any]:
    return checkout_payments(payload)


@mcp.tool()
def adyen_checkout_payments_details(payload: Dict[str, Any]) -> Dict[str, Any]:
    return checkout_payments_details(payload)


@mcp.tool()
def adyen_checkout_capture(payment_psp_reference: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return checkout_payments_capture(payment_psp_reference, payload)


@mcp.tool()
def adyen_checkout_refund(payment_psp_reference: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return checkout_payments_refund(payment_psp_reference, payload)


@mcp.tool()
def adyen_checkout_cancel(payment_psp_reference: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return checkout_payments_cancel(payment_psp_reference, payload)


@mcp.tool()
def adyen_checkout_payment_link_create(payload: Dict[str, Any]) -> Dict[str, Any]:
    return checkout_payment_links_create(payload)


@mcp.tool()
def adyen_checkout_payment_link_get(link_id: str) -> Dict[str, Any]:
    return checkout_payment_links_get(link_id)


@mcp.tool()
def adyen_checkout_payment_link_update(link_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return checkout_payment_links_update(link_id, payload)


@mcp.tool()
def adyen_checkout_stored_payment_methods_list(shopper_reference: Optional[str] = None) -> Dict[str, Any]:
    return checkout_stored_payment_methods_list(shopper_reference)


@mcp.tool()
def adyen_checkout_stored_payment_method_delete(stored_payment_method_id: str) -> Dict[str, Any]:
    return checkout_stored_payment_method_delete(stored_payment_method_id)


@mcp.tool()
def adyen_payment_authorise(payload: Dict[str, Any]) -> Dict[str, Any]:
    return payment_authorise(payload)


@mcp.tool()
def adyen_payment_capture(payload: Dict[str, Any]) -> Dict[str, Any]:
    return payment_capture(payload)


@mcp.tool()
def adyen_payment_refund(payload: Dict[str, Any]) -> Dict[str, Any]:
    return payment_refund(payload)


@mcp.tool()
def adyen_payment_cancel(payload: Dict[str, Any]) -> Dict[str, Any]:
    return payment_cancel(payload)


@mcp.tool()
def adyen_payment_cancel_or_refund(payload: Dict[str, Any]) -> Dict[str, Any]:
    return payment_cancel_or_refund(payload)


@mcp.tool()
def adyen_payment_adjust_authorisation(payload: Dict[str, Any]) -> Dict[str, Any]:
    return payment_adjust_authorisation(payload)


@mcp.tool()
def adyen_payment_technical_cancel(payload: Dict[str, Any]) -> Dict[str, Any]:
    return payment_technical_cancel(payload)


@mcp.tool()
def adyen_management_me() -> Dict[str, Any]:
    return management_me()


@mcp.tool()
def adyen_management_list_companies(page_number: int = 1, page_size: int = 10) -> Dict[str, Any]:
    return management_list_companies(page_number=page_number, page_size=page_size)


@mcp.tool()
def adyen_management_get_company(company_id: str) -> Dict[str, Any]:
    return management_get_company(company_id)


@mcp.tool()
def adyen_management_list_merchants(page_number: int = 1, page_size: int = 10) -> Dict[str, Any]:
    return management_list_merchants(page_number=page_number, page_size=page_size)


@mcp.tool()
def adyen_management_get_merchant(merchant_id: str) -> Dict[str, Any]:
    return management_get_merchant(merchant_id)


@mcp.tool()
def adyen_management_list_stores(page_number: int = 1, page_size: int = 10, merchant_id: Optional[str] = None) -> Dict[str, Any]:
    return management_list_stores(page_number=page_number, page_size=page_size, merchant_id=merchant_id)


@mcp.tool()
def adyen_management_get_store(store_id: str) -> Dict[str, Any]:
    return management_get_store(store_id)


@mcp.tool()
def adyen_management_create_store(merchant_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return management_create_store(merchant_id, payload)


@mcp.tool()
def adyen_management_update_store(store_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return management_update_store(store_id, payload)


@mcp.tool()
def adyen_management_list_webhooks(merchant_id: str, page_number: int = 1, page_size: int = 10) -> Dict[str, Any]:
    return management_list_webhooks(merchant_id, page_number=page_number, page_size=page_size)


@mcp.tool()
def adyen_management_get_webhook(merchant_id: str, webhook_id: str) -> Dict[str, Any]:
    return management_get_webhook(merchant_id, webhook_id)


@mcp.tool()
def adyen_management_create_webhook(merchant_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return management_create_webhook(merchant_id, payload)


@mcp.tool()
def adyen_management_update_webhook(merchant_id: str, webhook_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return management_update_webhook(merchant_id, webhook_id, payload)


@mcp.tool()
def adyen_management_delete_webhook(merchant_id: str, webhook_id: str) -> Dict[str, Any]:
    return management_delete_webhook(merchant_id, webhook_id)


@mcp.tool()
def adyen_management_list_api_credentials(merchant_id: str) -> Dict[str, Any]:
    return management_list_api_credentials(merchant_id)


@mcp.tool()
def adyen_management_get_api_credential(merchant_id: str, api_credential_id: str) -> Dict[str, Any]:
    return management_get_api_credential(merchant_id, api_credential_id)


@mcp.tool()
def adyen_management_generate_api_key(merchant_id: str, api_credential_id: str) -> Dict[str, Any]:
    return management_generate_api_key(merchant_id, api_credential_id)


@mcp.tool()
def adyen_management_generate_client_key(merchant_id: str, api_credential_id: str) -> Dict[str, Any]:
    return management_generate_client_key(merchant_id, api_credential_id)


if __name__ == "__main__":
    mcp.run()
