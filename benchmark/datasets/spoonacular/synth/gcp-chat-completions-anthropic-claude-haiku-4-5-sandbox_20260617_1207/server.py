#!/usr/bin/env python3
"""
MCP Server for Spoonacular Food API
Provides comprehensive tools for recipe search, ingredient lookup, meal planning, and more.
"""

import os
import json
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("spoonacular")

# Get API key from environment
API_KEY = os.getenv("SPOONACULAR_API_KEY")
BASE_URL = "https://api.spoonacular.com"

if not API_KEY:
    raise ValueError("SPOONACULAR_API_KEY environment variable is required")


def make_request(endpoint: str, method: str = "GET", params: Optional[dict] = None, data: Optional[dict] = None) -> dict:
    """Make a request to the Spoonacular API."""
    if params is None:
        params = {}
    
    params["apiKey"] = API_KEY
    url = f"{BASE_URL}{endpoint}"
    
    try:
        if method == "GET":
            response = requests.get(url, params=params, timeout=10)
        elif method == "POST":
            response = requests.post(url, params=params, data=data, timeout=10)
        elif method == "DELETE":
            response = requests.delete(url, params=params, timeout=10)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Failed to parse API response as JSON"}


# ============================================================================
# MISC ENDPOINTS
# ============================================================================

@mcp.tool()
def search_all_food(query: str, offset: int = 0, number: int = 10) -> dict:
    """Search all food content (recipes, products, menu items, etc.)."""
    return make_request("/food/search", params={"query": query, "offset": offset, "number": number})

@mcp.tool()
def search_food_videos(query: str, type: Optional[str] = None, cuisine: Optional[str] = None, diet: Optional[str] = None, includeIngredients: Optional[str] = None, excludeIngredients: Optional[str] = None, minLength: int = 0, maxLength: int = 999, offset: int = 0, number: int = 10) -> dict:
    """Search food videos."""
    params = {"query": query, "minLength": minLength, "maxLength": maxLength, "offset": offset, "number": number}
    for k, v in [("type", type), ("cuisine", cuisine), ("diet", diet), ("includeIngredients", includeIngredients), ("excludeIngredients", excludeIngredients)]:
        if v is not None: params[k] = v
    return make_request("/food/videos/search", params=params)

@mcp.tool()
def get_quick_answer(q: str) -> dict:
    """Get a quick answer to a nutrition question."""
    return make_request("/recipes/quickAnswer", params={"q": q})

@mcp.tool()
def detect_food_in_text(text: str) -> dict:
    """Detect food items mentioned in text."""
    return make_request("/food/detect", method="POST", data={"text": text})

@mcp.tool()
def search_site_content(query: str) -> dict:
    """Search spoonacular site content."""
    return make_request("/food/site/search", params={"query": query})

@mcp.tool()
def get_random_food_joke() -> dict:
    """Get a random food joke."""
    return make_request("/food/jokes/random")

@mcp.tool()
def get_random_food_trivia() -> dict:
    """Get random food trivia."""
    return make_request("/food/trivia/random")

@mcp.tool()
def talk_to_chatbot(text: str, contextId: Optional[str] = None) -> dict:
    """Talk to the spoonacular chatbot."""
    params = {"text": text}
    if contextId: params["contextId"] = contextId
    return make_request("/food/converse", params=params)

@mcp.tool()
def get_conversation_suggests(query: str, contextId: Optional[str] = None) -> dict:
    """Get conversation suggestions."""
    params = {"query": query}
    if contextId: params["contextId"] = contextId
    return make_request("/food/converse/suggest", params=params)


if __name__ == "__main__":
    mcp.run()=================================
# RECIPES ENDPOINTS
# ============================================================================

