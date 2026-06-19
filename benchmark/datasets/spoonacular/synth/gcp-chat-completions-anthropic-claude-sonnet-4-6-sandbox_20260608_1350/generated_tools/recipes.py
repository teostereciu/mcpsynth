"""Spoonacular Recipes API tools."""
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


def _post(path: str, params: dict, data: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    data = {k: v for k, v in data.items() if v is not None}
    try:
        r = requests.post(f"{BASE_URL}{path}", params=params, data=data, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def search_recipes(
    query: Optional[str] = None,
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
    """Search through thousands of recipes using advanced filtering and ranking.
    Supports filtering by query, cuisine, diet, intolerances, nutrients, and more."""
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
) -> list:
    """Find recipes that adhere to given nutritional limits (calories, protein, fat, carbs, etc.)."""
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


def search_recipes_by_ingredients(
    ingredients: str,
    number: Optional[int] = None,
    ranking: Optional[int] = None,
    ignore_pantry: Optional[bool] = None,
) -> list:
    """Find recipes that use as many of the given ingredients as possible.
    ingredients: comma-separated list of ingredients (e.g. 'apples,flour,sugar').
    ranking: 1=maximize used ingredients, 2=minimize missing ingredients."""
    return _get("/recipes/findByIngredients", {
        "ingredients": ingredients,
        "number": number,
        "ranking": ranking,
        "ignorePantry": ignore_pantry,
    })


def get_recipe_information(
    recipe_id: int,
    include_nutrition: Optional[bool] = None,
    add_wine_pairing: Optional[bool] = None,
    add_taste_data: Optional[bool] = None,
) -> dict:
    """Get detailed information about a recipe by its ID, including ingredients, instructions, and nutrition."""
    return _get(f"/recipes/{recipe_id}/information", {
        "includeNutrition": include_nutrition,
        "addWinePairing": add_wine_pairing,
        "addTasteData": add_taste_data,
    })


def get_recipe_information_bulk(
    ids: str,
    include_nutrition: Optional[bool] = None,
) -> list:
    """Get information about multiple recipes at once.
    ids: comma-separated list of recipe IDs."""
    return _get("/recipes/informationBulk", {
        "ids": ids,
        "includeNutrition": include_nutrition,
    })


def get_similar_recipes(
    recipe_id: int,
    number: Optional[int] = None,
) -> list:
    """Find recipes similar to the given recipe ID."""
    return _get(f"/recipes/{recipe_id}/similar", {
        "number": number,
    })


def get_random_recipes(
    limit_license: Optional[bool] = None,
    include_tags: Optional[str] = None,
    exclude_tags: Optional[str] = None,
    number: Optional[int] = None,
) -> dict:
    """Get random (popular) recipes. Optionally filter by tags."""
    return _get("/recipes/random", {
        "limitLicense": limit_license,
        "include-tags": include_tags,
        "exclude-tags": exclude_tags,
        "number": number,
    })


def autocomplete_recipe_search(
    query: str,
    number: Optional[int] = None,
) -> list:
    """Autocomplete a partial recipe search query."""
    return _get("/recipes/autocomplete", {
        "query": query,
        "number": number,
    })


def get_recipe_taste_by_id(
    recipe_id: int,
    normalize: Optional[bool] = None,
) -> dict:
    """Get taste data (sweetness, saltiness, sourness, bitterness, savoriness, fattiness, spiciness) for a recipe."""
    return _get(f"/recipes/{recipe_id}/tasteWidget.json", {
        "normalize": normalize,
    })


def get_recipe_equipment_by_id(recipe_id: int) -> dict:
    """Get the equipment needed for a recipe by its ID."""
    return _get(f"/recipes/{recipe_id}/equipmentWidget.json", {})


def get_recipe_price_breakdown_by_id(recipe_id: int) -> dict:
    """Get the price breakdown of a recipe by its ID."""
    return _get(f"/recipes/{recipe_id}/priceBreakdownWidget.json", {})


def get_recipe_ingredients_by_id(recipe_id: int) -> dict:
    """Get the ingredients for a recipe by its ID."""
    return _get(f"/recipes/{recipe_id}/ingredientWidget.json", {})


def get_recipe_nutrition_by_id(recipe_id: int) -> dict:
    """Get the nutritional information for a recipe by its ID."""
    return _get(f"/recipes/{recipe_id}/nutritionWidget.json", {})


def get_analyzed_recipe_instructions(
    recipe_id: int,
    step_breakdown: Optional[bool] = None,
) -> list:
    """Get an analyzed breakdown of a recipe's instructions, including ingredients and equipment per step."""
    return _get(f"/recipes/{recipe_id}/analyzedInstructions", {
        "stepBreakdown": step_breakdown,
    })


def extract_recipe_from_website(
    url: str,
    force_extraction: Optional[bool] = None,
    analyze: Optional[bool] = None,
    include_nutrition: Optional[bool] = None,
    include_taste: Optional[bool] = None,
) -> dict:
    """Extract recipe data (title, ingredients, instructions) from any properly formatted website URL."""
    return _get("/recipes/extract", {
        "url": url,
        "forceExtraction": force_extraction,
        "analyze": analyze,
        "includeNutrition": include_nutrition,
        "includeTaste": include_taste,
    })


def analyze_recipe(
    title: str,
    servings: Optional[str] = None,
    ingredients: Optional[str] = None,
    instructions: Optional[str] = None,
    language: Optional[str] = None,
    include_nutrition: Optional[bool] = None,
    include_taste: Optional[bool] = None,
) -> dict:
    """Send raw recipe information (title, servings, ingredients) to get computed badges, diets, and nutrition."""
    return _post("/recipes/analyze", {
        "language": language,
        "includeNutrition": include_nutrition,
        "includeTaste": include_taste,
    }, {
        "title": title,
        "servings": servings,
        "ingredients": ingredients,
        "instructions": instructions,
    })


def summarize_recipe(recipe_id: int) -> dict:
    """Get a short summary of a recipe."""
    return _get(f"/recipes/{recipe_id}/summary", {})


def analyze_recipe_instructions(instructions: str) -> list:
    """Break down recipe instructions into atomic steps with ingredients and equipment per step."""
    return _post("/recipes/analyzeInstructions", {}, {
        "instructions": instructions,
    })


def classify_cuisine(
    title: str,
    ingredient_list: Optional[str] = None,
    language: Optional[str] = None,
) -> dict:
    """Classify the cuisine of a recipe based on its title and ingredient list."""
    return _post("/recipes/cuisine", {
        "language": language,
    }, {
        "title": title,
        "ingredientList": ingredient_list,
    })


def analyze_recipe_search_query(q: str) -> dict:
    """Analyze a recipe search query to understand its intent (ingredients, cuisine, diet, etc.)."""
    return _get("/recipes/queries/analyze", {"q": q})
