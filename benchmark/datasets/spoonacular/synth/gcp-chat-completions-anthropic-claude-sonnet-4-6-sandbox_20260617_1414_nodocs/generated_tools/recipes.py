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
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


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

    Args:
        query: Natural-language search query (e.g. 'pasta carbonara').
        cuisine: Comma-separated cuisines to include (e.g. 'italian,mexican').
        exclude_cuisine: Comma-separated cuisines to exclude.
        diet: Diet label (e.g. 'vegetarian', 'vegan', 'gluten free', 'ketogenic').
        intolerances: Comma-separated intolerances (e.g. 'gluten,dairy').
        equipment: Comma-separated equipment needed (e.g. 'pan,oven').
        include_ingredients: Comma-separated ingredients that must be included.
        exclude_ingredients: Comma-separated ingredients to exclude.
        type: Meal type (e.g. 'main course', 'dessert', 'breakfast').
        instructions_required: Only return recipes with instructions when True.
        fill_ingredients: Add ingredient information to each recipe result.
        add_recipe_information: Add full recipe information to each result.
        add_recipe_nutrition: Add nutrition information to each result.
        min_calories: Minimum calories per serving.
        max_calories: Maximum calories per serving.
        min_protein: Minimum protein (g) per serving.
        max_protein: Maximum protein (g) per serving.
        min_fat: Minimum fat (g) per serving.
        max_fat: Maximum fat (g) per serving.
        min_carbs: Minimum carbohydrates (g) per serving.
        max_carbs: Maximum carbohydrates (g) per serving.
        sort: Sort results by (e.g. 'calories', 'time', 'popularity', 'healthiness').
        sort_direction: 'asc' or 'desc'.
        offset: Number of results to skip (for pagination).
        number: Number of results to return (default 10, max 100).

    Returns:
        dict with 'results' list and 'totalResults' count.
    """
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
    })


def search_recipes_by_ingredients(
    ingredients: str,
    number: int = 10,
    ranking: int = 1,
    ignore_pantry: bool = True,
) -> list:
    """
    Find recipes that use a given set of ingredients. Useful for 'what can I cook
    with what I have' scenarios.

    Args:
        ingredients: Comma-separated list of ingredients (e.g. 'apples,flour,sugar').
        number: Maximum number of recipes to return (default 10).
        ranking: 1 = maximize used ingredients, 2 = minimize missing ingredients.
        ignore_pantry: Ignore typical pantry items like water, salt, flour when True.

    Returns:
        List of recipe objects with usedIngredients and missedIngredients.
    """
    return _get("/recipes/findByIngredients", {
        "ingredients": ingredients,
        "number": number,
        "ranking": ranking,
        "ignorePantry": ignore_pantry,
    })


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
    random: bool = False,
) -> list:
    """
    Search recipes by nutrient ranges. All nutrient values are per serving.

    Args:
        min_calories: Minimum calories per serving.
        max_calories: Maximum calories per serving.
        min_protein: Minimum protein in grams.
        max_protein: Maximum protein in grams.
        min_fat: Minimum fat in grams.
        max_fat: Maximum fat in grams.
        min_carbs: Minimum carbohydrates in grams.
        max_carbs: Maximum carbohydrates in grams.
        min_fiber: Minimum fiber in grams.
        max_fiber: Maximum fiber in grams.
        min_sugar: Minimum sugar in grams.
        max_sugar: Maximum sugar in grams.
        number: Number of results (default 10).
        offset: Offset for pagination.
        random: Return random results within the constraints when True.

    Returns:
        List of recipe objects matching the nutrient constraints.
    """
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
        "number": number,
        "offset": offset,
        "random": random,
    })


def autocomplete_recipe_search(query: str, number: int = 10) -> list:
    """
    Autocomplete a partial recipe search query. Useful for building search UIs
    or suggesting recipe names as the user types.

    Args:
        query: Partial recipe name to autocomplete (e.g. 'chick').
        number: Number of suggestions to return (default 10, max 25).

    Returns:
        List of autocomplete suggestion objects with 'id' and 'title'.
    """
    return _get("/recipes/autocomplete", {"query": query, "number": number})


# ---------------------------------------------------------------------------
# Recipe Information
# ---------------------------------------------------------------------------

def get_recipe_information(recipe_id: int, include_nutrition: bool = False) -> dict:
    """
    Get full information about a recipe by its Spoonacular ID, including
    ingredients, instructions, servings, cooking time, and more.

    Args:
        recipe_id: Spoonacular recipe ID.
        include_nutrition: Include detailed nutrition data when True.

    Returns:
        dict with complete recipe information.
    """
    return _get(f"/recipes/{recipe_id}/information", {
        "includeNutrition": include_nutrition,
    })


def get_recipe_information_bulk(ids: str, include_nutrition: bool = False) -> list:
    """
    Get information for multiple recipes in a single request.

    Args:
        ids: Comma-separated list of recipe IDs (e.g. '715538,716429').
        include_nutrition: Include nutrition data for each recipe when True.

    Returns:
        List of recipe information dicts.
    """
    return _get("/recipes/informationBulk", {
        "ids": ids,
        "includeNutrition": include_nutrition,
    })


def get_recipe_ingredients(recipe_id: int) -> dict:
    """
    Get the ingredient list for a recipe, including amounts and units.

    Args:
        recipe_id: Spoonacular recipe ID.

    Returns:
        dict with 'ingredients' list containing name, amount, and unit.
    """
    return _get(f"/recipes/{recipe_id}/ingredientWidget.json", {})


def get_recipe_nutrition(recipe_id: int) -> dict:
    """
    Get detailed nutrition information for a recipe, including macros and
    a full breakdown of vitamins and minerals.

    Args:
        recipe_id: Spoonacular recipe ID.

    Returns:
        dict with calories, macronutrients, and micronutrient breakdown.
    """
    return _get(f"/recipes/{recipe_id}/nutritionWidget.json", {})


def get_recipe_instructions(recipe_id: int, step_breakdown: bool = True) -> list:
    """
    Get step-by-step cooking instructions for a recipe.

    Args:
        recipe_id: Spoonacular recipe ID.
        step_breakdown: Break instructions into individual steps when True.

    Returns:
        List of instruction blocks, each with a list of steps.
    """
    return _get(f"/recipes/{recipe_id}/analyzedInstructions", {
        "stepBreakdown": step_breakdown,
    })


def get_similar_recipes(recipe_id: int, number: int = 10) -> list:
    """
    Find recipes similar to a given recipe.

    Args:
        recipe_id: Spoonacular recipe ID to find similar recipes for.
        number: Number of similar recipes to return (default 10).

    Returns:
        List of similar recipe objects with id, title, and readyInMinutes.
    """
    return _get(f"/recipes/{recipe_id}/similar", {"number": number})


def get_random_recipes(
    tags: str = None,
    number: int = 10,
    include_nutrition: bool = False,
) -> dict:
    """
    Get a set of random recipes, optionally filtered by tags.

    Args:
        tags: Comma-separated tags to filter by (e.g. 'vegetarian,dessert').
        number: Number of random recipes to return (default 10).
        include_nutrition: Include nutrition data when True.

    Returns:
        dict with 'recipes' list of random recipe objects.
    """
    return _get("/recipes/random", {
        "tags": tags,
        "number": number,
        "includeNutrition": include_nutrition,
    })


def summarize_recipe(recipe_id: int) -> dict:
    """
    Get a short summary/description of a recipe.

    Args:
        recipe_id: Spoonacular recipe ID.

    Returns:
        dict with 'id', 'title', and 'summary' (HTML string).
    """
    return _get(f"/recipes/{recipe_id}/summary", {})


def analyze_recipe_instructions(instructions: str) -> list:
    """
    Parse and analyze a block of free-text recipe instructions into structured steps.

    Args:
        instructions: Raw instruction text to parse.

    Returns:
        List of parsed instruction steps with ingredients and equipment.
    """
    try:
        key = _api_key()
    except ValueError as exc:
        return [{"error": str(exc)}]
    try:
        resp = requests.post(
            f"{BASE_URL}/recipes/analyzeInstructions",
            params={"apiKey": key},
            data={"instructions": instructions},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return [{"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}]
    except Exception as exc:
        return [{"error": str(exc)}]


def get_recipe_price_breakdown(recipe_id: int) -> dict:
    """
    Get the estimated price breakdown per ingredient for a recipe.

    Args:
        recipe_id: Spoonacular recipe ID.

    Returns:
        dict with ingredient costs and total estimated cost in cents.
    """
    return _get(f"/recipes/{recipe_id}/priceBreakdownWidget.json", {})


def get_recipe_taste(recipe_id: int, normalize: bool = True) -> dict:
    """
    Get the taste profile of a recipe (sweetness, saltiness, sourness, etc.).

    Args:
        recipe_id: Spoonacular recipe ID.
        normalize: Normalize taste values to a 0-100 scale when True.

    Returns:
        dict with taste dimension scores.
    """
    return _get(f"/recipes/{recipe_id}/tasteWidget.json", {"normalize": normalize})
