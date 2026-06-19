from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

API_ROOT = "/sell/account/v1"
SCOPE = "https://api.ebay.com/oauth/api_scope/sell.account"


def register(mcp):
    # Fulfillment policies
    @mcp.tool()
    def account_get_fulfillment_policies(marketplace_id: str, *, content_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /fulfillment_policy - Retrieve fulfillment policies."""
        return request_json(
            "GET",
            API_ROOT,
            "/fulfillment_policy",
            scope=SCOPE,
            params={"marketplace_id": marketplace_id},
            headers={"Content-Language": content_language} if content_language else None,
        )

    @mcp.tool()
    def account_get_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
        """GET /fulfillment_policy/{fulfillmentPolicyId} - Retrieve a fulfillment policy."""
        return request_json("GET", API_ROOT, f"/fulfillment_policy/{fulfillment_policy_id}", scope=SCOPE)

    @mcp.tool()
    def account_get_fulfillment_policy_by_name(marketplace_id: str, name: str, *, content_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /fulfillment_policy/get_by_policy_name - Retrieve fulfillment policy by name."""
        params = {"marketplace_id": marketplace_id, "name": name}
        return request_json(
            "GET",
            API_ROOT,
            "/fulfillment_policy/get_by_policy_name",
            scope=SCOPE,
            params=params,
            headers={"Content-Language": content_language} if content_language else None,
        )

    @mcp.tool()
    def account_create_fulfillment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
        """POST /fulfillment_policy/ - Create a fulfillment policy."""
        return request_json(
            "POST",
            API_ROOT,
            "/fulfillment_policy/",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=policy,
        )

    @mcp.tool()
    def account_update_fulfillment_policy(fulfillment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
        """PUT /fulfillment_policy/{fulfillmentPolicyId} - Update a fulfillment policy."""
        return request_json(
            "PUT",
            API_ROOT,
            f"/fulfillment_policy/{fulfillment_policy_id}",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=policy,
        )

    @mcp.tool()
    def account_delete_fulfillment_policy(fulfillment_policy_id: str) -> Dict[str, Any]:
        """DELETE /fulfillment_policy/{fulfillmentPolicyId} - Delete a fulfillment policy."""
        return request_json("DELETE", API_ROOT, f"/fulfillment_policy/{fulfillment_policy_id}", scope=SCOPE)

    # Payment policies
    @mcp.tool()
    def account_get_payment_policies(marketplace_id: str, *, content_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /payment_policy - Retrieve payment policies."""
        return request_json(
            "GET",
            API_ROOT,
            "/payment_policy",
            scope=SCOPE,
            params={"marketplace_id": marketplace_id},
            headers={"Content-Language": content_language} if content_language else None,
        )

    @mcp.tool()
    def account_get_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
        """GET /payment_policy/{payment_policy_id} - Retrieve a payment policy."""
        return request_json("GET", API_ROOT, f"/payment_policy/{payment_policy_id}", scope=SCOPE)

    @mcp.tool()
    def account_get_payment_policy_by_name(marketplace_id: str, name: str, *, content_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /payment_policy/get_by_policy_name - Retrieve payment policy by name."""
        params = {"marketplace_id": marketplace_id, "name": name}
        return request_json(
            "GET",
            API_ROOT,
            "/payment_policy/get_by_policy_name",
            scope=SCOPE,
            params=params,
            headers={"Content-Language": content_language} if content_language else None,
        )

    @mcp.tool()
    def account_create_payment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
        """POST /payment_policy - Create a payment policy."""
        return request_json(
            "POST",
            API_ROOT,
            "/payment_policy",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=policy,
        )

    @mcp.tool()
    def account_update_payment_policy(payment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
        """PUT /payment_policy/{payment_policy_id} - Update a payment policy."""
        return request_json(
            "PUT",
            API_ROOT,
            f"/payment_policy/{payment_policy_id}",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=policy,
        )

    @mcp.tool()
    def account_delete_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
        """DELETE /payment_policy/{payment_policy_id} - Delete a payment policy."""
        return request_json("DELETE", API_ROOT, f"/payment_policy/{payment_policy_id}", scope=SCOPE)

    # Return policies
    @mcp.tool()
    def account_get_return_policies(marketplace_id: str, *, content_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /return_policy - Retrieve return policies."""
        return request_json(
            "GET",
            API_ROOT,
            "/return_policy",
            scope=SCOPE,
            params={"marketplace_id": marketplace_id},
            headers={"Content-Language": content_language} if content_language else None,
        )

    @mcp.tool()
    def account_get_return_policy(return_policy_id: str) -> Dict[str, Any]:
        """GET /return_policy/{return_policy_id} - Retrieve a return policy."""
        return request_json("GET", API_ROOT, f"/return_policy/{return_policy_id}", scope=SCOPE)

    @mcp.tool()
    def account_get_return_policy_by_name(marketplace_id: str, name: str, *, content_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /return_policy/get_by_policy_name - Retrieve return policy by name."""
        params = {"marketplace_id": marketplace_id, "name": name}
        return request_json(
            "GET",
            API_ROOT,
            "/return_policy/get_by_policy_name",
            scope=SCOPE,
            params=params,
            headers={"Content-Language": content_language} if content_language else None,
        )

    @mcp.tool()
    def account_create_return_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
        """POST /return_policy - Create a return policy."""
        return request_json(
            "POST",
            API_ROOT,
            "/return_policy",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=policy,
        )

    @mcp.tool()
    def account_update_return_policy(return_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
        """PUT /return_policy/{return_policy_id} - Update a return policy."""
        return request_json(
            "PUT",
            API_ROOT,
            f"/return_policy/{return_policy_id}",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=policy,
        )

    @mcp.tool()
    def account_delete_return_policy(return_policy_id: str) -> Dict[str, Any]:
        """DELETE /return_policy/{return_policy_id} - Delete a return policy."""
        return request_json("DELETE", API_ROOT, f"/return_policy/{return_policy_id}", scope=SCOPE)

    # Custom policies
    @mcp.tool()
    def account_get_custom_policies(policy_types: Optional[str] = None) -> Dict[str, Any]:
        """GET /custom_policy/ - Retrieve custom policies."""
        params = {"policy_types": policy_types} if policy_types else None
        return request_json("GET", API_ROOT, "/custom_policy/", scope=SCOPE, params=params)

    @mcp.tool()
    def account_get_custom_policy(custom_policy_id: str) -> Dict[str, Any]:
        """GET /custom_policy/{custom_policy_id} - Retrieve a custom policy."""
        return request_json("GET", API_ROOT, f"/custom_policy/{custom_policy_id}", scope=SCOPE)

    @mcp.tool()
    def account_create_custom_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
        """POST /custom_policy/ - Create a custom policy."""
        return request_json(
            "POST",
            API_ROOT,
            "/custom_policy/",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=policy,
        )

    @mcp.tool()
    def account_update_custom_policy(custom_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
        """PUT /custom_policy/{custom_policy_id} - Update a custom policy."""
        return request_json(
            "PUT",
            API_ROOT,
            f"/custom_policy/{custom_policy_id}",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=policy,
        )

    # Sales tax
    @mcp.tool()
    def account_get_sales_taxes(marketplace_id: Optional[str] = None) -> Dict[str, Any]:
        """GET /sales_tax - Retrieve sales taxes."""
        params = {"marketplace_id": marketplace_id} if marketplace_id else None
        return request_json("GET", API_ROOT, "/sales_tax", scope=SCOPE, params=params)

    @mcp.tool()
    def account_get_sales_tax(country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
        """GET /sales_tax/{countryCode}/{jurisdictionId} - Retrieve sales tax."""
        return request_json("GET", API_ROOT, f"/sales_tax/{country_code}/{jurisdiction_id}", scope=SCOPE)

    @mcp.tool()
    def account_create_or_replace_sales_tax(country_code: str, jurisdiction_id: str, sales_tax: Dict[str, Any]) -> Dict[str, Any]:
        """PUT /sales_tax/{countryCode}/{jurisdictionId} - Create or replace sales tax."""
        return request_json(
            "PUT",
            API_ROOT,
            f"/sales_tax/{country_code}/{jurisdiction_id}",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=sales_tax,
        )

    @mcp.tool()
    def account_delete_sales_tax(country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
        """DELETE /sales_tax/{countryCode}/{jurisdictionId} - Delete sales tax."""
        return request_json("DELETE", API_ROOT, f"/sales_tax/{country_code}/{jurisdiction_id}", scope=SCOPE)

    @mcp.tool()
    def account_bulk_create_or_replace_sales_tax(payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /bulk_create_or_replace_sales_tax - Bulk create/replace sales tax."""
        return request_json(
            "POST",
            API_ROOT,
            "/bulk_create_or_replace_sales_tax",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    # Programs, privileges, subscription, rate tables
    @mcp.tool()
    def account_get_opted_in_programs() -> Dict[str, Any]:
        """GET /program/get_opted_in_programs - Retrieve opted-in programs."""
        return request_json("GET", API_ROOT, "/program/get_opted_in_programs", scope=SCOPE)

    @mcp.tool()
    def account_opt_in_to_program(payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /program/opt_in - Opt in to a program."""
        return request_json(
            "POST",
            API_ROOT,
            "/program/opt_in",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def account_opt_out_of_program(payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /program/opt_out - Opt out of a program."""
        return request_json(
            "POST",
            API_ROOT,
            "/program/opt_out",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def account_get_privileges() -> Dict[str, Any]:
        """GET /privilege - Retrieve seller privileges."""
        return request_json("GET", API_ROOT, "/privilege", scope=SCOPE)

    @mcp.tool()
    def account_get_subscription() -> Dict[str, Any]:
        """GET /subscription - Retrieve subscription."""
        return request_json("GET", API_ROOT, "/subscription", scope=SCOPE)

    @mcp.tool()
    def account_get_rate_tables() -> Dict[str, Any]:
        """GET /rate_table - Retrieve rate tables."""
        return request_json("GET", API_ROOT, "/rate_table", scope=SCOPE)

    @mcp.tool()
    def account_get_payments_program(marketplace_id: str, payments_program_type: str) -> Dict[str, Any]:
        """GET /payments_program/{marketplace_id}/{payments_program_type} - Retrieve payments program."""
        return request_json(
            "GET",
            API_ROOT,
            f"/payments_program/{marketplace_id}/{payments_program_type}",
            scope=SCOPE,
        )

    @mcp.tool()
    def account_get_payments_program_onboarding(marketplace_id: str, payments_program_type: str) -> Dict[str, Any]:
        """GET /payments_program/{marketplace_id}/{payments_program_type}/onboarding - Retrieve onboarding."""
        return request_json(
            "GET",
            API_ROOT,
            f"/payments_program/{marketplace_id}/{payments_program_type}/onboarding",
            scope=SCOPE,
        )