@mcp.tool()
def search_recipes(query: str, cuisine: Optional[str] = None, diet: Optional[str] = None, intolerances: Optional[str] = None, type: Optional[str] = None, instructionsRequired: bool = False, fillIngredients: bool = False, addRecipeInformation: bool = False, addRecipeInstructions: bool = False, addRecipeNutrition: bool = False, maxReadyTime: Optional[int] = None, minServings: Optional[int] = None, maxServings: Optional[int] = None, offset: int = 0, number: int = 10, minCalories: Optional[int] = None, maxCalories: Optional[int] = None, minProtein: Optional[int] = None, maxProtein: Optional[int] = None, minFat: Optional[int] = None, maxFat: Optional[int] = None, minCarbs: Optional[int] = None, maxCarbs: Optional[int] = None, sort: Optional[str] = None, sortDirection: Optional[str] = None) -> dict:
    """Search through thousands of recipes using advanced filtering and ranking."""
    params = {"query": query, "offset": offset, "number": number, "instructionsRequired": instructionsRequired, "fillIngredients": fillIngredients, "addRecipeInformation": addRecipeInformation, "addRecipeInstructions": addRecipeInstructions, "addRecipeNutrition": addRecipeNutrition}
    for k, v in [("cuisine", cuisine), ("diet", diet), ("intolerances", intolerances), ("type", type), ("maxReadyTime", maxReadyTime), ("minServings", minServings), ("maxServings", maxServings), ("minCalories", minCalories), ("maxCalories", maxCalories), ("minProtein", minProtein), ("maxProtein", maxProtein), ("minFat", minFat), ("maxFat", maxFat), ("minCarbs", minCarbs), ("maxCarbs", maxCarbs), ("sort", sort), ("sortDirection", sortDirection)]:
        if v is not None: params[k] = v
    return make_request("/recipes/complexSearch", params=params)

@mcp.tool()
def search_recipes_by_nutrients(minCalories: Optional[int] = None, maxCalories: Optional[int] = None, minProtein: Optional[int] = None, maxProtein: Optional[int] = None, minFat: Optional[int] = None, maxFat: Optional[int] = None, minCarbs: Optional[int] = None, maxCarbs: Optional[int] = None, offset: int = 0, number: int = 10) -> dict:
    """Find recipes that adhere to given nutritional limits."""
    params = {"offset": offset, "number": number}
    for k, v in [("minCalories", minCalories), ("maxCalories", maxCalories), ("minProtein", minProtein), ("maxProtein", maxProtein), ("minFat", minFat), ("maxFat", maxFat), ("minCarbs", minCarbs), ("maxCarbs", maxCarbs)]:
        if v is not None: params[k] = v
    return make_request("/recipes/findByNutrients", params=params)

@mcp.tool()
def search_recipes_by_ingredients(ingredients: str, number: int = 10, ranking: int = 2, ignorePantry: bool = False) -> dict:
    """Search recipes by ingredients."""
    return make_request("/recipes/findByIngredients", params={"ingredients": ingredients, "number": number, "ranking": ranking, "ignorePantry": ignorePantry})

@mcp.tool()
def get_recipe_information(id: int, includeNutrition: bool = False) -> dict:
    """Get detailed information about a recipe."""
    return make_request(f"/recipes/{id}/information", params={"includeNutrition": includeNutrition})

@mcp.tool()
def get_recipe_information_bulk(ids: str, includeNutrition: bool = False) -> dict:
    """Get information about multiple recipes at once."""
    return make_request("/recipes/informationBulk", params={"ids": ids, "includeNutrition": includeNutrition})

@mcp.tool()
def get_similar_recipes(id: int, number: int = 10) -> dict:
    """Get similar recipes to a given recipe."""
    return make_request(f"/recipes/{id}/similar", params={"number": number})

@mcp.tool()
def get_random_recipes(number: int = 10, tags: Optional[str] = None) -> dict:
    """Get random recipes."""
    params = {"number": number}
    if tags: params["tags"] = tags
    return make_request("/recipes/random", params=params)

@mcp.tool()
def autocomplete_recipe_search(query: str, number: int = 10) -> dict:
    """Autocomplete recipe search."""
    return make_request("/recipes/autocomplete", params={"query": query, "number": number})

@mcp.tool()
def get_recipe_taste_by_id(id: int) -> dict:
    """Get taste profile of a recipe by ID."""
    return make_request(f"/recipes/{id}/tasteWidget.json")

