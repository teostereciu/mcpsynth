from typing import Any, Dict, Optional

from .http_client import request_json


def menu_items_search(
    query: str,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    addMenuItemInformation: Optional[bool] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /food/menuItems/search"""
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
        "addMenuItemInformation": addMenuItemInformation,
        "offset": offset,
        "number": number,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/food/menuItems/search", params=params)


def menu_items_get_information(id: int) -> Dict[str, Any]:
    """GET /food/menuItems/{id}"""
    return request_json("GET", f"/food/menuItems/{id}")


def menu_items_autocomplete(query: str, number: Optional[int] = None) -> Dict[str, Any]:
    """GET /food/menuItems/suggest"""
    params: Dict[str, Any] = {"query": query}
    if number is not None:
        params["number"] = number
    return request_json("GET", "/food/menuItems/suggest", params=params)
