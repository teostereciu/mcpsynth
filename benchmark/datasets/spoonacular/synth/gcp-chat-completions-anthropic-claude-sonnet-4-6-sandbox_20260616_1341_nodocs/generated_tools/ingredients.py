"""
Spoonacular Ingredient tools — search, info, substitutes, parse.
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
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# Search ingredients
# ---------------------------------------------------------------------------

def search_ingredients(
    query: str,
    number: int = 10,
    offset: int = 0,
    sort: str = "",
    sort_direction: str = "",
    add_children: bool = False,
    min_protein_percent: float = None,
    max_protein_percent: float = None,
    min_fat_percent: float = None,
    max_fat_percent: float = None,
    min_carbs_percent: float = None,
    max_carbs_percent: float = None,
    intolerances: str = "",
    language: str = "en",
) -> dict:
    """
    Search for ingredients by name with optional nutritional filters.

    Args:
        query: The ingredient name to search for (e.g. 'apple').
        number: Number of results to return (max 100).
        offset: Pagination offset.
        sort: Sort field (e.g. 'calories', 'protein').
        sort_direction: 'asc' or 'desc'.
        add_children: Whether to add children of found ingredients.
        min_protein_percent: Minimum protein percentage.
        max_protein_percent: Maximum protein percentage.
        min_fat_percent: Minimum fat percentage.
        max_fat_percent: Maximum fat percentage.
        min_carbs_percent: Minimum carbohydrate percentage.
        max_carbs_percent: Maximum carbohydrate percentage.
        intolerances: Comma-separated intolerances to filter out.
        language: Language for results ('en' or 'de').

    Returns:
        dict with 'results' list and 'totalResults'.
    """
    try:
        params: dict = {
            "query": query,
            "number": number,
            "offset": offset,
            "addChildren": add_children,
            "language": language,
        }
        if sort:
            params["sort"] = sort
        if sort_direction:
            params["sortDirection"] = sort_direction
        if intolerances:
            params["intolerances"] = intolerances
        for key, val in [
            ("minProteinPercent", min_protein_percent),
            ("maxProteinPercent", max_protein_percent),
            ("minFatPercent", min_fat_percent),
            ("maxFatPercent", max_fat_percent),
            ("minCarbsPercent", min_carbs_percent),
            ("maxCarbsPercent", max_carbs_percent),
        ]:
            if val is not None:
                params[key] = val
        return _get("/food/ingredients/search", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get ingredient information
# ---------------------------------------------------------------------------

def get_ingredient_information(
    ingredient_id: int,
    amount: float = 100,
    unit: str = "grams",
) -> dict:
    """
    Get detailed information about an ingredient including nutrition per amount.

    Args:
        ingredient_id: The Spoonacular ingredient ID.
        amount: The amount of the ingredient.
        unit: The unit for the amount (e.g. 'grams', 'oz', 'cup').

    Returns:
        dict with ingredient details, nutrition, and possible units.
    """
    try:
        params = {"amount": amount, "unit": unit}
        return _get(f"/food/ingredients/{ingredient_id}/information", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Get ingredient substitutes
# ---------------------------------------------------------------------------

def get_ingredient_substitutes(ingredient_name: str) -> dict:
    """
    Get substitutes for a given ingredient.

    Args:
        ingredient_name: The name of the ingredient to find substitutes for.

    Returns:
        dict with 'ingredient' name and 'substitutes' list.
    """
    try:
        params = {"ingredientName": ingredient_name}
        return _get("/food/ingredients/substitutes", params)
    except Exception as exc:
        return {"error": str(exc)}


def get_ingredient_substitutes_by_id(ingredient_id: int) -> dict:
    """
    Get substitutes for an ingredient by its Spoonacular ID.

    Args:
        ingredient_id: The Spoonacular ingredient ID.

    Returns:
        dict with 'ingredient' name and 'substitutes' list.
    """
    try:
        return _get(f"/food/ingredients/{ingredient_id}/substitutes", {})
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Parse ingredients
# ---------------------------------------------------------------------------

def parse_ingredients(
    ingredient_list: str,
    servings: int = 1,
    include_nutrition: bool = False,
    language: str = "en",
) -> list:
    """
    Parse a list of ingredient strings into structured data with amounts, units,
    and Spoonacular ingredient IDs.

    Args:
        ingredient_list: Newline-separated ingredient strings
                         (e.g. '2 cups flour\\n1 tsp salt').
        servings: Number of servings the ingredient list is for.
        include_nutrition: Whether to include nutrition data per ingredient.
        language: Language of the ingredient list ('en' or 'de').

    Returns:
        List of parsed ingredient objects.
    """
    try:
        key = _api_key()
        url = f"{BASE_URL}/recipes/parseIngredients"
        resp = requests.post(
            url,
            params={"apiKey": key, "language": language},
            data={
                "ingredientList": ingredient_list,
                "servings": servings,
                "includeNutrition": include_nutrition,
            },
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Convert amounts
# ---------------------------------------------------------------------------

def convert_amounts(
    ingredient_name: str,
    source_amount: float,
    source_unit: str,
    target_unit: str,
) -> dict:
    """
    Convert an ingredient amount from one unit to another.

    Args:
        ingredient_name: The name of the ingredient (e.g. 'flour').
        source_amount: The amount in the source unit.
        source_unit: The source unit (e.g. 'cups').
        target_unit: The target unit (e.g. 'grams').

    Returns:
        dict with 'sourceAmount', 'sourceUnit', 'targetAmount', 'targetUnit', 'answer'.
    """
    try:
        params = {
            "ingredientName": ingredient_name,
            "sourceAmount": source_amount,
            "sourceUnit": source_unit,
            "targetUnit": target_unit,
        }
        return _get("/recipes/convert", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Autocomplete ingredient search
# ---------------------------------------------------------------------------

def autocomplete_ingredient_search(
    query: str,
    number: int = 10,
    intolerances: str = "",
    language: str = "en",
) -> list:
    """
    Autocomplete an ingredient search query.

    Args:
        query: Partial ingredient name to autocomplete.
        number: Number of suggestions to return (max 100).
        intolerances: Comma-separated intolerances to filter out.
        language: Language for results ('en' or 'de').

    Returns:
        List of autocomplete suggestion objects with id, name, and image.
    """
    try:
        params: dict = {"query": query, "number": number, "language": language}
        if intolerances:
            params["intolerances"] = intolerances
        return _get("/food/ingredients/autocomplete", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Compute glycemic load
# ---------------------------------------------------------------------------

def compute_glycemic_load(ingredient_list: list) -> dict:
    """
    Compute the glycemic load of a list of ingredients.

    Args:
        ingredient_list: List of ingredient strings with amounts
                         (e.g. ['1 cup rice', '2 tbsp sugar']).

    Returns:
        dict with total glycemic load and per-ingredient breakdown.
    """
    try:
        key = _api_key()
        url = f"{BASE_URL}/food/ingredients/glycemicLoad"
        resp = requests.post(
            url,
            params={"apiKey": key},
            json={"ingredients": ingredient_list},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}
