"""
Spoonacular Recipes API tools.
Endpoints covered:
  - GET /recipes/complexSearch
  - GET /recipes/findByNutrients
  - GET /recipes/findByIngredients
  - GET /recipes/{id}/information
  - GET /recipes/informationBulk
  - GET /recipes/{id}/similar
  - GET /recipes/random
  - GET /recipes/autocomplete
  - GET /recipes/{id}/tasteWidget.json
  - GET /recipes/{id}/equipmentWidget.json
  - GET /recipes/{id}/priceBreakdownWidget.json
  - GET /recipes/{id}/ingredientWidget.json
  - GET /recipes/{id}/nutritionWidget.json
  - GET /recipes/{id}/analyzedInstructions
  - GET /recipes/extract
  - POST /recipes/analyze
  - GET /recipes/{id}/summary
  - POST /recipes/analyzeInstructions
  - POST /recipes/cuisine
  - GET /recipes/analyzeQuery
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


def _post(path: str, data: dict, params: dict | None = None) -> dict:
    if params is None:
        params = {}
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    data = {k: v for k, v in data.items() if v is not None}
    try:
        resp = requests.post(
            f"{BASE_URL}{path}",
            data=data,
            params=params,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ---------------------------------------------------------------------------
# Search Recipes (complex search)
# ---------------------------------------------------------------------------

def search_recipes(
    query: str,
    cuisine: Optional[str] = None,
    exclude_cuisine: Optional[str] = None,
    diet: Optional[str] = None,
    intolerances: Optional[str] = None,
    equipment: Optional[str] = None,
    include_ingredients: Optional[str] = None,
    exclude_ingredients: Optional[str] = None,
    type: Optional[str] = None,
    instructions_required: Optional[bool] = None,
    fill_ingredients: Optional[bool] = None,
    add_recipe_information: Optional[bool] = None,
    add_recipe_nutrition: Optional[bool] = None,
    max_ready_time: Optional[int] = None,
    min_servings: Optional[int] = None,
    max_servings: Optional[int] = None,
    sort: Optional[str] = None,
    sort_direction: Optional[str] = None,
    min_calories: Optional[float] = None,
    max_calories: Optional[float] = None,
    min_protein: Optional[float] = None,
    max_protein: Optional[float] = None,
    min_fat: Optional[float] = None,
    max_fat: Optional[float] = None,
    min_carbs: Optional[float] = None,
    max_carbs: Optional[float] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> dict:
    """Search recipes using advanced filtering and ranking (complex search)."""
    return _get("/recipes/complexSearch", {
        "query": query,
        "cuisine": cuisine,
        "excludeCuisine": exclude_cuisine,
        "diet": diet,
        "intolerances": intolerances,
        "equipment": equipment,
        "includeIngredients": include_ingredients,
        "excludeIngredients": exclude_ingredients,
        "type": type,
        "instructionsRequired": instructions_required,
        "fillIngredients": fill_ingredients,
        "addRecipeInformation": add_recipe_information,
        "addRecipeNutrition": add_recipe_nutrition,
        "maxReadyTime": max_ready_time,
        "minServings": min_servings,
        "maxServings": max_servings,
        "sort": sort,
        "sortDirection": sort_direction,
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


# ---------------------------------------------------------------------------
# Search Recipes by Nutrients
# ---------------------------------------------------------------------------

def search_recipes_by_nutrients(
    min_calories: Optional[float] = None,
    max_calories: Optional[float] = None,
    min_protein: Optional[float] = None,
    max_protein: Optional[float] = None,
    min_fat: Optional[float] = None,
    max_fat: Optional[float] = None,
    min_carbs: Optional[float] = None,
    max_carbs: Optional[float] = None,
    min_fiber: Optional[float] = None,
    max_fiber: Optional[float] = None,
    min_sugar: Optional[float] = None,
    max_sugar: Optional[float] = None,
    min_sodium: Optional[float] = None,
    max_sodium: Optional[float] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
    random: Optional[bool] = None,
) -> dict:
    """Find recipes that adhere to given nutritional limits."""
    return _get("/recipes/findByNutrients", {
        "minCalories": min_calories,
        "maxCalories": max_calories,
        "minProtein": min_protein,
        "maxProtein": max_protein,
        "minFat": min_fat,
        "maxFat": max_fat,
        "minCarbs": min_carbs,
        "maxCarbs": max_carbs,
        "minFiber": min_fiber,
        "maxFiber": max_fiber,
        "minSugar": min_sugar,
        "maxSugar": max_sugar,
        "minSodium": min_sodium,
        "maxSodium": max_sodium,
        "offset": offset,
        "number": number,
        "random": random,
    })


# ---------------------------------------------------------------------------
# Search Recipes by Ingredients
# ---------------------------------------------------------------------------

def search_recipes_by_ingredients(
    ingredients: str,
    number: Optional[int] = None,
    ranking: Optional[int] = None,
    ignore_pantry: Optional[bool] = None,
) -> dict:
    """Find recipes that use as many of the given ingredients as possible."""
    return _get("/recipes/findByIngredients", {
        "ingredients": ingredients,
        "number": number,
        "ranking": ranking,
        "ignorePantry": ignore_pantry,
    })


# ---------------------------------------------------------------------------
# Get Recipe Information
# ---------------------------------------------------------------------------

def get_recipe_information(
    recipe_id: int,
    include_nutrition: Optional[bool] = None,
    add_wine_pairing: Optional[bool] = None,
    add_taste_data: Optional[bool] = None,
) -> dict:
    """Get detailed information about a recipe by its ID."""
    return _get(f"/recipes/{recipe_id}/information", {
        "includeNutrition": include_nutrition,
        "addWinePairing": add_wine_pairing,
        "addTasteData": add_taste_data,
    })


# ---------------------------------------------------------------------------
# Get Recipe Information Bulk
# ---------------------------------------------------------------------------

def get_recipe_information_bulk(
    ids: str,
    include_nutrition: Optional[bool] = None,
) -> dict:
    """Get information about multiple recipes at once (comma-separated IDs)."""
    return _get("/recipes/informationBulk", {
        "ids": ids,
        "includeNutrition": include_nutrition,
    })


# ---------------------------------------------------------------------------
# Get Similar Recipes
# ---------------------------------------------------------------------------

def get_similar_recipes(
    recipe_id: int,
    number: Optional[int] = None,
) -> dict:
    """Find recipes similar to a given recipe."""
    return _get(f"/recipes/{recipe_id}/similar", {
        "number": number,
    })


# ---------------------------------------------------------------------------
# Get Random Recipes
# ---------------------------------------------------------------------------

def get_random_recipes(
    limit_license: Optional[bool] = None,
    tags: Optional[str] = None,
    number: Optional[int] = None,
) -> dict:
    """Get random (popular) recipes, optionally filtered by tags."""
    return _get("/recipes/random", {
        "limitLicense": limit_license,
        "tags": tags,
        "number": number,
    })


# ---------------------------------------------------------------------------
# Autocomplete Recipe Search
# ---------------------------------------------------------------------------

def autocomplete_recipe_search(
    query: str,
    number: Optional[int] = None,
) -> dict:
    """Autocomplete a partial recipe search query."""
    return _get("/recipes/autocomplete", {
        "query": query,
        "number": number,
    })


# ---------------------------------------------------------------------------
# Taste by ID
# ---------------------------------------------------------------------------

def get_recipe_taste_by_id(recipe_id: int, normalize: Optional[bool] = None) -> dict:
    """Get taste data for a recipe (sweetness, saltiness, sourness, etc.)."""
    return _get(f"/recipes/{recipe_id}/tasteWidget.json", {
        "normalize": normalize,
    })


# ---------------------------------------------------------------------------
# Equipment by ID
# ---------------------------------------------------------------------------

def get_recipe_equipment_by_id(recipe_id: int) -> dict:
    """Get the equipment needed to make a recipe."""
    return _get(f"/recipes/{recipe_id}/equipmentWidget.json", {})


# ---------------------------------------------------------------------------
# Price Breakdown by ID
# ---------------------------------------------------------------------------

def get_recipe_price_breakdown_by_id(recipe_id: int) -> dict:
    """Get the price breakdown of a recipe's ingredients."""
    return _get(f"/recipes/{recipe_id}/priceBreakdownWidget.json", {})


