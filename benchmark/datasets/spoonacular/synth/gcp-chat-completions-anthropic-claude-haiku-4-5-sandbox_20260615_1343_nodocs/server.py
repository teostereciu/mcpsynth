#!/usr/bin/env python3
"""
MCP Server for Spoonacular Food API
Provides tools for recipe search, meal planning, nutrition, and more.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
server = FastMCP("spoonacular")

# Get API key from environment
API_KEY = os.getenv("SPOONACULAR_API_KEY")
BASE_URL = "https://api.spoonacular.com"

if not API_KEY:
    raise ValueError("SPOONACULAR_API_KEY environment variable is required")


def make_request(endpoint: str, method: str = "GET", params: Optional[dict] = None) -> dict:
    """Make a request to the Spoonacular API."""
    if params is None:
        params = {}
    
    # Add API key to all requests
    params["apiKey"] = API_KEY
    
    url = f"{BASE_URL}{endpoint}"
    
    try:
        if method == "GET":
            response = requests.get(url, params=params, timeout=10)
        elif method == "POST":
            response = requests.post(url, params=params, timeout=10)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from API"}


# ============================================================================
# RECIPE SEARCH TOOLS
# ============================================================================

@server.tool()
def search_recipes(
    query: str,
    number: int = 10,
    offset: int = 0,
    type: Optional[str] = None,
    cuisine: Optional[str] = None,
    diet: Optional[str] = None,
    intolerances: Optional[str] = None,
) -> dict:
    """
    Search for recipes by query string.
    
    Args:
        query: The search query (e.g., "pasta", "chicken")
        number: Number of results to return (default: 10, max: 100)
        offset: Offset for pagination (default: 0)
        type: Filter by recipe type (e.g., "main course", "dessert", "appetizer")
        cuisine: Filter by cuisine (e.g., "italian", "mexican", "asian")
        diet: Filter by diet (e.g., "vegetarian", "vegan", "paleo")
        intolerances: Comma-separated intolerances (e.g., "dairy,gluten")
    
    Returns:
        Dictionary with search results including recipe IDs, titles, and images
    """
    params = {
        "query": query,
        "number": min(number, 100),
        "offset": offset,
    }
    
    if type:
        params["type"] = type
    if cuisine:
        params["cuisine"] = cuisine
    if diet:
        params["diet"] = diet
    if intolerances:
        params["intolerances"] = intolerances
    
    return make_request("/recipes/complexSearch", params=params)


@server.tool()
def search_recipes_by_ingredients(
    ingredients: str,
    number: int = 10,
    ranking: str = "maximize",
    add_recipe_information: bool = False,
) -> dict:
    """
    Search for recipes by ingredients.
    
    Args:
        ingredients: Comma-separated list of ingredients
        number: Number of results to return (default: 10, max: 100)
        ranking: Ranking method - "maximize" (default) or "minimize"
        add_recipe_information: Include full recipe information (default: False)
    
    Returns:
        List of recipes that can be made with the given ingredients
    """
    params = {
        "ingredients": ingredients,
        "number": min(number, 100),
        "ranking": ranking,
        "addRecipeInformation": add_recipe_information,
    }
    
    return make_request("/recipes/findByIngredients", params=params)


@server.tool()
def search_recipes_by_nutrients(
    min_carbs: Optional[float] = None,
    max_carbs: Optional[float] = None,
    min_protein: Optional[float] = None,
    max_protein: Optional[float] = None,
    min_fat: Optional[float] = None,
    max_fat: Optional[float] = None,
    min_calories: Optional[float] = None,
    max_calories: Optional[float] = None,
    number: int = 10,
    offset: int = 0,
) -> dict:
    """
    Search for recipes by nutritional values.
    
    Args:
        min_carbs: Minimum carbs in grams
        max_carbs: Maximum carbs in grams
        min_protein: Minimum protein in grams
        max_protein: Maximum protein in grams
        min_fat: Minimum fat in grams
        max_fat: Maximum fat in grams
        min_calories: Minimum calories
        max_calories: Maximum calories
        number: Number of results (default: 10)
        offset: Pagination offset (default: 0)
    
    Returns:
        List of recipes matching the nutritional criteria
    """
    params = {
        "number": min(number, 100),
        "offset": offset,
    }
    
    if min_carbs is not None:
        params["minCarbs"] = min_carbs
    if max_carbs is not None:
        params["maxCarbs"] = max_carbs
    if min_protein is not None:
        params["minProtein"] = min_protein
    if max_protein is not None:
        params["maxProtein"] = max_protein
    if min_fat is not None:
        params["minFat"] = min_fat
    if max_fat is not None:
        params["maxFat"] = max_fat
    if min_calories is not None:
        params["minCalories"] = min_calories
    if max_calories is not None:
        params["maxCalories"] = max_calories
    
    return make_request("/recipes/findByNutrients", params=params)


@server.tool()
def autocomplete_recipe_search(query: str, number: int = 10) -> dict:
    """
    Autocomplete recipe search.
    
    Args:
        query: The search query
        number: Number of results (default: 10)
    
    Returns:
        List of recipe name suggestions
    """
    params = {
        "query": query,
        "number": number,
    }
    
    return make_request("/recipes/autocomplete", params=params)


# ============================================================================
# RECIPE INFORMATION TOOLS
# ============================================================================

@server.tool()
def get_recipe_information(recipe_id: int, include_nutrition: bool = False) -> dict:
    """
    Get detailed information about a recipe.
    
    Args:
        recipe_id: The recipe ID
        include_nutrition: Include nutrition information (default: False)
    
    Returns:
        Detailed recipe information including ingredients, instructions, etc.
    """
    params = {
        "includeNutrition": include_nutrition,
    }
    
    return make_request(f"/recipes/{recipe_id}/information", params=params)


@server.tool()
def get_recipe_instructions(recipe_id: int) -> dict:
    """
    Get cooking instructions for a recipe.
    
    Args:
        recipe_id: The recipe ID
    
    Returns:
        Recipe instructions and steps
    """
    return make_request(f"/recipes/{recipe_id}/analyzedInstructions")


@server.tool()
def get_similar_recipes(recipe_id: int, number: int = 5) -> dict:
    """
    Get recipes similar to a given recipe.
    
    Args:
        recipe_id: The recipe ID
        number: Number of similar recipes to return (default: 5)
    
    Returns:
        List of similar recipes
    """
    params = {
        "number": number,
    }
    
    return make_request(f"/recipes/{recipe_id}/similar", params=params)


@server.tool()
def get_recipe_summary(recipe_id: int) -> dict:
    """
    Get a summary of a recipe.
    
    Args:
        recipe_id: The recipe ID
    
    Returns:
        Recipe summary with title, image, and description
    """
    return make_request(f"/recipes/{recipe_id}/summary")


# ============================================================================
# INGREDIENT SEARCH TOOLS
# ============================================================================

@server.tool()
def search_ingredients(
    query: str,
    number: int = 10,
    offset: int = 0,
) -> dict:
    """
    Search for ingredients.
    
    Args:
        query: The search query
        number: Number of results (default: 10)
        offset: Pagination offset (default: 0)
    
    Returns:
        List of matching ingredients
    """
    params = {
        "query": query,
        "number": number,
        "offset": offset,
    }
    
    return make_request("/food/ingredients/search", params=params)


@server.tool()
def get_ingredient_information(ingredient_id: int) -> dict:
    """
    Get detailed information about an ingredient.
    
    Args:
        ingredient_id: The ingredient ID
    
    Returns:
        Ingredient information including nutrition, image, etc.
    """
    return make_request(f"/food/ingredients/{ingredient_id}/information")


@server.tool()
def autocomplete_ingredient_search(query: str, number: int = 10) -> dict:
    """
    Autocomplete ingredient search.
    
    Args:
        query: The search query
        number: Number of results (default: 10)
    
    Returns:
        List of ingredient name suggestions
    """
    params = {
        "query": query,
        "number": number,
    }
    
    return make_request("/food/ingredients/autocomplete", params=params)


@server.tool()
def parse_ingredients(ingredients: str) -> dict:
    """
    Parse a list of ingredients from text.
    
    Args:
        ingredients: Comma-separated or newline-separated list of ingredients
    
    Returns:
        Parsed ingredients with quantities and units
    """
    params = {
        "ingredients": ingredients,
    }
    
    return make_request("/recipes/parseIngredients", params=params, method="POST")


# ============================================================================
# MEAL PLANNING TOOLS
# ============================================================================

@server.tool()
def generate_meal_plan(
    time_frame: str = "day",
    diet: Optional[str] = None,
    exclude_recipe: Optional[str] = None,
    target_calories: Optional[int] = None,
) -> dict:
    """
    Generate a meal plan.
    
    Args:
        time_frame: "day" or "week" (default: "day")
        diet: Diet type (e.g., "vegetarian", "vegan", "paleo")
        exclude_recipe: Recipe IDs to exclude (comma-separated)
        target_calories: Target daily calories
    
    Returns:
        Generated meal plan with recipes and nutrition info
    """
    params = {
        "timeFrame": time_frame,
    }
    
    if diet:
        params["diet"] = diet
    if exclude_recipe:
        params["exclude"] = exclude_recipe
    if target_calories:
        params["targetCalories"] = target_calories
    
    return make_request("/mealplanner/generate", params=params)


@server.tool()
def get_meal_plan_day(date: str, hash_value: Optional[str] = None) -> dict:
    """
    Get a meal plan for a specific day.
    
    Args:
        date: Date in YYYY-MM-DD format
        hash_value: Hash value for the meal plan (optional)
    
    Returns:
        Meal plan for the specified day
    """
    params = {
        "date": date,
    }
    
    if hash_value:
        params["hash"] = hash_value
    
    return make_request("/mealplanner/day", params=params)


@server.tool()
def get_meal_plan_week(start_date: str, hash_value: Optional[str] = None) -> dict:
    """
    Get a meal plan for a week.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        hash_value: Hash value for the meal plan (optional)
    
    Returns:
        Meal plan for the week
    """
    params = {
        "startDate": start_date,
    }
    
    if hash_value:
        params["hash"] = hash_value
    
    return make_request("/mealplanner/week", params=params)


# ============================================================================
# NUTRITION TOOLS
# ============================================================================

@server.tool()
def get_nutrition_by_id(recipe_id: int) -> dict:
    """
    Get nutrition information for a recipe by ID.
    
    Args:
        recipe_id: The recipe ID
    
    Returns:
        Detailed nutrition information
    """
    return make_request(f"/recipes/{recipe_id}/nutritionWidget.json")


@server.tool()
def get_nutrition_by_ingredients(ingredients: str) -> dict:
    """
    Get nutrition information for a list of ingredients.
    
    Args:
        ingredients: Comma-separated list of ingredients with quantities
    
    Returns:
        Nutrition information for the ingredients
    """
    params = {
        "ingredients": ingredients,
    }
    
    return make_request("/recipes/nutritionByIngredients", params=params, method="POST")


@server.tool()
def visualize_nutrition(recipe_id: int) -> dict:
    """
    Get nutrition visualization data for a recipe.
    
    Args:
        recipe_id: The recipe ID
    
    Returns:
        Nutrition visualization data
    """
    return make_request(f"/recipes/{recipe_id}/nutritionLabel.json")


# ============================================================================
# WINE PAIRING TOOLS
# ============================================================================

@server.tool()
def get_wine_pairing(food: str, max_price: Optional[int] = None) -> dict:
    """
    Get wine pairing recommendations for a food.
    
    Args:
        food: The food to pair wine with
        max_price: Maximum price for the wine (optional)
    
    Returns:
        Wine pairing recommendations
    """
    params = {
        "food": food,
    }
    
    if max_price:
        params["maxPrice"] = max_price
    
    return make_request("/food/wine/pairing", params=params)


@server.tool()
def get_wine_description(wine: str) -> dict:
    """
    Get description and pairing information for a wine.
    
    Args:
        wine: The wine name
    
    Returns:
        Wine description and pairing information
    """
    params = {
        "wine": wine,
    }
    
    return make_request("/food/wine/description", params=params)


# ============================================================================
# ADDITIONAL UTILITY TOOLS
# ============================================================================

@server.tool()
def get_random_recipes(number: int = 1, tags: Optional[str] = None) -> dict:
    """
    Get random recipes.
    
    Args:
        number: Number of random recipes (default: 1, max: 100)
        tags: Comma-separated tags to filter by (optional)
    
    Returns:
        Random recipes
    """
    params = {
        "number": min(number, 100),
    }
    
    if tags:
        params["tags"] = tags
    
    return make_request("/recipes/random", params=params)


@server.tool()
def get_recipe_taste(recipe_id: int) -> dict:
    """
    Get taste profile for a recipe.
    
    Args:
        recipe_id: The recipe ID
    
    Returns:
        Taste profile data (sweetness, saltiness, etc.)
    """
    return make_request(f"/recipes/{recipe_id}/tasteWidget.json")


@server.tool()
def classify_cuisine(title: str, ingredients: Optional[str] = None) -> dict:
    """
    Classify the cuisine type of a recipe.
    
    Args:
        title: Recipe title
        ingredients: Comma-separated ingredients (optional)
    
    Returns:
        Cuisine classification
    """
    params = {
        "title": title,
    }
    
    if ingredients:
        params["ingredients"] = ingredients
    
    return make_request("/recipes/cuisine", params=params, method="POST")


if __name__ == "__main__":
    server.run()
