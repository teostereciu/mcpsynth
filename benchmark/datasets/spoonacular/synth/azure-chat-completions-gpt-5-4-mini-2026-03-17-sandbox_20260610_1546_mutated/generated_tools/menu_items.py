from typing import Any, Dict

from server import _request


def search_menu_items(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/menuItems/search", params=params)


def get_menu_item_information(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/food/menuItems/{id}", params=params)


def autocomplete_menu_item_search(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/menuItems/suggest", params=params)
