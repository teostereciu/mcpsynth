"""
Spoonacular Menu Items tools — search restaurant menu items, get details.
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
    params["apiKey"] = _api_key()
    url = f"{BASE_URL}{path}"
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# Search menu items
# ---------------------------------------------------------------------------

def search_menu_items(
    query: str,
    number: int = 10,
    offset: int = 0,
    min_calories: float = None,
    max_calories: float = None,
    min_protein: float = None,
    max_protein: float = None,
    min_fat: float = None,
    max_fat: float = None,
    min_carbs: float = None,
    max_carbs: float = None,
) -> dict:
    """
    Search for restaurant menu items in the Spoonacular database.

    Args:
        query: The menu item name or keyword to search for.
        number: Number of results to return (max 100).
        offset: Pagination offset.
        min_calories: Minimum calories per serving.
        max_calories: Maximum calories per serving.
        min_protein: Minimum protein (g) per serving.
        max_protein: Maximum protein (g) per serving.
        min_fat: Minimum fat (g) per serving.
        max_fat: Maximum fat (g) per serving.
        min_carbs: Minimum carbohydrates (g) per serving.
        max_carbs: Maximum carbohydrates (g) per serving.

    Returns:
        dict with 'menuItems' list and 'totalMenuItems' count.
    """
    try:
        params: dict = {"query": query, "number": number, "offset": offset}
        for key, val in [
            ("minCalories", min_calories), ("maxCalories", max_calories),
            ("minProtein", min_protein), ("maxProtein", max_protein),
            ("minFat", min_fat), ("maxFat", max_fat),
            ("minCarbs", min_carbs), ("maxCarbs", max_carbs),
        ]:
            if val is not None:
                params[key] = val
        return _get("/food/menuItems/search", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get menu item information
# ---------------------------------------------------------------------------

def get_menu_item_information(menu_item_id: int) -> dict:
    """
    Get detailed information about a restaurant menu item by its Spoonacular ID.

    Args:
        menu_item_id: The Spoonacular menu item ID.

    Returns:
        dict with menu item details including nutrition, restaurant, and badges.
    """
    try:
        return _get(f"/food/menuItems/{menu_item_id}", {})
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Autocomplete menu item search
# ---------------------------------------------------------------------------

def autocomplete_menu_item_search(query: str, number: int = 10) -> list:
    """
    Autocomplete a menu item search query.

    Args:
        query: Partial menu item name to autocomplete.
        number: Number of suggestions to return.

    Returns:
        List of autocomplete suggestion objects.
    """
    try:
        params = {"query": query, "number": number}
        return _get("/food/menuItems/suggest", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Menu item nutrition by ID
# ---------------------------------------------------------------------------

def get_menu_item_nutrition(menu_item_id: int) -> dict:
    """
    Get nutrition information for a restaurant menu item.

    Args:
        menu_item_id: The Spoonacular menu item ID.

    Returns:
        dict with detailed nutrition facts for the menu item.
    """
    try:
        return _get(f"/food/menuItems/{menu_item_id}/nutritionWidget.json", {})
    except Exception as exc:
        return {"error": str(exc)}
