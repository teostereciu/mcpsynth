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
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


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
    Search for ingredients by name with optional nutrient and intolerance filters.

    Args:
        query: Ingredient name to search for (e.g. 'apple', 'whole wheat flour').
        add_children: Include child ingredients in results when True.
        min_protein_percent: Minimum protein percentage of daily needs.
        max_protein_percent: Maximum protein percentage of daily needs.
        min_fat_percent: Minimum fat percentage of daily needs.
        max_fat_percent: Maximum fat percentage of daily needs.
        min_carbs_percent: Minimum carbs percentage of daily needs.
        max_carbs_percent: Maximum carbs percentage of daily needs.
        meta_information: Add meta information (aisle, image) to results when True.
        intolerances: Comma-separated intolerances to filter out (e.g. 'gluten,dairy').
        sort: Sort field (e.g. 'calories', 'protein').
        sort_direction: 'asc' or 'desc'.
        offset: Pagination offset.
        number: Number of results (default 10).

    Returns:
        dict with 'results' list and 'totalResults'.
    """
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
        "offset": offset,
        "number": number,
    })


def get_ingredient_information(
    ingredient_id: int,
    amount: float = None,
    unit: str = None,
) -> dict:
    """
    Get detailed information about an ingredient by its Spoonacular ID,
    including nutrition, possible units, and aisle location.

    Args:
        ingredient_id: Spoonacular ingredient ID.
        amount: Amount of the ingredient to compute nutrition for.
        unit: Unit for the amount (e.g. 'grams', 'cups', 'oz').

    Returns:
        dict with ingredient details and nutrition for the given amount.
    """
    return _get(f"/food/ingredients/{ingredient_id}/information", {
        "amount": amount,
        "unit": unit,
    })


def get_ingredient_substitutes(ingredient_name: str) -> dict:
    """
    Get ingredient substitutes for a given ingredient name.

    Args:
        ingredient_name: Name of the ingredient to find substitutes for
                         (e.g. 'butter', 'eggs').

    Returns:
        dict with 'ingredient' name and 'substitutes' list.
    """
    return _get("/food/ingredients/substitutes", {"ingredientName": ingredient_name})


def get_ingredient_substitutes_by_id(ingredient_id: int) -> dict:
    """
    Get ingredient substitutes for a given ingredient by its Spoonacular ID.

    Args:
        ingredient_id: Spoonacular ingredient ID.

    Returns:
        dict with 'ingredient' name and 'substitutes' list.
    """
    return _get(f"/food/ingredients/{ingredient_id}/substitutes", {})


def parse_ingredients(
    ingredient_list: str,
    servings: int = 1,
    include_nutrition: bool = False,
    language: str = "en",
) -> list:
    """
    Parse a free-text ingredient list into structured ingredient objects
    with amounts, units, and Spoonacular IDs.

    Args:
        ingredient_list: Newline-separated ingredient strings
                         (e.g. '1 cup flour\\n2 eggs\\n1 tsp salt').
        servings: Number of servings the ingredient list is for (default 1).
        include_nutrition: Include nutrition data per ingredient when True.
        language: Language of the ingredient list ('en' or 'de').

    Returns:
        List of parsed ingredient objects with name, amount, unit, and ID.
    """
    try:
        key = _api_key()
    except ValueError as exc:
        return [{"error": str(exc)}]
    try:
        resp = requests.post(
            f"{BASE_URL}/recipes/parseIngredients",
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
    except requests.HTTPError as exc:
        return [{"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}]
    except Exception as exc:
        return [{"error": str(exc)}]


def autocomplete_ingredient_search(
    query: str,
    number: int = 10,
    meta_information: bool = False,
    intolerances: str = None,
) -> list:
    """
    Autocomplete an ingredient search query. Useful for ingredient-picker UIs.

    Args:
        query: Partial ingredient name (e.g. 'tom' → 'tomato', 'tomato paste').
        number: Number of suggestions to return (default 10).
        meta_information: Include aisle and image info when True.
        intolerances: Comma-separated intolerances to filter out.

    Returns:
        List of autocomplete suggestion objects with 'id' and 'name'.
    """
    return _get("/food/ingredients/autocomplete", {
        "query": query,
        "number": number,
        "metaInformation": meta_information,
        "intolerances": intolerances,
    })


def compute_ingredient_amount(
    ingredient_id: int,
    nutrient: str,
    target: float,
    unit: str = None,
) -> dict:
    """
    Compute how much of an ingredient is needed to reach a target amount of
    a specific nutrient.

    Args:
        ingredient_id: Spoonacular ingredient ID.
        nutrient: Nutrient name (e.g. 'protein', 'calories', 'fat').
        target: Target amount of the nutrient.
        unit: Desired unit for the result (e.g. 'grams', 'oz').

    Returns:
        dict with 'amount' and 'unit' needed to hit the target nutrient.
    """
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
    """
    Convert an ingredient amount from one unit to another
    (e.g. '2 cups of flour' → grams).

    Args:
        ingredient_name: Name of the ingredient (e.g. 'flour', 'milk').
        source_amount: Amount in the source unit.
        source_unit: Source unit (e.g. 'cups', 'tablespoons').
        target_unit: Target unit (e.g. 'grams', 'oz').

    Returns:
        dict with 'sourceAmount', 'sourceUnit', 'targetAmount', 'targetUnit', 'answer'.
    """
    return _get("/recipes/convert", {
        "ingredientName": ingredient_name,
        "sourceAmount": source_amount,
        "sourceUnit": source_unit,
        "targetUnit": target_unit,
    })
