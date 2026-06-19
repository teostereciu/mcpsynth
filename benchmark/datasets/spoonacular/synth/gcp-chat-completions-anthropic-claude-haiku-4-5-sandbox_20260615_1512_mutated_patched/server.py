#!/usr/bin/env python3
"""
MCP Server for Spoonacular Food API
Provides tools for recipe search, ingredient information, meal planning, and more.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("spoonacular")

# Get API key from environment
API_KEY = os.getenv("SPOONACULAR_API_KEY")
BASE_URL = "https://api.spoonacular.com"

if not API_KEY:
    raise ValueError("SPOONACULAR_API_KEY environment variable is required")


def make_request(method: str, endpoint: str, params: dict = None) -> Any:
    """Make a request to the Spoonacular API."""
    if params is None:
        params = {}
    
    # Add API key to all requests
    params["apiKey"] = API_KEY
    
    url = f"{BASE_URL}{endpoint}"
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, data=params)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Failed to parse API response"}


# ============================================================================
# RECIPES ENDPOINTS
# ============================================================================

@mcp.tool()
def search_recipes(
    search_query: str,
    cuisine: Optional[str] = None,
    exclude_cuisine: Optional[str] = None,
    diet_type: Optional[str] = None,
    intolerances: Optional[str] = None,
    equipment: Optional[str] = None,
    ingredients: Optional[str] = None,
    exclude_ingredients: Optional[str] = None,
    type_: Optional[str] = None,
    instructions_required: Optional[bool] = None,
    fill_ingredients: Optional[bool] = None,
    add_recipe_information: Optional[bool] = None,
    add_recipe_instructions: Optional[bool] = None,
    add_recipe_nutrition: Optional[bool] = None,
    author: Optional[str] = None,
    tags: Optional[str] = None,
    recipe_box_id: Optional[int] = None,
    title_match: Optional[str] = None,
    max_ready_time: Optional[int] = None,
    min_servings: Optional[int] = None,
    max_servings: Optional[int] = None,
    ignore_pantry: Optional[bool] = None,
    sort: Optional[str] = None,
    sort_direction: Optional[str] = None,
    min_carbs: Optional[float] = None,
    max_carbs: Optional[float] = None,
    min_protein: Optional[float] = None,
    max_protein: Optional[float] = None,
    min_calories: Optional[int] = None,
    max_calories: Optional[int] = None,
    min_fat: Optional[float] = None,
    max_fat: Optional[float] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Any:
    """Search recipes with advanced filtering and ranking."""
    params = {"search_query": search_query}
    
    # Add optional parameters
    if cuisine is not None:
        params["cuisine"] = cuisine
    if exclude_cuisine is not None:
        params["excludeCuisine"] = exclude_cuisine
    if diet_type is not None:
        params["diet"] = diet_type
    if intolerances is not None:
        params["intolerances"] = intolerances
    if equipment is not None:
        params["equipment"] = equipment
    if ingredients is not None:
        params["includeIngredients"] = ingredients
    if exclude_ingredients is not None:
        params["excludeIngredients"] = exclude_ingredients
    if type_ is not None:
        params["type"] = type_
    if instructions_required is not None:
        params["instructionsRequired"] = instructions_required
    if fill_ingredients is not None:
        params["fillIngredients"] = fill_ingredients
    if add_recipe_information is not None:
        params["addRecipeInformation"] = add_recipe_information
    if add_recipe_instructions is not None:
        params["addRecipeInstructions"] = add_recipe_instructions
    if add_recipe_nutrition is not None:
        params["addRecipeNutrition"] = add_recipe_nutrition
    if author is not None:
        params["author"] = author
    if tags is not None:
        params["tags"] = tags
    if recipe_box_id is not None:
        params["recipeBoxId"] = recipe_box_id
    if title_match is not None:
        params["titleMatch"] = title_match
    if max_ready_time is not None:
        params["maxReadyTime"] = max_ready_time
    if min_servings is not None:
        params["minServings"] = min_servings
    if max_servings is not None:
        params["maxServings"] = max_servings
    if ignore_pantry is not None:
        params["ignorePantry"] = ignore_pantry
    if sort is not None:
        params["sort"] = sort
    if sort_direction is not None:
        params["sortDirection"] = sort_direction
    if min_carbs is not None:
        params["minCarbs"] = min_carbs
    if max_carbs is not None:
        params["maxCarbs"] = max_carbs
    if min_protein is not None:
        params["minProtein"] = min_protein
    if max_protein is not None:
        params["maxProtein"] = max_protein
    if min_calories is not None:
        params["minCalories"] = min_calories
    if max_calories is not None:
        params["maxCalories"] = max_calories
    if min_fat is not None:
        params["minFat"] = min_fat
    if max_fat is not None:
        params["maxFat"] = max_fat
    if offset is not None:
        params["offset"] = offset
    if number is not None:
        params["number"] = number
    
    return make_request("GET", "/recipes/complexSearch", params)


@mcp.tool()
def search_recipes_by_nutrients(
    min_carbs: Optional[float] = None,
    max_carbs: Optional[float] = None,
    min_protein: Optional[float] = None,
    max_protein: Optional[float] = None,
    min_calories: Optional[int] = None,
    max_calories: Optional[int] = None,
    min_fat: Optional[float] = None,
    max_fat: Optional[float] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Any:
    """Find recipes that adhere to given nutritional limits."""
    params = {}
    
    if min_carbs is not None:
        params["minCarbs"] = min_carbs
    if max_carbs is not None:
        params["maxCarbs"] = max_carbs
    if min_protein is not None:
        params["minProtein"] = min_protein
    if max_protein is not None:
        params["maxProtein"] = max_protein
    if min_calories is not None:
        params["minCalories"] = min_calories
    if max_calories is not None:
        params["maxCalories"] = max_calories
    if min_fat is not None:
        params["minFat"] = min_fat
    if max_fat is not None:
        params["maxFat"] = max_fat
    if offset is not None:
        params["offset"] = offset
    if number is not None:
        params["number"] = number
    
    return make_request("GET", "/recipes/findByNutrients", params)


@mcp.tool()
def search_recipes_by_ingredients(
    ingredients: str,
    number: Optional[int] = None,
    ranking: Optional[int] = None,
    add_recipe_information: Optional[bool] = None,
) -> Any:
    """Search recipes by ingredients."""
    params = {"ingredients": ingredients}
    
    if number is not None:
        params["number"] = number
    if ranking is not None:
        params["ranking"] = ranking
    if add_recipe_information is not None:
        params["addRecipeInformation"] = add_recipe_information
    
    return make_request("GET", "/recipes/findByIngredients", params)


@mcp.tool()
def get_recipe_information(
    recipe_id: int,
    include_nutrition: Optional[bool] = None,
) -> Any:
    """Get detailed information about a recipe."""
    params = {}
    
    if include_nutrition is not None:
        params["includeNutrition"] = include_nutrition
    
    return make_request("GET", f"/recipes/{recipe_id}/information", params)


@mcp.tool()
def get_recipe_information_bulk(recipe_ids: str) -> Any:
    """Get information for multiple recipes at once."""
    params = {"ids": recipe_ids}
    return make_request("GET", "/recipes/informationBulk", params)


@mcp.tool()
def get_similar_recipes(recipe_id: int, number: Optional[int] = None) -> Any:
    """Get recipes similar to a given recipe."""
    params = {}
    if number is not None:
        params["number"] = number
    
    return make_request("GET", f"/recipes/{recipe_id}/similar", params)


@mcp.tool()
def get_random_recipes(
    number: Optional[int] = None,
    tags: Optional[str] = None,
) -> Any:
    """Get random recipes."""
    params = {}
    if number is not None:
        params["number"] = number
    if tags is not None:
        params["tags"] = tags
    
    return make_request("GET", "/recipes/random", params)


@mcp.tool()
def autocomplete_recipe_search(query: str, number: Optional[int] = None) -> Any:
    """Autocomplete recipe search."""
    params = {"query": query}
    if number is not None:
        params["number"] = number
    
    return make_request("GET", "/recipes/autocomplete", params)


@mcp.tool()
def get_recipe_taste_by_id(recipe_id: int) -> Any:
    """Get taste information for a recipe."""
    return make_request("GET", f"/recipes/{recipe_id}/tasteWidget.json")


@mcp.tool()
def get_recipe_equipment_by_id(recipe_id: int) -> Any:
    """Get equipment information for a recipe."""
    return make_request("GET", f"/recipes/{recipe_id}/equipmentWidget.json")


@mcp.tool()
def get_recipe_price_breakdown_by_id(recipe_id: int) -> Any:
    """Get price breakdown for a recipe."""
    return make_request("GET", f"/recipes/{recipe_id}/priceBreakdownWidget.json")


@mcp.tool()
def get_recipe_ingredients_by_id(recipe_id: int) -> Any:
    """Get ingredients for a recipe."""
    return make_request("GET", f"/recipes/{recipe_id}/ingredientWidget.json")


@mcp.tool()
def get_recipe_nutrition_by_id(recipe_id: int) -> Any:
    """Get nutrition information for a recipe."""
    return make_request("GET", f"/recipes/{recipe_id}/nutritionWidget.json")


@mcp.tool()
def get_analyzed_recipe_instructions(recipe_id: int) -> Any:
    """Get analyzed recipe instructions."""
    return make_request("GET", f"/recipes/{recipe_id}/analyzedInstructions")


@mcp.tool()
def extract_recipe_from_website(url: str) -> Any:
    """Extract recipe information from a website URL."""
    params = {"url": url}
    return make_request("GET", "/recipes/extract", params)


@mcp.tool()
def analyze_recipe(
    title: str,
    ingredients: str,
    servings: int,
) -> Any:
    """Analyze a recipe."""
    params = {
        "title": title,
        "ingredients": ingredients,
        "servings": servings,
    }
    return make_request("POST", "/recipes/analyze", params)


@mcp.tool()
def summarize_recipe(recipe_id: int) -> Any:
    """Get a summary of a recipe."""
    return make_request("GET", f"/recipes/{recipe_id}/summary")


@mcp.tool()
def analyze_recipe_instructions(recipe_id: int) -> Any:
    """Analyze recipe instructions."""
    return make_request("GET", f"/recipes/{recipe_id}/analyzeInstructions")


@mcp.tool()
def classify_cuisine(
    title: str,
    ingredients: str,
) -> Any:
    """Classify the cuisine of a recipe."""
    params = {
        "title": title,
        "ingredients": ingredients,
    }
    return make_request("POST", "/recipes/cuisine", params)


@mcp.tool()
def analyze_recipe_search_query(query: str) -> Any:
    """Analyze a recipe search query."""
    params = {"q": query}
    return make_request("GET", "/recipes/queries/analyze", params)


# ============================================================================
# INGREDIENTS ENDPOINTS
# ============================================================================

@mcp.tool()
def search_ingredients(
    search_query: str,
    add_children: Optional[bool] = None,
    min_protein_percent: Optional[float] = None,
    max_protein_percent: Optional[float] = None,
    min_fat_percent: Optional[float] = None,
    max_fat_percent: Optional[float] = None,
    min_carbs_percent: Optional[float] = None,
    max_carbs_percent: Optional[float] = None,
    meta_information: Optional[bool] = None,
    intolerances: Optional[str] = None,
    sort: Optional[str] = None,
    sort_direction: Optional[str] = None,
    language: Optional[str] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Any:
    """Search for ingredients."""
    params = {"query": search_query}
    
    if add_children is not None:
        params["addChildren"] = add_children
    if min_protein_percent is not None:
        params["minProteinPercent"] = min_protein_percent
    if max_protein_percent is not None:
        params["maxProteinPercent"] = max_protein_percent
    if min_fat_percent is not None:
        params["minFatPercent"] = min_fat_percent
    if max_fat_percent is not None:
        params["maxFatPercent"] = max_fat_percent
    if min_carbs_percent is not None:
        params["minCarbsPercent"] = min_carbs_percent
    if max_carbs_percent is not None:
        params["maxCarbsPercent"] = max_carbs_percent
    if meta_information is not None:
        params["metaInformation"] = meta_information
    if intolerances is not None:
        params["intolerances"] = intolerances
    if sort is not None:
        params["sort"] = sort
    if sort_direction is not None:
        params["sortDirection"] = sort_direction
    if language is not None:
        params["language"] = language
    if offset is not None:
        params["offset"] = offset
    if number is not None:
        params["number"] = number
    
    return make_request("GET", "/food/ingredients/search", params)


@mcp.tool()
def get_ingredient_information(
    ingredient_id: int,
    amount: Optional[float] = None,
    unit: Optional[str] = None,
    locale: Optional[str] = None,
) -> Any:
    """Get detailed information about an ingredient."""
    params = {}
    
    if amount is not None:
        params["amount"] = amount
    if unit is not None:
        params["unit"] = unit
    if locale is not None:
        params["locale"] = locale
    
    return make_request("GET", f"/food/ingredients/{ingredient_id}/information", params)


@mcp.tool()
def compute_ingredient_amount(
    ingredient_id: int,
    nutrient: str,
    target: float,
    unit: Optional[str] = None,
) -> Any:
    """Compute the amount of an ingredient needed for a nutritional goal."""
    params = {
        "nutrient": nutrient,
        "target": target,
    }
    
    if unit is not None:
        params["unit"] = unit
    
    return make_request("GET", f"/food/ingredients/{ingredient_id}/amount", params)


@mcp.tool()
def convert_amounts(
    ingredient_name: str,
    source_amount: float,
    source_unit: str,
    target_unit: str,
) -> Any:
    """Convert ingredient amounts between units."""
    params = {
        "ingredientName": ingredient_name,
        "sourceAmount": source_amount,
        "sourceUnit": source_unit,
        "targetUnit": target_unit,
    }
    
    return make_request("GET", "/recipes/convert", params)


@mcp.tool()
def parse_ingredients(
    ingredient_list: str,
    servings: int,
    include_nutrition: Optional[bool] = None,
    language: Optional[str] = None,
) -> Any:
    """Parse ingredients from plain text."""
    params = {
        "ingredientList": ingredient_list,
        "servings": servings,
    }
    
    if include_nutrition is not None:
        params["includeNutrition"] = include_nutrition
    if language is not None:
        params["language"] = language
    
    return make_request("POST", "/recipes/parseIngredients", params)


@mcp.tool()
def compute_glycemic_load(ingredient_id: int, amount: float, unit: str) -> Any:
    """Compute the glycemic load of an ingredient."""
    params = {
        "amount": amount,
        "unit": unit,
    }
    
    return make_request("GET", f"/food/ingredients/{ingredient_id}/glycemicLoad", params)


@mcp.tool()
def autocomplete_ingredient_search(query: str, number: Optional[int] = None) -> Any:
    """Autocomplete ingredient search."""
    params = {"query": query}
    
    if number is not None:
        params["number"] = number
    
    return make_request("GET", "/food/ingredients/autocomplete", params)


@mcp.tool()
def get_ingredient_substitutes(ingredient_name: str) -> Any:
    """Get substitutes for an ingredient."""
    params = {"ingredientName": ingredient_name}
    return make_request("GET", "/food/ingredients/substitutes", params)


@mcp.tool()
def get_ingredient_substitutes_by_id(ingredient_id: int) -> Any:
    """Get substitutes for an ingredient by ID."""
    return make_request("GET", f"/food/ingredients/{ingredient_id}/substitutes")


# ============================================================================
# MEAL PLANNING ENDPOINTS
# ============================================================================

@mcp.tool()
def get_meal_plan_week(
    username: str,
    start_date: Optional[str] = None,
    hash_: Optional[str] = None,
) -> Any:
    """Get a weekly meal plan."""
    params = {}
    
    if start_date is not None:
        params["startDate"] = start_date
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("GET", f"/mealplanner/{username}/week/{start_date or ''}", params)


@mcp.tool()
def get_meal_plan_day(
    username: str,
    date: str,
    hash_: Optional[str] = None,
) -> Any:
    """Get a daily meal plan."""
    params = {}
    
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("GET", f"/mealplanner/{username}/day/{date}", params)


@mcp.tool()
def generate_meal_plan(
    time_frame: str,
    target_calories: Optional[int] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None,
) -> Any:
    """Generate a meal plan."""
    params = {"timeFrame": time_frame}
    
    if target_calories is not None:
        params["targetCalories"] = target_calories
    if diet is not None:
        params["diet"] = diet
    if exclude is not None:
        params["exclude"] = exclude
    
    return make_request("GET", "/mealplanner/generate", params)


@mcp.tool()
def add_to_meal_plan(
    username: str,
    date: str,
    slot: int,
    position: int,
    recipe_id: int,
    hash_: Optional[str] = None,
) -> Any:
    """Add a recipe to a meal plan."""
    params = {
        "date": date,
        "slot": slot,
        "position": position,
        "id": recipe_id,
    }
    
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("POST", f"/mealplanner/{username}/items", params)


@mcp.tool()
def clear_meal_plan_day(
    username: str,
    date: str,
    hash_: Optional[str] = None,
) -> Any:
    """Clear a day from a meal plan."""
    params = {}
    
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("DELETE", f"/mealplanner/{username}/day/{date}", params)


@mcp.tool()
def delete_from_meal_plan(
    username: str,
    item_id: int,
    hash_: Optional[str] = None,
) -> Any:
    """Delete an item from a meal plan."""
    params = {}
    
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("DELETE", f"/mealplanner/{username}/items/{item_id}", params)


@mcp.tool()
def get_meal_plan_templates() -> Any:
    """Get meal plan templates."""
    return make_request("GET", "/mealplanner/templates")


@mcp.tool()
def get_meal_plan_template(template_id: int) -> Any:
    """Get a specific meal plan template."""
    return make_request("GET", f"/mealplanner/templates/{template_id}")


@mcp.tool()
def add_meal_plan_template(
    username: str,
    name: str,
    items: str,
    hash_: Optional[str] = None,
) -> Any:
    """Add a meal plan template."""
    params = {
        "name": name,
        "items": items,
    }
    
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("POST", f"/mealplanner/{username}/templates", params)


@mcp.tool()
def delete_meal_plan_template(
    username: str,
    template_id: int,
    hash_: Optional[str] = None,
) -> Any:
    """Delete a meal plan template."""
    params = {}
    
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("DELETE", f"/mealplanner/{username}/templates/{template_id}", params)


@mcp.tool()
def get_shopping_list(
    username: str,
    hash_: Optional[str] = None,
) -> Any:
    """Get a shopping list."""
    params = {}
    
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("GET", f"/mealplanner/{username}/shopping-list", params)


@mcp.tool()
def add_to_shopping_list(
    username: str,
    item: str,
    aisle: Optional[str] = None,
    parse: Optional[bool] = None,
    hash_: Optional[str] = None,
) -> Any:
    """Add an item to a shopping list."""
    params = {"item": item}
    
    if aisle is not None:
        params["aisle"] = aisle
    if parse is not None:
        params["parse"] = parse
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("POST", f"/mealplanner/{username}/shopping-list/items", params)


@mcp.tool()
def delete_from_shopping_list(
    username: str,
    item_id: int,
    hash_: Optional[str] = None,
) -> Any:
    """Delete an item from a shopping list."""
    params = {}
    
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("DELETE", f"/mealplanner/{username}/shopping-list/items/{item_id}", params)


@mcp.tool()
def generate_shopping_list(
    username: str,
    start_date: str,
    end_date: str,
    hash_: Optional[str] = None,
) -> Any:
    """Generate a shopping list from a meal plan."""
    params = {
        "startDate": start_date,
        "endDate": end_date,
    }
    
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("POST", f"/mealplanner/{username}/shopping-list/generate", params)


@mcp.tool()
def compute_shopping_list(
    username: str,
    start_date: str,
    end_date: str,
    hash_: Optional[str] = None,
) -> Any:
    """Compute a shopping list."""
    params = {
        "startDate": start_date,
        "endDate": end_date,
    }
    
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("GET", f"/mealplanner/{username}/shopping-list/compute", params)


@mcp.tool()
def search_custom_foods(
    username: str,
    query: str,
    hash_: Optional[str] = None,
) -> Any:
    """Search custom foods."""
    params = {"query": query}
    
    if hash_ is not None:
        params["hash"] = hash_
    
    return make_request("GET", f"/mealplanner/{username}/foods/search", params)


@mcp.tool()
def connect_user(
    username: str,
    first_name: str,
    last_name: str,
    email: str,
) -> Any:
    """Connect a user to the meal planner."""
    params = {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
    }
    
    return make_request("POST", f"/users/connect", params)


# ============================================================================
# MENU ITEMS ENDPOINTS
# ============================================================================

@mcp.tool()
def search_menu_items(
    query: str,
    min_calories: Optional[int] = None,
    max_calories: Optional[int] = None,
    min_carbs: Optional[float] = None,
    max_carbs: Optional[float] = None,
    min_protein: Optional[float] = None,
    max_protein: Optional[float] = None,
    min_fat: Optional[float] = None,
    max_fat: Optional[float] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Any:
    """Search menu items."""
    params = {"query": query}
    
    if min_calories is not None:
        params["minCalories"] = min_calories
    if max_calories is not None:
        params["maxCalories"] = max_calories
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
    if offset is not None:
        params["offset"] = offset
    if number is not None:
        params["number"] = number
    
    return make_request("GET", "/food/menuItems/search", params)


@mcp.tool()
def get_menu_item_information(menu_item_id: int) -> Any:
    """Get information about a menu item."""
    return make_request("GET", f"/food/menuItems/{menu_item_id}")


@mcp.tool()
def autocomplete_menu_item_search(query: str, number: Optional[int] = None) -> Any:
    """Autocomplete menu item search."""
    params = {"query": query}
    
    if number is not None:
        params["number"] = number
    
    return make_request("GET", "/food/menuItems/autocomplete", params)


# ============================================================================
# PRODUCTS ENDPOINTS
# ============================================================================

@mcp.tool()
def search_grocery_products(
    query: str,
    min_calories: Optional[int] = None,
    max_calories: Optional[int] = None,
    min_carbs: Optional[float] = None,
    max_carbs: Optional[float] = None,
    min_protein: Optional[float] = None,
    max_protein: Optional[float] = None,
    min_fat: Optional[float] = None,
    max_fat: Optional[float] = None,
    add_product_information: Optional[bool] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Any:
    """Search grocery products."""
    params = {"query": query}
    
    if min_calories is not None:
        params["minCalories"] = min_calories
    if max_calories is not None:
        params["maxCalories"] = max_calories
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
    if add_product_information is not None:
        params["addProductInformation"] = add_product_information
    if offset is not None:
        params["offset"] = offset
    if number is not None:
        params["number"] = number
    
    return make_request("GET", "/food/products/search", params)


@mcp.tool()
def get_grocery_products_overview() -> Any:
    """Get an overview of grocery products."""
    return make_request("GET", "/food/products")


@mcp.tool()
def search_grocery_products_by_upc(upc: str) -> Any:
    """Search grocery products by UPC code."""
    params = {"upc": upc}
    return make_request("GET", "/food/products/upc/{upc}", params)


@mcp.tool()
def get_product_information(product_id: int) -> Any:
    """Get information about a product."""
    return make_request("GET", f"/food/products/{product_id}")


@mcp.tool()
def get_comparable_products(product_id: int) -> Any:
    """Get comparable products."""
    return make_request("GET", f"/food/products/{product_id}/comparable")


@mcp.tool()
def autocomplete_product_search(query: str, number: Optional[int] = None) -> Any:
    """Autocomplete product search."""
    params = {"query": query}
    
    if number is not None:
        params["number"] = number
    
    return make_request("GET", "/food/products/autocomplete", params)


@mcp.tool()
def classify_grocery_product(
    product_name: str,
    nutrition: Optional[str] = None,
) -> Any:
    """Classify a grocery product."""
    params = {"productName": product_name}
    
    if nutrition is not None:
        params["nutrition"] = nutrition
    
    return make_request("POST", "/food/products/classify", params)


@mcp.tool()
def classify_grocery_product_bulk(products: str) -> Any:
    """Classify multiple grocery products."""
    params = {"products": products}
    return make_request("POST", "/food/products/classifyBatch", params)


@mcp.tool()
def map_ingredients_to_grocery_products(
    ingredients: str,
    number: Optional[int] = None,
) -> Any:
    """Map ingredients to grocery products."""
    params = {"ingredients": ingredients}
    
    if number is not None:
        params["number"] = number
    
    return make_request("POST", "/food/ingredients/map", params)


# ============================================================================
# WINE ENDPOINTS
# ============================================================================

@mcp.tool()
def get_wine_pairing(food: str, max_price: Optional[float] = None) -> Any:
    """Get wine pairing recommendations for a food."""
    params = {"food": food}
    
    if max_price is not None:
        params["maxPrice"] = max_price
    
    return make_request("GET", "/food/wine/pairing", params)


@mcp.tool()
def get_wine_description(wine: str) -> Any:
    """Get a description of a wine."""
    params = {"wine": wine}
    return make_request("GET", "/food/wine/description", params)


@mcp.tool()
def get_wine_recommendation(
    wine: str,
    max_price: Optional[float] = None,
    min_rating: Optional[float] = None,
    number: Optional[int] = None,
) -> Any:
    """Get wine recommendations."""
    params = {"wine": wine}
    
    if max_price is not None:
        params["maxPrice"] = max_price
    if min_rating is not None:
        params["minRating"] = min_rating
    if number is not None:
        params["number"] = number
    
    return make_request("GET", "/food/wine/recommendation", params)


# ============================================================================
# MISC ENDPOINTS
# ============================================================================

@mcp.tool()
def search_all_food(query: str, number: Optional[int] = None, offset: Optional[int] = None) -> Any:
    """Search all food items."""
    params = {"query": query}
    
    if number is not None:
        params["number"] = number
    if offset is not None:
        params["offset"] = offset
    
    return make_request("GET", "/food/search", params)


@mcp.tool()
def search_food_videos(query: str, number: Optional[int] = None) -> Any:
    """Search food videos."""
    params = {"query": query}
    
    if number is not None:
        params["number"] = number
    
    return make_request("GET", "/food/videos/search", params)


@mcp.tool()
def get_quick_answer(query: str) -> Any:
    """Get a quick answer to a food question."""
    params = {"q": query}
    return make_request("GET", "/recipes/quickAnswer", params)


@mcp.tool()
def detect_food_in_text(text: str) -> Any:
    """Detect food items mentioned in text."""
    params = {"text": text}
    return make_request("POST", "/food/detect", params)


@mcp.tool()
def search_site_content(query: str) -> Any:
    """Search site content."""
    params = {"query": query}
    return make_request("GET", "/food/site/search", params)


@mcp.tool()
def get_random_food_joke() -> Any:
    """Get a random food joke."""
    return make_request("GET", "/food/jokes/random")


@mcp.tool()
def get_random_food_trivia() -> Any:
    """Get random food trivia."""
    return make_request("GET", "/food/trivia/random")


@mcp.tool()
def talk_to_chatbot(text: str, context_id: Optional[str] = None) -> Any:
    """Talk to the food chatbot."""
    params = {"text": text}
    
    if context_id is not None:
        params["contextId"] = context_id
    
    return make_request("POST", "/food/converse", params)


@mcp.tool()
def get_conversation_suggests(query: str, context_id: Optional[str] = None) -> Any:
    """Get conversation suggestions."""
    params = {"query": query}
    
    if context_id is not None:
        params["contextId"] = context_id
    
    return make_request("GET", "/food/converse/suggest", params)


@mcp.tool()
def classify_image(image_url: str) -> Any:
    """Classify food in an image."""
    params = {"imageUrl": image_url}
    return make_request("POST", "/food/images/classify", params)


if __name__ == "__main__":
    mcp.run()