# ---------------------------------------------------------------------------
# Ingredients by ID
# ---------------------------------------------------------------------------

def get_recipe_ingredients_by_id(
    recipe_id: int,
    servings: Optional[int] = None,
) -> dict:
    """Get the ingredients for a recipe."""
    return _get(f"/recipes/{recipe_id}/ingredientWidget.json", {
        "servings": servings,
    })


# ---------------------------------------------------------------------------
# Nutrition by ID
# ---------------------------------------------------------------------------

def get_recipe_nutrition_by_id(recipe_id: int) -> dict:
    """Get the nutritional information for a recipe."""
    return _get(f"/recipes/{recipe_id}/nutritionWidget.json", {})


# ---------------------------------------------------------------------------
# Get Analyzed Recipe Instructions
# ---------------------------------------------------------------------------

def get_analyzed_recipe_instructions(
    recipe_id: int,
    step_breakdown: Optional[bool] = None,
) -> dict:
    """Get an analyzed breakdown of a recipe's instructions (steps, ingredients, equipment)."""
    return _get(f"/recipes/{recipe_id}/analyzedInstructions", {
        "stepBreakdown": step_breakdown,
    })


# ---------------------------------------------------------------------------
# Extract Recipe from Website
# ---------------------------------------------------------------------------

def extract_recipe_from_website(
    url: str,
    force_extraction: Optional[bool] = None,
    analyze: Optional[bool] = None,
    include_nutrition: Optional[bool] = None,
    include_taste: Optional[bool] = None,
) -> dict:
    """Extract recipe data (title, ingredients, instructions) from a website URL."""
    return _get("/recipes/extract", {
        "url": url,
        "forceExtraction": force_extraction,
        "analyze": analyze,
        "includeNutrition": include_nutrition,
        "includeTaste": include_taste,
    })


