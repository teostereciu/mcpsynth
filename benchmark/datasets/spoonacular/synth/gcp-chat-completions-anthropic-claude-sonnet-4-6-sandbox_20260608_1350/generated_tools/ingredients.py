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


def _get(path: str, params: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        r = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, params: dict, data: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    data = {k: v for k, v in data.items() if v is not None}
    try:
        r = requests.post(f"{BASE_URL}{path}", params=params, data=data, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
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
    language: Optional[str] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> dict:
    """Search for simple whole foods (fruits, vegetables, nuts, grains, meat, fish, dairy, etc.)."""
    return _get("/food/ingredients/search", {
        "query": query,
        "addChildren": add_children,
        "minProteinPercent": min_protein_percent,
        "maxProteinPercent": max_protein_percent,
        "minFatPercent": min_fat_percent,
        "maxFatPercent": max_fat_percent,
        "minCarbsPercent": min_carbs_percent,
        "maxCarbsPercent": max_carbs_percent,
        "metaInformation": meta_information,
        "intolerances": intolerances,
        "sort": sort,
        "sortDirection": sort_direction,
        "language": language,
        "offset": offset,
        "number": number,
    })


def get_ingredient_information(
    ingredient_id: int,
    amount: Optional[float] = None,
    unit: Optional[str] = None,
) -> dict:
    """Get all available information about an ingredient by its ID, including nutrition and aisle."""
    return _get(f"/food/ingredients/{ingredient_id}/information", {
        "amount": amount,
        "unit": unit,
    })


def compute_ingredient_amount(
    ingredient_id: int,
    nutrient: str,
    target: float,
    unit: Optional[str] = None,
) -> dict:
    """Compute how much of an ingredient you need to reach a specific nutritional goal.
    E.g. how much pineapple to get 10g of protein."""
    return _get(f"/food/ingredients/{ingredient_id}/amount", {
        "nutrient": nutrient,
        "target": target,
        "unit": unit,
    })


def convert_amounts(
    ingredient_name: str,
    source_amount: float,
    source_unit: str,
    target_unit: str,
) -> dict:
    """Convert ingredient amounts between units, e.g. '2 cups of flour to grams'."""
    return _get("/recipes/convert", {
        "ingredientName": ingredient_name,
        "sourceAmount": source_amount,
        "sourceUnit": source_unit,
        "targetUnit": target_unit,
    })


def parse_ingredients(
    ingredient_list: str,
    servings: float,
    include_nutrition: Optional[bool] = None,
    language: Optional[str] = None,
) -> list:
    """Extract and parse ingredients from plain text ingredient list.
    ingredient_list: one ingredient per line."""
    return _post("/recipes/parseIngredients", {
        "language": language,
    }, {
        "ingredientList": ingredient_list,
        "servings": servings,
        "includeNutrition": include_nutrition,
    })


def compute_glycemic_load(
    ingredients: list,
    language: Optional[str] = None,
) -> dict:
    """Compute the glycemic load of a list of ingredients.
    ingredients: list of ingredient strings (e.g. ['1 cup rice', '2 apples'])."""
    import json
    params = {"language": language} if language else {}
    params["apiKey"] = _api_key()
    try:
        r = requests.post(
            f"{BASE_URL}/food/ingredients/glycemicLoad",
            params=params,
            json={"ingredients": ingredients},
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def autocomplete_ingredient_search(
    query: str,
    number: Optional[int] = None,
    meta_information: Optional[bool] = None,
    intolerances: Optional[str] = None,
    language: Optional[str] = None,
) -> list:
    """Autocomplete a partial ingredient search query."""
    return _get("/food/ingredients/autocomplete", {
        "query": query,
        "number": number,
        "metaInformation": meta_information,
        "intolerances": intolerances,
        "language": language,
    })


def get_ingredient_substitutes(ingredient_name: str) -> dict:
    """Get ingredient substitutes for a given ingredient name."""
    return _get("/food/ingredients/substitutes", {
        "ingredientName": ingredient_name,
    })


def get_ingredient_substitutes_by_id(ingredient_id: int) -> dict:
    """Get ingredient substitutes for a given ingredient ID."""
    return _get(f"/food/ingredients/{ingredient_id}/substitutes", {})
