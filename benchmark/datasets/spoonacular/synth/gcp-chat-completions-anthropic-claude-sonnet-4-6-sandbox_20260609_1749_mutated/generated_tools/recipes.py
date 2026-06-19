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


def _get(path: str, params: dict) -> dict:
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, data: dict, params: dict = None) -> dict:
    p = params or {}
    p["apiKey"] = _api_key()
    try:
        resp = requests.post(f"{BASE_URL}{path}", data=data, params=p, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_recipes(
    query: str,
    cuisine: Optional[str] = None,
    exclude_cuisine: Optional[str] = None,
    diet: Optional[str] = None,
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
    """Search recipes using advanced filtering (complex search)."""
    params = {"query": query, "offset": offset, "number": number}
    if cuisine: params["cuisine"] = cuisine
    if exclude_cuisine: params["excludeCuisine"] = exclude_cuisine
    if diet: params["diet"] = diet
    if intolerances: params["intolerances"] = intolerances
    if equipment: params["equipment"] = equipment
    if ingredients: params["includeIngredients"] = ingredients
    if exclude_ingredients: params["excludeIngredients"] = exclude_ingredients
    if type: params["type"] = type
    if instructions_required is not None: params["instructionsRequired"] = instructions_required
    if add_recipe_information is not None: params["addRecipeInformation"] = add_recipe_information
    if add_recipe_nutrition is not None: params["addRecipeNutrition"] = add_recipe_nutrition
    if max_ready_time is not None: params["maxReadyTime"] = max_ready_time
    if min_servings is not None: params["minServings"] = min_servings
    if max_servings is not None: params["maxServings"] = max_servings
    if sort: params["sort"] = sort
    if sort_direction: params["sortDirection"] = sort_direction
    if min_calories is not None: params["minCalories"] = min_calories
    if max_calories is not None: params["maxCalories"] = max_calories
    if min_protein is not None: params["minProtein"] = min_protein
    if max_protein is not None: params["maxProtein"] = max_protein
    if min_fat is not None: params["minFat"] = min_fat
    if max_fat is not None: params["maxFat"] = max_fat
    if min_carbs is not None: params["minCarbs"] = min_carbs
    if max_carbs is not None: params["maxCarbs"] = max_carbs
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
) -> list:
    """Find recipes that adhere to given nutritional limits."""
    params: dict = {"offset": offset, "number": number}
    if min_calories is not None: params["minCalories"] = min_calories
    if max_calories is not None: params["maxCalories"] = max_calories
    if min_protein is not None: params["minProtein"] = min_protein
    if max_protein is not None: params["maxProtein"] = max_protein
    if min_fat is not None: params["minFat"] = min_fat
    if max_fat is not None: params["maxFat"] = max_fat
    if min_carbs is not None: params["minCarbs"] = min_carbs
    if max_carbs is not None: params["maxCarbs"] = max_carbs
    if min_fiber is not None: params["minFiber"] = min_fiber
    if max_fiber is not None: params["maxFiber"] = max_fiber
    if min_sugar is not None: params["minSugar"] = min_sugar
    if max_sugar is not None: params["maxSugar"] = max_sugar
    if min_sodium is not None: params["minSodium"] = min_sodium
    if max_sodium is not None: params["maxSodium"] = max_sodium
    return _get("/recipes/findByNutrients", params)


def search_recipes_by_ingredients(
    ingredients: str,
    number: int = 10,
    ranking: int = 1,
    ignore_pantry: bool = True,
) -> list:
    """Find recipes that use the given ingredients (what's-in-your-fridge style)."""
    params = {
        "ingredients": ingredients,
        "number": number,
        "ranking": ranking,
        "ignorePantry": ignore_pantry,
    }
    return _get("/recipes/findByIngredients", params)


def get_recipe_information(recipe_id: int, include_nutrition: bool = False) -> dict:
    """Get detailed information about a recipe by its ID."""
    params = {"includeNutrition": include_nutrition}
    return _get(f"/recipes/{recipe_id}/information", params)


def get_recipe_information_bulk(ids: str, include_nutrition: bool = False) -> list:
    """Get information about multiple recipes at once (comma-separated IDs)."""
    params = {"ids": ids, "includeNutrition": include_nutrition}
    return _get("/recipes/informationBulk", params)


def get_similar_recipes(recipe_id: int, number: int = 10) -> list:
    """Find recipes similar to the given recipe."""
    params = {"number": number}
    return _get(f"/recipes/{recipe_id}/similar", params)


def get_random_recipes(
    limit_license: bool = False,
    tags: Optional[str] = None,
    number: int = 10,
) -> dict:
    """Get random (popular) recipes, optionally filtered by tags."""
    params: dict = {"number": number, "limitLicense": limit_license}
    if tags: params["tags"] = tags
    return _get("/recipes/random", params)


def autocomplete_recipe_search(query: str, number: int = 10) -> list:
    """Autocomplete a partial recipe search query."""
    params = {"query": query, "number": number}
    return _get("/recipes/autocomplete", params)


def get_recipe_taste_by_id(recipe_id: int, normalize: bool = True) -> dict:
    """Get taste data (sweetness, saltiness, etc.) for a recipe by ID."""
    params = {"normalize": normalize}
    return _get(f"/recipes/{recipe_id}/tasteWidget.json", params)


def get_recipe_equipment_by_id(recipe_id: int) -> dict:
    """Get equipment used in a recipe by ID."""
    return _get(f"/recipes/{recipe_id}/equipmentWidget.json", {})


def get_recipe_price_breakdown_by_id(recipe_id: int) -> dict:
    """Get price breakdown for a recipe by ID."""
    return _get(f"/recipes/{recipe_id}/priceBreakdownWidget.json", {})


def get_recipe_ingredients_by_id(recipe_id: int) -> dict:
    """Get ingredients for a recipe by ID."""
    return _get(f"/recipes/{recipe_id}/ingredientWidget.json", {})


def get_recipe_nutrition_by_id(recipe_id: int) -> dict:
    """Get nutritional information for a recipe by ID."""
    return _get(f"/recipes/{recipe_id}/nutritionWidget.json", {})


def get_analyzed_recipe_instructions(recipe_id: int, step_breakdown: bool = False) -> list:
    """Get step-by-step analyzed instructions for a recipe."""
    params = {"stepBreakdown": step_breakdown}
    return _get(f"/recipes/{recipe_id}/analyzedInstructions", params)


def extract_recipe_from_website(url: str, analyze_instructions: bool = False, force_extraction: bool = False) -> dict:
    """Extract recipe data (title, ingredients, instructions) from a website URL."""
    params = {
        "url": url,
        "analyzeInstructions": analyze_instructions,
        "forceExtraction": force_extraction,
    }
    return _get("/recipes/extract", params)


def analyze_recipe(
    title: str,
    servings: Optional[str] = None,
    ingredient_list: Optional[str] = None,
    instructions: Optional[str] = None,
    language: str = "en",
) -> dict:
    """Analyze raw recipe information (title, ingredients, instructions) for nutrition, diets, etc."""
    data: dict = {"title": title, "language": language}
    if servings: data["servings"] = servings
    if ingredient_list: data["ingredientList"] = ingredient_list
    if instructions: data["instructions"] = instructions
    return _post("/recipes/analyze", data)


def summarize_recipe(recipe_id: int) -> dict:
    """Get a short summary of a recipe."""
    return _get(f"/recipes/{recipe_id}/summary", {})


def analyze_recipe_instructions(instructions: str) -> dict:
    """Break down recipe instructions into atomic steps with ingredients and equipment."""
    data = {"instructions": instructions}
    return _post("/recipes/analyzeInstructions", data)


def classify_cuisine(title: str, ingredient_list: str, language: str = "en") -> dict:
    """Classify the cuisine of a recipe given its title and ingredient list."""
    data = {"title": title, "ingredientList": ingredient_list, "language": language}
    return _post("/recipes/cuisine", data)


def analyze_recipe_search_query(q: str) -> dict:
    """Analyze a recipe search query to understand its intent and extract entities."""
    params = {"q": q}
    return _get("/recipes/queries/analyze", params)
