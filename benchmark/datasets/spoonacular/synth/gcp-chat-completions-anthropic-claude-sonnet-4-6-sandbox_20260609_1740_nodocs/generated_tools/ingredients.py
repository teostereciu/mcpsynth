"""
Spoonacular Ingredient tools — search, info, substitutes, parsing.
"""
import os
import requests

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def search_ingredients(
    query: str,
    add_children: bool = None,
    min_protein_percent: float = None,
    max_protein_percent: float = None,
    min_fat_percent: float = None,
    max_fat_percent: float = None,
    min_carbs_percent: float = None,
    max_carbs_percent: float = None,
    meta_information: bool = None,
    intolerances: str = None,
    sort: str = None,
    sort_direction: str = None,
    offset: int = None,
    number: int = 10,
) -> dict:
    """
    Search for ingredients by name with optional nutrient percentage filters,
    intolerance filters, and sorting options.
    """
    params = {
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
        "offset": offset,
        "number": number,
    }
    return _get("/food/ingredients/search", params)


def get_ingredient_information(
    ingredient_id: int,
    amount: float = None,
    unit: str = None,
) -> dict:
    """
    Get detailed information about an ingredient by its Spoonacular ID,
    including nutrition facts for a given amount and unit.
    """
    params = {"amount": amount, "unit": unit}
    return _get(f"/food/ingredients/{ingredient_id}/information", params)


def get_ingredient_substitutes(ingredient_name: str) -> dict:
    """
    Get substitutes for an ingredient by its name (e.g. 'butter').
    Returns a list of possible substitutions.
    """
    params = {"ingredientName": ingredient_name}
    return _get("/food/ingredients/substitutes", params)


def get_ingredient_substitutes_by_id(ingredient_id: int) -> dict:
    """
    Get substitutes for an ingredient by its Spoonacular ID.
    Returns a list of possible substitutions.
    """
    return _get(f"/food/ingredients/{ingredient_id}/substitutes", {})


def autocomplete_ingredient_search(
    query: str,
    number: int = 10,
    meta_information: bool = None,
    intolerances: str = None,
) -> list:
    """
    Autocomplete an ingredient search query. Returns a list of ingredient
    name suggestions matching the query prefix.
    """
    params = {
        "query": query,
        "number": number,
        "metaInformation": meta_information,
        "intolerances": intolerances,
    }
    return _get("/food/ingredients/autocomplete", params)


def parse_ingredients(
    ingredient_list: str,
    servings: float,
    include_nutrition: bool = False,
    language: str = None,
) -> list:
    """
    Parse a newline-separated list of ingredient strings (e.g. '1 cup flour')
    into structured ingredient objects with amounts, units, and nutrition.
    """
    try:
        api_key = _api_key()
        data = {
            "ingredientList": ingredient_list,
            "servings": servings,
            "includeNutrition": include_nutrition,
        }
        if language:
            data["language"] = language
        resp = requests.post(
            f"{BASE_URL}/recipes/parseIngredients",
            params={"apiKey": api_key},
            data=data,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def compute_ingredient_amount(
    ingredient_id: int,
    nutrient: str,
    target: float,
    unit: str = None,
) -> dict:
    """
    Compute how much of an ingredient is needed to reach a target amount of
    a specific nutrient (e.g. how many grams of almonds to get 10g of protein).
    """
    params = {"nutrient": nutrient, "target": target, "unit": unit}
    return _get(f"/food/ingredients/{ingredient_id}/amount", params)


def get_ingredient_nutrition_by_id(
    ingredient_id: int,
    amount: float,
    unit: str = None,
) -> dict:
    """
    Get the nutritional information for a specific amount of an ingredient
    identified by its Spoonacular ID.
    """
    params = {"amount": amount, "unit": unit}
    return _get(f"/food/ingredients/{ingredient_id}/nutritionWidget.json", params)
