"""
Spoonacular Nutrition tools — nutrient lookup, recipe nutrition analysis,
menu item nutrition, and grocery product nutrition.
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


def _post_form(path: str, data: dict, params: dict = None) -> dict | list:
    if params is None:
        params = {}
    params = {k: v for k, v in params.items() if v is not None}
    data = {k: v for k, v in data.items() if v is not None}
    try:
        params["apiKey"] = _api_key()
    except ValueError as exc:
        return {"error": str(exc)}
    try:
        resp = requests.post(
            f"{BASE_URL}{path}", params=params, data=data, timeout=15
        )
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
        dict with calories, macros, and full nutrient breakdown including
        percent daily values.
    """
    return _get(f"/recipes/{recipe_id}/nutritionWidget.json", {})


def analyze_recipe_nutrition(
    title: str,
    ingredient_list: str,
    servings: int = 1,
    include_nutrition: bool = True,
) -> dict:
    """
    Analyze the nutrition of a custom recipe given its title and ingredient list.

    Args:
        title: Recipe title.
        ingredient_list: Newline-separated ingredient strings
                         (e.g. '1 cup flour\\n2 eggs').
        servings: Number of servings the recipe makes.
        include_nutrition: Return full nutrition breakdown when True.

    Returns:
        dict with nutrition information for the analyzed recipe.
    """
    return _post_form(
        "/recipes/analyze",
        {
            "title": title,
            "ingredientList": ingredient_list,
            "servings": servings,
            "includeNutrition": include_nutrition,
        },
    )


def get_recipe_nutrition_label(recipe_id: int) -> dict:
    """
    Get the nutrition label (as structured data) for a recipe.

    Args:
        recipe_id: Spoonacular recipe ID.

    Returns:
        dict representing the nutrition label with serving size and nutrients.
    """
    return _get(f"/recipes/{recipe_id}/nutritionLabel.json", {})


# ---------------------------------------------------------------------------
# Grocery Products Nutrition
# ---------------------------------------------------------------------------

def search_grocery_products(
    query: str,
    min_calories: float = None,
    max_calories: float = None,
    min_protein: float = None,
    max_protein: float = None,
    min_fat: float = None,
    max_fat: float = None,
    min_carbs: float = None,
    max_carbs: float = None,
    add_product_information: bool = None,
    offset: int = None,
    number: int = 10,
) -> dict:
    """
    Search for grocery/packaged food products with optional nutrient filters.

    Args:
        query: Product name or keyword (e.g. 'greek yogurt', 'whole grain bread').
        min_calories: Minimum calories per serving.
        max_calories: Maximum calories per serving.
        min_protein: Minimum protein (g) per serving.
        max_protein: Maximum protein (g) per serving.
        min_fat: Minimum fat (g) per serving.
        max_fat: Maximum fat (g) per serving.
        min_carbs: Minimum carbs (g) per serving.
        max_carbs: Maximum carbs (g) per serving.
        add_product_information: Include full product info in results when True.
        offset: Pagination offset.
        number: Number of results (default 10).

    Returns:
        dict with 'products' list and 'totalProducts' count.
    """
    return _get("/food/products/search", {
        "query": query,
        "minCalories": min_calories,
        "maxCalories": max_calories,
        "minProtein": min_protein,
        "maxProtein": max_protein,
        "minFat": min_fat,
        "maxFat": max_fat,
        "minCarbs": min_carbs,
        "maxCarbs": max_carbs,
        "addProductInformation": add_product_information,
        "offset": offset,
        "number": number,
    })


def get_grocery_product_information(product_id: int) -> dict:
    """
    Get detailed information about a grocery product by its Spoonacular ID,
    including ingredients, nutrition, and badges.

    Args:
        product_id: Spoonacular grocery product ID.

    Returns:
        dict with full product details.
    """
    return _get(f"/food/products/{product_id}", {})


def get_grocery_product_nutrition(product_id: int) -> dict:
    """
    Get the nutrition label data for a grocery product.

    Args:
        product_id: Spoonacular grocery product ID.

    Returns:
        dict with nutrition label information.
    """
    return _get(f"/food/products/{product_id}/nutritionWidget.json", {})


def autocomplete_product_search(query: str, number: int = 10) -> list:
    """
    Autocomplete a grocery product search query.

    Args:
        query: Partial product name to autocomplete.
        number: Number of suggestions (default 10).

    Returns:
        List of product suggestion objects.
    """
    return _get("/food/products/suggest", {"query": query, "number": number})


# ---------------------------------------------------------------------------
# Menu Items Nutrition
# ---------------------------------------------------------------------------

def search_menu_items(
    query: str,
    min_calories: float = None,
    max_calories: float = None,
    min_protein: float = None,
    max_protein: float = None,
    min_fat: float = None,
    max_fat: float = None,
    min_carbs: float = None,
    max_carbs: float = None,
    offset: int = None,
    number: int = 10,
) -> dict:
    """
    Search restaurant menu items with optional nutrient filters.

    Args:
        query: Menu item name or keyword (e.g. 'big mac', 'caesar salad').
        min_calories: Minimum calories.
        max_calories: Maximum calories.
        min_protein: Minimum protein (g).
        max_protein: Maximum protein (g).
        min_fat: Minimum fat (g).
        max_fat: Maximum fat (g).
        min_carbs: Minimum carbs (g).
        max_carbs: Maximum carbs (g).
        offset: Pagination offset.
        number: Number of results (default 10).

    Returns:
        dict with 'menuItems' list and 'totalMenuItems' count.
    """
    return _get("/food/menuItems/search", {
        "query": query,
        "minCalories": min_calories,
        "maxCalories": max_calories,
        "minProtein": min_protein,
        "maxProtein": max_protein,
        "minFat": min_fat,
        "maxFat": max_fat,
        "minCarbs": min_carbs,
        "maxCarbs": max_carbs,
        "offset": offset,
        "number": number,
    })


def get_menu_item_information(menu_item_id: int) -> dict:
    """
    Get detailed information about a restaurant menu item by its Spoonacular ID.

    Args:
        menu_item_id: Spoonacular menu item ID.

    Returns:
        dict with menu item details including nutrition.
    """
    return _get(f"/food/menuItems/{menu_item_id}", {})


def get_menu_item_nutrition(menu_item_id: int) -> dict:
    """
    Get the nutrition label data for a restaurant menu item.

    Args:
        menu_item_id: Spoonacular menu item ID.

    Returns:
        dict with nutrition label information.
    """
    return _get(f"/food/menuItems/{menu_item_id}/nutritionWidget.json", {})


# ---------------------------------------------------------------------------
# General Nutrition Utilities
# ---------------------------------------------------------------------------

def guess_nutrition_by_dish_name(title: str) -> dict:
    """
    Quickly estimate the nutrition of a dish just from its name, without
    needing a full ingredient list.

    Args:
        title: Dish name (e.g. 'spaghetti bolognese', 'chicken tikka masala').

    Returns:
        dict with estimated calories, protein, fat, and carbs.
    """
    return _get("/recipes/guessNutrition", {"title": title})


def compute_glycemic_load(ingredients: list) -> dict:
    """
    Compute the glycemic load of a list of ingredients.

    Args:
        ingredients: List of ingredient strings
                     (e.g. ['1 cup rice', '2 tbsp honey']).

    Returns:
        dict with glycemic index and glycemic load values.
    """
    try:
        key = _api_key()
    except ValueError as exc:
        return {"error": str(exc)}
    try:
        resp = requests.post(
            f"{BASE_URL}/food/ingredients/glycemicLoad",
            params={"apiKey": key},
            json={"ingredients": ingredients},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}
