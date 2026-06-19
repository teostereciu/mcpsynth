"""
Spoonacular Recipes API tools.
Source: docs/api_recipes.md
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict | list:
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(BASE_URL + path, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, params: dict, data: dict) -> dict | list:
    params["apiKey"] = _api_key()
    try:
        resp = requests.post(BASE_URL + path, params=params, data=data, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


def register_recipes(mcp: FastMCP):

    @mcp.tool()
    def search_recipes(
        search_query: str,
        cuisine: str = "",
        exclude_cuisine: str = "",
        diet_type: str = "",
        intolerances: str = "",
        equipment: str = "",
        ingredients: str = "",
        exclude_ingredients: str = "",
        type: str = "",
        instructions_required: bool = False,
        add_recipe_information: bool = False,
        add_recipe_nutrition: bool = False,
        max_ready_time: int = None,
        min_servings: int = None,
        max_servings: int = None,
        sort: str = "",
        sort_direction: str = "",
        min_calories: float = None,
        max_calories: float = None,
        min_protein: float = None,
        max_protein: float = None,
        min_fat: float = None,
        max_fat: float = None,
        min_carbs: float = None,
        max_carbs: float = None,
        offset: int = 0,
        number: int = 10,
    ) -> dict:
        """Search through thousands of recipes using advanced filtering and ranking.
        Supports filtering by cuisine, diet, intolerances, ingredients, nutrients, and more."""
        params = {"offset": offset, "number": number}
        if search_query:
            params["query"] = search_query
        if cuisine:
            params["cuisine"] = cuisine
        if exclude_cuisine:
            params["excludeCuisine"] = exclude_cuisine
        if diet_type:
            params["diet"] = diet_type
        if intolerances:
            params["intolerances"] = intolerances
        if equipment:
            params["equipment"] = equipment
        if ingredients:
            params["includeIngredients"] = ingredients
        if exclude_ingredients:
            params["excludeIngredients"] = exclude_ingredients
        if type:
            params["type"] = type
        if instructions_required:
            params["instructionsRequired"] = instructions_required
        if add_recipe_information:
            params["addRecipeInformation"] = add_recipe_information
        if add_recipe_nutrition:
            params["addRecipeNutrition"] = add_recipe_nutrition
        if max_ready_time is not None:
            params["maxReadyTime"] = max_ready_time
        if min_servings is not None:
            params["minServings"] = min_servings
        if max_servings is not None:
            params["maxServings"] = max_servings
        if sort:
            params["sort"] = sort
        if sort_direction:
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

    @mcp.tool()
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
        min_sodium: float = None,
        max_sodium: float = None,
        offset: int = 0,
        number: int = 10,
    ) -> list:
        """Find recipes that adhere to given nutritional limits (calories, protein, fat, carbs, etc.)."""
        params = {"offset": offset, "number": number}
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

    @mcp.tool()
    def search_recipes_by_ingredients(
        ingredients: str,
        number: int = 10,
        ranking: int = 1,
        ignore_pantry: bool = True,
    ) -> list:
        """Find recipes that use a given set of ingredients. Returns recipes that maximize used ingredients
        and minimize missing ones. ingredients: comma-separated list (e.g. 'apples,flour,sugar')."""
        params = {
            "ingredients": ingredients,
            "number": number,
            "ranking": ranking,
            "ignorePantry": ignore_pantry,
        }
        return _get("/recipes/findByIngredients", params)

    @mcp.tool()
    def get_recipe_information(
        recipe_id: int,
        include_nutrition: bool = False,
    ) -> dict:
        """Get detailed information about a recipe by its ID, including ingredients, instructions, and metadata."""
        params = {"includeNutrition": include_nutrition}
        return _get(f"/recipes/{recipe_id}/information", params)

    @mcp.tool()
    def get_recipe_information_bulk(
        recipe_ids: str,
        include_nutrition: bool = False,
    ) -> list:
        """Get information about multiple recipes at once. recipe_ids: comma-separated list of recipe IDs."""
        params = {"ids": recipe_ids, "includeNutrition": include_nutrition}
        return _get("/recipes/informationBulk", params)

    @mcp.tool()
    def get_similar_recipes(
        recipe_id: int,
        number: int = 10,
    ) -> list:
        """Find recipes similar to a given recipe by its ID."""
        params = {"number": number}
        return _get(f"/recipes/{recipe_id}/similar", params)

    @mcp.tool()
    def get_random_recipes(
        limit_license: bool = False,
        tags: str = "",
        number: int = 10,
    ) -> dict:
        """Get random recipes. Optionally filter by tags (e.g. 'vegetarian,dessert')."""
        params = {"number": number, "limitLicense": limit_license}
        if tags:
            params["tags"] = tags
        return _get("/recipes/random", params)

    @mcp.tool()
    def autocomplete_recipe_search(
        search_query: str,
        number: int = 10,
    ) -> list:
        """Autocomplete a partial recipe search query. Returns recipe title suggestions."""
        params = {"query": search_query, "number": number}
        return _get("/recipes/autocomplete", params)

    @mcp.tool()
    def get_recipe_taste_by_id(recipe_id: int, normalize: bool = True) -> dict:
        """Get the taste profile (sweetness, saltiness, sourness, bitterness, savoriness, fattiness, spiciness) of a recipe by ID."""
        params = {"normalize": normalize}
        return _get(f"/recipes/{recipe_id}/tasteWidget.json", params)

    @mcp.tool()
    def get_recipe_equipment_by_id(recipe_id: int) -> dict:
        """Get the equipment needed for a recipe by its ID."""
        return _get(f"/recipes/{recipe_id}/equipmentWidget.json", {})

    @mcp.tool()
    def get_recipe_price_breakdown_by_id(recipe_id: int) -> dict:
        """Get the price breakdown of a recipe by its ID, including cost per serving."""
        return _get(f"/recipes/{recipe_id}/priceBreakdownWidget.json", {})

    @mcp.tool()
    def get_recipe_ingredients_by_id(recipe_id: int) -> dict:
        """Get the ingredients for a recipe by its ID."""
        return _get(f"/recipes/{recipe_id}/ingredientWidget.json", {})

    @mcp.tool()
    def get_recipe_nutrition_by_id(recipe_id: int) -> dict:
        """Get the full nutritional information for a recipe by its ID."""
        return _get(f"/recipes/{recipe_id}/nutritionWidget.json", {})

    @mcp.tool()
    def get_analyzed_recipe_instructions(
        recipe_id: int,
        step_breakdown: bool = False,
    ) -> list:
        """Get step-by-step analyzed instructions for a recipe by its ID."""
        params = {"stepBreakdown": step_breakdown}
        return _get(f"/recipes/{recipe_id}/analyzedInstructions", params)

    @mcp.tool()
    def extract_recipe_from_website(
        url: str,
        force_extraction: bool = False,
        analyze: bool = False,
        include_nutrition: bool = False,
        include_taste: bool = False,
    ) -> dict:
        """Extract recipe data from any recipe website URL."""
        params = {
            "url": url,
            "forceExtraction": force_extraction,
            "analyze": analyze,
            "includeNutrition": include_nutrition,
            "includeTaste": include_taste,
        }
        return _get("/recipes/extract", params)

    @mcp.tool()
    def analyze_recipe(
        title: str,
        servings: int,
        ingredient_list: str,
        instructions: str,
        language: str = "en",
        include_nutrition: bool = False,
        include_taste: bool = False,
    ) -> dict:
        """Analyze a recipe by providing its title, servings, ingredients, and instructions.
        Returns detailed nutritional and taste information."""
        params = {"language": language, "includeNutrition": include_nutrition, "includeTaste": include_taste}
        data = {
            "title": title,
            "servings": servings,
            "ingredientList": ingredient_list,
            "instructions": instructions,
        }
        return _post("/recipes/analyze", params, data)

    @mcp.tool()
    def summarize_recipe(recipe_id: int) -> dict:
        """Automatically generate a short description that summarizes key information about a recipe."""
        return _get(f"/recipes/{recipe_id}/summary", {})

    @mcp.tool()
    def analyze_recipe_instructions(instructions: str) -> list:
        """Parse and analyze recipe instructions text, breaking them into steps with ingredients and equipment."""
        data = {"instructions": instructions}
        return _post("/recipes/analyzeInstructions", {}, data)

    @mcp.tool()
    def classify_cuisine(
        title: str,
        ingredient_list: str,
        language: str = "en",
    ) -> dict:
        """Classify the cuisine of a recipe based on its title and ingredient list."""
        params = {"language": language}
        data = {"title": title, "ingredientList": ingredient_list}
        return _post("/recipes/cuisine", params, data)

    @mcp.tool()
    def analyze_recipe_search_query(q: str) -> dict:
        """Parse a recipe search query to understand what the user is looking for
        (e.g. 'low fat pasta' → diet: low fat, ingredient: pasta)."""
        params = {"q": q}
        return _get("/recipes/queries/analyze", params)
