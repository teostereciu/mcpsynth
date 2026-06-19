import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.spoonacular.com"


def _request(method: str, path: str, params: Optional[Dict[str, Any]] = None, json_body: Any = None, data: Any = None, headers: Optional[Dict[str, str]] = None) -> Any:
    api_key = os.getenv("SPOONACULAR_API_KEY")
    if not api_key:
        return {"error": "Missing SPOONACULAR_API_KEY environment variable"}

    query = {k: v for k, v in (params or {}).items() if v is not None}
    query["apiKey"] = api_key

    try:
        response = requests.request(method, f"{BASE_URL}{path}", params=query, json=json_body, data=data, headers=headers, timeout=60)
        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            return response.json()
        return {"content": response.text, "content_type": content_type}
    except requests.RequestException as exc:
        detail = None
        response = getattr(exc, "response", None)
        if response is not None:
            try:
                detail = response.json()
            except Exception:
                detail = response.text
        return {"error": str(exc), "details": detail}


def search_recipes(
    query: Optional[str] = None,
    cuisine: Optional[str] = None,
    excludeCuisine: Optional[str] = None,
    diet: Optional[str] = None,
    intolerances: Optional[str] = None,
    equipment: Optional[str] = None,
    includeIngredients: Optional[str] = None,
    excludeIngredients: Optional[str] = None,
    type: Optional[str] = None,
    instructionsRequired: Optional[bool] = None,
    fillIngredients: Optional[bool] = None,
    addRecipeInformation: Optional[bool] = None,
    addRecipeInstructions: Optional[bool] = None,
    addRecipeNutrition: Optional[bool] = None,
    author: Optional[str] = None,
    tags: Optional[str] = None,
    recipeBoxId: Optional[int] = None,
    titleMatch: Optional[str] = None,
    maxReadyTime: Optional[int] = None,
    minServings: Optional[int] = None,
    maxServings: Optional[int] = None,
    ignorePantry: Optional[bool] = None,
    sort: Optional[str] = None,
    sortDirection: Optional[str] = None,
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Any:
    return _request("GET", "/recipes/complexSearch", locals())


def search_recipes_by_nutrients(
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    number: Optional[int] = None,
    random: Optional[bool] = None,
    limitLicense: Optional[bool] = None,
) -> Any:
    return _request("GET", "/recipes/findByNutrients", locals())


def search_recipes_by_ingredients(
    ingredients: str,
    number: Optional[int] = None,
    limitLicense: Optional[bool] = None,
    ranking: Optional[int] = None,
    ignorePantry: Optional[bool] = None,
) -> Any:
    return _request("GET", "/recipes/findByIngredients", locals())


def get_recipe_information(id: int, includeNutrition: Optional[bool] = None) -> Any:
    return _request("GET", f"/recipes/{id}/information", {"includeNutrition": includeNutrition})


def get_similar_recipes(id: int, number: Optional[int] = None) -> Any:
    return _request("GET", f"/recipes/{id}/similar", {"number": number})


def get_random_recipes(number: Optional[int] = None, tags: Optional[str] = None) -> Any:
    params = {"number": number, "include-tags": tags}
    return _request("GET", "/recipes/random", params)


def autocomplete_recipe_search(query: str, number: Optional[int] = None) -> Any:
    return _request("GET", "/recipes/autocomplete", locals())


def get_recipe_taste(id: int, normalize: Optional[bool] = None) -> Any:
    return _request("GET", f"/recipes/{id}/tasteWidget.json", {"normalize": normalize})


def get_recipe_equipment(id: int) -> Any:
    return _request("GET", f"/recipes/{id}/equipmentWidget.json")


def get_recipe_price_breakdown(id: int) -> Any:
    return _request("GET", f"/recipes/{id}/priceBreakdownWidget.json")


def get_recipe_ingredients(id: int) -> Any:
    return _request("GET", f"/recipes/{id}/ingredientWidget.json")


def get_recipe_nutrition(id: int) -> Any:
    return _request("GET", f"/recipes/{id}/nutritionWidget.json")


def get_analyzed_recipe_instructions(id: int, stepBreakdown: Optional[bool] = None) -> Any:
    return _request("GET", f"/recipes/{id}/analyzedInstructions", {"stepBreakdown": stepBreakdown})


def extract_recipe_from_website(url: str, forceExtraction: Optional[bool] = None, analyze: Optional[bool] = None) -> Any:
    return _request("GET", "/recipes/extract", locals())


def summarize_recipe(id: int) -> Any:
    return _request("GET", f"/recipes/{id}/summary")


def analyze_recipe_search_query(q: str) -> Any:
    return _request("GET", "/recipes/queries/analyze", {"q": q})
