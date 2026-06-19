from typing import Any, Dict, Optional

from .http_client import request_json


def search_menu_items(
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
    addMenuItemInformation: Optional[bool] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Any:
    """GET /food/menuItems/search"""
    params: Dict[str, Any] = {
        "search_query": search_query,
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
    }
    return request_json("GET", "/food/menuItems/search", params=params)


def get_menu_item_information(*, id: int) -> Any:
    """GET /food/menuItems/{id}"""
    return request_json("GET", f"/food/menuItems/{id}")


def autocomplete_menu_item_search(*, search_query: str, number: Optional[int] = None) -> Any:
    """GET /food/menuItems/suggest"""
    return request_json("GET", "/food/menuItems/suggest", params={"search_query": search_query, "number": number})
