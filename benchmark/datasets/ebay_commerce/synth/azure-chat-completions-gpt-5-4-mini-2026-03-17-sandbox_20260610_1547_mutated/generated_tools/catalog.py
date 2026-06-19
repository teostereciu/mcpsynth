from typing import Any, Dict
from .common import get_base_url, get_token, request_json


def get_product(epid: str, marketplace_id: str = None) -> Dict[str, Any]:
    token = get_token("client_credentials").get("access_token")
    if not token:
        return {"error": "unable to obtain app token"}
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id} if marketplace_id else None
    return request_json("GET", f"{get_base_url()}/commerce/catalog/v1_beta/product/{epid}", token, headers=headers)


def search_products(query: str = None, gtin: str = None, mpn: str = None, category_id: str = None, aspects: str = None, field_groups: str = None, page_size: str = None, marketplace_id: str = None) -> Dict[str, Any]:
    token = get_token("client_credentials").get("access_token")
    if not token:
        return {"error": "unable to obtain app token"}
    params = {k: v for k, v in {"query": query, "gtin": gtin, "mpn": mpn, "category_id": category_id, "aspects": aspects, "field_groups": field_groups, "page_size": page_size}.items() if v is not None}
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id} if marketplace_id else None
    return request_json("GET", f"{get_base_url()}/commerce/catalog/v1_beta/product_summary/search", token, params=params, headers=headers)
