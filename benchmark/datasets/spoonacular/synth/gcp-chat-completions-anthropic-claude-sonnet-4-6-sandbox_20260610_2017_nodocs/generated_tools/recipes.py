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


# ---------------------------------------------------------------------------
# Recipe Search
# ---------------------------------------------------------------------------

def complex_recipe_search(
    query: str = "",
    cuisine: str = "",
    diet: str = "",
    intolerances: str = "",
    include_ingredients: str = "",
    exclude_ingredients: str = "",
    type: str = "",
    max_ready_time: int = 0,
    min_calories: float = 0,
    max_calories: float = 0,
    min_protein: float = 0,
    max_protein: float = 0,
    min_fat: float = 0,
    max_fat: float = 0,
    min_carbs: float = 0,
    max_carbs: float = 0,
    sort: str = "",
    sort_direction: str = "",
    offset: int = 0,
    number: int = 10,
    add_recipe_nutrition: bool = False,
    add_recipe_information: bool = False,
) -> dict:
    """
    Search recipes using a complex set of filters including query text, cuisine,
    diet, intolerances, included/excluded ingredients, meal type, ready time,
    macronutrient ranges, and sorting options.

    Args:
        query: Free-text search query (e.g. "pasta").
        cuisine: Comma-separated cuisines (e.g. "italian,mexican").
        diet: Diet label (e.g. "vegetarian", "vegan", "gluten free").
        intolerances: Comma-separated intolerances (e.g. "dairy,egg").
        include_ingredients: Comma-separated ingredients that must be included.
        exclude_ingredients: Comma-separated ingredients to exclude.
        type: Meal type (e.g. "main course", "dessert", "breakfast").
        max_ready_time: Maximum ready time in minutes.
        min_calories: Minimum calories per serving.
        max_calories: Maximum calories per serving.
        min_protein: Minimum protein (g) per serving.
        max_protein: Maximum protein (g) per serving.
        min_fat: Minimum fat (g) per serving.
        max_fat: Maximum fat (g) per serving.
        min_carbs: Minimum carbohydrates (g) per serving.
        max_carbs: Maximum carbohydrates (g) per serving.
        sort: Sort field (e.g. "calories", "time", "popularity", "healthiness").
        sort_direction: "asc" or "desc".
        offset: Number of results to skip (for pagination).
        number: Number of results to return (max 100).
        add_recipe_nutrition: Include nutrition data in results.
        add_recipe_information: Include full recipe information in results.

    Returns:
        dict with 'results' list and 'totalResults' count.
    """
    params: dict = {"number": number, "offset": offset}
    if query:
        params["query"] = query
    if cuisine:
        params["cuisine"] = cuisine
    if diet:
        params["diet"] = diet
    if intolerances:
        params["intolerances"] = intolerances
    if include_ingredients:
        params["includeIngredients"] = include_ingredients
    if exclude_ingredients:
        params["excludeIngredients"] = exclude_ingredients
    if type:
        params["type"] = type
    if max_ready_time > 0:
        params["maxReadyTime"] = max_ready_time
    if min_calories > 0:
        params["minCalories"] = min_calories
    if max_calories > 0:
        params["maxCalories"] = max_calories
    if min_protein > 0:
        params["minProtein"] = min_protein
    if max_protein > 0:
        params["maxProtein"] = max_protein
    if min_fat > 0:
        params["minFat"] = min_fat
    if max_fat > 0:
        params["maxFat"] = max_fat
    if min_carbs > 0:
        params["minCarbs"] = min_carbs
    if max_carbs > 0:
        params["maxCarbs"] = max_carbs
    if sort:
        params["sort"] = sort
    if sort_direction:
        params["sortDirection"] = sort_direction
    if add_recipe_nutrition:
        params["addRecipeNutrition"] = True
    if add_recipe_information:
        params["addRecipeInformation"] = True
    return _get("/recipes/complexSearch", params)


def search_recipes_by_ingredients(
    ingredients: str,
    number: int = 10,
    ranking: int = 1,
    ignore_pantry: bool = True,
) -> list:
    """
    Find recipes that use a given set of ingredients. Useful for 'what can I cook
    with what I have?' queries.

    Args:
        ingredients: Comma-separated list of ingredients (e.g. "apples,flour,sugar").
        number: Number of recipes to return (max 100).
        ranking: 1 = maximize used ingredients, 2 = minimize missing ingredients.
        ignore_pantry: Whether to ignore typical pantry items (salt, water, etc.).

    Returns:
        List of recipe objects with usedIngredients and missedIngredients.
    """
    params = {
        "ingredients": ingredients,
        "number": number,
        "ranking": ranking,
        "ignorePantry": ignore_pantry,
    }
    return _get("/recipes/findByIngredients", params)


def search_recipes_by_nutrients(
    min_calories: float = 0,
    max_calories: float = 0,
    min_protein: float = 0,
    max_protein: float = 0,
    min_fat: float = 0,
    max_fat: float = 0,
    min_carbs: float = 0,
    max_carbs: float = 0,
    min_fiber: float = 0,
    max_fiber: float = 0,
    min_sugar: float = 0,
    max_sugar: float = 0,
    number: int = 10,
    offset: int = 0,
    random: bool = False,
) -> list:
    """
    Search recipes by nutrient ranges (calories, protein, fat, carbs, fiber, sugar).

    Args:
        min_calories / max_calories: Calorie range per serving.
        min_protein / max_protein: Protein (g) range per serving.
        min_fat / max_fat: Fat (g) range per serving.
        min_carbs / max_carbs: Carbohydrate (g) range per serving.
        min_fiber / max_fiber: Fiber (g) range per serving.
        min_sugar / max_sugar: Sugar (g) range per serving.
        number: Number of results (max 100).
        offset: Pagination offset.
        random: Return random results within the constraints.

    Returns:
        List of recipe objects matching the nutrient constraints.
    """
    params: dict = {"number": number, "offset": offset}
    for name, val in [
        ("minCalories", min_calories), ("maxCalories", max_calories),
        ("minProtein", min_protein), ("maxProtein", max_protein),
        ("minFat", min_fat), ("maxFat", max_fat),
        ("minCarbs", min_carbs), ("maxCarbs", max_carbs),
        ("minFiber", min_fiber), ("maxFiber", max_fiber),
        ("minSugar", min_sugar), ("maxSugar", max_sugar),
    ]:
        if val > 0:
            params[name] = val
    if random:
        params["random"] = True
    return _get("/recipes/findByNutrients", params)


