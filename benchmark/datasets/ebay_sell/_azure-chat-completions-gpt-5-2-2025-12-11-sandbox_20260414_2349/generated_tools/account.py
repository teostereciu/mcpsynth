from typing import Any, Dict, Optional

from . import client as _shared
from .client import SCOPE_ACCOUNT
from . import mcp

API = "/sell/account/v1"


@mcp.tool()
def account_get_fulfillment_policies(
    marketplace_id: str,
    *,
    content_language: Optional[str] = None,
) -> Any:
    """GET /fulfillment_policy"""
    headers = {"Content-Language": content_language} if content_language else None
    return _shared.client.request(
        "GET",
        API,
        "/fulfillment_policy",
        scope=SCOPE_ACCOUNT,
        marketplace_id=marketplace_id,
        params={"marketplace_id": marketplace_id},
        headers=headers,
    )


@mcp.tool()
def account_get_payment_policies(
    marketplace_id: str,
    *,
    content_language: Optional[str] = None,
) -> Any:
    """GET /payment_policy"""
    headers = {"Content-Language": content_language} if content_language else None
    return _shared.client.request(
        "GET",
        API,
        "/payment_policy",
        scope=SCOPE_ACCOUNT,
        marketplace_id=marketplace_id,
        params={"marketplace_id": marketplace_id},
        headers=headers,
    )


@mcp.tool()
def account_get_return_policies(
    marketplace_id: str,
    *,
    content_language: Optional[str] = None,
) -> Any:
    """GET /return_policy"""
    headers = {"Content-Language": content_language} if content_language else None
    return _shared.client.request(
        "GET",
        API,
        "/return_policy",
        scope=SCOPE_ACCOUNT,
        marketplace_id=marketplace_id,
        params={"marketplace_id": marketplace_id},
        headers=headers,
    )


@mcp.tool()
def account_get_sales_taxes(
    country_code: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /sales_tax/{countryCode}"""
    return _shared.client.request(
        "GET",
        API,
        f"/sales_tax/{country_code}",
        scope=SCOPE_ACCOUNT,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def account_get_privileges(*, marketplace_id: str = "EBAY_US") -> Any:
    """GET /privilege"""
    return _shared.client.request(
        "GET",
        API,
        "/privilege",
        scope=SCOPE_ACCOUNT,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def account_get_subscription(*, marketplace_id: str = "EBAY_US") -> Any:
    """GET /subscription"""
    return _shared.client.request(
        "GET",
        API,
        "/subscription",
        scope=SCOPE_ACCOUNT,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def account_get_opted_in_programs(*, marketplace_id: str = "EBAY_US") -> Any:
    """GET /program/get_opted_in_programs"""
    return _shared.client.request(
        "GET",
        API,
        "/program/get_opted_in_programs",
        scope=SCOPE_ACCOUNT,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def account_opt_in_to_program(
    program: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /program/opt_in"""
    return _shared.client.request(
        "POST",
        API,
        "/program/opt_in",
        scope=SCOPE_ACCOUNT,
        marketplace_id=marketplace_id,
        json=program,
    )


@mcp.tool()
def account_opt_out_of_program(
    program_type: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /program/opt_out"""
    return _shared.client.request(
        "POST",
        API,
        "/program/opt_out",
        scope=SCOPE_ACCOUNT,
        marketplace_id=marketplace_id,
        json={"programType": program_type},
    )
