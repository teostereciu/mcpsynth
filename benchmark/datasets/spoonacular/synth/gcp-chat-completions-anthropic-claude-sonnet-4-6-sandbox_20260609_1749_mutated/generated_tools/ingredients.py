"""Spoonacular Ingredients API tools."""
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
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, data: dict, params: dict = None) -> dict:
    p = params or {}
    p["apiKey"] = _api_key()
    try:
        resp = requests.post(f"{BASE_URL}{path}", data=data, params=p, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_ingredients(
    query: str,
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
    language: str = "en",
    offset: int = 0,
    number: int = 10,
) -> dict:
    """Search for simple whole foods (fruits, vegetables, nuts, grains, meat, fish, dairy, etc.)."""
    params: dict = {"query": query, "language": language, "offset": offset, "number": number}
    if add_children is not None: params["addChildren"] = add_children
    if min_protein_percent is not None: params["minProteinPercent"] = min_protein_percent
    if max_protein_percent is not None: params["maxProteinPercent"] = max_protein_percent
    if min_fat_percent is not None: params["minFatPercent"] = min_fat_percent
    if max_fat_percent is not None: params["maxFatPercent"] = max_fat_percent
    if min_carbs_percent is not None: params["minCarbsPercent"] = min_carbs_percent
    if max_carbs_percent is not None: params["maxCarbsPercent"] = max_carbs_percent
    if meta_information is not None: params["metaInformation"] = meta_information
    if intolerances: params["intolerances"] = intolerances
    if sort: params["sort"] = sort
    if sort_direction: params["sortDirection"] = sort_direction
    return _get("/food/ingredients/search", params)


def get_ingredient_information(
    ingredient_id: int,
    amount: Optional[float] = None,
    unit: Optional[str] = None,
) -> dict:
    """Get all available information about an ingredient by its ID."""
    params: dict = {}
    if amount is not None: params["amount"] = amount
    if unit: params["unit"] = unit
    return _get(f"/food/ingredients/{ingredient_id}/information", params)


def compute_ingredient_amount(
    ingredient_id: int,
    nutrient: str,
    target: float,
    unit: Optional[str] = None,
) -> dict:
    """Compute how much of an ingredient you need to reach a nutritional goal."""
    params: dict = {"nutrient": nutrient, "target": target}
    if unit: params["unit"] = unit
    return _get(f"/food/ingredients/{ingredient_id}/amount", params)


def convert_amounts(
    ingredient_name: str,
    source_amount: float,
    source_unit: str,
    target_unit: str,
) -> dict:
    """Convert ingredient amounts between units (e.g. '2 cups of flour to grams')."""
    params = {
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
) -> list:
    """Extract/parse ingredients from plain text (one ingredient per line)."""
    data = {
        "ingredientList": ingredient_list,
        "servings": servings,
        "includeNutrition": include_nutrition,
        "language": language,
    }
    return _post("/recipes/parseIngredients", data)


def compute_glycemic_load(ingredient_list: list, language: str = "en") -> dict:
    """Compute the glycemic load of a list of ingredients."""
    import json
    params = {"language": language}
    params["apiKey"] = _api_key()
    try:
        resp = requests.post(
            f"{BASE_URL}/food/ingredients/glycemicLoad",
            json={"ingredients": ingredient_list},
            params=params,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def autocomplete_ingredient_search(
    query: str,
    number: int = 10,
    meta_information: bool = False,
    intolerances: Optional[str] = None,
    language: str = "en",
) -> list:
    """Autocomplete an ingredient search query."""
    params: dict = {"query": query, "number": number, "metaInformation": meta_information, "language": language}
    if intolerances: params["intolerances"] = intolerances
    return _get("/food/ingredients/autocomplete", params)


def get_ingredient_substitutes(ingredient_name: str) -> dict:
    """Get substitutes for an ingredient by name."""
    params = {"ingredientName": ingredient_name}
    return _get("/food/ingredients/substitutes", params)


def get_ingredient_substitutes_by_id(ingredient_id: int) -> dict:
    """Get substitutes for an ingredient by its ID."""
    return _get(f"/food/ingredients/{ingredient_id}/substitutes", {})
