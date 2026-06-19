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
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, params: dict, data: dict) -> dict:
    params["apiKey"] = _api_key()
    try:
        resp = requests.post(f"{BASE_URL}{path}", params=params, data=data, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_recipes(
    search_query: str,
    cuisine: Optional[str] = None,
    exclude_cuisine: Optional[str] = None,
    diet_type: Optional[str] = None,
    intolerances: Optional[str] = None,
    equipment: Optional[str] = None,
    ingredients: Optional[str] = None,
    exclude_ingredients: Optional[str] = None,
    type: Optional[str] = None,
    instructions_required: Optional[bool] = None,
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
    offset: int = 0,
    number: int = 10,
) -> dict:
    """Search through thousands of recipes using advanced filtering and ranking.
    Supports filtering by cuisine, diet, intolerances, ingredients, nutrients, and more."""
    params: dict = {"search_query": search_query, "offset": offset, "number": number}
    if cuisine is not None:
        params["cuisine"] = cuisine
    if exclude_cuisine is not None:
        params["excludeCuisine"] = exclude_cuisine
    if diet_type is not None:
        params["diet_type"] = diet_type
    if intolerances is not None:
        params["intolerances"] = intolerances
    if equipment is not None:
        params["equipment"] = equipment
    if ingredients is not None:
        params["ingredients"] = ingredients
    if exclude_ingredients is not None:
        params["excludeIngredients"] = exclude_ingredients
    if type is not None:
        params["type"] = type
    if instructions_required is not None:
        params["instructionsRequired"] = instructions_required
    if add_recipe_information is not None:
        params["addRecipeInformation"] = add_recipe_information
    if add_recipe_nutrition is not None:
        params["addRecipeNutrition"] = add_recipe_nutrition
    if max_ready_time is not None:
        params["maxReadyTime"] = max_ready_time
    if min_servings is not None:
        params["minServings"] = min_servings
    if max_servings is not None:
        params["maxServings"] = max_servings
    if sort is not None:
        params["sort"] = sort
    if sort_direction is not None:
        params["sortDirection"] = sort_direction
    if min_calories is not None:
        params["minCalories"] = min_calories
    if max_calories is not None:
        params["maxCalories"] = max_calories
    if min_protein is not None:
        params["minProtein"] = min_protein
    if max_protein is not None:
        params["maxProtein"] = max_protein
    if min_fat is not None:
        params["minFat"] = min_fat
    if max_fat is not None:
        params["maxFat"] = max_fat
    if min_carbs is not None:
        params["minCarbs"] = min_carbs
    if max_carbs is not None:
        params["maxCarbs"] = max_carbs
    return _get("/recipes/complexSearch", params)


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
    offset: int = 0,
    number: int = 10,
) -> dict:
    """Find recipes that adhere to given nutritional limits (calories, protein, fat, carbs, etc.)."""
    params: dict = {"offset": offset, "number": number}
    if min_calories is not None:
        params["minCalories"] = min_calories
    if max_calories is not None:
        params["maxCalories"] = max_calories
    if min_protein is not None:
        params["minProtein"] = min_protein
    if max_protein is not None:
        params["maxProtein"] = max_protein
    if min_fat is not None:
        params["minFat"] = min_fat
    if max_fat is not None:
        params["maxFat"] = max_fat
    if min_carbs is not None:
        params["minCarbs"] = min_carbs
    if max_carbs is not None:
        params["maxCarbs"] = max_carbs
    if min_fiber is not None:
        params["minFiber"] = min_fiber
    if max_fiber is not None:
        params["maxFiber"] = max_fiber
    if min_sugar is not None:
        params["minSugar"] = min_sugar
    if max_sugar is not None:
        params["maxSugar"] = max_sugar
    if min_sodium is not None:
        params["minSodium"] = min_sodium
    if max_sodium is not None:
        params["maxSodium"] = max_sodium
    return _get("/recipes/findByNutrients", params)


def search_recipes_by_ingredients(
    ingredients: str,
    number: int = 10,
    ranking: Optional[int] = None,
    ignore_pantry: Optional[bool] = None,
) -> dict:
    """Find recipes that use a given set of ingredients. Returns recipes with used/missed/unused ingredient info.
    ingredients: comma-separated list of ingredients (e.g. 'apples,flour,sugar').
    ranking: 1=maximize used ingredients, 2=minimize missing ingredients."""
    params: dict = {"ingredients": ingredients, "number": number}
    if ranking is not None:
        params["ranking"] = ranking
    if ignore_pantry is not None:
        params["ignorePantry"] = ignore_pantry
    return _get("/recipes/findByIngredients", params)


def get_recipe_information(
    recipe_id: int,
    include_nutrition: bool = False,
) -> dict:
    """Get detailed information about a recipe by its ID, including ingredients, instructions, and optionally nutrition."""
    params: dict = {"includeNutrition": include_nutrition}
    return _get(f"/recipes/{recipe_id}/information", params)


