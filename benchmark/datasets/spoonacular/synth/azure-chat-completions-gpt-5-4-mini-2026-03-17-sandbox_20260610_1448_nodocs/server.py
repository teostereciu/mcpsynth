import os
import requests
from typing import Any, Dict
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.spoonacular.com"
API_KEY = os.getenv("SPOONACULAR_API_KEY", "")

mcp = FastMCP("spoonacular-food-api")


def _request(method: str, path: str, params: Dict[str, Any] | None = None, json_body: Any = None):
    try:
        if not API_KEY:
            return {"error": "SPOONACULAR_API_KEY is not set"}
        p = dict(params or {})
        p["apiKey"] = API_KEY
        resp = requests.request(method, f"{BASE_URL}{path}", params=p, json=json_body, timeout=30)
        resp.raise_for_status()
        if "application/json" in resp.headers.get("content-type", ""):
            return resp.json()
        return resp.text
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def search_recipes(query: str, number: int = 10, cuisine: str | None = None, diet: str | None = None):
    params = {"query": query, "number": number}
    if cuisine: params["cuisine"] = cuisine
    if diet: params["diet"] = diet
    return _request("GET", "/recipes/complexSearch", params)


@mcp.tool()
def search_recipes_by_ingredients(ingredients: str, number: int = 10):
    return _request("GET", "/recipes/findByIngredients", {"ingredients": ingredients, "number": number})


@mcp.tool()
def search_recipes_by_nutrients(minProtein: float | None = None, maxCalories: float | None = None):
    params = {}
    if minProtein is not None: params["minProtein"] = minProtein
    if maxCalories is not None: params["maxCalories"] = maxCalories
    return _request("GET", "/recipes/findByNutrients", params)


@mcp.tool()
def get_recipe_information(recipe_id: int):
    return _request("GET", f"/recipes/{recipe_id}/information")


@mcp.tool()
def get_recipe_ingredients(recipe_id: int):
    return _request("GET", f"/recipes/{recipe_id}/ingredientWidget.json")


@mcp.tool()
def get_recipe_nutrition(recipe_id: int):
    return _request("GET", f"/recipes/{recipe_id}/nutritionWidget.json")


@mcp.tool()
def get_recipe_instructions(recipe_id: int):
    return _request("GET", f"/recipes/{recipe_id}/analyzedInstructions")


@mcp.tool()
def get_similar_recipes(recipe_id: int, number: int = 5):
    return _request("GET", f"/recipes/{recipe_id}/similar", {"number": number})


@mcp.tool()
def search_ingredients(query: str, number: int = 10):
    return _request("GET", "/food/ingredients/search", {"query": query, "number": number})


@mcp.tool()
def get_ingredient_information(ingredient_id: int, amount: float = 1, unit: str = "g"):
    return _request("GET", f"/food/ingredients/{ingredient_id}/information", {"amount": amount, "unit": unit})


@mcp.tool()
def parse_ingredients(ingredient_list: list[str]):
    return _request("POST", "/recipes/parseIngredients", {"ingredientList": ingredient_list})


@mcp.tool()
def generate_meal_plan(target_calories: int = 2000, time_frame: str = "day"):
    return _request("GET", "/mealplanner/generate", {"targetCalories": target_calories, "timeFrame": time_frame})


@mcp.tool()
def get_meal_plan(username: str, date: str):
    return _request("GET", f"/mealplanner/{username}/day/{date}")


@mcp.tool()
def get_nutrition_by_id(recipe_id: int):
    return _request("GET", f"/recipes/{recipe_id}/nutritionWidget.json")


@mcp.tool()
def visualize_nutrition(recipe_id: int):
    return _request("GET", f"/recipes/{recipe_id}/nutritionWidget.json")


@mcp.tool()
def get_wine_pairing(food: str):
    return _request("GET", "/food/wine/pairing", {"food": food})


@mcp.tool()
def get_wine_description(wine: str):
    return _request("GET", f"/food/wine/{wine}/description")


@mcp.tool()
def autocomplete(query: str, number: int = 10):
    return _request("GET", "/food/ingredients/autocomplete", {"query": query, "number": number})


if __name__ == "__main__":
    mcp.run(transport="stdio")
