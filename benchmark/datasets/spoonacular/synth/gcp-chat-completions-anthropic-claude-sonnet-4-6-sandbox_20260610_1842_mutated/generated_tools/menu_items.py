"""
Spoonacular Menu Items API tools.
Endpoints covered:
  - GET /food/menuItems/search
  - GET /food/menuItems/{id}
  - GET /food/menuItems/suggest
"""

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
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ---------------------------------------------------------------------------
# Search Menu Items
# ---------------------------------------------------------------------------

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
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> dict:
    """Search over 115,000 menu items from fast food and chain restaurants."""
    return _get("/food/menuItems/search", {
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
    })


# ---------------------------------------------------------------------------
# Get Menu Item Information
# ---------------------------------------------------------------------------

def get_menu_item_information(menu_item_id: int) -> dict:
    """Get all available information about a menu item by its ID (nutrition, restaurant, etc.)."""
    return _get(f"/food/menuItems/{menu_item_id}", {})


# ---------------------------------------------------------------------------
# Autocomplete Menu Item Search
# ---------------------------------------------------------------------------

def autocomplete_menu_item_search(
    query: str,
    number: Optional[int] = None,
) -> dict:
    """Generate autocomplete suggestions for menu items based on a partial query."""
    return _get("/food/menuItems/suggest", {
        "query": query,
        "number": number,
    })
