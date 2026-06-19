from typing import Any, Dict, Optional

from .http_client import request_json


def search_grocery_products(
    *,
    search_query: str,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    addProductInformation: Optional[bool] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /food/products/search"""
    params: Dict[str, Any] = {"query": search_query}
    for k, v in {
        "minCalories": minCalories,
        "maxCalories": maxCalories,
        "minCarbs": minCarbs,
        "maxCarbs": maxCarbs,
        "minProtein": minProtein,
        "maxProtein": maxProtein,
        "minFat": minFat,
        "maxFat": maxFat,
        "addProductInformation": addProductInformation,
        "offset": offset,
        "number": number,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/food/products/search", params=params)


def search_grocery_products_by_upc(*, upc: str) -> Dict[str, Any]:
    """GET /food/products/upc/{upc}"""
    return request_json("GET", f"/food/products/upc/{upc}")


def get_product_information(*, id: int) -> Dict[str, Any]:
    """GET /food/products/{id}"""
    return request_json("GET", f"/food/products/{id}")
