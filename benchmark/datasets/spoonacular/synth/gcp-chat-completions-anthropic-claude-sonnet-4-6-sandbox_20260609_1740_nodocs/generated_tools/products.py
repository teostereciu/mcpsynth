"""
Spoonacular Food Products tools — search grocery products, get product info,
compare products, classify products.
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


def search_grocery_products(
    query: str,
    min_calories: float = None,
    max_calories: float = None,
    min_carbs: float = None,
    max_carbs: float = None,
    min_protein: float = None,
    max_protein: float = None,
    min_fat: float = None,
    max_fat: float = None,
    add_product_information: bool = None,
    offset: int = None,
    number: int = 10,
) -> dict:
    """
    Search for grocery/food products by name with optional nutritional filters.
    Returns a list of matching products with basic information.
    """
    params = {
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
    }
    return _get("/food/products/search", params)


def get_product_information(product_id: int) -> dict:
    """
    Get detailed information about a grocery product by its Spoonacular ID,
    including ingredients, nutrition facts, and badges.
    """
    return _get(f"/food/products/{product_id}", {})


def get_comparable_products(upc: str) -> dict:
    """
    Find comparable grocery products for a given product identified by its
    UPC barcode. Returns similar products with nutritional comparison.
    """
    return _get(f"/food/products/upc/{upc}/comparable", {})


def search_grocery_products_by_upc(upc: str) -> dict:
    """
    Look up a grocery product by its UPC barcode. Returns product details
    including name, nutrition, and ingredients.
    """
    return _get(f"/food/products/upc/{upc}", {})


def autocomplete_product_search(query: str, number: int = 10) -> list:
    """
    Autocomplete a grocery product search query. Returns a list of product
    name suggestions matching the query prefix.
    """
    params = {"query": query, "number": number}
    return _get("/food/products/suggest", params)


def classify_grocery_product(
    title: str,
    upc: str = None,
    plu_code: str = None,
) -> dict:
    """
    Classify a grocery product into a category given its title and optionally
    its UPC or PLU code.
    """
    try:
        api_key = _api_key()
        data = {"title": title}
        if upc:
            data["upc"] = upc
        if plu_code:
            data["pluCode"] = plu_code
        resp = requests.post(
            f"{BASE_URL}/food/products/classify",
            params={"apiKey": api_key},
            json=data,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def classify_grocery_product_bulk(products: list) -> list:
    """
    Classify multiple grocery products at once. Provide a list of dicts,
    each with a 'title' key and optionally 'upc' and 'pluCode'.
    Returns category classifications for each product.
    """
    try:
        api_key = _api_key()
        resp = requests.post(
            f"{BASE_URL}/food/products/classifyBatch",
            params={"apiKey": api_key},
            json=products,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def get_product_nutrition_by_id(product_id: int) -> dict:
    """
    Get the nutritional information for a grocery product by its Spoonacular ID.
    Returns macros, vitamins, minerals, and serving size information.
    """
    return _get(f"/food/products/{product_id}/nutritionWidget.json", {})
