from typing import Any, Dict, Optional

from .ebay_client import EbayClient


TAXONOMY_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/get_default_category_tree_id"""
    client = EbayClient()
    return client.request(
        "GET",
        client.api_base,
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        params={"marketplace_id": marketplace_id},
        auth="app",
        scope=TAXONOMY_SCOPE,
    )


def get_category_tree(category_tree_id: str, *, accept_gzip: bool = True) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}"""
    client = EbayClient()
    headers = {"Accept-Encoding": "gzip"} if accept_gzip else {}
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        headers=headers,
        auth="app",
        scope=TAXONOMY_SCOPE,
        timeout=120,
    )


def get_category_subtree(
    category_tree_id: str,
    category_id: str,
    *,
    accept_gzip: bool = True,
) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree"""
    client = EbayClient()
    headers = {"Accept-Encoding": "gzip"} if accept_gzip else {}
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        params={"category_id": category_id},
        headers=headers,
        auth="app",
        scope=TAXONOMY_SCOPE,
        timeout=120,
    )


def get_category_suggestions(
    category_tree_id: str,
    query: str,
    *,
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions"""
    client = EbayClient()
    headers: Dict[str, str] = {}
    if accept_language:
        headers["Accept-Language"] = accept_language
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params={"query": query},
        headers=headers,
        auth="app",
        scope=TAXONOMY_SCOPE,
    )


def get_item_aspects_for_category(
    category_tree_id: str,
    category_id: str,
    *,
    marketplace_id: Optional[str] = None,
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category"""
    client = EbayClient()
    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if accept_language:
        headers["Accept-Language"] = accept_language
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_id": category_id},
        headers=headers,
        auth="app",
        scope=TAXONOMY_SCOPE,
    )


def fetch_item_aspects(category_tree_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects

    Note: eBay returns a gzipped JSON file as application/octet-stream.
    This tool returns the raw bytes base64-encoded.
    """
    import base64

    client = EbayClient()
    # Use low-level request to preserve bytes
    url = client.api_base.rstrip("/") + f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects"
    try:
        token = client.get_app_token(scope=TAXONOMY_SCOPE)
    except Exception as e:
        return {"error": str(e)}

    import requests

    try:
        resp = requests.get(
            url,
            headers={"Authorization": f"Bearer {token}", "Accept": "application/octet-stream"},
            timeout=300,
        )
    except Exception as e:
        return {"error": str(e)}

    if resp.status_code >= 400:
        try:
            return {"error": resp.json(), "status_code": resp.status_code}
        except Exception:
            return {"error": resp.text, "status_code": resp.status_code}

    return {
        "status_code": resp.status_code,
        "content_type": resp.headers.get("Content-Type"),
        "content_base64": base64.b64encode(resp.content).decode("ascii"),
    }


def get_expired_categories(category_tree_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories"""
    client = EbayClient()
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
        auth="app",
        scope=TAXONOMY_SCOPE,
    )


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties"""
    client = EbayClient()
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        params={"category_id": category_id},
        auth="app",
        scope=TAXONOMY_SCOPE,
    )


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    *,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values"""
    client = EbayClient()
    params: Dict[str, Any] = {"category_id": category_id, "compatibility_property": compatibility_property}
    if filter is not None:
        params["filter"] = filter
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        params=params,
        auth="app",
        scope=TAXONOMY_SCOPE,
        timeout=120,
    )