def autocomplete_recipe_search(query: str, number: int = 10) -> list:
    """
    Autocomplete a partial recipe name query. Useful for search-as-you-type UIs.

    Args:
        query: Partial recipe name to autocomplete.
        number: Number of suggestions to return (max 25).

    Returns:
        List of autocomplete suggestion objects with id and title.
    """
    return _get("/recipes/autocomplete", {"query": query, "number": number})


# ---------------------------------------------------------------------------
# Recipe Information
# ---------------------------------------------------------------------------

def get_recipe_information(recipe_id: int, include_nutrition: bool = False) -> dict:
    """
    Get full information about a recipe by its Spoonacular ID, including
    ingredients, instructions, servings, ready time, and optionally nutrition.

    Args:
        recipe_id: Spoonacular recipe ID.
        include_nutrition: Whether to include full nutrition data.

    Returns:
        dict with complete recipe details.
    """
    params = {"includeNutrition": include_nutrition}
    return _get(f"/recipes/{recipe_id}/information", params)


def get_recipe_information_bulk(ids: str, include_nutrition: bool = False) -> list:
    """
    Get information for multiple recipes at once.

    Args:
        ids: Comma-separated list of recipe IDs (e.g. "715538,716429").
        include_nutrition: Whether to include nutrition data.

    Returns:
        List of recipe information dicts.
    """
    params = {"ids": ids, "includeNutrition": include_nutrition}
    return _get("/recipes/informationBulk", params)


def get_recipe_ingredients(recipe_id: int) -> dict:
    """
    Get the ingredient list for a recipe, including amounts and units.

    Args:
        recipe_id: Spoonacular recipe ID.

    Returns:
        dict with 'ingredients' list.
    """
    return _get(f"/recipes/{recipe_id}/ingredientWidget.json", {})


def get_recipe_nutrition(recipe_id: int) -> dict:
    """
    Get detailed nutrition information for a recipe by ID.

    Args:
        recipe_id: Spoonacular recipe ID.

    Returns:
        dict with calories, macros, and full nutrient breakdown.
    """
    return _get(f"/recipes/{recipe_id}/nutritionWidget.json", {})


def get_recipe_instructions(recipe_id: int, step_breakdown: bool = True) -> list:
    """
    Get step-by-step cooking instructions for a recipe.

    Args:
        recipe_id: Spoonacular recipe ID.
        step_breakdown: Whether to break instructions into individual steps.

    Returns:
        List of instruction blocks, each with steps.
    """
    params = {"stepBreakdown": step_breakdown}
    return _get(f"/recipes/{recipe_id}/analyzedInstructions", params)


def get_similar_recipes(recipe_id: int, number: int = 10) -> list:
    """
    Find recipes similar to a given recipe.

    Args:
        recipe_id: Spoonacular recipe ID.
        number: Number of similar recipes to return.

    Returns:
        List of similar recipe objects.
    """
    return _get(f"/recipes/{recipe_id}/similar", {"number": number})


def get_random_recipes(
    tags: str = "",
    number: int = 1,
    include_nutrition: bool = False,
) -> dict:
    """
    Get one or more random recipes, optionally filtered by tags.

    Args:
        tags: Comma-separated tags to filter by (e.g. "vegetarian,dessert").
        number: Number of random recipes to return.
        include_nutrition: Whether to include nutrition data.

    Returns:
        dict with 'recipes' list.
    """
    params: dict = {"number": number, "includeNutrition": include_nutrition}
    if tags:
        params["tags"] = tags
    return _get("/recipes/random", params)


def summarize_recipe(recipe_id: int) -> dict:
    """
    Get a short text summary of a recipe.

    Args:
        recipe_id: Spoonacular recipe ID.

    Returns:
        dict with 'id', 'title', and 'summary' (HTML string).
    """
    return _get(f"/recipes/{recipe_id}/summary", {})


def analyze_recipe_instructions(instructions: str) -> dict:
    """
    Parse and analyze free-text recipe instructions into structured steps.

    Args:
        instructions: Raw recipe instructions as plain text.

    Returns:
        dict with parsed steps and identified ingredients/equipment.
    """
    key = _api_key()
    url = f"{BASE_URL}/recipes/analyzeInstructions"
    try:
        resp = requests.post(
            url,
            params={"apiKey": key},
            data={"instructions": instructions},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def guess_nutrition_by_dish_name(title: str) -> dict:
    """
    Estimate the nutrition of a dish just from its name (no recipe needed).

    Args:
        title: Name of the dish (e.g. "Spaghetti Bolognese").

    Returns:
        dict with estimated calories, fat, protein, carbs.
    """
    return _get("/recipes/guessNutrition", {"title": title})


def get_recipe_price_breakdown(recipe_id: int) -> dict:
    """
    Get the estimated cost per serving and per ingredient for a recipe.

    Args:
        recipe_id: Spoonacular recipe ID.

    Returns:
        dict with ingredient costs and total estimated price.
    """
    return _get(f"/recipes/{recipe_id}/priceBreakdownWidget.json", {})
