"""
Spoonacular Ingredients API tools.
Endpoints covered:
  - GET /food/ingredients/search
  - GET /food/ingredients/{id}/information
  - GET /food/ingredients/{id}/amount
  - GET /recipes/convert
  - POST /recipes/parseIngredients
  - POST /food/ingredients/glycemicLoad
  - GET /food/ingredients/autocomplete
  - GET /food/ingredients/{id}/substitutes
  - GET /food/ingredients/substitutes
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
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, params: dict, data: dict) -> dict:
    params["apiKey"] = _api_key()
    try:
        resp = requests.post(f"{BASE_URL}{path}", params=params, data=data, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_ingredients(
    search_query: str,
    add_children: Optional[bool] = None,
    min_protein_percent: Optional[float] = None,
    max_protein_percent: Optional[float] = None,
    min_fat_percent: Optional[float] = None,
    max_fat_percent: Optional[float] = None,
    min_carbs_percent: Optional[float] = None,
    max_carbs_percent: Optional[float] = None,
    meta_information: Optional[bool] = None,
    intolerances: Optional[str] = None,
    sort: Optional[str] = None,
    sort_direction: Optional[str] = None,
    language: Optional[str] = None,
    offset: int = 0,
    number: int = 10,
) -> dict:
    """Search for simple whole foods (fruits, vegetables, nuts, grains, meat, fish, dairy, etc.)."""
    params: dict = {"search_query": search_query, "offset": offset, "number": number}
    if add_children is not None:
        params["addChildren"] = add_children
    if min_protein_percent is not None:
        params["minProteinPercent"] = min_protein_percent
    if max_protein_percent is not None:
        params["maxProteinPercent"] = max_protein_percent
    if min_fat_percent is not None:
        params["minFatPercent"] = min_fat_percent
    if max_fat_percent is not None:
        params["maxFatPercent"] = max_fat_percent
    if min_carbs_percent is not None:
        params["minCarbsPercent"] = min_carbs_percent
    if max_carbs_percent is not None:
        params["maxCarbsPercent"] = max_carbs_percent
    if meta_information is not None:
        params["metaInformation"] = meta_information
    if intolerances is not None:
        params["intolerances"] = intolerances
    if sort is not None:
        params["sort"] = sort
    if sort_direction is not None:
        params["sortDirection"] = sort_direction
    if language is not None:
        params["language"] = language
    return _get("/food/ingredients/search", params)


def get_ingredient_information(
    ingredient_id: int,
    amount: Optional[float] = None,
    unit: Optional[str] = None,
    locale: Optional[str] = None,
) -> dict:
    """Get all available information about an ingredient by its ID (image, aisle, nutrition, etc.)."""
    params: dict = {}
    if amount is not None:
        params["amount"] = amount
    if unit is not None:
        params["unit"] = unit
    if locale is not None:
        params["locale"] = locale
    return _get(f"/food/ingredients/{ingredient_id}/information", params)


def compute_ingredient_amount(
    ingredient_id: int,
    nutrient: str,
    target: float,
    unit: Optional[str] = None,
) -> dict:
    """Compute how much of an ingredient you need to reach a specific nutritional goal.
    E.g. how much pineapple to get 10g of protein."""
    params: dict = {"nutrient": nutrient, "target": target}
    if unit is not None:
        params["unit"] = unit
    return _get(f"/food/ingredients/{ingredient_id}/amount", params)


def convert_amounts(
    ingredient_name: str,
    source_amount: float,
    source_unit: str,
    target_unit: str,
) -> dict:
    """Convert ingredient amounts between units, e.g. '2 cups of flour to grams'."""
    params: dict = {
        "ingredientName": ingredient_name,
        "sourceAmount": source_amount,
        "sourceUnit": source_unit,
        "targetUnit": target_unit,
    }
    return _get("/recipes/convert", params)


def parse_ingredients(
    ingredient_list: str,
    servings: float,
    include_nutrition: bool = False,
    language: str = "en",
) -> dict:
    """Extract structured ingredient data from plain text ingredient list (one ingredient per line)."""
    data: dict = {
        "ingredientList": ingredient_list,
        "servings": servings,
        "includeNutrition": include_nutrition,
        "language": language,
    }
    return _post("/recipes/parseIngredients", {}, data)


def compute_glycemic_load(
    ingredient_list: str,
    language: str = "en",
) -> dict:
    """Compute the glycemic load of a list of ingredients (one per line)."""
    data: dict = {"ingredientList": ingredient_list, "language": language}
    return _post("/food/ingredients/glycemicLoad", {}, data)


def autocomplete_ingredient_search(
    search_query: str,
    number: int = 10,
    meta_information: Optional[bool] = None,
    intolerances: Optional[str] = None,
    language: Optional[str] = None,
) -> dict:
    """Autocomplete an ingredient search query. Returns ingredient name suggestions."""
    params: dict = {"query": search_query, "number": number}
    if meta_information is not None:
        params["metaInformation"] = meta_information
    if intolerances is not None:
        params["intolerances"] = intolerances
    if language is not None:
        params["language"] = language
    return _get("/food/ingredients/autocomplete", params)


def get_ingredient_substitutes(ingredient_name: str) -> dict:
    """Get ingredient substitutes for a given ingredient name (e.g. 'butter')."""
    params: dict = {"ingredientName": ingredient_name}
    return _get("/food/ingredients/substitutes", params)


def get_ingredient_substitutes_by_id(ingredient_id: int) -> dict:
    """Get ingredient substitutes for a given ingredient by its ID."""
    return _get(f"/food/ingredients/{ingredient_id}/substitutes", {})
