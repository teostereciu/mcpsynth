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
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# Complex search
# ---------------------------------------------------------------------------

def complex_search_recipes(
    query: str = "",
    cuisine: str = "",
    diet: str = "",
    intolerances: str = "",
    include_ingredients: str = "",
    exclude_ingredients: str = "",
    type: str = "",
    max_ready_time: int = None,
    min_calories: float = None,
    max_calories: float = None,
    min_protein: float = None,
    max_protein: float = None,
    min_fat: float = None,
    max_fat: float = None,
    min_carbs: float = None,
    max_carbs: float = None,
    sort: str = "",
    sort_direction: str = "",
    offset: int = 0,
    number: int = 10,
    add_recipe_nutrition: bool = False,
    add_recipe_information: bool = False,
) -> dict:
    """
    Search recipes using Spoonacular's complex search endpoint with rich filtering
    options including cuisine, diet, intolerances, ingredients, nutrients, and sorting.

    Args:
        query: Natural-language search query (e.g. 'pasta carbonara').
        cuisine: Comma-separated cuisines (e.g. 'italian,mexican').
        diet: Diet label (e.g. 'vegetarian', 'vegan', 'gluten free', 'ketogenic').
        intolerances: Comma-separated intolerances (e.g. 'gluten,dairy').
        include_ingredients: Comma-separated ingredients that must be included.
        exclude_ingredients: Comma-separated ingredients to exclude.
        type: Meal type (e.g. 'main course', 'dessert', 'breakfast').
        max_ready_time: Maximum preparation + cooking time in minutes.
        min_calories: Minimum calories per serving.
        max_calories: Maximum calories per serving.
        min_protein: Minimum protein (g) per serving.
        max_protein: Maximum protein (g) per serving.
        min_fat: Minimum fat (g) per serving.
        max_fat: Maximum fat (g) per serving.
        min_carbs: Minimum carbohydrates (g) per serving.
        max_carbs: Maximum carbohydrates (g) per serving.
        sort: Sort field (e.g. 'calories', 'time', 'popularity', 'healthiness').
        sort_direction: 'asc' or 'desc'.
        offset: Number of results to skip (for pagination).
        number: Number of results to return (max 100).
        add_recipe_nutrition: Include nutrition data in results.
        add_recipe_information: Include full recipe info in results.

    Returns:
        dict with 'results' list and 'totalResults' count.
    """
    try:
        params: dict = {"offset": offset, "number": number}
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
        if max_ready_time is not None:
            params["maxReadyTime"] = max_ready_time
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
        if sort:
            params["sort"] = sort
        if sort_direction:
            params["sortDirection"] = sort_direction
        if add_recipe_nutrition:
            params["addRecipeNutrition"] = True
        if add_recipe_information:
            params["addRecipeInformation"] = True
        return _get("/recipes/complexSearch", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Search by ingredients
# ---------------------------------------------------------------------------

def search_recipes_by_ingredients(
    ingredients: str,
    number: int = 10,
    ranking: int = 1,
    ignore_pantry: bool = True,
) -> list:
    """
    Find recipes that use a given set of ingredients.

    Args:
        ingredients: Comma-separated list of ingredients (e.g. 'apples,flour,sugar').
        number: Number of recipes to return (max 100).
        ranking: 1 = maximize used ingredients, 2 = minimize missing ingredients.
        ignore_pantry: Whether to ignore typical pantry items (salt, water, etc.).

    Returns:
        List of recipe objects with usedIngredients and missedIngredients.
    """
    try:
        params = {
            "ingredients": ingredients,
            "number": number,
            "ranking": ranking,
            "ignorePantry": ignore_pantry,
        }
        return _get("/recipes/findByIngredients", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Search by nutrients
# ---------------------------------------------------------------------------

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
    offset: int = 0,
    random: bool = False,
) -> list:
    """
    Search recipes by their nutritional content per serving.

    Args:
        min_calories: Minimum calories per serving.
        max_calories: Maximum calories per serving.
        min_protein: Minimum protein (g).
        max_protein: Maximum protein (g).
        min_fat: Minimum fat (g).
        max_fat: Maximum fat (g).
        min_carbs: Minimum carbohydrates (g).
        max_carbs: Maximum carbohydrates (g).
        min_fiber: Minimum fiber (g).
        max_fiber: Maximum fiber (g).
        min_sugar: Minimum sugar (g).
        max_sugar: Maximum sugar (g).
        number: Number of results (max 100).
        offset: Pagination offset.
        random: Return random results within the constraints.

    Returns:
        List of recipe objects matching the nutritional constraints.
    """
    try:
        params: dict = {"number": number, "offset": offset, "random": random}
        for key, val in [
            ("minCalories", min_calories), ("maxCalories", max_calories),
            ("minProtein", min_protein), ("maxProtein", max_protein),
            ("minFat", min_fat), ("maxFat", max_fat),
            ("minCarbs", min_carbs), ("maxCarbs", max_carbs),
            ("minFiber", min_fiber), ("maxFiber", max_fiber),
            ("minSugar", min_sugar), ("maxSugar", max_sugar),
        ]:
            if val is not None:
                params[key] = val
        return _get("/recipes/findByNutrients", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Recipe information
# ---------------------------------------------------------------------------

def get_recipe_information(recipe_id: int, include_nutrition: bool = False) -> dict:
    """
    Get full information about a recipe by its Spoonacular ID.

    Args:
        recipe_id: The Spoonacular recipe ID.
        include_nutrition: Whether to include nutrition data in the response.

    Returns:
        dict with recipe details (title, ingredients, instructions, nutrition, etc.).
    """
    try:
        params = {"includeNutrition": include_nutrition}
        return _get(f"/recipes/{recipe_id}/information", params)
    except Exception as exc:
        return {"error": str(exc)}


def get_recipe_information_bulk(recipe_ids: str, include_nutrition: bool = False) -> list:
    """
    Get information for multiple recipes in a single request.

    Args:
        recipe_ids: Comma-separated list of recipe IDs (e.g. '715538,716429').
        include_nutrition: Whether to include nutrition data.

    Returns:
        List of recipe information dicts.
    """
    try:
        params = {"ids": recipe_ids, "includeNutrition": include_nutrition}
        return _get("/recipes/informationBulk", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Ingredients
# ---------------------------------------------------------------------------

def get_recipe_ingredients(recipe_id: int) -> dict:
    """
    Get the ingredient list for a recipe.

    Args:
        recipe_id: The Spoonacular recipe ID.

    Returns:
        dict with 'ingredients' list including amounts and units.
    """
    try:
        return _get(f"/recipes/{recipe_id}/ingredientWidget.json", {})
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Nutrition
# ---------------------------------------------------------------------------

def get_recipe_nutrition(recipe_id: int) -> dict:
    """
    Get detailed nutrition information for a recipe.

    Args:
        recipe_id: The Spoonacular recipe ID.

    Returns:
        dict with calories, macros, vitamins, minerals, etc.
    """
    try:
        return _get(f"/recipes/{recipe_id}/nutritionWidget.json", {})
    except Exception as exc:
        return {"error": str(exc)}


def get_recipe_nutrition_label(recipe_id: int) -> dict:
    """
    Get the nutrition label (as structured data) for a recipe.

    Args:
        recipe_id: The Spoonacular recipe ID.

    Returns:
        dict representing the nutrition label data.
    """
    try:
        return _get(f"/recipes/{recipe_id}/nutritionLabel.json", {})
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Instructions
# ---------------------------------------------------------------------------

def get_recipe_instructions(recipe_id: int, step_breakdown: bool = True) -> list:
    """
    Get step-by-step cooking instructions for a recipe.

    Args:
        recipe_id: The Spoonacular recipe ID.
        step_breakdown: Whether to break instructions into individual steps.

    Returns:
        List of instruction step objects.
    """
    try:
        params = {"stepBreakdown": step_breakdown}
        return _get(f"/recipes/{recipe_id}/analyzedInstructions", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Similar recipes
# ---------------------------------------------------------------------------

def get_similar_recipes(recipe_id: int, number: int = 10) -> list:
    """
    Find recipes similar to a given recipe.

    Args:
        recipe_id: The Spoonacular recipe ID to find similar recipes for.
        number: Number of similar recipes to return.

    Returns:
        List of similar recipe objects.
    """
    try:
        params = {"number": number}
        return _get(f"/recipes/{recipe_id}/similar", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Random recipes
# ---------------------------------------------------------------------------

def get_random_recipes(
    tags: str = "",
    number: int = 1,
    include_nutrition: bool = False,
) -> dict:
    """
    Get one or more random recipes, optionally filtered by tags.

    Args:
        tags: Comma-separated tags to filter by (e.g. 'vegetarian,dessert').
        number: Number of random recipes to return.
        include_nutrition: Whether to include nutrition data.

    Returns:
        dict with 'recipes' list.
    """
    try:
        params: dict = {"number": number, "includeNutrition": include_nutrition}
        if tags:
            params["tags"] = tags
        return _get("/recipes/random", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Autocomplete recipe search
# ---------------------------------------------------------------------------

def autocomplete_recipe_search(query: str, number: int = 10) -> list:
    """
    Autocomplete a partial recipe search query.

    Args:
        query: Partial recipe name to autocomplete.
        number: Number of suggestions to return (max 25).

    Returns:
        List of autocomplete suggestion objects with id and title.
    """
    try:
        params = {"query": query, "number": number}
        return _get("/recipes/autocomplete", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Summarize recipe
# ---------------------------------------------------------------------------

def summarize_recipe(recipe_id: int) -> dict:
    """
    Get a short summary of a recipe.

    Args:
        recipe_id: The Spoonacular recipe ID.

    Returns:
        dict with 'id', 'title', and 'summary' (HTML string).
    """
    try:
        return _get(f"/recipes/{recipe_id}/summary", {})
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Analyze recipe
# ---------------------------------------------------------------------------

def analyze_recipe_instructions(instructions: str) -> dict:
    """
    Parse and analyze free-text recipe instructions into structured steps.

    Args:
        instructions: Raw recipe instruction text to analyze.

    Returns:
        dict with parsed steps, ingredients, and equipment.
    """
    try:
        key = _api_key()
        url = f"{BASE_URL}/recipes/analyzeInstructions"
        resp = requests.post(
            url,
            params={"apiKey": key},
            data={"instructions": instructions},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Taste / price breakdown
# ---------------------------------------------------------------------------

def get_recipe_taste(recipe_id: int) -> dict:
    """
    Get the taste profile (sweetness, saltiness, sourness, bitterness, savoriness,
    fattiness, spiciness) for a recipe.

    Args:
        recipe_id: The Spoonacular recipe ID.

    Returns:
        dict with taste scores.
    """
    try:
        return _get(f"/recipes/{recipe_id}/tasteWidget.json", {})
    except Exception as exc:
        return {"error": str(exc)}


def get_recipe_price_breakdown(recipe_id: int) -> dict:
    """
    Get the estimated price breakdown per ingredient and total cost for a recipe.

    Args:
        recipe_id: The Spoonacular recipe ID.

    Returns:
        dict with per-ingredient costs and total price in cents.
    """
    try:
        return _get(f"/recipes/{recipe_id}/priceBreakdownWidget.json", {})
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Guess nutrition by dish name
# ---------------------------------------------------------------------------

def guess_nutrition_by_dish_name(title: str) -> dict:
    """
    Quickly estimate the nutrition of a dish given only its name.

    Args:
        title: The name of the dish (e.g. 'Spaghetti Bolognese').

    Returns:
        dict with estimated calories, protein, fat, and carbs.
    """
    try:
        params = {"title": title}
        return _get("/recipes/guessNutrition", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Classify cuisine
# ---------------------------------------------------------------------------

def classify_cuisine(title: str, ingredient_list: str = "") -> dict:
    """
    Classify the cuisine of a recipe based on its title and ingredients.

    Args:
        title: The recipe title.
        ingredient_list: Newline-separated list of ingredients.

    Returns:
        dict with 'cuisine' and 'confidence'.
    """
    try:
        key = _api_key()
        url = f"{BASE_URL}/recipes/cuisine"
        resp = requests.post(
            url,
            params={"apiKey": key},
            data={"title": title, "ingredientList": ingredient_list},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}
