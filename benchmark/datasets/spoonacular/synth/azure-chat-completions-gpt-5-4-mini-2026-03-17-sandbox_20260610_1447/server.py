import os
import requests
from typing import Any, Dict
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.spoonacular.com"
API_KEY = os.getenv("SPOONACULAR_API_KEY")

mcp = FastMCP("spoonacular")


def _request(method: str, path: str, params: Dict[str, Any] | None = None, data: Dict[str, Any] | None = None):
    if not API_KEY:
        return {"error": "SPOONACULAR_API_KEY is not set"}
    try:
        p = {"apiKey": API_KEY}
        if params:
            p.update({k: v for k, v in params.items() if v is not None})
        resp = requests.request(method, f"{BASE_URL}{path}", params=p, data=data, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def search_recipes(query: str | None = None, **kwargs):
    return _request("GET", "/recipes/complexSearch", {"query": query, **kwargs})


@mcp.tool()
def search_recipes_by_nutrients(**kwargs):
    return _request("GET", "/recipes/findByNutrients", kwargs)


@mcp.tool()
def search_recipes_by_nutrients(**kwargs):
    return _request("GET", "/recipes/findByNutrients", kwargs)


@mcp.tool()
def search_recipes_by_ingredients(**kwargs):
    return _request("GET", "/recipes/findByIngredients", kwargs)


@mcp.tool()
def get_recipe_information(id: int, **kwargs):
    return _request("GET", f"/recipes/{id}/information", kwargs)


@mcp.tool()
def get_recipe_information(id: int, **kwargs):
    return _request("GET", f"/recipes/{id}/information", kwargs)


@mcp.tool()
def get_recipe_information_bulk(ids: str):
    return _request("GET", "/recipes/informationBulk", {"ids": ids})


@mcp.tool()
def get_similar_recipes(id: int, **kwargs):
    return _request("GET", f"/recipes/{id}/similar", kwargs)


@mcp.tool()
def get_random_recipes(**kwargs):
    return _request("GET", "/recipes/random", kwargs)


@mcp.tool()
def autocomplete_recipe_search(query: str, **kwargs):
    return _request("GET", "/recipes/autocomplete", {"query": query, **kwargs})


@mcp.tool()
def ingredient_search(query: str, **kwargs):
    return _request("GET", "/food/ingredients/search", {"query": query, **kwargs})


@mcp.tool()
def get_ingredient_information(id: int, **kwargs):
    return _request("GET", f"/food/ingredients/{id}/information", kwargs)


@mcp.tool()
def parse_ingredients(ingredientList: str, **kwargs):
    return _request("POST", "/recipes/parseIngredients", kwargs, {"ingredientList": ingredientList})


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
def get_wine_pairing(food: str, **kwargs):
    return _request("GET", "/food/wine/pairing", {"food": food, **kwargs})


@mcp.tool()
def get_wine_description(wine: str):
    return _request("GET", "/food/wine/description", {"wine": wine})


@mcp.tool()
def search_all_food(query: str, **kwargs):
    return _request("GET", "/food/search", {"query": query, **kwargs})


@mcp.tool()
def search_food_videos(query: str, **kwargs):
    return _request("GET", "/food/videos/search", {"query": query, **kwargs})


@mcp.tool()
def quick_answer(q: str):
    return _request("GET", "/recipes/quickAnswer", {"q": q})


@mcp.tool()
def detect_food_in_text(text: str):
    return _request("POST", "/food/detect", data={"text": text})


@mcp.tool()
def search_site_content(query: str):
    return _request("GET", "/food/site/search", {"query": query})


if __name__ == "__main__":
    mcp.run()
