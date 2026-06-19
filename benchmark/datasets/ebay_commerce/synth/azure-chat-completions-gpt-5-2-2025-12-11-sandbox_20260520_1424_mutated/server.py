import os
import json
import base64
from typing import Any, Dict, Optional

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

APP_NAME = "ebay-commerce-mcp"

DEFAULT_API_BASE = os.getenv("EBAY_API_BASE", "https://api.ebay.com")
DEFAULT_APIM_BASE = os.getenv("EBAY_APIM_BASE", "https://apim.ebay.com")
DEFAULT_SANDBOX = os.getenv("EBAY_SANDBOX", "false").lower() in ("1", "true", "yes")


def _pick_base(host: str, sandbox: Optional[bool] = None) -> str:
    use_sandbox = DEFAULT_SANDBOX if sandbox is None else sandbox
    if host == "apim":
        return os.getenv(
            "EBAY_APIM_BASE",
            "https://apim.sandbox.ebay.com" if use_sandbox else DEFAULT_APIM_BASE,
        )
    return os.getenv(
        "EBAY_API_BASE",
        "https://api.sandbox.ebay.com" if use_sandbox else DEFAULT_API_BASE,
    )


def _auth_header(access_token: Optional[str]) -> Dict[str, str]:
    token = access_token or os.getenv("EBAY_ACCESS_TOKEN")
    if not token:
        raise ValueError(
            "Missing OAuth access token. Provide 'access_token' or set EBAY_ACCESS_TOKEN."
        )
    return {"Authorization": f"Bearer {token}"}


