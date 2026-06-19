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


def _get(path: str, params: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        r = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, params: dict, json_body) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        r = requests.post(f"{BASE_URL}{path}", params=params, json=json_body, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
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


def search_grocery_products_by_upc(upc: str) -> dict:
    """Get information about a packaged food product using its UPC barcode number."""
    return _get(f"/food/products/upc/{upc}", {})


def get_product_information(product_id: int) -> dict:
    """Get full information about a grocery product by its ID, including ingredients, nutrition, and cost."""
    return _get(f"/food/products/{product_id}", {})


def get_comparable_products(upc: str) -> dict:
    """Find comparable grocery products based on a product's UPC."""
    return _get(f"/food/products/upc/{upc}/comparable", {})


def autocomplete_product_search(query: str, number: Optional[int] = None) -> dict:
    """Generate autocomplete suggestions for grocery products based on a partial query."""
    return _get("/food/products/suggest", {
        "query": query,
        "number": number,
    })


def classify_grocery_product(
    title: str,
    locale: Optional[str] = None,
) -> dict:
    """Classify a packaged food product to a basic category (e.g. a specific brand of milk → 'milk')."""
    params = {}
    if locale:
        params["locale"] = locale
    params["apiKey"] = _api_key()
    try:
        r = requests.post(
            f"{BASE_URL}/food/products/classify",
            params=params,
            json={"title": title},
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def classify_grocery_product_bulk(products: list, locale: Optional[str] = None) -> list:
    """Classify multiple grocery products at once.
    products: list of dicts with 'title' and optionally 'upc' and 'plu_code'."""
    params = {"apiKey": _api_key()}
    if locale:
        params["locale"] = locale
    try:
        r = requests.post(
            f"{BASE_URL}/food/products/classifyBatch",
            params=params,
            json={"products": products},
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def map_ingredients_to_grocery_products(
    ingredients: list,
    servings: float,
) -> list:
    """Map a list of recipe ingredients to grocery products.
    ingredients: list of ingredient name strings.
    servings: number of servings the recipe makes."""
    params = {"apiKey": _api_key()}
    try:
        r = requests.post(
            f"{BASE_URL}/food/ingredients/map",
            params=params,
            json={"ingredients": ingredients, "servings": servings},
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}
