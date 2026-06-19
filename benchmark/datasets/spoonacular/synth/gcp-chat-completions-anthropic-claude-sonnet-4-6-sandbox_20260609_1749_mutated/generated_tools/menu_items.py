"""Spoonacular Menu Items API tools."""
import os
import requests
from typing import Optional

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable not set")
    return key


def _get(path: str, params: dict) -> dict:
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_menu_items(
    query: str,
    min_calories: Optional[float] = None,
    max_calories: Optional[float] = None,
    min_carbs: Optional[float] = None,
    max_carbs: Optional[float] = None,
    min_protein: Optional[float] = None,
    max_protein: Optional[float] = None,
    min_fat: Optional[float] = None,
    max_fat: Optional[float] = None,
    add_menu_item_information: Optional[bool] = None,
    offset: int = 0,
    number: int = 10,
) -> dict:
    """Search over 115,000 menu items from fast food and chain restaurants."""
    params: dict = {"query": query, "offset": offset, "number": number}
    if min_calories is not None: params["minCalories"] = min_calories
    if max_calories is not None: params["maxCalories"] = max_calories
    if min_carbs is not None: params["minCarbs"] = min_carbs
    if max_carbs is not None: params["maxCarbs"] = max_carbs
    if min_protein is not None: params["minProtein"] = min_protein
    if max_protein is not None: params["maxProtein"] = max_protein
    if min_fat is not None: params["minFat"] = min_fat
    if max_fat is not None: params["maxFat"] = max_fat
    if add_menu_item_information is not None: params["addMenuItemInformation"] = add_menu_item_information
    return _get("/food/menuItems/search", params)


def get_menu_item_information(menu_item_id: int) -> dict:
    """Get all available information about a menu item by its ID, including nutrition."""
    return _get(f"/food/menuItems/{menu_item_id}", {})


def autocomplete_menu_item_search(query: str, number: int = 10) -> dict:
    """Generate autocomplete suggestions for menu items based on a partial query."""
    params = {"query": query, "number": number}
    return _get("/food/menuItems/suggest", params)
