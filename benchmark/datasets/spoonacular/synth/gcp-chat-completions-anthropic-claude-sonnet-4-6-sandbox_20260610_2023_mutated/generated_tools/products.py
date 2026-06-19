"""
Spoonacular Grocery Products API tools.
Endpoints covered:
  - GET  /food/products/search
  - GET  /food/products/upc/{upc}
  - GET  /food/products/{id}
  - GET  /food/products/{id}/comparable
  - GET  /food/products/suggest
  - POST /food/products/classify
  - POST /food/products/classifyBatch
  - POST /food/ingredients/map
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
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, params: dict, json_body: Optional[dict] = None, data: Optional[dict] = None) -> dict:
    params["apiKey"] = _api_key()
    try:
        if json_body is not None:
            resp = requests.post(f"{BASE_URL}{path}", params=params, json=json_body, timeout=15)
        else:
            resp = requests.post(f"{BASE_URL}{path}", params=params, data=data, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_grocery_products(
    search_query: str,
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
    """Search packaged food products such as frozen pizza or Greek yogurt.
    Supports nutritional filters."""
    params: dict = {"search_query": search_query, "offset": offset, "number": number}
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
    if add_product_information is not None:
        params["addProductInformation"] = add_product_information
    return _get("/food/products/search", params)


def search_grocery_products_by_upc(upc: str) -> dict:
    """Get information about a packaged food product using its UPC barcode number."""
    return _get(f"/food/products/upc/{upc}", {})


def get_product_information(product_id: int) -> dict:
    """Get full information about a grocery product by its ID (ingredients, nutrition, badges, etc.)."""
    return _get(f"/food/products/{product_id}", {})


def get_comparable_products(product_id: int) -> dict:
    """Find grocery products comparable (similar nutritional profile) to a given product by its ID."""
    return _get(f"/food/products/{product_id}/comparable", {})


def autocomplete_product_search(search_query: str, number: int = 10) -> dict:
    """Generate autocomplete suggestions for grocery products based on a partial search query."""
    params: dict = {"query": search_query, "number": number}
    return _get("/food/products/suggest", params)


def classify_grocery_product(
    title: str,
    upc: Optional[str] = None,
    plu_code: Optional[str] = None,
    gtin: Optional[str] = None,
    language: str = "en",
    locale: str = "en_US",
) -> dict:
    """Classify a grocery product into a category given its title and optionally UPC/PLU/GTIN."""
    body: dict = {"title": title, "language": language, "locale": locale}
    if upc is not None:
        body["upc"] = upc
    if plu_code is not None:
        body["pluCode"] = plu_code
    if gtin is not None:
        body["gtin"] = gtin
    return _post("/food/products/classify", {}, json_body=body)


def classify_grocery_product_bulk(
    products: list,
    language: str = "en",
    locale: str = "en_US",
) -> dict:
    """Classify multiple grocery products at once.
    products: list of dicts, each with at least a 'title' key."""
    params: dict = {"language": language, "locale": locale}
    return _post("/food/products/classifyBatch", params, json_body=products)


def map_ingredients_to_grocery_products(
    ingredients: list,
    servings: float,
) -> dict:
    """Map a list of ingredient names to grocery products.
    ingredients: list of ingredient name strings.
    servings: the number of servings."""
    body: dict = {"ingredients": ingredients, "servings": servings}
    return _post("/food/ingredients/map", {}, json_body=body)
