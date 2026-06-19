from typing import Any, Dict, Optional

from .http_client import request_json


def products_search(
    query: str,
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
    params: Dict[str, Any] = {"query": query}
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


def products_get_by_upc(upc: str) -> Dict[str, Any]:
    """GET /food/products/upc/{upc}"""
    return request_json("GET", f"/food/products/upc/{upc}")


def products_get_information(id: int) -> Dict[str, Any]:
    """GET /food/products/{id}"""
    return request_json("GET", f"/food/products/{id}")


def products_comparable_by_upc(upc: str) -> Dict[str, Any]:
    """GET /food/products/upc/{upc}/comparable"""
    return request_json("GET", f"/food/products/upc/{upc}/comparable")


def products_autocomplete(query: str, number: Optional[int] = None) -> Dict[str, Any]:
    """GET /food/products/suggest"""
    params: Dict[str, Any] = {"query": query}
    if number is not None:
        params["number"] = number
    return request_json("GET", "/food/products/suggest", params=params)


def products_classify(body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /food/products/classify"""
    return request_json("POST", "/food/products/classify", json_body=body)


def products_classify_batch(body: Any) -> Dict[str, Any]:
    """POST /food/products/classifyBatch"""
    return request_json("POST", "/food/products/classifyBatch", json_body={"items": body} if not isinstance(body, dict) else body)


def ingredients_map_to_products(body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /food/ingredients/map"""
    return request_json("POST", "/food/ingredients/map", json_body=body)
