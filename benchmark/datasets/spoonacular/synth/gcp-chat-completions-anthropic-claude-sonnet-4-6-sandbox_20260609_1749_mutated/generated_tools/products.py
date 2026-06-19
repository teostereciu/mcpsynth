"""Spoonacular Grocery Products API tools."""
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


def _post(path: str, json_body: dict, params: dict = None) -> dict:
    p = params or {}
    p["apiKey"] = _api_key()
    try:
        resp = requests.post(f"{BASE_URL}{path}", json=json_body, params=p, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_grocery_products(
    query: str,
    min_calories: Optional[float] = None,
    max_calories: Optional[float] = None,
    min_carbs: Optional[float] = None,
    max_carbs: Optional[float] = None,
    min_protein: Optional[float] = None,
    max_protein: Optional[float] = None,
    min_fat: Optional[float] = None,
    max_fat: Optional[float] = None,
    add_product_information: Optional[bool] = None,
    offset: int = 0,
    number: int = 10,
) -> dict:
    """Search packaged food products such as frozen pizza or Greek yogurt."""
    params: dict = {"query": query, "offset": offset, "number": number}
    if min_calories is not None: params["minCalories"] = min_calories
    if max_calories is not None: params["maxCalories"] = max_calories
    if min_carbs is not None: params["minCarbs"] = min_carbs
    if max_carbs is not None: params["maxCarbs"] = max_carbs
    if min_protein is not None: params["minProtein"] = min_protein
    if max_protein is not None: params["maxProtein"] = max_protein
    if min_fat is not None: params["minFat"] = min_fat
    if max_fat is not None: params["maxFat"] = max_fat
    if add_product_information is not None: params["addProductInformation"] = add_product_information
    return _get("/food/products/search", params)


def search_grocery_products_by_upc(upc: str) -> dict:
    """Get information about a packaged food product using its UPC barcode."""
    return _get(f"/food/products/upc/{upc}", {})


def get_product_information(product_id: int) -> dict:
    """Get full information about a grocery product by its ID (nutrition, ingredients, etc.)."""
    return _get(f"/food/products/{product_id}", {})


def get_comparable_products(upc: str) -> dict:
    """Find comparable grocery products based on a product's UPC."""
    return _get(f"/food/products/upc/{upc}/comparable", {})


def autocomplete_product_search(query: str, number: int = 10) -> dict:
    """Generate autocomplete suggestions for grocery product searches."""
    params = {"query": query, "number": number}
    return _get("/food/products/suggest", params)


def classify_grocery_product(title: str, locale: str = "en_US") -> dict:
    """Classify a grocery product into a category given its title."""
    return _post("/food/products/classify", {"title": title, "locale": locale})


def classify_grocery_product_bulk(products: list) -> list:
    """Classify multiple grocery products at once.

    products: list of dicts, each with 'title' and optionally 'locale'.
    """
    return _post("/food/products/classifyBatch", {"products": products})


def map_ingredients_to_grocery_products(ingredients: list, servings: float) -> list:
    """Map a list of ingredient strings to actual grocery products.

    ingredients: list of ingredient strings, e.g. ["1 cup flour", "2 eggs"]
    servings: the number of servings.
    """
    return _post(
        "/food/ingredients/map",
        {"ingredients": ingredients, "servings": servings},
    )
