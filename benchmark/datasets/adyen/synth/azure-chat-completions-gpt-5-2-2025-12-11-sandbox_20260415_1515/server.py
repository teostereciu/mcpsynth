from __future__ import annotations

from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools.checkout import (
    checkout_create_payment_link,
    checkout_create_session,
    checkout_delete_stored_payment_method,
    checkout_get_payment_link,
    checkout_get_session,
    checkout_list_stored_payment_methods,
    checkout_payment_methods,
    checkout_payment_methods_balance,
    checkout_payments,
    checkout_payments_amount_update,
    checkout_payments_cancel,
    checkout_payments_capture,
    checkout_payments_details,
    checkout_payments_refund,
    checkout_payments_reversal,
    checkout_update_payment_link,
)
from generated_tools.management import (
    management_activate_merchant,
    management_create_merchant,
    management_create_merchant_api_credential,
    management_create_merchant_webhook,
    management_create_store,
    management_delete_merchant_webhook,
    management_generate_api_key_for_merchant_credential,
    management_generate_client_key_for_merchant_credential,
    management_generate_hmac_merchant_webhook,
    management_get_company,
    management_get_merchant,
    management_get_merchant_api_credential,
    management_get_merchant_webhook,
    management_get_store,
    management_list_companies,
    management_list_company_merchants,
    management_list_merchant_api_credentials,
    management_list_merchant_webhooks,
    management_list_merchants,
    management_list_stores,
    management_test_merchant_webhook,
    management_update_merchant_api_credential,
    management_update_merchant_webhook,
    management_update_store,
)
from generated_tools.payment import (
    payment_adjust_authorisation,
    payment_authorise,
    payment_authorise3d,
    payment_authorise3ds2,
    payment_cancel,
    payment_cancel_or_refund,
    payment_capture,
    payment_donate,
    payment_get_authentication_result,
    payment_refund,
    payment_retrieve_3ds2_result,
    payment_technical_cancel,
    payment_void_pending_refund,
)

mcp = FastMCP("adyen")


# Checkout tools