@mcp.tool()
def get_recipe_equipment_by_id(id: int) -> dict:
    """Get equipment needed for a recipe by ID."""
    return make_request(f"/recipes/{id}/equipmentWidget.json")

@mcp.tool()
def get_recipe_price_breakdown_by_id(id: int) -> dict:
    """Get price breakdown of a recipe by ID."""
    return make_request(f"/recipes/{id}/priceBreakdownWidget.json")

@mcp.tool()
def get_recipe_ingredients_by_id(id: int) -> dict:
    """Get ingredients of a recipe by ID."""
    return make_request(f"/recipes/{id}/ingredientsWidget.json")

@mcp.tool()
def get_recipe_nutrition_by_id(id: int) -> dict:
    """Get nutrition information of a recipe by ID."""
    return make_request(f"/recipes/{id}/nutritionWidget.json")

@mcp.tool()
def get_analyzed_recipe_instructions(id: int) -> dict:
    """Get analyzed recipe instructions."""
    return make_request(f"/recipes/{id}/analyzedInstructions")

@mcp.tool()
def extract_recipe_from_website(url: str) -> dict:
    """Extract recipe information from a website URL."""
    return make_request("/recipes/extract", params={"url": url})

@mcp.tool()
def analyze_recipe(title: str, ingredients: str, servings: int = 1) -> dict:
    """Analyze a recipe."""
    return make_request("/recipes/analyze", method="POST", data={"title": title, "ingredients": ingredients, "servings": servings})

@mcp.tool()
def summarize_recipe(id: int) -> dict:
    """Summarize a recipe."""
    return make_request(f"/recipes/{id}/summary")

@mcp.tool()
def analyze_recipe_instructions(instructions: str) -> dict:
    """Analyze recipe instructions."""
    return make_request("/recipes/analyzeInstructions", method="POST", data={"instructions": instructions})

@mcp.tool()
def classify_cuisine(title: str, ingredients: str) -> dict:
    """Classify the cuisine of a recipe."""
    return make_request("/recipes/cuisine", method="POST", data={"title": title, "ingredients": ingredients})

@mcp.tool()
def analyze_recipe_search_query(q: str) -> dict:
    """Analyze a recipe search query."""
    return make_request("/recipes/queries/analyze", params={"q": q})

# ============================================================================
# INGREDIENTS ENDPOINTS
# ============================================================================

@mcp.tool()
def search_ingredients(query: str, addChildren: bool = False, number: int = 10, offset: int = 0, sort: Optional[str] = None, sortDirection: Optional[str] = None) -> dict:
    """Search for ingredients."""
    params = {"query": query, "addChildren": addChildren, "number": number, "offset": offset}
    if sort: params["sort"] = sort
    if sortDirection: params["sortDirection"] = sortDirection
    return make_request("/food/ingredients/search", params=params)

@mcp.tool()
def get_ingredient_information(id: int, amount: Optional[float] = None, unit: Optional[str] = None) -> dict:
    """Get detailed information about an ingredient."""
    params = {}
    if amount: params["amount"] = amount
    if unit: params["unit"] = unit
    return make_request(f"/food/ingredients/{id}/information", params=params)

@mcp.tool()
def compute_ingredient_amount(id: int, nutrient: str, target: float, unit: Optional[str] = None) -> dict:
    """Compute the amount of an ingredient needed for a nutritional goal."""
    params = {"nutrient": nutrient, "target": target}
    if unit: params["unit"] = unit
    return make_request(f"/food/ingredients/{id}/amount", params=params)

@mcp.tool()
def convert_amounts(ingredientName: str, sourceAmount: float, sourceUnit: str, targetUnit: str) -> dict:
    """Convert ingredient amounts between units."""
    return make_request("/recipes/convert", params={"ingredientName": ingredientName, "sourceAmount": sourceAmount, "sourceUnit": sourceUnit, "targetUnit": targetUnit})

@mcp.tool()
def parse_ingredients(ingredientList: str, servings: int = 1, includeNutrition: bool = False) -> dict:
    """Parse ingredients from plain text."""
    return make_request("/recipes/parseIngredients", method="POST", data={"ingredientList": ingredientList, "servings": servings, "includeNutrition": includeNutrition})

