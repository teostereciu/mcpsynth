"""
Spoonacular Nutrition tools — nutrient lookup, recipe nutrition analysis,
menu item nutrition, and food product nutrition.
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
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def _post(path: str, data: dict) -> dict | list:
    params = {"apiKey": _api_key()}
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.post(url, params=params, data=data, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Recipe Nutrition
# ---------------------------------------------------------------------------

def get_recipe_nutrition_by_id(recipe_id: int) -> dict:
    """
    Get the full nutrition label data for a recipe by its Spoonacular ID.

    Args:
        recipe_id: Spoonacular recipe ID.

    Returns:
        dict with calories, macros, vitamins, minerals, and per-serving data.
    """
    return _get(f"/recipes/{recipe_id}/nutritionWidget.json", {})


def analyze_recipe_nutrition(
    title: str,
    ingredient_list: str,
    servings: int = 1,
    include_nutrition: bool = True,
) -> dict:
    """
    Analyze the nutrition of a recipe given its title and ingredient list.

    Args:
        title: Recipe title.
        ingredient_list: Newline-separated ingredient strings.
        servings: Number of servings.
        include_nutrition: Whether to include full nutrition breakdown.

    Returns:
        dict with nutrition information for the analyzed recipe.
    """
    data = {
        "title": title,
        "ingredientList": ingredient_list,
        "servings": servings,
        "includeNutrition": include_nutrition,
    }
    return _post("/recipes/analyze", data)


def get_nutrition_for_recipe_from_url(url: str, analyze_instructions: bool = False) -> dict:
    """
    Extract and analyze nutrition from a recipe URL (web scraping + analysis).

    Args:
        url: URL of the recipe page.
        analyze_instructions: Whether to also analyze the instructions.

    Returns:
        dict with extracted recipe data and nutrition.
    """
    params: dict = {"url": url}
    if analyze_instructions:
        params["analyzeInstructions"] = True
    return _get("/recipes/extract", params)


# ---------------------------------------------------------------------------
# Food / Menu Item Nutrition
# ---------------------------------------------------------------------------

def search_food_products(
    query: str,
    min_calories: float = 0,
    max_calories: float = 0,
    min_protein: float = 0,
    max_protein: float = 0,
    min_fat: float = 0,
    max_fat: float = 0,
    min_carbs: float = 0,
    max_carbs: float = 0,
    add_product_information: bool = False,
    offset: int = 0,
    number: int = 10,
) -> dict:
    """
    Search packaged food products in the Spoonacular database.

    Args:
        query: Search term (e.g. "greek yogurt", "protein bar").
        min_calories / max_calories: Calorie range per serving.
        min_protein / max_protein: Protein (g) range per serving.
        min_fat / max_fat: Fat (g) range per serving.
        min_carbs / max_carbs: Carbohydrate (g) range per serving.
        add_product_information: Include full product info in results.
        offset: Pagination offset.
        number: Number of results (max 100).

    Returns:
        dict with 'products' list and 'totalProducts'.
    """
    params: dict = {"query": query, "offset": offset, "number": number}
    for name, val in [
        ("minCalories", min_calories), ("maxCalories", max_calories),
        ("minProtein", min_protein), ("maxProtein", max_protein),
        ("minFat", min_fat), ("maxFat", max_fat),
        ("minCarbs", min_carbs), ("maxCarbs", max_carbs),
    ]:
        if val > 0:
            params[name] = val
    if add_product_information:
        params["addProductInformation"] = True
    return _get("/food/products/search", params)


def get_food_product_information(product_id: int) -> dict:
    """
    Get detailed information about a packaged food product by its ID.

    Args:
        product_id: Spoonacular food product ID.

    Returns:
        dict with product details, ingredients, and nutrition.
    """
    return _get(f"/food/products/{product_id}", {})


def search_menu_items(
    query: str,
    min_calories: float = 0,
    max_calories: float = 0,
    min_protein: float = 0,
    max_protein: float = 0,
    min_fat: float = 0,
    max_fat: float = 0,
    min_carbs: float = 0,
    max_carbs: float = 0,
    add_menu_item_information: bool = False,
    offset: int = 0,
    number: int = 10,
) -> dict:
    """
    Search restaurant menu items in the Spoonacular database.

    Args:
        query: Search term (e.g. "Big Mac", "caesar salad").
        min_calories / max_calories: Calorie range per serving.
        min_protein / max_protein: Protein (g) range per serving.
        min_fat / max_fat: Fat (g) range per serving.
        min_carbs / max_carbs: Carbohydrate (g) range per serving.
        add_menu_item_information: Include full menu item info in results.
        offset: Pagination offset.
        number: Number of results (max 100).

    Returns:
        dict with 'menuItems' list and 'totalMenuItems'.
    """
    params: dict = {"query": query, "offset": offset, "number": number}
    for name, val in [
        ("minCalories", min_calories), ("maxCalories", max_calories),
        ("minProtein", min_protein), ("maxProtein", max_protein),
        ("minFat", min_fat), ("maxFat", max_fat),
        ("minCarbs", min_carbs), ("maxCarbs", max_carbs),
    ]:
        if val > 0:
            params[name] = val
    if add_menu_item_information:
        params["addMenuItemInformation"] = True
    return _get("/food/menuItems/search", params)


def get_menu_item_information(menu_item_id: int) -> dict:
    """
    Get detailed information about a restaurant menu item by its ID.

    Args:
        menu_item_id: Spoonacular menu item ID.

    Returns:
        dict with menu item details and nutrition.
    """
    return _get(f"/food/menuItems/{menu_item_id}", {})


def get_comparable_products(upc: str) -> dict:
    """
    Find food products comparable to a given product by UPC barcode.

    Args:
        upc: UPC barcode string of the product.

    Returns:
        dict with comparable products and their nutrition comparison.
    """
    return _get(f"/food/products/upc/{upc}", {})


def map_ingredients_to_grocery_products(
    ingredient_list: str,
    servings: int = 1,
) -> list:
    """
    Map a list of recipe ingredients to actual grocery products.

    Args:
        ingredient_list: Newline-separated ingredient strings.
        servings: Number of servings.

    Returns:
        List of ingredient-to-product mappings.
    """
    data = {"ingredientList": ingredient_list, "servings": servings}
    return _post("/food/ingredients/map", data)
