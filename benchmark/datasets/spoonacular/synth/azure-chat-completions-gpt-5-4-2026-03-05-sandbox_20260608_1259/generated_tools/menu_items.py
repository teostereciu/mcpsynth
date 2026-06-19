from typing import Any, Optional

from generated_tools.recipes import _request


def search_menu_items(
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
) -> Any:
    return _request("GET", "/food/menuItems/search", locals())


def get_menu_item_information(id: int) -> Any:
    return _request("GET", f"/food/menuItems/{id}")


def autocomplete_menu_item_search(query: str, number: Optional[int] = None) -> Any:
    return _request("GET", "/food/menuItems/suggest", locals())
