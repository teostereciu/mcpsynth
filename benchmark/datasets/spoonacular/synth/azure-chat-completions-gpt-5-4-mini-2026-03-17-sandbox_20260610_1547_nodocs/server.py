import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.spoonacular.com"
API_KEY = os.getenv("SPOONACULAR_API_KEY")

mcp = FastMCP("spoonacular")


def _request(method: str, path: str, *, params: Dict[str, Any] | None = None, json_body: Dict[str, Any] | None = None):
    if not API_KEY:
        return {"error": "SPOONACULAR_API_KEY is not set"}
    try:
        query = dict(params or {})
        query["apiKey"] = API_KEY
        resp = requests.request(method, f"{BASE_URL}{path}", params=query, json=json_body, timeout=30)
        resp.raise_for_status()
        if resp.headers.get("content-type", "").startswith("application/json"):
            return resp.json()
        return {"content": resp.text}
    except requests.HTTPError:
        try:
            return resp.json()
        except Exception:
            return {"error": f"HTTP {resp.status_code}"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def search_recipes(query: str, number: int = 10, offset: int = 0, cuisine: str | None = None, diet: str | None = None, intolerances: str | None = None):
    params = {"query": query, "number": number, "offset": offset}
    if cuisine is not None:
        params["cuisine"] = cuisine
    if diet is not None:
        params["diet"] = diet
    if intolerances is not None:
        params["intolerances"] = intolerances
    return _request("GET", "/recipes/complexSearch", params=params)


@mcp.tool()
def search_recipes_by_ingredients(ingredients: str, number: int = 10, ranking: int = 1):
    return _request("GET", "/recipes/findByIngredients", params={"ingredients": ingredients, "number": number, "ranking": ranking})


@mcp.tool()
def search_recipes_by_nutrients(minCalories: int | None = None, maxCalories: int | None = None, minProtein: int | None = None, maxProtein: int | None = None):
    params = {}
    for k, v in {"minCalories": minCalories, "maxCalories": maxCalories, "minProtein": minProtein, "maxProtein": maxProtein}.items():
        if v is not None:
            params[k] = v
    return _request("GET", "/recipes/findByNutrients", params=params)


@mcp.tool()
def get_recipe_information(recipe_id: int, includeNutrition: bool = False):
    return _request("GET", f"/recipes/{recipe_id}/information", params={"includeNutrition": str(includeNutrition).lower()})


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
    return _request("GET", f"/recipes/{recipe_id}/similar", params={"number": number})


@mcp.tool()
def search_ingredients(query: str, number: int = 10):
    return _request("GET", "/food/ingredients/search", params={"query": query, "number": number})


@mcp.tool()
def get_ingredient_information(ingredient_id: int, amount: float = 1, unit: str = "gram"):
    return _request("GET", f"/food/ingredients/{ingredient_id}/information", params={"amount": amount, "unit": unit})


@mcp.tool()
def parse_ingredients(ingredients: list[str]):
    return _request("POST", "/recipes/parseIngredients", params={}, json_body={"ingredientList": ingredients})


@mcp.tool()
def generate_meal_plan(timeFrame: str = "day", targetCalories: int | None = None, diet: str | None = None):
    params = {"timeFrame": timeFrame}
    if targetCalories is not None:
        params["targetCalories"] = targetCalories
    if diet is not None:
        params["diet"] = diet
    return _request("GET", "/mealplanner/generate", params=params)


@mcp.tool()
def get_meal_plan(meal_plan_id: int):
    return _request("GET", f"/mealplanner/{meal_plan_id}")


@mcp.tool()
def get_nutrition_by_id(recipe_id: int):
    return _request("GET", f"/recipes/{recipe_id}/nutritionWidget.json")


@mcp.tool()
def visualize_nutrition(recipe_id: int):
    return _request("GET", f"/recipes/{recipe_id}/nutritionWidget.json")


@mcp.tool()
def get_wine_pairing(food: str):
    return _request("GET", "/food/wine/pairing", params={"food": food})


@mcp.tool()
def get_wine_description(wine: str):
    return _request("GET", "/food/wine/description", params={"wine": wine})


@mcp.tool()
def autocomplete(query: str, number: int = 10):
    return _request("GET", "/food/ingredients/autocomplete", params={"query": query, "number": number})


if __name__ == "__main__":
    mcp.run(transport="stdio")
