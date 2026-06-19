"""
Spoonacular Nutrition tools — analyze recipes, compute nutrition from text/image.
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
# Analyze a recipe (POST with full recipe data)
# ---------------------------------------------------------------------------

def analyze_recipe(
    title: str,
    ingredient_list: str,
    servings: int = 1,
    include_nutrition: bool = True,
    language: str = "en",
) -> dict:
    """
    Analyze a recipe by providing its title, ingredients, and servings to get
    full nutritional information.

    Args:
        title: The recipe title.
        ingredient_list: Newline-separated ingredient strings
                         (e.g. '2 cups flour\\n1 tsp salt').
        servings: Number of servings the recipe makes.
        include_nutrition: Whether to include detailed nutrition data.
        language: Language of the ingredients ('en' or 'de').

    Returns:
        dict with nutrition facts, ingredient details, and cost estimate.
    """
    try:
        key = _api_key()
        url = f"{BASE_URL}/recipes/analyze"
        resp = requests.post(
            url,
            params={"apiKey": key, "language": language, "includeNutrition": include_nutrition},
            json={
                "title": title,
                "ingredientList": ingredient_list,
                "servings": servings,
            },
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Nutrition by ID (already in recipes.py as get_recipe_nutrition, but here
# we expose the /food/nutrition endpoint for arbitrary food items)
# ---------------------------------------------------------------------------

def get_nutrition_by_id(nutrition_id: int) -> dict:
    """
    Get nutrition information for a food item by its Spoonacular ID.

    Args:
        nutrition_id: The Spoonacular food/ingredient ID.

    Returns:
        dict with detailed nutrition facts.
    """
    try:
        return _get(f"/food/ingredients/{nutrition_id}/information", {"amount": 100, "unit": "grams"})
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Map ingredients to grocery products
# ---------------------------------------------------------------------------

def map_ingredients_to_grocery_products(
    ingredient_list: list,
    servings: int = 1,
) -> list:
    """
    Map a list of recipe ingredients to actual grocery products available for purchase.

    Args:
        ingredient_list: List of ingredient strings (e.g. ['2 cups flour', '1 egg']).
        servings: Number of servings.

    Returns:
        List of mapped grocery product objects per ingredient.
    """
    try:
        key = _api_key()
        url = f"{BASE_URL}/food/ingredients/map"
        resp = requests.post(
            url,
            params={"apiKey": key},
            json={"ingredients": ingredient_list, "servings": servings},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Detect food in text
# ---------------------------------------------------------------------------

def detect_food_in_text(text: str) -> dict:
    """
    Detect food items mentioned in a free-text string.

    Args:
        text: Any text that may contain food mentions
              (e.g. 'I had a bowl of pasta and a glass of orange juice').

    Returns:
        dict with list of detected food annotations and their positions.
    """
    try:
        key = _api_key()
        url = f"{BASE_URL}/food/detect"
        resp = requests.post(
            url,
            params={"apiKey": key},
            data={"text": text},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Search grocery products
# ---------------------------------------------------------------------------

def search_grocery_products(
    query: str,
    number: int = 10,
    offset: int = 0,
    min_calories: float = None,
    max_calories: float = None,
    min_protein: float = None,
    max_protein: float = None,
    min_fat: float = None,
    max_fat: float = None,
    min_carbs: float = None,
    max_carbs: float = None,
) -> dict:
    """
    Search for packaged grocery products in the Spoonacular database.

    Args:
        query: Product name or keyword to search for.
        number: Number of results to return (max 100).
        offset: Pagination offset.
        min_calories: Minimum calories per serving.
        max_calories: Maximum calories per serving.
        min_protein: Minimum protein (g) per serving.
        max_protein: Maximum protein (g) per serving.
        min_fat: Minimum fat (g) per serving.
        max_fat: Maximum fat (g) per serving.
        min_carbs: Minimum carbohydrates (g) per serving.
        max_carbs: Maximum carbohydrates (g) per serving.

    Returns:
        dict with 'products' list and 'totalProducts' count.
    """
    try:
        params: dict = {"query": query, "number": number, "offset": offset}
        for key, val in [
            ("minCalories", min_calories), ("maxCalories", max_calories),
            ("minProtein", min_protein), ("maxProtein", max_protein),
            ("minFat", min_fat), ("maxFat", max_fat),
            ("minCarbs", min_carbs), ("maxCarbs", max_carbs),
        ]:
            if val is not None:
                params[key] = val
        return _get("/food/products/search", params)
    except Exception as exc:
        return {"error": str(exc)}


def get_grocery_product_information(product_id: int) -> dict:
    """
    Get detailed information about a grocery product by its Spoonacular ID.

    Args:
        product_id: The Spoonacular grocery product ID.

    Returns:
        dict with product details including nutrition, ingredients, and badges.
    """
    try:
        return _get(f"/food/products/{product_id}", {})
    except Exception as exc:
        return {"error": str(exc)}


def get_comparable_products(upc: str) -> dict:
    """
    Find comparable (similar) grocery products for a given product UPC.

    Args:
        upc: The UPC barcode of the product.

    Returns:
        dict with comparable products and their nutritional comparison.
    """
    try:
        return _get(f"/food/products/upc/{upc}/comparable", {})
    except Exception as exc:
        return {"error": str(exc)}


def search_grocery_products_by_upc(upc: str) -> dict:
    """
    Get grocery product information by UPC barcode.

    Args:
        upc: The UPC barcode of the product.

    Returns:
        dict with product details including nutrition facts.
    """
    try:
        return _get(f"/food/products/upc/{upc}", {})
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Classify grocery product
# ---------------------------------------------------------------------------

def classify_grocery_product(
    title: str,
    upc: str = "",
    plu_code: str = "",
) -> dict:
    """
    Classify a grocery product into a category based on its title.

    Args:
        title: The product title.
        upc: Optional UPC barcode.
        plu_code: Optional PLU code.

    Returns:
        dict with 'cleanTitle', 'image', 'category', 'breadcrumbs', and 'usdaCode'.
    """
    try:
        key = _api_key()
        url = f"{BASE_URL}/food/products/classify"
        payload: dict = {"title": title}
        if upc:
            payload["upc"] = upc
        if plu_code:
            payload["pluCode"] = plu_code
        resp = requests.post(
            url,
            params={"apiKey": key},
            json=payload,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}
