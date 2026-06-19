from typing import Optional, Dict, Any
from .recipes import make_request

def search_ingredients(query: str, intolerances: Optional[str] = None, number: int = 10) -> Any:
    """Search for ingredients."""
    params = {"query": query, "number": number}
    if intolerances: params["intolerances"] = intolerances
    return make_request("GET", "/food/ingredients/search", params=params)

def get_ingredient_information(id: int, amount: Optional[float] = None, unit: Optional[str] = None) -> Any:
    """Get information about a specific ingredient."""
    params = {}
    if amount is not None: params["amount"] = amount
    if unit: params["unit"] = unit
    return make_request("GET", f"/food/ingredients/{id}/information", params=params)

def parse_ingredients(ingredientList: str, servings: int = 1, includeNutrition: bool = False) -> Any:
    """Parse ingredients. ingredientList should be a newline-separated list of ingredients."""
    params = {"includeNutrition": str(includeNutrition).lower()}
    data = {"ingredientList": ingredientList, "servings": servings}
    return make_request("POST", "/recipes/parseIngredients", params=params, data=data)