@mcp.tool()
def autocomplete_ingredient_search(query: str, number: int = 10) -> dict:
    """Autocomplete ingredient search."""
    return make_request("/food/ingredients/autocomplete", params={"query": query, "number": number})

@mcp.tool()
def get_ingredient_substitutes(ingredientName: str) -> dict:
    """Get substitutes for an ingredient."""
    return make_request("/food/ingredients/substitutes", params={"ingredientName": ingredientName})

@mcp.tool()
def get_ingredient_substitutes_by_id(id: int) -> dict:
    """Get substitutes for an ingredient by ID."""
    return make_request(f"/food/ingredients/{id}/substitutes")

# ============================================================================
# MENU ITEMS ENDPOINTS
# ============================================================================

@mcp.tool()
def search_menu_items(query: str, minCalories: Optional[int] = None, maxCalories: Optional[int] = None, minCarbs: Optional[int] = None, maxCarbs: Optional[int] = None, minProtein: Optional[int] = None, maxProtein: Optional[int] = None, minFat: Optional[int] = None, maxFat: Optional[int] = None, addMenuItemInformation: bool = False, offset: int = 0, number: int = 10) -> dict:
    """Search menu items from restaurants."""
    params = {"query": query, "addMenuItemInformation": addMenuItemInformation, "offset": offset, "number": number}
    for k, v in [("minCalories", minCalories), ("maxCalories", maxCalories), ("minCarbs", minCarbs), ("maxCarbs", maxCarbs), ("minProtein", minProtein), ("maxProtein", maxProtein), ("minFat", minFat), ("maxFat", maxFat)]:
        if v is not None: params[k] = v
    return make_request("/food/menuItems/search", params=params)

@mcp.tool()
def get_menu_item_information(id: int) -> dict:
    """Get detailed information about a menu item."""
    return make_request(f"/food/menuItems/{id}")

@mcp.tool()
def autocomplete_menu_item_search(query: str, number: int = 10) -> dict:
    """Autocomplete menu item search."""
    return make_request("/food/menuItems/suggest", params={"query": query, "number": number})

# ============================================================================
# PRODUCTS ENDPOINTS
# ============================================================================

@mcp.tool()
def search_grocery_products(query: str, minCalories: Optional[int] = None, maxCalories: Optional[int] = None, minCarbs: Optional[int] = None, maxCarbs: Optional[int] = None, minProtein: Optional[int] = None, maxProtein: Optional[int] = None, minFat: Optional[int] = None, maxFat: Optional[int] = None, addProductInformation: bool = False, offset: int = 0, number: int = 10) -> dict:
    """Search grocery products."""
    params = {"query": query, "addProductInformation": addProductInformation, "offset": offset, "number": number}
    for k, v in [("minCalories", minCalories), ("maxCalories", maxCalories), ("minCarbs", minCarbs), ("maxCarbs", maxCarbs), ("minProtein", minProtein), ("maxProtein", maxProtein), ("minFat", minFat), ("maxFat", maxFat)]:
        if v is not None: params[k] = v
    return make_request("/food/products/search", params=params)

@mcp.tool()
def search_grocery_products_by_upc(upc: str) -> dict:
    """Search grocery products by UPC code."""
    return make_request(f"/food/products/upc/{upc}")

@mcp.tool()
def get_product_information(id: int) -> dict:
    """Get detailed information about a product."""
    return make_request(f"/food/products/{id}")

@mcp.tool()
def get_comparable_products(id: int) -> dict:
    """Get comparable products."""
    return make_request(f"/food/products/{id}/comparable")

@mcp.tool()
def autocomplete_product_search(query: str, number: int = 10) -> dict:
    """Autocomplete product search."""
    return make_request("/food/products/suggest", params={"query": query, "number": number})

@mcp.tool()
def classify_grocery_product(upcCode: str, title: Optional[str] = None) -> dict:
    """Classify a grocery product."""
    data = {"upcCode": upcCode}
    if title: data["title"] = title
    return make_request("/food/products/classify", method="POST", data=data)

