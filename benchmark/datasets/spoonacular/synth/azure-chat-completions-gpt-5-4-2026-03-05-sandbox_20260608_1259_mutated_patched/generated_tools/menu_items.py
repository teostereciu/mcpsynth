from typing import Any, Optional

from .common import spoonacular_request


def search_menu_items(
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
    return spoonacular_request("GET", "/food/menuItems/search", params=locals())


def get_menu_item_information(id: int) -> Any:
    return spoonacular_request("GET", f"/food/menuItems/{id}")


def autocomplete_menu_item_search(search_query: str, number: Optional[int] = None) -> Any:
    return spoonacular_request("GET", "/food/menuItems/suggest", params=locals())
