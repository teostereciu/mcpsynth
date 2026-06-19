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
        raise RuntimeError(f"Missing environment variable {API_KEY_ENV}")
    return key


def _request(method: str, path: str, params: Dict[str, Any] | None = None, data: Dict[str, Any] | None = None):
    try:
        q = dict(params or {})
        q["apiKey"] = _api_key()
        resp = requests.request(method, f"{BASE_URL}{path}", params=q, data=data, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def search_recipes(query: str | None = None, cuisine: str | None = None, excludeCuisine: str | None = None, diet: str | None = None, intolerances: str | None = None, includeIngredients: str | None = None, excludeIngredients: str | None = None, type: str | None = None, instructionsRequired: bool | None = None, fillIngredients: bool | None = None, addRecipeInformation: bool | None = None, addRecipeInstructions: bool | None = None, addRecipeNutrition: bool | None = None, maxReadyTime: int | None = None, minServings: int | None = None, maxServings: int | None = None, ignorePantry: bool | None = None, sort: str | None = None, sortDirection: str | None = None, number: int | None = None, offset: int | None = None):
    return _request("GET", "/recipes/complexSearch", locals())


@mcp.tool()
def search_recipes_by_nutrients(**kwargs):
    return _request("GET", "/recipes/findByNutrients", kwargs)


@mcp.tool()
def search_recipes_by_ingredients(ingredients: str, number: int | None = None, ranking: int | None = None, ignorePantry: bool | None = None):
    return _request("GET", "/recipes/findByIngredients", locals())


@mcp.tool()
def get_recipe_information(id: int, includeNutrition: bool | None = None):
    return _request("GET", f"/recipes/{id}/information", locals())


@mcp.tool()
def get_similar_recipes(id: int, number: int | None = None):
    return _request("GET", f"/recipes/{id}/similar", locals())


@mcp.tool()
def autocomplete_recipe_search(query: str, number: int | None = None):
    return _request("GET", "/recipes/autocomplete", locals())


@mcp.tool()
def ingredient_search(query: str, addChildren: bool | None = None, metaInformation: bool | None = None, intolerances: str | None = None, sort: str | None = None, sortDirection: str | None = None, language: str | None = None, number: int | None = None, offset: int | None = None):
    return _request("GET", "/food/ingredients/search", locals())


@mcp.tool()
def get_ingredient_information(id: int, amount: float | None = None, unit: str | None = None, locale: str | None = None):
    return _request("GET", f"/food/ingredients/{id}/information", locals())


@mcp.tool()
def parse_ingredients(ingredientList: str, servings: int | None = None, includeNutrition: bool | None = None, language: str | None = None):
    return _request("POST", "/recipes/parseIngredients", data=locals())


@mcp.tool()
def get_meal_plan_week(username: str, start_date: str, hash: str):
    return _request("GET", f"/mealplanner/{username}/week/{start_date}", {"hash": hash})


@mcp.tool()
def get_meal_plan_day(username: str, date: str, hash: str):
    return _request("GET", f"/mealplanner/{username}/day/{date}", {"hash": hash})


@mcp.tool()
def generate_meal_plan(**kwargs):
    return _request("GET", "/mealplanner/generate", kwargs)


@mcp.tool()
def wine_pairing(food: str, maxPrice: float | None = None):
    return _request("GET", "/food/wine/pairing", locals())


@mcp.tool()
def wine_description(wine: str):
    return _request("GET", "/food/wine/description", locals())


@mcp.tool()
def dish_pairing_for_wine(wine: str):
    return _request("GET", "/food/wine/dishes", locals())


@mcp.tool()
def wine_recommendation(wine: str, maxPrice: float | None = None, minRating: float | None = None, number: int | None = None):
    return _request("GET", "/food/wine/recommendation", locals())


if __name__ == "__main__":
    mcp.run()
