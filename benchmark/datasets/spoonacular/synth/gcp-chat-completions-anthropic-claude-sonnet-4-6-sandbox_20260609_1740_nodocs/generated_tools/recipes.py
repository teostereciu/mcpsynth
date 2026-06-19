"""
Spoonacular Recipe tools — search, details, ingredients, nutrition, instructions, similar.
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


# ---------------------------------------------------------------------------
# Recipe Search
# ---------------------------------------------------------------------------

def complex_recipe_search(
    query: str = "",
    cuisine: str = None,
    exclude_cuisine: str = None,
    diet: str = None,
    intolerances: str = None,
    equipment: str = None,
    include_ingredients: str = None,
    exclude_ingredients: str = None,
    type: str = None,
    instructions_required: bool = None,
    fill_ingredients: bool = None,
    add_recipe_information: bool = None,
    add_recipe_nutrition: bool = None,
    min_calories: float = None,
    max_calories: float = None,
    min_protein: float = None,
    max_protein: float = None,
    min_fat: float = None,
    max_fat: float = None,
    min_carbs: float = None,
    max_carbs: float = None,
    sort: str = None,
    sort_direction: str = None,
    offset: int = None,
    number: int = 10,
) -> dict:
    """
    Search recipes using Spoonacular's complex search endpoint with rich filtering
    options including cuisine, diet, intolerances, nutrients, and sorting.
    """
    params = {
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
        "minCalories": min_calories,
        "maxCalories": max_calories,
        "minProtein": min_protein,
        "maxProtein": max_protein,
        "minFat": min_fat,
        "maxFat": max_fat,
        "minCarbs": min_carbs,
        "maxCarbs": max_carbs,
        "sort": sort,
        "sortDirection": sort_direction,
        "offset": offset,
        "number": number,
    }
    return _get("/recipes/complexSearch", params)


def search_recipes_by_ingredients(
    ingredients: str,
    number: int = 10,
    ranking: int = None,
    ignore_pantry: bool = None,
) -> dict:
    """
    Find recipes that use a given set of ingredients. Provide a comma-separated
    list of ingredients (e.g. 'apples,flour,sugar').
    """
    params = {
        "ingredients": ingredients,
        "number": number,
        "ranking": ranking,
        "ignorePantry": ignore_pantry,
    }
    return _get("/recipes/findByIngredients", params)


def search_recipes_by_nutrients(
    min_calories: float = None,
    max_calories: float = None,
    min_protein: float = None,
    max_protein: float = None,
    min_fat: float = None,
    max_fat: float = None,
    min_carbs: float = None,
    max_carbs: float = None,
    min_fiber: float = None,
    max_fiber: float = None,
    min_sugar: float = None,
    max_sugar: float = None,
    number: int = 10,
    offset: int = None,
    random: bool = None,
) -> dict:
    """
    Search recipes by nutritional constraints such as calorie range, protein,
    fat, carbohydrates, fiber, and sugar.
    """
    params = {
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
        "number": number,
        "offset": offset,
        "random": random,
    }
    return _get("/recipes/findByNutrients", params)


def autocomplete_recipe_search(query: str, number: int = 10) -> list:
    """
    Autocomplete a partial recipe search query. Returns a list of suggested
    recipe titles matching the query prefix.
    """
    params = {"query": query, "number": number}
    return _get("/recipes/autocomplete", params)


# ---------------------------------------------------------------------------
# Recipe Information
# ---------------------------------------------------------------------------

def get_recipe_information(recipe_id: int, include_nutrition: bool = False) -> dict:
    """
    Get detailed information about a recipe by its Spoonacular ID, including
    ingredients, instructions, cuisine, diet labels, and optionally nutrition.
    """
    params = {"includeNutrition": include_nutrition}
    return _get(f"/recipes/{recipe_id}/information", params)


def get_recipe_information_bulk(ids: str, include_nutrition: bool = False) -> list:
    """
    Get information for multiple recipes at once. Provide a comma-separated
    string of recipe IDs (e.g. '715538,716429').
    """
    params = {"ids": ids, "includeNutrition": include_nutrition}
    return _get("/recipes/informationBulk", params)


def get_recipe_ingredients(recipe_id: int) -> dict:
    """
    Get the ingredient list for a recipe by its ID, including amounts and units.
    """
    return _get(f"/recipes/{recipe_id}/ingredientWidget.json", {})


def get_recipe_nutrition(recipe_id: int) -> dict:
    """
    Get the full nutritional information for a recipe by its ID, including
    macros, vitamins, and minerals.
    """
    return _get(f"/recipes/{recipe_id}/nutritionWidget.json", {})


def get_recipe_instructions(recipe_id: int, step_breakdown: bool = None) -> dict:
    """
    Get step-by-step cooking instructions for a recipe by its ID.
    Optionally break steps into sub-steps.
    """
    params = {"stepBreakdown": step_breakdown}
    return _get(f"/recipes/{recipe_id}/analyzedInstructions", params)


def get_similar_recipes(recipe_id: int, number: int = 10) -> list:
    """
    Find recipes similar to a given recipe ID. Returns a list of similar
    recipe summaries.
    """
    params = {"number": number}
    return _get(f"/recipes/{recipe_id}/similar", params)


def get_random_recipes(
    tags: str = None,
    number: int = 10,
    include_nutrition: bool = False,
) -> dict:
    """
    Get a set of random recipes, optionally filtered by tags such as
    'vegetarian', 'dessert', etc.
    """
    params = {"tags": tags, "number": number, "includeNutrition": include_nutrition}
    return _get("/recipes/random", params)


def summarize_recipe(recipe_id: int) -> dict:
    """
    Get a short text summary of a recipe by its ID.
    """
    return _get(f"/recipes/{recipe_id}/summary", {})


def get_recipe_taste(recipe_id: int, normalize: bool = None) -> dict:
    """
    Get the taste profile (sweetness, saltiness, sourness, bitterness,
    savoriness, fattiness, spiciness) for a recipe by its ID.
    """
    params = {"normalize": normalize}
    return _get(f"/recipes/{recipe_id}/tasteWidget.json", params)


def analyze_recipe_instructions(instructions: str) -> dict:
    """
    Parse and analyze a block of free-text recipe instructions into structured
    steps with ingredients and equipment.
    """
    try:
        api_key = _api_key()
        resp = requests.post(
            f"{BASE_URL}/recipes/analyzeInstructions",
            params={"apiKey": api_key},
            data={"instructions": instructions},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def guess_nutrition_by_dish_name(title: str) -> dict:
    """
    Estimate the nutrition of a dish given only its name/title, without a
    full recipe.
    """
    params = {"title": title}
    return _get("/recipes/guessNutrition", params)


def classify_cuisine(title: str, ingredient_list: str = None) -> dict:
    """
    Classify the cuisine of a recipe given its title and optionally a
    newline-separated ingredient list.
    """
    try:
        api_key = _api_key()
        data = {"title": title}
        if ingredient_list:
            data["ingredientList"] = ingredient_list
        resp = requests.post(
            f"{BASE_URL}/recipes/cuisine",
            params={"apiKey": api_key},
            data=data,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}
