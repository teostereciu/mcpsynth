"""
Spoonacular Ingredients API tools.
Source: docs/api_ingredients.md
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict | list:
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(BASE_URL + path, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, params: dict, data: dict) -> dict | list:
    params["apiKey"] = _api_key()
    try:
        resp = requests.post(BASE_URL + path, params=params, data=data, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


def register_ingredients(mcp: FastMCP):

    @mcp.tool()
    def search_ingredients(
        search_query: str,
        add_children: bool = False,
        min_protein_percent: float = None,
        max_protein_percent: float = None,
        min_fat_percent: float = None,
        max_fat_percent: float = None,
        min_carbs_percent: float = None,
        max_carbs_percent: float = None,
        meta_information: bool = False,
        intolerances: str = "",
        sort: str = "",
        sort_direction: str = "",
        language: str = "en",
        offset: int = 0,
        number: int = 10,
    ) -> dict:
        """Search for simple whole foods (fruits, vegetables, nuts, grains, meat, fish, dairy, etc.)."""
        params = {
            "query": search_query,
            "addChildren": add_children,
            "metaInformation": meta_information,
            "language": language,
            "offset": offset,
            "number": number,
        }
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
        if intolerances:
            params["intolerances"] = intolerances
        if sort:
            params["sort"] = sort
        if sort_direction:
            params["sortDirection"] = sort_direction
        return _get("/food/ingredients/search", params)

    @mcp.tool()
    def get_ingredient_information(
        ingredient_id: int,
        amount: float = None,
        unit: str = "",
    ) -> dict:
        """Get all available information about an ingredient by its ID, including nutrition, cost, and aisle."""
        params = {}
        if amount is not None:
            params["amount"] = amount
        if unit:
            params["unit"] = unit
        return _get(f"/food/ingredients/{ingredient_id}/information", params)

    @mcp.tool()
    def compute_ingredient_amount(
        ingredient_id: int,
        nutrient: str,
        target: float,
        unit: str = "",
    ) -> dict:
        """Compute how much of an ingredient you need to reach a specific nutritional goal.
        E.g. how much pineapple to get 10g of protein."""
        params = {"nutrient": nutrient, "target": target}
        if unit:
            params["unit"] = unit
        return _get(f"/food/ingredients/{ingredient_id}/amount", params)

    @mcp.tool()
    def convert_amounts(
        ingredient_name: str,
        source_amount: float,
        source_unit: str,
        target_unit: str,
    ) -> dict:
        """Convert ingredient amounts between units. E.g. '2 cups of flour to grams'."""
        params = {
            "ingredientName": ingredient_name,
            "sourceAmount": source_amount,
            "sourceUnit": source_unit,
            "targetUnit": target_unit,
        }
        return _get("/recipes/convert", params)

    @mcp.tool()
    def parse_ingredients(
        ingredient_list: str,
        servings: int,
        include_nutrition: bool = False,
        language: str = "en",
    ) -> list:
        """Extract and parse ingredients from plain text. One ingredient per line.
        Returns structured ingredient data including amounts, units, and optionally nutrition."""
        params = {}
        data = {
            "ingredientList": ingredient_list,
            "servings": servings,
            "includeNutrition": include_nutrition,
            "language": language,
        }
        return _post("/recipes/parseIngredients", params, data)

    @mcp.tool()
    def compute_glycemic_load(
        ingredient_list: str,
        language: str = "en",
    ) -> dict:
        """Compute the glycemic load of a list of ingredients."""
        params = {"language": language}
        data = {"ingredientList": ingredient_list}
        return _post("/food/ingredients/glycemicLoad", params, data)

    @mcp.tool()
    def autocomplete_ingredient_search(
        search_query: str,
        number: int = 10,
        meta_information: bool = False,
        intolerances: str = "",
        language: str = "en",
    ) -> list:
        """Autocomplete an ingredient search query. Returns ingredient name suggestions."""
        params = {
            "query": search_query,
            "number": number,
            "metaInformation": meta_information,
            "language": language,
        }
        if intolerances:
            params["intolerances"] = intolerances
        return _get("/food/ingredients/autocomplete", params)

    @mcp.tool()
    def get_ingredient_substitutes(ingredient_name: str) -> dict:
        """Get ingredient substitutes for a given ingredient name (e.g. 'butter')."""
        params = {"ingredientName": ingredient_name}
        return _get("/food/ingredients/substitutes", params)

    @mcp.tool()
    def get_ingredient_substitutes_by_id(ingredient_id: int) -> dict:
        """Get ingredient substitutes for a given ingredient by its ID."""
        return _get(f"/food/ingredients/{ingredient_id}/substitutes", {})