@mcp.tool()
def adyen_checkout_create_session(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return checkout_create_session(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_checkout_get_session(sessionId: str) -> Dict[str, Any]:
    return checkout_get_session(sessionId)


@mcp.tool()
def adyen_checkout_payment_methods(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return checkout_payment_methods(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_checkout_payment_methods_balance(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return checkout_payment_methods_balance(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_checkout_payments(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return checkout_payments(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_checkout_payments_details(body: Dict[str, Any]) -> Dict[str, Any]:
    return checkout_payments_details(body)


@mcp.tool()
def adyen_checkout_payments_amount_update(paymentPspReference: str, body: Dict[str, Any]) -> Dict[str, Any]:
    return checkout_payments_amount_update(paymentPspReference, body)


@mcp.tool()
def adyen_checkout_payments_capture(paymentPspReference: str, body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return checkout_payments_capture(paymentPspReference, body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_checkout_payments_refund(paymentPspReference: str, body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return checkout_payments_refund(paymentPspReference, body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_checkout_payments_cancel(paymentPspReference: str, body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return checkout_payments_cancel(paymentPspReference, body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_checkout_payments_reversal(paymentPspReference: str, body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return checkout_payments_reversal(paymentPspReference, body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_checkout_create_payment_link(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return checkout_create_payment_link(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_checkout_get_payment_link(linkId: str) -> Dict[str, Any]:
    return checkout_get_payment_link(linkId)


@mcp.tool()
def adyen_checkout_update_payment_link(linkId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    return checkout_update_payment_link(linkId, body)


@mcp.tool()
def adyen_checkout_list_stored_payment_methods(shopperReference: str, merchantAccount: str | None = None) -> Dict[str, Any]:
    return checkout_list_stored_payment_methods(shopperReference=shopperReference, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_checkout_delete_stored_payment_method(storedPaymentMethodId: str) -> Dict[str, Any]:
    return checkout_delete_stored_payment_method(storedPaymentMethodId)


# Payment tools

@mcp.tool()
def adyen_payment_authorise(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return payment_authorise(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_payment_authorise3d(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return payment_authorise3d(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_payment_authorise3ds2(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return payment_authorise3ds2(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_payment_get_authentication_result(body: Dict[str, Any]) -> Dict[str, Any]:
    return payment_get_authentication_result(body)


@mcp.tool()
def adyen_payment_retrieve_3ds2_result(body: Dict[str, Any]) -> Dict[str, Any]:
    return payment_retrieve_3ds2_result(body)


@mcp.tool()
def adyen_payment_adjust_authorisation(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return payment_adjust_authorisation(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_payment_capture(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return payment_capture(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_payment_refund(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return payment_refund(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_payment_cancel(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return payment_cancel(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_payment_cancel_or_refund(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return payment_cancel_or_refund(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_payment_technical_cancel(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return payment_technical_cancel(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_payment_void_pending_refund(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return payment_void_pending_refund(body, merchantAccount=merchantAccount)


@mcp.tool()
def adyen_payment_donate(body: Dict[str, Any], merchantAccount: str | None = None) -> Dict[str, Any]:
    return payment_donate(body, merchantAccount=merchantAccount)


# Management tools

@mcp.tool()
def adyen_management_list_companies() -> Dict[str, Any]:
    return management_list_companies()


@mcp.tool()
def adyen_management_get_company(companyId: str) -> Dict[str, Any]:
    return management_get_company(companyId)


@mcp.tool()
def adyen_management_list_company_merchants(companyId: str | None = None) -> Dict[str, Any]:
    return management_list_company_merchants(companyId)


@mcp.tool()
def adyen_management_list_merchants() -> Dict[str, Any]:
    return management_list_merchants()


@mcp.tool()
def adyen_management_get_merchant(merchantId: str) -> Dict[str, Any]:
    return management_get_merchant(merchantId)


@mcp.tool()
def adyen_management_create_merchant(body: Dict[str, Any]) -> Dict[str, Any]:
    return management_create_merchant(body)


@mcp.tool()
def adyen_management_activate_merchant(merchantId: str) -> Dict[str, Any]:
    return management_activate_merchant(merchantId)


@mcp.tool()
def adyen_management_list_stores(merchantId: str | None = None) -> Dict[str, Any]:
    return management_list_stores(merchantId=merchantId)


@mcp.tool()
def adyen_management_get_store(storeId: str) -> Dict[str, Any]:
    return management_get_store(storeId)


@mcp.tool()
def adyen_management_create_store(merchantId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    return management_create_store(body, merchantId=merchantId)


@mcp.tool()
def adyen_management_update_store(storeId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    return management_update_store(storeId, body)


@mcp.tool()
def adyen_management_list_merchant_webhooks(merchantId: str) -> Dict[str, Any]:
    return management_list_merchant_webhooks(merchantId)


@mcp.tool()
def adyen_management_get_merchant_webhook(merchantId: str, webhookId: str) -> Dict[str, Any]:
    return management_get_merchant_webhook(merchantId, webhookId)


@mcp.tool()
def adyen_management_create_merchant_webhook(merchantId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    return management_create_merchant_webhook(merchantId, body)


@mcp.tool()
def adyen_management_update_merchant_webhook(merchantId: str, webhookId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    return management_update_merchant_webhook(merchantId, webhookId, body)


@mcp.tool()
def adyen_management_delete_merchant_webhook(merchantId: str, webhookId: str) -> Dict[str, Any]:
    return management_delete_merchant_webhook(merchantId, webhookId)


@mcp.tool()
def adyen_management_test_merchant_webhook(merchantId: str, webhookId: str) -> Dict[str, Any]:
    return management_test_merchant_webhook(merchantId, webhookId)


@mcp.tool()
def adyen_management_generate_hmac_merchant_webhook(merchantId: str, webhookId: str) -> Dict[str, Any]:
    return management_generate_hmac_merchant_webhook(merchantId, webhookId)


@mcp.tool()
def adyen_management_list_merchant_api_credentials(merchantId: str) -> Dict[str, Any]:
    return management_list_merchant_api_credentials(merchantId)


@mcp.tool()
def adyen_management_get_merchant_api_credential(merchantId: str, apiCredentialId: str) -> Dict[str, Any]:
    return management_get_merchant_api_credential(merchantId, apiCredentialId)


@mcp.tool()
def adyen_management_create_merchant_api_credential(merchantId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    return management_create_merchant_api_credential(merchantId, body)


@mcp.tool()
def adyen_management_update_merchant_api_credential(merchantId: str, apiCredentialId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    return management_update_merchant_api_credential(merchantId, apiCredentialId, body)


@mcp.tool()
def adyen_management_generate_api_key_for_merchant_credential(merchantId: str, apiCredentialId: str) -> Dict[str, Any]:
    return management_generate_api_key_for_merchant_credential(merchantId, apiCredentialId)


@mcp.tool()
def adyen_management_generate_client_key_for_merchant_credential(merchantId: str, apiCredentialId: str) -> Dict[str, Any]:
    return management_generate_client_key_for_merchant_credential(merchantId, apiCredentialId)


if __name__ == "__main__":
    mcp.run()
