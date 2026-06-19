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


def _post_json(path: str, body: dict, params: dict | None = None) -> dict:
    if params is None:
        params = {}
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    body = {k: v for k, v in body.items() if v is not None}
    try:
        resp = requests.post(
            f"{BASE_URL}{path}",
            json=body,
            params=params,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ---------------------------------------------------------------------------
# Search Grocery Products
# ---------------------------------------------------------------------------

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
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> dict:
    """Search packaged food products such as frozen pizza or Greek yogurt."""
    return _get("/food/products/search", {
        "query": query,
        "minCalories": min_calories,
        "maxCalories": max_calories,
        "minCarbs": min_carbs,
        "maxCarbs": max_carbs,
        "minProtein": min_protein,
        "maxProtein": max_protein,
        "minFat": min_fat,
        "maxFat": max_fat,
        "addProductInformation": add_product_information,
        "offset": offset,
        "number": number,
    })


# ---------------------------------------------------------------------------
# Search Grocery Products by UPC
# ---------------------------------------------------------------------------

def get_grocery_product_by_upc(upc: str) -> dict:
    """Get information about a packaged food product using its UPC barcode."""
    return _get(f"/food/products/upc/{upc}", {})


# ---------------------------------------------------------------------------
# Get Product Information
# ---------------------------------------------------------------------------

def get_product_information(product_id: int) -> dict:
    """Get full information about a grocery product by its ID (ingredients, nutrition, cost, etc.)."""
    return _get(f"/food/products/{product_id}", {})


# ---------------------------------------------------------------------------
# Get Comparable Products
# ---------------------------------------------------------------------------

def get_comparable_products(product_id: int) -> dict:
    """Get comparable products to a given grocery product."""
    return _get(f"/food/products/{product_id}/comparable", {})


# ---------------------------------------------------------------------------
# Autocomplete Product Search
# ---------------------------------------------------------------------------

def autocomplete_product_search(
    query: str,
    number: Optional[int] = None,
) -> dict:
    """Generate autocomplete suggestions for grocery product searches."""
    return _get("/food/products/suggest", {
        "query": query,
        "number": number,
    })


# ---------------------------------------------------------------------------
# Classify Grocery Product
# ---------------------------------------------------------------------------

def classify_grocery_product(
    title: str,
    upc: Optional[str] = None,
    plu_code: Optional[str] = None,
    gtin: Optional[str] = None,
    brand: Optional[str] = None,
    ingredient_list: Optional[str] = None,
    locale: Optional[str] = None,
) -> dict:
    """Classify a grocery product into a basic category (e.g. a specific milk brand → 'milk')."""
    return _post_json("/food/products/classify", {
        "title": title,
        "upc": upc,
        "pluCode": plu_code,
        "gtin": gtin,
        "brand": brand,
        "ingredientList": ingredient_list,
        "locale": locale,
    })


# ---------------------------------------------------------------------------
# Classify Grocery Product Bulk
# ---------------------------------------------------------------------------

def classify_grocery_product_bulk(
    products: list,
    locale: Optional[str] = None,
) -> dict:
    """Classify multiple grocery products at once."""
    return _post_json("/food/products/classifyBatch", {
        "products": products,
        "locale": locale,
    })


# ---------------------------------------------------------------------------
# Map Ingredients to Grocery Products
# ---------------------------------------------------------------------------

def map_ingredients_to_grocery_products(
    ingredients: list,
    servings: int,
) -> dict:
    """Map a list of recipe ingredients to grocery products."""
    return _post_json("/food/ingredients/map", {
        "ingredients": ingredients,
        "servings": servings,
    })
