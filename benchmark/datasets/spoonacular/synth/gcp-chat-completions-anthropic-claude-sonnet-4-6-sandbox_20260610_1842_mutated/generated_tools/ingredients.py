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
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, data: dict, params: dict | None = None) -> dict:
    if params is None:
        params = {}
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    data = {k: v for k, v in data.items() if v is not None}
    try:
        resp = requests.post(
            f"{BASE_URL}{path}",
            data=data,
            params=params,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ---------------------------------------------------------------------------
# Ingredient Search
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Get Ingredient Information
# ---------------------------------------------------------------------------

def get_ingredient_information(
    ingredient_id: int,
    amount: Optional[float] = None,
    unit: Optional[str] = None,
    locale: Optional[str] = None,
) -> dict:
    """Get all available information about an ingredient by its ID (image, aisle, nutrition, etc.)."""
    return _get(f"/food/ingredients/{ingredient_id}/information", {
        "amount": amount,
        "unit": unit,
        "locale": locale,
    })


# ---------------------------------------------------------------------------
# Compute Ingredient Amount
# ---------------------------------------------------------------------------

def compute_ingredient_amount(
    ingredient_id: int,
    nutrient: str,
    target: float,
    unit: Optional[str] = None,
) -> dict:
    """Compute how much of an ingredient you need to reach a specific nutritional goal."""
    return _get(f"/food/ingredients/{ingredient_id}/amount", {
        "nutrient": nutrient,
        "target": target,
        "unit": unit,
    })


# ---------------------------------------------------------------------------
# Convert Amounts
# ---------------------------------------------------------------------------

def convert_amounts(
    ingredient_name: str,
    source_amount: float,
    source_unit: str,
    target_unit: str,
) -> dict:
    """Convert ingredient amounts between units (e.g. '2 cups of flour to grams')."""
    return _get("/recipes/convert", {
        "ingredientName": ingredient_name,
        "sourceAmount": source_amount,
        "sourceUnit": source_unit,
        "targetUnit": target_unit,
    })


# ---------------------------------------------------------------------------
# Parse Ingredients
# ---------------------------------------------------------------------------

def parse_ingredients(
    ingredient_list: str,
    servings: int,
    include_nutrition: Optional[bool] = None,
    language: Optional[str] = None,
) -> dict:
    """Extract structured ingredient data from plain text ingredient lines."""
    return _post("/recipes/parseIngredients", {
        "ingredientList": ingredient_list,
        "servings": servings,
        "includeNutrition": include_nutrition,
        "language": language,
    })


# ---------------------------------------------------------------------------
# Compute Glycemic Load
# ---------------------------------------------------------------------------

def compute_glycemic_load(
    ingredient_list: str,
    servings: Optional[int] = None,
    language: Optional[str] = None,
) -> dict:
    """Compute the glycemic load of a list of ingredients."""
    return _post("/food/ingredients/glycemicLoad", {
        "ingredientList": ingredient_list,
        "servings": servings,
        "language": language,
    })


# ---------------------------------------------------------------------------
# Autocomplete Ingredient Search
# ---------------------------------------------------------------------------

def autocomplete_ingredient_search(
    query: str,
    number: Optional[int] = None,
    meta_information: Optional[bool] = None,
    intolerances: Optional[str] = None,
    language: Optional[str] = None,
) -> dict:
    """Autocomplete an ingredient search query."""
    return _get("/food/ingredients/autocomplete", {
        "query": query,
        "number": number,
        "metaInformation": meta_information,
        "intolerances": intolerances,
        "language": language,
    })


# ---------------------------------------------------------------------------
# Get Ingredient Substitutes by ID
# ---------------------------------------------------------------------------

def get_ingredient_substitutes_by_id(ingredient_id: int) -> dict:
    """Get ingredient substitutes for a given ingredient by its ID."""
    return _get(f"/food/ingredients/{ingredient_id}/substitutes", {})


# ---------------------------------------------------------------------------
# Get Ingredient Substitutes (by name)
# ---------------------------------------------------------------------------

def get_ingredient_substitutes(ingredient_name: str) -> dict:
    """Get ingredient substitutes for a given ingredient by its name."""
    return _get("/food/ingredients/substitutes", {
        "ingredientName": ingredient_name,
    })