@mcp.tool()
def classify_grocery_product_bulk(products: str) -> dict:
    """Classify multiple grocery products."""
    return make_request("/food/products/classifyBulk", method="POST", data={"products": products})

@mcp.tool()
def map_ingredients_to_grocery_products(ingredients: str) -> dict:
    """Map ingredients to grocery products."""
    return make_request("/food/ingredients/map", method="POST", data={"ingredients": ingredients})

# ============================================================================
# MEAL PLANNING ENDPOINTS
# ============================================================================

@mcp.tool()
def get_meal_plan_week(username: str, start_date: str, hash: str) -> dict:
    """Get a meal plan for a week."""
    return make_request(f"/mealplanner/{username}/week/{start_date}", params={"hash": hash})

@mcp.tool()
def get_meal_plan_day(username: str, date: str, hash: str) -> dict:
    """Get a meal plan for a day."""
    return make_request(f"/mealplanner/{username}/day/{date}", params={"hash": hash})

@mcp.tool()
def generate_meal_plan(timeFrame: str = "day", targetCalories: Optional[int] = None, diet: Optional[str] = None, exclude: Optional[str] = None) -> dict:
    """Generate a meal plan."""
    params = {"timeFrame": timeFrame}
    if targetCalories: params["targetCalories"] = targetCalories
    if diet: params["diet"] = diet
    if exclude: params["exclude"] = exclude
    return make_request("/mealplanner/generate", params=params)

@mcp.tool()
def add_to_meal_plan(username: str, hash: str, date: str, slot: int, type: str, value: dict) -> dict:
    """Add an item to a meal plan."""
    data = {"date": date, "slot": slot, "type": type, "value": json.dumps(value)}
    return make_request(f"/mealplanner/{username}/items", method="POST", params={"hash": hash}, data=data)

@mcp.tool()
def clear_meal_plan_day(username: str, date: str, hash: str) -> dict:
    """Clear a meal plan day."""
    return make_request(f"/mealplanner/{username}/day/{date}", method="DELETE", params={"hash": hash})

@mcp.tool()
def delete_from_meal_plan(username: str, item_id: int, hash: str) -> dict:
    """Delete an item from a meal plan."""
    return make_request(f"/mealplanner/{username}/items/{item_id}", method="DELETE", params={"hash": hash})

@mcp.tool()
def get_meal_plan_templates() -> dict:
    """Get meal plan templates."""
    return make_request("/mealplanner/templates")

@mcp.tool()
def get_meal_plan_template(id: int) -> dict:
    """Get a specific meal plan template."""
    return make_request(f"/mealplanner/templates/{id}")

@mcp.tool()
def add_meal_plan_template(username: str, hash: str, name: str) -> dict:
    """Add a meal plan template."""
    return make_request(f"/mealplanner/{username}/templates", method="POST", params={"hash": hash}, data={"name": name})

@mcp.tool()
def delete_meal_plan_template(username: str, id: int, hash: str) -> dict:
    """Delete a meal plan template."""
    return make_request(f"/mealplanner/{username}/templates/{id}", method="DELETE", params={"hash": hash})

@mcp.tool()
def get_shopping_list(username: str, hash: str) -> dict:
    """Get a shopping list."""
    return make_request(f"/mealplanner/{username}/shopping-list", params={"hash": hash})

@mcp.tool()
def add_to_shopping_list(username: str, hash: str, item: str, aisle: Optional[str] = None, parse: bool = True) -> dict:
    """Add an item to a shopping list."""
    data = {"item": item, "parse": parse}
    if aisle: data["aisle"] = aisle
    return make_request(f"/mealplanner/{username}/shopping-list/items", method="POST", params={"hash": hash}, data=data)

@mcp.tool()
def delete_from_shopping_list(username: str, item_id: int, hash: str) -> dict:
    """Delete an item from a shopping list."""
    return make_request(f"/mealplanner/{username}/shopping-list/items/{item_id}", method="DELETE", params={"hash": hash})

@mcp.tool()
def generate_shopping_list(username: str, start_date: str, end_date: str, hash: str) -> dict:
    """Generate a shopping list from a meal plan."""
    return make_request(f"/mealplanner/{username}/shopping-list/generate", params={"hash": hash, "start-date": start_date, "end-date": end_date})

