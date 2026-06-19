import os
import requests
from typing import Any, Dict, List, Optional, Union
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Spoonacular")

# Base URL for Spoonacular API
BASE_URL = "https://api.spoonacular.com"

def make_request(method: str, endpoint: str, params: Dict[str, Any] = None, data: Dict[str, Any] = None) -> Any:
    """Helper function to make requests to the Spoonacular API."""
    api_key = os.environ.get("SPOONACULAR_API_KEY")
    if not api_key:
        return {"error": "SPOONACULAR_API_KEY environment variable is not set."}
    
    if params is None:
        params = {}
    params["apiKey"] = api_key
    
    url = f"{BASE_URL}{endpoint}"
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, params=params, data=data)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
            
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        try:
            return {"error": response.json().get("message", str(e))}
        except Exception:
            return {"error": str(e)}

@mcp.tool()
def search_recipes(query: str, cuisine: Optional[str] = None, diet: Optional[str] = None, intolerances: Optional[str] = None, type: Optional[str] = None, maxReadyTime: Optional[int] = None, number: int = 10) -> Any:
    """Search recipes by query and filters."""
    params = {
        "query": query,
        "number": number
    }
    if cuisine: params["cuisine"] = cuisine
    if diet: params["diet"] = diet
    if intolerances: params["intolerances"] = intolerances
    if type: params["type"] = type
    if maxReadyTime: params["maxReadyTime"] = maxReadyTime
    return make_request("GET", "/recipes/complexSearch", params=params)

@mcp.tool()
def search_recipes_by_nutrients(minCarbs: Optional[int] = None, maxCarbs: Optional[int] = None, minProtein: Optional[int] = None, maxProtein: Optional[int] = None, minCalories: Optional[int] = None, maxCalories: Optional[int] = None, minFat: Optional[int] = None, maxFat: Optional[int] = None, number: int = 10) -> Any:
    """Search recipes by nutrients."""
    params = {"number": number}
    if minCarbs is not None: params["minCarbs"] = minCarbs
    if maxCarbs is not None: params["maxCarbs"] = maxCarbs
    if minProtein is not None: params["minProtein"] = minProtein
    if maxProtein is not None: params["maxProtein"] = maxProtein
    if minCalories is not None: params["minCalories"] = minCalories
    if maxCalories is not None: params["maxCalories"] = maxCalories
    if minFat is not None: params["minFat"] = minFat
    if maxFat is not None: params["maxFat"] = maxFat
    return make_request("GET", "/recipes/findByNutrients", params=params)

@mcp.tool()
def search_recipes_by_ingredients(ingredients: str, number: int = 10, limitLicense: bool = True, ranking: int = 1, ignorePantry: bool = True) -> Any:
    """Search recipes by ingredients."""
    params = {
        "ingredients": ingredients,
        "number": number,
        "limitLicense": limitLicense,
        "ranking": ranking,
        "ignorePantry": ignorePantry
    }
    return make_request("GET", "/recipes/findByIngredients", params=params)

@mcp.tool()
def get_recipe_information(id: int, includeNutrition: bool = False) -> Any:
    """Get information about a specific recipe."""
    params = {"includeNutrition": includeNutrition}
    return make_request("GET", f"/recipes/{id}/information", params=params)

@mcp.tool()
def get_recipe_ingredients(id: int) -> Any:
    """Get ingredients for a specific recipe."""
    return make_request("GET", f"/recipes/{id}/ingredientWidget.json")

@mcp.tool()
def get_recipe_nutrition(id: int) -> Any:
    """Get nutrition for a specific recipe."""
    return make_request("GET", f"/recipes/{id}/nutritionWidget.json")

@mcp.tool()
def get_recipe_instructions(id: int, stepBreakdown: bool = True) -> Any:
    """Get analyzed instructions for a specific recipe."""
    params = {"stepBreakdown": stepBreakdown}
    return make_request("GET", f"/recipes/{id}/analyzedInstructions", params=params)

@mcp.tool()
def get_similar_recipes(id: int, number: int = 10) -> Any:
    """Get similar recipes to a specific recipe."""
    params = {"number": number}
    return make_request("GET", f"/recipes/{id}/similar", params=params)

@mcp.tool()
def search_ingredients(query: str, number: int = 10, intolerances: Optional[str] = None) -> Any:
    """Search for ingredients."""
    params = {"query": query, "number": number}
    if intolerances: params["intolerances"] = intolerances
    return make_request("GET", "/food/ingredients/search", params=params)

@mcp.tool()
def get_ingredient_information(id: int, amount: Optional[float] = None, unit: Optional[str] = None) -> Any:
    """Get information about a specific ingredient."""
    params = {}
    if amount is not None: params["amount"] = amount
    if unit is not None: params["unit"] = unit
    return make_request("GET", f"/food/ingredients/{id}/information", params=params)

@mcp.tool()
def parse_ingredients(ingredientList: str, servings: int = 1, includeNutrition: bool = False) -> Any:
    """Parse ingredients."""
    data = {"ingredientList": ingredientList}
    params = {"servings": servings, "includeNutrition": includeNutrition}
    return make_request("POST", "/recipes/parseIngredients", params=params, data=data)

@mcp.tool()
def generate_meal_plan(timeFrame: str = "day", targetCalories: Optional[int] = None, diet: Optional[str] = None, exclude: Optional[str] = None) -> Any:
    """Generate a meal plan."""
    params = {"timeFrame": timeFrame}
    if targetCalories is not None: params["targetCalories"] = targetCalories
    if diet: params["diet"] = diet
    if exclude: params["exclude"] = exclude
    return make_request("GET", "/mealplanner/generate", params=params)

@mcp.tool()
def get_meal_plan_week(username: str, start_date: str, hash: str) -> Any:
    """Get a meal plan for a week."""
    params = {"hash": hash}
    return make_request("GET", f"/mealplanner/{username}/week/{start_date}", params=params)

@mcp.tool()
def get_meal_plan_day(username: str, date: str, hash: str) -> Any:
    """Get a meal plan for a day."""
    params = {"hash": hash}
    return make_request("GET", f"/mealplanner/{username}/day/{date}", params=params)

@mcp.tool()
def get_wine_pairing(food: str, maxPrice: Optional[float] = None) -> Any:
    """Get a wine pairing for a dish."""
    params = {"food": food}
    if maxPrice is not None: params["maxPrice"] = maxPrice
    return make_request("GET", "/food/wine/pairing", params=params)

@mcp.tool()
def get_wine_description(wine: str) -> Any:
    """Get a description of a wine."""
    params = {"wine": wine}
    return make_request("GET", "/food/wine/description", params=params)

@mcp.tool()
def autocomplete_recipe_search(query: str, number: int = 10) -> Any:
    """Autocomplete a recipe search."""
    params = {"query": query, "number": number}
    return make_request("GET", "/recipes/autocomplete", params=params)

@mcp.tool()
def autocomplete_ingredient_search(query: str, number: int = 10, metaInformation: bool = False) -> Any:
    """Autocomplete an ingredient search."""
    params = {"query": query, "number": number, "metaInformation": metaInformation}
    return make_request("GET", "/food/ingredients/autocomplete", params=params)

@mcp.tool()
def visualize_recipe_nutrition(id: int, defaultCss: bool = True) -> Any:
    """Visualize recipe nutrition as an HTML widget."""
    params = {"defaultCss": defaultCss}
    return make_request("GET", f"/recipes/{id}/nutritionWidget", params=params)

if __name__ == "__main__":
    mcp.run()