def _clean_headers(headers: Optional[Dict[str, str]]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    if headers:
        for k, v in headers.items():
            if v is None:
                continue
            out[str(k)] = str(v)
    return out


async def _request(
    *,
    method: str,
    host: str,
    path: str,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Any = None,
    content: Any = None,
) -> Dict[str, Any]:
    base = _pick_base(host, sandbox)
    url = base.rstrip("/") + "/" + path.lstrip("/")

    req_headers = {}
    req_headers.update(_auth_header(access_token))
    req_headers.update(_clean_headers(headers))

    timeout = httpx.Timeout(60.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        resp = await client.request(
            method=method,
            url=url,
            params=params,
            headers=req_headers,
            json=json_body,
            content=content,
        )

    # Try to parse JSON; otherwise return text
    parsed: Any
    try:
        parsed = resp.json()
    except Exception:
        parsed = resp.text

    return {
        "url": str(resp.request.url),
        "method": method.upper(),
        "status_code": resp.status_code,
        "headers": dict(resp.headers),
        "data": parsed,
    }


mcp = FastMCP(APP_NAME)


# ---------------------- Catalog API ----------------------

@mcp.tool()
async def catalog_get_product(
    product_id: str,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
    marketplace_id: Optional[str] = None,
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    """Get details for a specific eBay catalog product.

    Docs: commerce/catalog/v1/product/{product_id}
    """
    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if accept_language:
        headers["Accept-Language"] = accept_language

    return await _request(
        method="GET",
        host="api",
        path=f"commerce/catalog/v1/product/{product_id}",
        access_token=access_token,
        sandbox=sandbox,
        headers=headers,
    )


@mcp.tool()
async def catalog_search_product_summaries(
    q: Optional[str] = None,
    gtin: Optional[str] = None,
    epid: Optional[str] = None,
    mpn: Optional[str] = None,
    brand: Optional[str] = None,
    category_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
    marketplace_id: Optional[str] = None,
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    """Search for product summaries.

    Docs: commerce/catalog/v1/product_summary/search
    """
    params: Dict[str, Any] = {}
    for k, v in {
        "q": q,
        "gtin": gtin,
        "epid": epid,
        "mpn": mpn,
        "brand": brand,
        "category_ids": category_ids,
        "limit": limit,
        "offset": offset,
    }.items():
        if v is not None:
            params[k] = v

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if accept_language:
        headers["Accept-Language"] = accept_language

    return await _request(
        method="GET",
        host="api",
        path="commerce/catalog/v1/product_summary/search",
        access_token=access_token,
        sandbox=sandbox,
        params=params,
        headers=headers,
    )


# ---------------------- Charity API ----------------------

@mcp.tool()
async def charity_get_charity_org(
    charity_org_id: str,
    marketplace_id: str,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Retrieve details about a supported charitable organization.

    Requires X-EBAY-C-MARKETPLACE-ID (EBAY_US or EBAY_GB).
    Docs: commerce/charity/v1/charity_org/{charity_org_id}
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return await _request(
        method="GET",
        host="api",
        path=f"commerce/charity/v1/charity_org/{charity_org_id}",
        access_token=access_token,
        sandbox=sandbox,
        headers=headers,
    )


@mcp.tool()
async def charity_search_charity_orgs(
    marketplace_id: str,
    q: Optional[str] = None,
    registration_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Search for supported charitable organizations.

    Docs: commerce/charity/v1/charity_org
    """
    params: Dict[str, Any] = {}
    for k, v in {"q": q, "registration_ids": registration_ids, "limit": limit, "offset": offset}.items():
        if v is not None:
            params[k] = v

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return await _request(
        method="GET",
        host="api",
        path="commerce/charity/v1/charity_org",
        access_token=access_token,
        sandbox=sandbox,
        params=params,
        headers=headers,
    )


# ---------------------- Identity API ----------------------

@mcp.tool()
async def identity_get_user(
    username: str,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Retrieve public information about an eBay user.

    Docs: commerce/identity/v1/user/{username}
    """
    return await _request(
        method="GET",
        host="api",
        path=f"commerce/identity/v1/user/{username}",
        access_token=access_token,
        sandbox=sandbox,
    )


# ---------------------- Media API (v1_beta) ----------------------

@mcp.tool()
async def media_create_document_from_url(
    documentType: str,
    documentUrl: str,
    languages: list[str],
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Download a document from a URL and add it to the user's account.

    Docs: commerce/media/v1_beta/document/create_document_from_url
    """
    body = {"documentType": documentType, "documentUrl": documentUrl, "languages": languages}
    return await _request(
        method="POST",
        host="api",
        path="commerce/media/v1_beta/document/create_document_from_url",
        access_token=access_token,
        sandbox=sandbox,
        headers={"Content-Type": "application/json"},
        json_body=body,
    )


@mcp.tool()
async def media_create_video(
    title: str,
    size: int,
    classification: list[dict],
    description: Optional[str] = None,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Create a video resource (metadata only). Upload is a separate call.

    Docs: apim.ebay.com/commerce/media/v1_beta/video
    """
    body: Dict[str, Any] = {"title": title, "size": size, "classification": classification}
    if description is not None:
        body["description"] = description

    return await _request(
        method="POST",
        host="apim",
        path="commerce/media/v1_beta/video",
        access_token=access_token,
        sandbox=sandbox,
        headers={"Content-Type": "application/json"},
        json_body=body,
    )


@mcp.tool()
async def media_create_image_from_file(
    file_base64: str,
    file_name: str,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Create an image resource from a file.

    Input is base64-encoded bytes of the image file.
    Docs: commerce/media/v1_beta/image/create_image_from_file
    """
    raw = base64.b64decode(file_base64)
    headers = {
        # Many eBay upload endpoints accept multipart/form-data; docs are truncated here.
        # We'll send as multipart with field name 'image'.
    }
    base = _pick_base("api", sandbox)
    url = base.rstrip("/") + "/commerce/media/v1_beta/image/create_image_from_file"

    req_headers = {}
    req_headers.update(_auth_header(access_token))

    timeout = httpx.Timeout(120.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        resp = await client.post(
            url,
            headers=req_headers,
            files={"image": (file_name, raw)},
        )

    try:
        data = resp.json()
    except Exception:
        data = resp.text

    return {
        "url": str(resp.request.url),
        "method": "POST",
        "status_code": resp.status_code,
        "headers": dict(resp.headers),
        "data": data,
    }


# ---------------------- Notification API ----------------------

@mcp.tool()
async def notification_get_destinations(
    page_size: Optional[int] = None,
    continuation_token: Optional[str] = None,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Retrieve a paginated collection of destination resources.

    Docs: commerce/notification/v1/destination
    """
    params: Dict[str, Any] = {}
    if page_size is not None:
        params["page_size"] = page_size
    if continuation_token is not None:
        params["continuation_token"] = continuation_token

    return await _request(
        method="GET",
        host="api",
        path="commerce/notification/v1/destination",
        access_token=access_token,
        sandbox=sandbox,
        params=params,
    )


@mcp.tool()
async def notification_create_destination(
    name: str,
    endpoint: str,
    verificationToken: str,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Create a destination endpoint for notifications.

    Docs: commerce/notification/v1/destination
    """
    body = {
        "name": name,
        "deliveryConfig": {"endpoint": endpoint, "verificationToken": verificationToken},
    }
    return await _request(
        method="POST",
        host="api",
        path="commerce/notification/v1/destination",
        access_token=access_token,
        sandbox=sandbox,
        headers={"Content-Type": "application/json"},
        json_body=body,
    )


@mcp.tool()
async def notification_create_subscription(
    topicId: str,
    status: str,
    destinationId: str,
    payload: dict,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Create a subscription to a notification topic.

    Docs: commerce/notification/v1/subscription
    """
    body = {
        "topicId": topicId,
        "status": status,
        "destinationId": destinationId,
        "payload": payload,
    }
    return await _request(
        method="POST",
        host="api",
        path="commerce/notification/v1/subscription",
        access_token=access_token,
        sandbox=sandbox,
        headers={"Content-Type": "application/json"},
        json_body=body,
    )


@mcp.tool()
async def notification_update_subscription(
    subscription_id: str,
    status: str,
    destinationId: str,
    payload: dict,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update a subscription.

    Docs: commerce/notification/v1/subscription/{subscription_id}
    """
    body = {"status": status, "destinationId": destinationId, "payload": payload}
    return await _request(
        method="PUT",
        host="api",
        path=f"commerce/notification/v1/subscription/{subscription_id}",
        access_token=access_token,
        sandbox=sandbox,
        headers={"Content-Type": "application/json"},
        json_body=body,
    )


# ---------------------- Taxonomy API ----------------------

@mcp.tool()
async def taxonomy_get_default_category_tree_id(
    marketplace_id: str,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Get the default category tree ID for a marketplace.

    Docs: commerce/taxonomy/v1/get_default_category_tree_id
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return await _request(
        method="GET",
        host="api",
        path="commerce/taxonomy/v1/get_default_category_tree_id",
        access_token=access_token,
        sandbox=sandbox,
        headers=headers,
    )


@mcp.tool()
async def taxonomy_get_category_suggestions(
    category_tree_id: str,
    query: str,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    """Get category suggestions for a query string.

    Docs: commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions
    """
    headers: Dict[str, str] = {}
    if accept_language:
        headers["Accept-Language"] = accept_language

    return await _request(
        method="GET",
        host="api",
        path=f"commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        access_token=access_token,
        sandbox=sandbox,
        params={"query": query},
        headers=headers,
    )


@mcp.tool()
async def taxonomy_get_item_aspects_for_category(
    category_tree_id: str,
    category_id: str,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    """Get item aspects metadata for a leaf category.

    Docs: commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category
    """
    headers: Dict[str, str] = {}
    if accept_language:
        headers["Accept-Language"] = accept_language

    return await _request(
        method="GET",
        host="api",
        path=f"commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        access_token=access_token,
        sandbox=sandbox,
        params={"category_id": category_id},
        headers=headers,
    )


# ---------------------- Translation API ----------------------

@mcp.tool()
async def translation_translate(
    from_: str,
    to: str,
    text: str,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Translate text.

    Docs: commerce/translation/v1/translate
    """
    body = {"from": from_, "to": to, "text": text}
    return await _request(
        method="POST",
        host="api",
        path="commerce/translation/v1/translate",
        access_token=access_token,
        sandbox=sandbox,
        headers={"Content-Type": "application/json"},
        json_body=body,
    )


# ---------------------- Generic escape hatch ----------------------

@mcp.tool()
async def ebay_raw_request(
    method: str,
    path: str,
    host: str = "api",
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Any = None,
    body_base64: Optional[str] = None,
    access_token: Optional[str] = None,
    sandbox: Optional[bool] = None,
) -> Dict[str, Any]:
    """Make an arbitrary request to eBay Commerce APIs.

    - host: 'api' (api.ebay.com) or 'apim' (apim.ebay.com)
    - path: e.g. 'commerce/notification/v1/destination'
    - body_base64: optional raw body bytes (base64) if not JSON
    """
    content = base64.b64decode(body_base64) if body_base64 else None
    return await _request(
        method=method,
        host=host,
        path=path,
        access_token=access_token,
        sandbox=sandbox,
        params=params,
        headers=headers,
        json_body=json_body,
        content=content,
    )


if __name__ == "__main__":
    mcp.run()
