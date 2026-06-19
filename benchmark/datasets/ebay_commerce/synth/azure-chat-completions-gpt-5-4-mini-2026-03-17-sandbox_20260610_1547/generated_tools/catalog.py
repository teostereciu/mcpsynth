from .common import get_app_token, get_base_url, request


def search_products(q=None, gtin=None, mpn=None, category_ids=None, aspect_filter=None, fieldgroups=None, limit=None, offset=None):
    tok = get_app_token()
    if "error" in tok:
        return tok
    params = {k: v for k, v in {"q": q, "gtin": gtin, "mpn": mpn, "category_ids": category_ids, "aspect_filter": aspect_filter, "fieldgroups": fieldgroups, "limit": limit, "offset": offset}.items() if v is not None}
    return request("GET", f"{get_base_url()}/commerce/catalog/v1_beta/product_summary/search", tok["access_token"], params=params)


def get_product(epid, marketplace_id=None):
    tok = get_app_token()
    if "error" in tok:
        return tok
    return request("GET", f"{get_base_url()}/commerce/catalog/v1_beta/product/{epid}", tok["access_token"], params={"X-EBAY-C-MARKETPLACE-ID": marketplace_id} if marketplace_id else None)
