from typing import Optional, Dict, Any
from generated_tools.client import request

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
) -> Dict[str, Any]:
    """
    Search for ingredients in the Spoonacular database.
    
    Args:
        query: The search query (e.g., "apple").
        addChildren: Whether to add children of the ingredient.
        minProteinPercent: Minimum protein percentage.
        maxProteinPercent: Maximum protein percentage.
        minFatPercent: Minimum fat percentage.
        maxFatPercent: Maximum fat percentage.
        minCarbsPercent: Minimum carbs percentage.
        maxCarbsPercent: Maximum carbs percentage.
        metaInformation: Whether to return more meta information about the ingredients.
        intolerances: A comma-separated list of intolerances (e.g., "dairy,gluten").
        sort: The strategy to sort results (e.g., "calories").
        sortDirection: The direction of sorting ("asc" or "desc").
        offset: The number of results to skip.
        number: The number of expected results (between 1 and 100).
    """
    params = {"query": query}
    locs = locals()
    for k, v in locs.items():
        if v is not None and k != "query":
            params[k] = v
            
    return request("GET", "/food/ingredients/search", params=params)

def get_ingredient_information(
    id: int,
    amount: Optional[float] = None,
    unit: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get detailed information about an ingredient by its ID, including nutrition.
    
    Args:
        id: The ingredient ID.
        amount: The amount of the ingredient (e.g., 150).
        unit: The unit of the amount (e.g., "grams").
    """
    params = {}
    if amount is not None:
        params["amount"] = amount
    if unit is not None:
        params["unit"] = unit
        
    return request("GET", f"/food/ingredients/{id}/information", params=params)

def parse_ingredients(
    ingredientList: str,
    servings: float,
    includeNutrition: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Parse a list of ingredient strings into structured data.
    
    Args:
        ingredientList: A newline-separated list of ingredient strings (e.g., "3 oz pork\n2 cups flour").
        servings: The number of servings.
        includeNutrition: Whether to include nutrition data in the response.
    """
    data = {
        "ingredientList": ingredientList,
        "servings": servings
    }
    params = {}
    if includeNutrition is not None:
        params["includeNutrition"] = includeNutrition
        
    # This endpoint expects application/x-www-form-urlencoded
    return request("POST", "/recipes/parseIngredients", params=params, data=data)

def autocomplete_ingredient_search(
    query: str,
    number: Optional[int] = None,
    metaInformation: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Autocomplete a search query for ingredients.
    
    Args:
        query: The query to autocomplete.
        number: The number of results to return (default 5).
        metaInformation: Whether to return more meta information about the ingredients.
    """
    params = {"query": query}
    if number is not None:
        params["number"] = number
    if metaInformation is not None:
        params["metaInformation"] = metaInformation
        
    return request("GET", "/food/ingredients/autocomplete", params=params)