def get_recipe_information_bulk(
    ids: str,
    include_nutrition: bool = False,
) -> dict:
    """Get information about multiple recipes at once. ids: comma-separated list of recipe IDs."""
    params: dict = {"ids": ids, "includeNutrition": include_nutrition}
    return _get("/recipes/informationBulk", params)


def get_similar_recipes(
    recipe_id: int,
    number: int = 10,
) -> dict:
    """Find recipes similar to a given recipe by its ID."""
    params: dict = {"number": number}
    return _get(f"/recipes/{recipe_id}/similar", params)


def get_random_recipes(
    limit_license: Optional[bool] = None,
    tags: Optional[str] = None,
    number: int = 10,
) -> dict:
    """Get random recipes. Optionally filter by tags (e.g. 'vegetarian,dessert')."""
    params: dict = {"number": number}
    if limit_license is not None:
        params["limitLicense"] = limit_license
    if tags is not None:
        params["tags"] = tags
    return _get("/recipes/random", params)


def autocomplete_recipe_search(
    search_query: str,
    number: int = 10,
) -> dict:
    """Autocomplete a partial recipe search query. Returns recipe title suggestions."""
    params: dict = {"query": search_query, "number": number}
    return _get("/recipes/autocomplete", params)


def get_recipe_taste_by_id(recipe_id: int) -> dict:
    """Get taste data (sweetness, saltiness, sourness, bitterness, savoriness, fattiness, spiciness) for a recipe."""
    return _get(f"/recipes/{recipe_id}/tasteWidget.json", {})


def get_recipe_equipment_by_id(recipe_id: int) -> dict:
    """Get the equipment needed for a recipe by its ID."""
    return _get(f"/recipes/{recipe_id}/equipmentWidget.json", {})


def get_recipe_price_breakdown_by_id(recipe_id: int) -> dict:
    """Get the price breakdown of a recipe by its ID (cost per ingredient and total)."""
    return _get(f"/recipes/{recipe_id}/priceBreakdownWidget.json", {})


def get_recipe_ingredients_by_id(recipe_id: int) -> dict:
    """Get the ingredients for a recipe by its ID."""
    return _get(f"/recipes/{recipe_id}/ingredientWidget.json", {})


def get_recipe_nutrition_by_id(recipe_id: int) -> dict:
    """Get the full nutritional information for a recipe by its ID."""
    return _get(f"/recipes/{recipe_id}/nutritionWidget.json", {})


def get_analyzed_recipe_instructions(
    recipe_id: int,
    step_breakdown: Optional[bool] = None,
) -> dict:
    """Get an analyzed breakdown of a recipe's instructions (steps, ingredients, equipment)."""
    params: dict = {}
    if step_breakdown is not None:
        params["stepBreakdown"] = step_breakdown
    return _get(f"/recipes/{recipe_id}/analyzedInstructions", params)


def extract_recipe_from_website(
    url: str,
    force_extraction: Optional[bool] = None,
    analyze: Optional[bool] = None,
) -> dict:
    """Extract recipe data from any recipe website URL."""
    params: dict = {"url": url}
    if force_extraction is not None:
        params["forceExtraction"] = force_extraction
    if analyze is not None:
        params["analyze"] = analyze
    return _get("/recipes/extract", params)


def analyze_recipe(
    title: str,
    servings: Optional[int] = None,
    ingredient_list: Optional[str] = None,
    instructions: Optional[str] = None,
    language: Optional[str] = None,
) -> dict:
    """Analyze a recipe (title, ingredients, instructions) and return structured data including nutrition."""
    data: dict = {"title": title}
    if servings is not None:
        data["servings"] = servings
    if ingredient_list is not None:
        data["ingredientList"] = ingredient_list
    if instructions is not None:
        data["instructions"] = instructions
    if language is not None:
        data["language"] = language
    return _post("/recipes/analyze", {}, data)


def summarize_recipe(recipe_id: int) -> dict:
    """Get a short summary of a recipe by its ID."""
    return _get(f"/recipes/{recipe_id}/summary", {})


def analyze_recipe_instructions(instructions: str) -> dict:
    """Parse and analyze free-form recipe instructions text into structured steps with ingredients and equipment."""
    return _post("/recipes/analyzeInstructions", {}, {"instructions": instructions})


def classify_cuisine(
    title: str,
    ingredient_list: Optional[str] = None,
    language: Optional[str] = None,
) -> dict:
    """Classify the cuisine of a recipe given its title and optionally its ingredient list."""
    data: dict = {"title": title}
    if ingredient_list is not None:
        data["ingredientList"] = ingredient_list
    if language is not None:
        data["language"] = language
    return _post("/recipes/cuisine", {}, data)


def analyze_recipe_search_query(q: str) -> dict:
    """Analyze a recipe search query to understand its intent (e.g. dish type, cuisine, diet)."""
    return _get("/recipes/analyzeQuery", {"q": q})
