import json
import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.spoonacular.com"
API_KEY_ENV = "SPOONACULAR_API_KEY"

mcp = FastMCP("spoonacular-food-api")


def _api_get(path: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    try:
        api_key = os.getenv(API_KEY_ENV)
        if not api_key:
            return {"error": f"Missing environment variable {API_KEY_ENV}"}
        query = dict(params or {})
        query["apiKey"] = api_key
        resp = requests.get(f"{BASE_URL}{path}", params=query, timeout=30)
        data = resp.json()
        if not resp.ok:
            return {"error": data.get("message", f"HTTP {resp.status_code}")}
        return data
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": ["search_recipes", "get_recipe_information", "search_ingredients", "generate_meal_plan", "get_wine_pairing", "autocomplete_search"]}


@mcp.tool()
def search_recipes(query: str, number: int = 10) -> Dict[str, Any]:
    return _api_get("/recipes/complexSearch", {"query": query, "number": number})


@mcp.tool()
def get_recipe_information(recipe_id: int, include_nutrition: bool = False) -> Dict[str, Any]:
    return _api_get(f"/recipes/{recipe_id}/information", {"includeNutrition": include_nutrition})


@mcp.tool()
def search_ingredients(query: str, number: int = 10) -> Dict[str, Any]:
    return _api_get("/food/ingredients/search", {"query": query, "number": number})


@mcp.tool()
def generate_meal_plan(target_calories: int = 2000, time_frame: str = "day") -> Dict[str, Any]:
    return _api_get("/mealplanner/generate", {"targetCalories": target_calories, "timeFrame": time_frame})


@mcp.tool()
def get_wine_pairing(food: str) -> Dict[str, Any]:
    return _api_get("/food/wine/pairing", {"food": food})


@mcp.tool()
def autocomplete_search(query: str, number: int = 10) -> Dict[str, Any]:
    return _api_get("/food/ingredients/autocomplete", {"query": query, "number": number})


if __name__ == "__main__":
    mcp.run(transport="stdio")
