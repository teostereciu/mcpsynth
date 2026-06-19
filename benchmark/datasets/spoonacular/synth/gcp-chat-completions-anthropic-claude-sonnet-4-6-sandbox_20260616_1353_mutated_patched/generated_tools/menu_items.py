"""
Spoonacular Menu Items API tools.
Source: docs/api_menu_items.md
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict | list:
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(BASE_URL + path, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


def register_menu_items(mcp: FastMCP):

    @mcp.tool()
    def search_menu_items(
        search_query: str,
        min_calories: float = None,
        max_calories: float = None,
        min_carbs: float = None,
        max_carbs: float = None,
        min_protein: float = None,
        max_protein: float = None,
        min_fat: float = None,
        max_fat: float = None,
        add_menu_item_information: bool = False,
        offset: int = 0,
        number: int = 10,
    ) -> dict:
        """Search over 115,000 menu items from 800+ fast food and chain restaurants
        (e.g. McDonald's Big Mac, Starbucks Mocha). Filter by nutritional content."""
        params = {
            "query": search_query,
            "addMenuItemInformation": add_menu_item_information,
            "offset": offset,
            "number": number,
        }
        if min_calories is not None:
            params["minCalories"] = min_calories
        if max_calories is not None:
            params["maxCalories"] = max_calories
        if min_carbs is not None:
            params["minCarbs"] = min_carbs
        if max_carbs is not None:
            params["maxCarbs"] = max_carbs
        if min_protein is not None:
            params["minProtein"] = min_protein
        if max_protein is not None:
            params["maxProtein"] = max_protein
        if min_fat is not None:
            params["minFat"] = min_fat
        if max_fat is not None:
            params["maxFat"] = max_fat
        return _get("/food/menuItems/search", params)

    @mcp.tool()
    def get_menu_item_information(menu_item_id: int) -> dict:
        """Get all available information about a menu item by its ID, including nutrition data."""
        return _get(f"/food/menuItems/{menu_item_id}", {})

    @mcp.tool()
    def autocomplete_menu_item_search(
        search_query: str,
        number: int = 10,
    ) -> dict:
        """Generate autocomplete suggestions for menu items based on a partial search query."""
        params = {"query": search_query, "number": number}
        return _get("/food/menuItems/suggest", params)
