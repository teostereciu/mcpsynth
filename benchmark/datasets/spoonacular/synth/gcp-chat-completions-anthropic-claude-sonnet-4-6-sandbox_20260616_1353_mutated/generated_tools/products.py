"""
Spoonacular Grocery Products API tools.
Source: docs/api_products.md
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


def _post(path: str, params: dict, json_body: dict) -> dict | list:
    params["apiKey"] = _api_key()
    try:
        resp = requests.post(BASE_URL + path, params=params, json=json_body, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


def register_products(mcp: FastMCP):

    @mcp.tool()
    def search_grocery_products(
        search_query: str,
        min_calories: float = None,
        max_calories: float = None,
        min_carbs: float = None,
        max_carbs: float = None,
        min_protein: float = None,
        max_protein: float = None,
        min_fat: float = None,
        max_fat: float = None,
        add_product_information: bool = False,
        offset: int = 0,
        number: int = 10,
    ) -> dict:
        """Search packaged food products such as frozen pizza or Greek yogurt.
        Filter by nutritional content per serving."""
        params = {
            "query": search_query,
            "addProductInformation": add_product_information,
            "offset": offset,
            "number": number,
        }
        if min_calories is not None:
            params["minCalories"] = min_calories
        if max_calories is not None:
            params["maxCalories"] = max_calories
        if min_carbs is not None:
            params["minCarbs"] = min_carbs
        if max_carbs is not None:
            params["maxCarbs"] = max_carbs
        if min_protein is not None:
            params["minProtein"] = min_protein
        if max_protein is not None:
            params["maxProtein"] = max_protein
        if min_fat is not None:
            params["minFat"] = min_fat
        if max_fat is not None:
            params["maxFat"] = max_fat
        return _get("/food/products/search", params)

    @mcp.tool()
    def search_grocery_products_by_upc(upc: str) -> dict:
        """Get information about a packaged food product using its UPC barcode number."""
        return _get(f"/food/products/upc/{upc}", {})

    @mcp.tool()
    def get_product_information(product_id: int) -> dict:
        """Get full information about a grocery product by its ID, including ingredients,
        nutrition, cost, and supermarket aisle location."""
        return _get(f"/food/products/{product_id}", {})

    @mcp.tool()
    def get_comparable_products(upc: str) -> dict:
        """Find comparable (similar) grocery products for a given product identified by UPC."""
        return _get(f"/food/products/upc/{upc}/comparable", {})

    @mcp.tool()
    def autocomplete_product_search(
        search_query: str,
        number: int = 10,
    ) -> dict:
        """Generate autocomplete suggestions for grocery product searches."""
        params = {"query": search_query, "number": number}
        return _get("/food/products/suggest", params)

    @mcp.tool()
    def classify_grocery_product(
        title: str,
        upc: str = "",
        plu_code: str = "",
    ) -> dict:
        """Classify a grocery product into categories based on its title and optionally UPC or PLU code."""
        params = {}
        body: dict = {"title": title}
        if upc:
            body["upc"] = upc
        if plu_code:
            body["pluCode"] = plu_code
        return _post("/food/products/classify", params, body)

    @mcp.tool()
    def classify_grocery_product_bulk(
        products: list,
    ) -> list:
        """Classify multiple grocery products at once. products: list of dicts with 'title' and optionally 'upc'."""
        params = {}
        return _post("/food/products/classifyBatch", params, products)

    @mcp.tool()
    def map_ingredients_to_grocery_products(
        ingredients: list,
        servings: float,
    ) -> list:
        """Map a list of ingredient names to actual grocery products.
        ingredients: list of ingredient name strings. servings: number of servings."""
        params = {}
        body = {"ingredients": ingredients, "servings": servings}
        return _post("/food/ingredients/map", params, body)
