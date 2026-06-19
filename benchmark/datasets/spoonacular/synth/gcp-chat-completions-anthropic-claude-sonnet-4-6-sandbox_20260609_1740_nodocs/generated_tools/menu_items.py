"""
Spoonacular Menu Items tools — search restaurant menu items, get item info.
"""
import os
import requests

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def search_menu_items(
    query: str,
    min_calories: float = None,
    max_calories: float = None,
    min_carbs: float = None,
    max_carbs: float = None,
    min_protein: float = None,
    max_protein: float = None,
    min_fat: float = None,
    max_fat: float = None,
    add_menu_item_information: bool = None,
    offset: int = None,
    number: int = 10,
) -> dict:
    """
    Search for restaurant menu items by name with optional nutritional filters.
    Returns a list of matching menu items with basic nutritional information.
    """
    params = {
        "query": query,
        "minCalories": min_calories,
        "maxCalories": max_calories,
        "minCarbs": min_carbs,
        "maxCarbs": max_carbs,
        "minProtein": min_protein,
        "maxProtein": max_protein,
        "minFat": min_fat,
        "maxFat": max_fat,
        "addMenuItemInformation": add_menu_item_information,
        "offset": offset,
        "number": number,
    }
    return _get("/food/menuItems/search", params)


def get_menu_item_information(menu_item_id: int) -> dict:
    """
    Get detailed information about a restaurant menu item by its Spoonacular ID,
    including nutritional data and restaurant name.
    """
    return _get(f"/food/menuItems/{menu_item_id}", {})


def autocomplete_menu_item_search(query: str, number: int = 10) -> list:
    """
    Autocomplete a restaurant menu item search query. Returns a list of
    menu item name suggestions matching the query prefix.
    """
    params = {"query": query, "number": number}
    return _get("/food/menuItems/suggest", params)


def get_menu_item_nutrition_by_id(menu_item_id: int) -> dict:
    """
    Get the nutritional information for a restaurant menu item by its
    Spoonacular ID. Returns macros, vitamins, minerals, and serving size.
    """
    return _get(f"/food/menuItems/{menu_item_id}/nutritionWidget.json", {})