@mcp.tool()
def compute_shopping_list(username: str, start_date: str, end_date: str, hash: str) -> dict:
    """Compute a shopping list."""
    return make_request(f"/mealplanner/{username}/shopping-list/compute", params={"hash": hash, "start-date": start_date, "end-date": end_date})

@mcp.tool()
def connect_user(body: dict) -> dict:
    """Connect a user to the meal planner."""
    return make_request("/users/connect", method="POST", data=body)

# ============================================================================
# WINE ENDPOINTS
# ============================================================================

@mcp.tool()
def get_wine_pairing(food: str, maxPrice: Optional[int] = None) -> dict:
    """Get wine pairing recommendations for a food."""
    params = {"food": food}
    if maxPrice: params["maxPrice"] = maxPrice
    return make_request("/food/wine/pairing", params=params)

@mcp.tool()
def get_wine_pairing_for_dish(wine: str) -> dict:
    """Get dish pairing recommendations for a wine."""
    return make_request("/food/wine/dishes", params={"wine": wine})

@mcp.tool()
def get_wine_description(wine: str) -> dict:
    """Get a description of a wine."""
    return make_request("/food/wine/description", params={"wine": wine})

@mcp.tool()
def get_wine_recommendation(wine: str, maxPrice: Optional[int] = None, minRating: Optional[float] = None, number: int = 3) -> dict:
    """Get wine recommendations."""
    params = {"wine": wine, "number": number}
    if maxPrice: params["maxPrice"] = maxPrice
    if minRating: params["minRating"] = minRating
    return make_request("/food/wine/recommendation", params=params)

# ============================================================================
# MISC ENDPOINTS
# ============================================================================

@mcp.tool()
def search_all_food(query: str, offset: int = 0, number: int = 10) -> dict:
    """Search all food content (recipes, products, menu items, etc.)."""
    return make_request("/food/search", params={"query": query, "offset": offset, "number": number})

@mcp.tool()
def search_food_videos(query: str, type: Optional[str] = None, cuisine: Optional[str] = None, diet: Optional[str] = None, includeIngredients: Optional[str] = None, excludeIngredients: Optional[str] = None, minLength: int = 0, maxLength: int = 999, offset: int = 0, number: int = 10) -> dict:
    """Search food videos."""
    params = {"query": query, "minLength": minLength, "maxLength": maxLength, "offset": offset, "number": number}
    for k, v in [("type", type), ("cuisine", cuisine), ("diet", diet), ("includeIngredients", includeIngredients), ("excludeIngredients", excludeIngredients)]:
        if v is not None: params[k] = v
    return make_request("/food/videos/search", params=params)

@mcp.tool()
def get_quick_answer(q: str) -> dict:
    """Get a quick answer to a nutrition question."""
    return make_request("/recipes/quickAnswer", params={"q": q})

@mcp.tool()
def detect_food_in_text(text: str) -> dict:
    """Detect food items mentioned in text."""
    return make_request("/food/detect", method="POST", data={"text": text})

@mcp.tool()
def search_site_content(query: str) -> dict:
    """Search spoonacular site content."""
    return make_request("/food/site/search", params={"query": query})

@mcp.tool()
def get_random_food_joke() -> dict:
    """Get a random food joke."""
    return make_request("/food/jokes/random")

@mcp.tool()
def get_random_food_trivia() -> dict:
    """Get random food trivia."""
    return make_request("/food/trivia/random")

@mcp.tool()
def talk_to_chatbot(text: str, contextId: Optional[str] = None) -> dict:
    """Talk to the spoonacular chatbot."""
    params = {"text": text}
    if contextId: params["contextId"] = contextId
    return make_request("/food/converse", params=params)

@mcp.tool()
def get_conversation_suggests(query: str, contextId: Optional[str] = None) -> dict:
    """Get conversation suggestions."""
    params = {"query": query}
    if contextId: params["contextId"] = contextId
    return make_request("/food/converse/suggest", params=params)


if __name__ == "__main__":
    mcp.run()
