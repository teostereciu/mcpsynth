import requests
from typing import Optional, Dict, Any

BASE_URL = "https://api.spoonacular.com"

def make_request(method: str, endpoint: str, params: Dict[str, Any] = None, data: Dict[str, Any] = None) -> Any:
    import os
    if params is None:
        params = {}
    params["apiKey"] = os.environ.get("SPOONACULAR_API_KEY")
    url = f"{BASE_URL}{endpoint}"
    try:
        if method.upper() == "GET":
            response = requests.get(url, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, params=params, data=data)
        else:
            return {"error": f"Unsupported method {method}"}
        response.raise_for_status()
        if "application/json" in response.headers.get("Content-Type", ""):
            return response.json()
        return {"result": response.text}
    except requests.exceptions.RequestException as e:
        try:
            return {"error": e.response.json()}
        except Exception:
            return {"error": str(e)}

def search_recipes(query: str, cuisine: Optional[str] = None, diet: Optional[str] = None, intolerances: Optional[str] = None, number: int = 10) -> Any:
    """Search recipes by query (complex search)."""
    params = {"query": query, "number": number}
    if cuisine: params["cuisine"] = cuisine
    if diet: params["diet"] = diet
    if intolerances: params["intolerances"] = intolerances
    return make_request("GET", "/recipes/complexSearch", params=params)

def search_recipes_by_ingredients(ingredients: str, number: int = 10, ranking: int = 1, ignorePantry: bool = True) -> Any:
    """Search recipes by ingredients. ingredients should be a comma-separated list."""
    params = {
        "ingredients": ingredients,
        "number": number,
        "ranking": ranking,
        "ignorePantry": str(ignorePantry).lower()
    }
    return make_request("GET", "/recipes/findByIngredients", params=params)

def search_recipes_by_nutrients(minCarbs: Optional[int] = None, maxCarbs: Optional[int] = None, minProtein: Optional[int] = None, maxProtein: Optional[int] = None, minCalories: Optional[int] = None, maxCalories: Optional[int] = None, number: int = 10) -> Any:
    """Search recipes by nutrients."""
    params = {"number": number}
    if minCarbs is not None: params["minCarbs"] = minCarbs
    if maxCarbs is not None: params["maxCarbs"] = maxCarbs
    if minProtein is not None: params["minProtein"] = minProtein
    if maxProtein is not None: params["maxProtein"] = maxProtein
    if minCalories is not None: params["minCalories"] = minCalories
    if maxCalories is not None: params["maxCalories"] = maxCalories
    return make_request("GET", "/recipes/findByNutrients", params=params)

def get_recipe_information(id: int, includeNutrition: bool = False) -> Any:
    """Get information about a specific recipe."""
    params = {"includeNutrition": str(includeNutrition).lower()}
    return make_request("GET", f"/recipes/{id}/information", params=params)

def get_recipe_ingredients(id: int) -> Any:
    """Get ingredients for a specific recipe by ID."""
    return make_request("GET", f"/recipes/{id}/ingredientWidget.json")

def get_recipe_instructions(id: int, stepBreakdown: bool = True) -> Any:
    """Get analyzed instructions for a specific recipe."""
    params = {"stepBreakdown": str(stepBreakdown).lower()}
    return make_request("GET", f"/recipes/{id}/analyzedInstructions", params=params)

def get_similar_recipes(id: int, number: int = 10) -> Any:
    """Get similar recipes to a specific recipe."""
    params = {"number": number}
    return make_request("GET", f"/recipes/{id}/similar", params=params)
