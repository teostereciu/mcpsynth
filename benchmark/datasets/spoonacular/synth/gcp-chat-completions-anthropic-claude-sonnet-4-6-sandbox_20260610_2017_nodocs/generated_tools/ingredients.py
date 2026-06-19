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
    params["apiKey"] = _api_key()
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def _post(path: str, data: dict) -> dict | list:
    params = {"apiKey": _api_key()}
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.post(url, params=params, data=data, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Ingredient Search & Info
# ---------------------------------------------------------------------------

def search_ingredients(
    query: str,
    number: int = 10,
    offset: int = 0,
    sort: str = "",
    sort_direction: str = "",
    add_children: bool = False,
    min_protein_percent: float = 0,
    max_protein_percent: float = 0,
    min_fat_percent: float = 0,
    max_fat_percent: float = 0,
    min_carbs_percent: float = 0,
    max_carbs_percent: float = 0,
    intolerances: str = "",
    language: str = "en",
) -> dict:
    """
    Search for ingredients by name with optional nutrient-percentage filters.

    Args:
        query: Search term (e.g. "apple", "whole wheat flour").
        number: Number of results to return (max 100).
        offset: Pagination offset.
        sort: Sort field (e.g. "calories", "protein").
        sort_direction: "asc" or "desc".
        add_children: Include child ingredients (e.g. varieties of apples).
        min_protein_percent / max_protein_percent: Protein % of calories range.
        min_fat_percent / max_fat_percent: Fat % of calories range.
        min_carbs_percent / max_carbs_percent: Carbs % of calories range.
        intolerances: Comma-separated intolerances to filter out.
        language: Language for results ("en" or "de").

    Returns:
        dict with 'results' list and 'totalResults'.
    """
    params: dict = {
        "query": query,
        "number": number,
        "offset": offset,
        "language": language,
    }
    if sort:
        params["sort"] = sort
    if sort_direction:
        params["sortDirection"] = sort_direction
    if add_children:
        params["addChildren"] = True
    if min_protein_percent > 0:
        params["minProteinPercent"] = min_protein_percent
    if max_protein_percent > 0:
        params["maxProteinPercent"] = max_protein_percent
    if min_fat_percent > 0:
        params["minFatPercent"] = min_fat_percent
    if max_fat_percent > 0:
        params["maxFatPercent"] = max_fat_percent
    if min_carbs_percent > 0:
        params["minCarbsPercent"] = min_carbs_percent
    if max_carbs_percent > 0:
        params["maxCarbsPercent"] = max_carbs_percent
    if intolerances:
        params["intolerances"] = intolerances
    return _get("/food/ingredients/search", params)


def get_ingredient_information(
    ingredient_id: int,
    amount: float = 100,
    unit: str = "grams",
) -> dict:
    """
    Get detailed information about an ingredient including nutrition for a
    specified amount and unit.

    Args:
        ingredient_id: Spoonacular ingredient ID.
        amount: Amount of the ingredient.
        unit: Unit for the amount (e.g. "grams", "oz", "cup").

    Returns:
        dict with ingredient details and nutrition for the given amount.
    """
    params = {"amount": amount, "unit": unit}
    return _get(f"/food/ingredients/{ingredient_id}/information", params)


def get_ingredient_substitutes(ingredient_name: str) -> dict:
    """
    Get substitutes for an ingredient by name.

    Args:
        ingredient_name: Name of the ingredient (e.g. "butter").

    Returns:
        dict with 'ingredient' name and 'substitutes' list.
    """
    return _get("/food/ingredients/substitutes", {"ingredientName": ingredient_name})


def get_ingredient_substitutes_by_id(ingredient_id: int) -> dict:
    """
    Get substitutes for an ingredient by its Spoonacular ID.

    Args:
        ingredient_id: Spoonacular ingredient ID.

    Returns:
        dict with 'ingredient' name and 'substitutes' list.
    """
    return _get(f"/food/ingredients/{ingredient_id}/substitutes", {})


def autocomplete_ingredient_search(
    query: str,
    number: int = 10,
    intolerances: str = "",
    language: str = "en",
) -> list:
    """
    Autocomplete an ingredient name query. Useful for search-as-you-type.

    Args:
        query: Partial ingredient name.
        number: Number of suggestions (max 25).
        intolerances: Comma-separated intolerances to filter out.
        language: Language ("en" or "de").

    Returns:
        List of autocomplete suggestion objects with id, name, and image.
    """
    params: dict = {"query": query, "number": number, "language": language}
    if intolerances:
        params["intolerances"] = intolerances
    return _get("/food/ingredients/autocomplete", params)


def parse_ingredients(
    ingredient_list: str,
    servings: int = 1,
    include_nutrition: bool = False,
    language: str = "en",
) -> list:
    """
    Parse a list of ingredient strings (as you'd find in a recipe) into
    structured ingredient objects with amounts, units, and IDs.

    Args:
        ingredient_list: Newline-separated ingredient strings
                         (e.g. "1 cup flour\\n2 eggs\\n1 tsp salt").
        servings: Number of servings the ingredient list is for.
        include_nutrition: Whether to include nutrition data per ingredient.
        language: Language of the ingredient list ("en" or "de").

    Returns:
        List of parsed ingredient objects.
    """
    data = {
        "ingredientList": ingredient_list,
        "servings": servings,
        "includeNutrition": include_nutrition,
        "language": language,
    }
    return _post("/recipes/parseIngredients", data)


def compute_ingredient_amount(
    ingredient_id: int,
    nutrient: str,
    target: float,
    unit: str = "grams",
) -> dict:
    """
    Compute how much of an ingredient you need to reach a target amount of
    a specific nutrient.

    Args:
        ingredient_id: Spoonacular ingredient ID.
        nutrient: Nutrient name (e.g. "protein", "calories", "fat").
        target: Target amount of the nutrient.
        unit: Unit for the returned amount (e.g. "grams", "oz").

    Returns:
        dict with 'amount' and 'unit'.
    """
    params = {"nutrient": nutrient, "target": target, "unit": unit}
    return _get(f"/food/ingredients/{ingredient_id}/amount", params)


def convert_amounts(
    ingredient_name: str,
    source_amount: float,
    source_unit: str,
    target_unit: str,
) -> dict:
    """
    Convert an ingredient amount from one unit to another
    (e.g. 2 cups of flour to grams).

    Args:
        ingredient_name: Name of the ingredient (e.g. "flour").
        source_amount: Amount in the source unit.
        source_unit: Source unit (e.g. "cups").
        target_unit: Target unit (e.g. "grams").

    Returns:
        dict with 'sourceAmount', 'sourceUnit', 'targetAmount', 'targetUnit', 'answer'.
    """
    params = {
        "ingredientName": ingredient_name,
        "sourceAmount": source_amount,
        "sourceUnit": source_unit,
        "targetUnit": target_unit,
    }
    return _get("/recipes/convert", params)
