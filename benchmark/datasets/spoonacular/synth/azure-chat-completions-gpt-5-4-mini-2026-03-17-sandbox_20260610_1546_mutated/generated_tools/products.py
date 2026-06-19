from typing import Any, Dict

from server import _request


def search_grocery_products(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/products/search", params=params)


def search_grocery_products_by_upc(upc: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/food/products/upc/{upc}", params=params)


def get_product_information(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/food/products/{id}", params=params)


def get_comparable_products(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/food/products/{id}/comparable", params=params)


def autocomplete_product_search(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/products/suggest", params=params)


def classify_grocery_product(**params: Any) -> Dict[str, Any]:
    return _request("POST", "/food/products/classify", data=params)


def classify_grocery_product_bulk(**params: Any) -> Dict[str, Any]:
    return _request("POST", "/food/products/classifyBatch", data=params)


def map_ingredients_to_grocery_products(**params: Any) -> Dict[str, Any]:
    return _request("POST", "/food/products/map", data=params)
