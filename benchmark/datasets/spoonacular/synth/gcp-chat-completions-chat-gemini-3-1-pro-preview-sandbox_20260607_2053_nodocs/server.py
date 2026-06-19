import os
import requests
from typing import Optional, List, Dict, Any
from fastmcp import FastMCP

mcp = FastMCP("spoonacular")

BASE_URL = "https://api.spoonacular.com"

def get_api_key() -> str:
    return os.environ.get("SPOONACULAR_API_KEY", "")

def make_request(method: str, endpoint: str, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> Any:
    if params is None:
        params = {}
    params["apiKey"] = get_api_key()
    
    url = f"{BASE_URL}{endpoint}"
    try:
        if method.upper() == "GET":
            response = requests.get(url, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, params=params, data=data)
        else:
            return {"error": f"Unsupported method {method}"}
            
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        try:
            return {"error": str(e), "details": response.json()}
        except Exception:
            return {"error": str(e)}

@mcp.tool()
def search_recipes_complex(
    query: Optional[str] = None,
    cuisine: Optional[str] = None,
    diet: Optional[str] = None,
    intolerances: Optional[str] = None,
    equipment: Optional[str] = None,
    includeIngredients: Optional[str] = None,
    excludeIngredients: Optional[str] = None,
    type: Optional[str] = None,
    instructionsRequired: Optional[bool] = None,
    fillIngredients: Optional[bool] = None,
    addRecipeInformation: Optional[bool] = None,
    addRecipeNutrition: Optional[bool] = None,
    maxReadyTime: Optional[int] = None,
    minServings: Optional[int] = None,
    maxServings: Optional[int] = None,
    ignorePantry: Optional[bool] = None,
    sort: Optional[str] = None,
    sortDirection: Optional[str] = None,
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None
) -> Any:
    """Search through hundreds of thousands of recipes using advanced filtering and ranking."""
    params = {k: v for k, v in locals().items() if v is not None}
    return make_request("GET", "/recipes/complexSearch", params=params)

@mcp.tool()
def search_recipes_by_ingredients(
    ingredients: str,
    number: Optional[int] = None,
    limitLicense: Optional[bool] = None,
    ranking: Optional[int] = None,
    ignorePantry: Optional[bool] = None
) -> Any:
    """Find recipes that use as many of the given ingredients as possible and require as few additional ingredients as possible."""
    params = {k: v for k, v in locals().items() if v is not None}
    return make_request("GET", "/recipes/findByIngredients", params=params)

@mcp.tool()
def search_recipes_by_nutrients(
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None
) -> Any:
    """Find a set of recipes that adhere to the given nutritional limits."""
    params = {k: v for k, v in locals().items() if v is not None}
    return make_request("GET", "/recipes/findByNutrients", params=params)

@mcp.tool()
def get_recipe_information(id: int, includeNutrition: Optional[bool] = None) -> Any:
    """Use a recipe id to get full information about a recipe, such as ingredients, nutrition, diet and allergen information, etc."""
    params = {}
    if includeNutrition is not None:
        params["includeNutrition"] = includeNutrition
    return make_request("GET", f"/recipes/{id}/information", params=params)

@mcp.tool()
def get_recipe_ingredients(id: int) -> Any:
    """Get a recipe's ingredient list."""
    return make_request("GET", f"/recipes/{id}/ingredientWidget.json")

@mcp.tool()
def get_recipe_nutrition(id: int) -> Any:
    """Get a recipe's nutrition data."""
    return make_request("GET", f"/recipes/{id}/nutritionWidget.json")

@mcp.tool()
def get_recipe_instructions(id: int, stepBreakdown: Optional[bool] = None) -> Any:
    """Get an analyzed breakdown of a recipe's instructions."""
    params = {}
    if stepBreakdown is not None:
        params["stepBreakdown"] = stepBreakdown
    return make_request("GET", f"/recipes/{id}/analyzedInstructions", params=params)

@mcp.tool()
def get_similar_recipes(id: int, number: Optional[int] = None, limitLicense: Optional[bool] = None) -> Any:
    """Find recipes which are similar to the given one."""
    params = {k: v for k, v in locals().items() if v is not None and k != "id"}
    return make_request("GET", f"/recipes/{id}/similar", params=params)

@mcp.tool()
def search_ingredients(
    query: str,
    addChildren: Optional[bool] = None,
    minProteinPercent: Optional[float] = None,
    maxProteinPercent: Optional[float] = None,
    minFatPercent: Optional[float] = None,
    maxFatPercent: Optional[float] = None,
    minCarbsPercent: Optional[float] = None,
    maxCarbsPercent: Optional[float] = None,
    metaInformation: Optional[bool] = None,
    intolerances: Optional[str] = None,
    sort: Optional[str] = None,
    sortDirection: Optional[str] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None
) -> Any:
    """Search for simple whole foods (e.g. fruits, vegetables, nuts, grains, meat, fish, dairy etc.)."""
    params = {k: v for k, v in locals().items() if v is not None}
    return make_request("GET", "/food/ingredients/search", params=params)

@mcp.tool()
def get_ingredient_information(id: int, amount: Optional[float] = None, unit: Optional[str] = None) -> Any:
    """Use an ingredient id to get all available information about an ingredient, such as its image and supermarket aisle."""
    params = {k: v for k, v in locals().items() if v is not None and k != "id"}
    return make_request("GET", f"/food/ingredients/{id}/information", params=params)

@mcp.tool()
def parse_ingredients(ingredientList: str, servings: Optional[float] = None, includeNutrition: Optional[bool] = None) -> Any:
    """Extract an ingredient from plain text."""
    params = {}
    if includeNutrition is not None:
        params["includeNutrition"] = includeNutrition
    data = {"ingredientList": ingredientList}
    if servings is not None:
        data["servings"] = servings
    return make_request("POST", "/recipes/parseIngredients", params=params, data=data)

@mcp.tool()
def generate_meal_plan(
    timeFrame: Optional[str] = None,
    targetCalories: Optional[float] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None
) -> Any:
    """Generate a meal plan with three meals per day (daily) or three meals per day for an entire week (weekly)."""
    params = {k: v for k, v in locals().items() if v is not None}
    return make_request("GET", "/mealplanner/generate", params=params)

@mcp.tool()
def get_meal_plan_template(username: str, hash: str, id: int) -> Any:
    """Get a meal plan template."""
    params = {"hash": hash}
    return make_request("GET", f"/mealplanner/{username}/templates/{id}", params=params)

@mcp.tool()
def get_wine_pairing(food: str, maxPrice: Optional[float] = None) -> Any:
    """Find a wine that goes well with a food."""
    params = {k: v for k, v in locals().items() if v is not None}
    return make_request("GET", "/food/wine/pairing", params=params)

@mcp.tool()
def get_wine_description(wine: str) -> Any:
    """Get a simple description of a certain wine, e.g. "malbec", "riesling", or "merlot"."""
    params = {"wine": wine}
    return make_request("GET", "/food/wine/description", params=params)

@mcp.tool()
def get_dish_pairing_for_wine(wine: str) -> Any:
    """Find a dish that goes well with a given wine."""
    params = {"wine": wine}
    return make_request("GET", "/food/wine/dishes", params=params)

@mcp.tool()
def autocomplete_recipe_search(query: str, number: Optional[int] = None) -> Any:
    """Autocomplete a partial input to suggest possible recipe names."""
    params = {k: v for k, v in locals().items() if v is not None}
    return make_request("GET", "/recipes/autocomplete", params=params)

@mcp.tool()
def autocomplete_ingredient_search(
    query: str,
    number: Optional[int] = None,
    metaInformation: Optional[bool] = None,
    intolerances: Optional[str] = None
) -> Any:
    """Autocomplete a partial input to suggest possible ingredient names."""
    params = {k: v for k, v in locals().items() if v is not None}
    return make_request("GET", "/food/ingredients/autocomplete", params=params)

if __name__ == "__main__":
    mcp.run()
