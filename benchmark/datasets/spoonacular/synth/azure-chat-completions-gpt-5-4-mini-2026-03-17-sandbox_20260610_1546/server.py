import json
import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.spoonacular.com"
API_KEY_ENV = "SPOONACULAR_API_KEY"

mcp = FastMCP("spoonacular-food-api")


def _api_key() -> str:
    key = os.getenv(API_KEY_ENV)
    if not key:
        raise ValueError(f"Missing environment variable {API_KEY_ENV}")
    return key


def _request(method: str, path: str, params: Dict[str, Any] | None = None, data: Dict[str, Any] | None = None) -> Any:
    try:
        query = dict(params or {})
        query["apiKey"] = _api_key()
        resp = requests.request(method, f"{BASE_URL}{path}", params=query, data=data, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def search_recipes(query: str, number: int = 10, offset: int = 0, **kwargs: Any) -> Any:
    return _request("GET", "/recipes/complexSearch", {"query": query, "number": number, "offset": offset, **kwargs})


@mcp.tool()
def search_recipes_by_nutrients(**kwargs: Any) -> Any:
    return _request("GET", "/recipes/findByNutrients", kwargs)


@mcp.tool()
def search_recipes_by_ingredients(ingredients: str, number: int = 10, ranking: int = 1, ignorePantry: bool = True) -> Any:
    return _request("GET", "/recipes/findByIngredients", {"ingredients": ingredients, "number": number, "ranking": ranking, "ignorePantry": ignorePantry})


@mcp.tool()
def get_recipe_information(id: int, includeNutrition: bool = False) -> Any:
    return _request("GET", f"/recipes/{id}/information", {"includeNutrition": includeNutrition})


@mcp.tool()
def get_similar_recipes(id: int, number: int = 5) -> Any:
    return _request("GET", f"/recipes/{id}/similar", {"number": number})


@mcp.tool()
def autocomplete_recipe_search(query: str, number: int = 10) -> Any:
    return _request("GET", "/recipes/autocomplete", {"query": query, "number": number})


@mcp.tool()
def get_analyzed_recipe_instructions(id: int) -> Any:
    return _request("GET", f"/recipes/{id}/analyzedInstructions")


@mcp.tool()
def search_ingredients(query: str, number: int = 10, offset: int = 0, **kwargs: Any) -> Any:
    return _request("GET", "/food/ingredients/search", {"query": query, "number": number, "offset": offset, **kwargs})


@mcp.tool()
def get_ingredient_information(id: int, amount: float | None = None, unit: str | None = None, locale: str | None = None) -> Any:
    params: Dict[str, Any] = {}
    if amount is not None:
        params["amount"] = amount
    if unit is not None:
        params["unit"] = unit
    if locale is not None:
        params["locale"] = locale
    return _request("GET", f"/food/ingredients/{id}/information", params)


@mcp.tool()
def parse_ingredients(ingredientList: str, servings: int = 1, includeNutrition: bool = False, language: str = "en") -> Any:
    return _request("POST", "/recipes/parseIngredients", {"ingredientList": ingredientList, "servings": servings, "includeNutrition": includeNutrition, "language": language})


@mcp.tool()
def autocomplete_ingredient_search(query: str, number: int = 10) -> Any:
    return _request("GET", "/food/ingredients/autocomplete", {"query": query, "number": number})


@mcp.tool()
def generate_meal_plan(timeFrame: str = "day", **kwargs: Any) -> Any:
    return _request("GET", "/mealplanner/generate", {"timeFrame": timeFrame, **kwargs})


@mcp.tool()
def get_meal_plan_day(username: str, date: str, hash: str) -> Any:
    return _request("GET", f"/mealplanner/{username}/day/{date}", {"hash": hash})


@mcp.tool()
def get_meal_plan_week(username: str, start_date: str, hash: str) -> Any:
    return _request("GET", f"/mealplanner/{username}/week/{start_date}", {"hash": hash})


@mcp.tool()
def get_nutrition_by_id(id: int) -> Any:
    return _request("GET", f"/recipes/{id}/nutritionWidget.json")


@mcp.tool()
def visualize_nutrition(id: int) -> Any:
    return _request("GET", f"/recipes/{id}/nutritionLabel")


@mcp.tool()
def wine_pairing(food: str, maxPrice: float | None = None) -> Any:
    params: Dict[str, Any] = {"food": food}
    if maxPrice is not None:
        params["maxPrice"] = maxPrice
    return _request("GET", "/food/wine/pairing", params)


@mcp.tool()
def wine_description(wine: str) -> Any:
    return _request("GET", "/food/wine/description", {"wine": wine})


@mcp.tool()
def dish_pairing_for_wine(wine: str) -> Any:
    return _request("GET", "/food/wine/dishes", {"wine": wine})


@mcp.tool()
def search_menu_items(query: str, number: int = 10, offset: int = 0, **kwargs: Any) -> Any:
    return _request("GET", "/food/menuItems/search", {"query": query, "number": number, "offset": offset, **kwargs})


@mcp.tool()
def get_menu_item_information(id: int) -> Any:
    return _request("GET", f"/food/menuItems/{id}")


@mcp.tool()
def autocomplete_menu_item_search(query: str, number: int = 10) -> Any:
    return _request("GET", "/food/menuItems/suggest", {"query": query, "number": number})


@mcp.tool()
def search_all_food(query: str, number: int = 10, offset: int = 0) -> Any:
    return _request("GET", "/food/search", {"query": query, "number": number, "offset": offset})


@mcp.tool()
def search_food_videos(query: str, number: int = 10, offset: int = 0, **kwargs: Any) -> Any:
    return _request("GET", "/food/videos/search", {"query": query, "number": number, "offset": offset, **kwargs})


@mcp.tool()
def quick_answer(q: str) -> Any:
    return _request("GET", "/recipes/quickAnswer", {"q": q})


@mcp.tool()
def detect_food_in_text(text: str) -> Any:
    return _request("POST", "/food/detect", {"text": text})


@mcp.tool()
def list_tools() -> Any:
    return [
        "search_recipes", "search_recipes_by_nutrients", "search_recipes_by_ingredients", "get_recipe_information",
        "get_similar_recipes", "autocomplete_recipe_search", "get_analyzed_recipe_instructions",
        "search_ingredients", "get_ingredient_information", "parse_ingredients", "autocomplete_ingredient_search",
        "generate_meal_plan", "get_meal_plan_day", "get_meal_plan_week", "get_nutrition_by_id", "visualize_nutrition",
        "wine_pairing", "wine_description", "dish_pairing_for_wine", "search_menu_items", "get_menu_item_information",
        "autocomplete_menu_item_search", "search_all_food", "search_food_videos", "quick_answer", "detect_food_in_text",
    ]


if __name__ == "__main__":
    mcp.run(transport="stdio")