# ---------------------------------------------------------------------------
# Analyze Recipe
# ---------------------------------------------------------------------------

def analyze_recipe(
    title: str,
    servings: Optional[int] = None,
    ingredient_list: Optional[str] = None,
    language: Optional[str] = None,
    include_nutrition: Optional[bool] = None,
    include_taste: Optional[bool] = None,
) -> dict:
    """Send raw recipe information to get computed badges, diets, nutrition, and more."""
    return _post("/recipes/analyze", {
        "title": title,
        "servings": servings,
        "ingredientList": ingredient_list,
        "language": language,
        "includeNutrition": include_nutrition,
        "includeTaste": include_taste,
    })


# ---------------------------------------------------------------------------
# Summarize Recipe
# ---------------------------------------------------------------------------

def summarize_recipe(recipe_id: int) -> dict:
    """Get a short summary of a recipe."""
    return _get(f"/recipes/{recipe_id}/summary", {})


# ---------------------------------------------------------------------------
# Analyze Recipe Instructions
# ---------------------------------------------------------------------------

def analyze_recipe_instructions(instructions: str) -> dict:
    """Break down recipe instructions into atomic steps with ingredients and equipment."""
    return _post("/recipes/analyzeInstructions", {
        "instructions": instructions,
    })


# ---------------------------------------------------------------------------
# Classify Cuisine
# ---------------------------------------------------------------------------

def classify_cuisine(
    title: str,
    ingredient_list: Optional[str] = None,
    language: Optional[str] = None,
) -> dict:
    """Classify the cuisine of a recipe based on its title and ingredient list."""
    return _post("/recipes/cuisine", {
        "title": title,
        "ingredientList": ingredient_list,
        "language": language,
    })


# ---------------------------------------------------------------------------
# Analyze Recipe Search Query
# ---------------------------------------------------------------------------

def analyze_recipe_search_query(q: str) -> dict:
    """Parse and analyze a recipe search query to understand its intent."""
    return _get("/recipes/analyzeQuery", {
        "q": q,
    })
