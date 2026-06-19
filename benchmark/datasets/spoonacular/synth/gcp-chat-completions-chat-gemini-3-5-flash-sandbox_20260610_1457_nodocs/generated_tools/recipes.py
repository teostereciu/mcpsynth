from typing import Optional, List, Dict, Any
from generated_tools.client import request

def search_recipes(
    query: Optional[str] = None,
    cuisine: Optional[str] = None,
    excludeCuisine: Optional[str] = None,
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
    author: Optional[str] = None,
    tags: Optional[str] = None,
    titleMatch: Optional[str] = None,
    maxReadyTime: Optional[int] = None,
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
) -> Dict[str, Any]:
    """
    Search through thousands of recipes using advanced filtering and search criteria.
    
    Args:
        query: The recipe name or keywords to search for (e.g., "pasta").
        cuisine: The cuisine(s) the recipes must match (comma-separated, e.g., "italian,mexican").
        excludeCuisine: The cuisine(s) the recipes must not match.
        diet: The diet for which the recipes must be suitable (e.g., "vegetarian", "vegan", "gluten free").
        intolerances: Food intolerances that the recipes must exclude (comma-separated, e.g., "dairy,egg").
        equipment: Equipment required for the recipe (comma-separated, e.g., "blender").
        includeIngredients: Ingredients that must be in the recipe (comma-separated, e.g., "tomato,cheese").
        excludeIngredients: Ingredients that must not be in the recipe.
        type: The type of recipe (e.g., "main course", "side dish", "dessert").
        instructionsRequired: Whether the recipes must have instructions.
        fillIngredients: Add information about the used and missing ingredients in each recipe.
        addRecipeInformation: If set to true, you get more information about the recipes returned.
        addRecipeNutrition: If set to true, you get nutritional information for each recipe.
        author: The username of the recipe author.
        tags: User tags that the recipes must have.
        titleMatch: A string that must be contained in the title of the recipe.
        maxReadyTime: The maximum time in minutes it should take to prepare/cook the recipe.
        ignorePantry: Whether to ignore typical pantry items like water, salt, flour, etc.
        sort: The strategy to sort results (e.g., "meta-score", "popularity", "healthiness", "price", "time").
        sortDirection: The direction of sorting ("asc" or "desc").
        minCarbs: Minimum amount of carbohydrates in grams.
        maxCarbs: Maximum amount of carbohydrates in grams.
        minProtein: Minimum amount of protein in grams.
        maxProtein: Maximum amount of protein in grams.
        minCalories: Minimum amount of calories.
        maxCalories: Maximum amount of calories.
        minFat: Minimum amount of fat in grams.
        maxFat: Maximum amount of fat in grams.
        offset: The number of results to skip (for pagination).
        number: The number of expected results (between 1 and 100).
    """
    params = {}
    locs = locals()
    for k, v in locs.items():
        if v is not None:
            params[k] = v
            
    return request("GET", "/recipes/complexSearch", params=params)

def search_recipes_by_ingredients(
    ingredients: str,
    number: Optional[int] = None,
    ranking: Optional[int] = None,
    ignorePantry: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Find recipes that use as many of the given ingredients as possible.
    
    Args:
        ingredients: A comma-separated list of ingredients that the recipes should contain (e.g., "apples,flour,sugar").
        number: The maximum number of recipes to return (default 10, max 100).
        ranking: Whether to maximize used ingredients (1) or minimize missing ingredients (2) first.
        ignorePantry: Whether to ignore typical pantry items like water, salt, flour, etc.
    """
    params = {"ingredients": ingredients}
    if number is not None:
        params["number"] = number
    if ranking is not None:
        params["ranking"] = ranking
    if ignorePantry is not None:
        params["ignorePantry"] = ignorePantry
        
    return request("GET", "/recipes/findByIngredients", params=params)

def search_recipes_by_nutrients(
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    number: Optional[int] = None,
    offset: Optional[int] = None
) -> Dict[str, Any]:
    """
    Find recipes which meet certain nutritional criteria.
    
    Args:
        minCarbs: Minimum carbs in grams.
        maxCarbs: Maximum carbs in grams.
        minProtein: Minimum protein in grams.
        maxProtein: Maximum protein in grams.
        minCalories: Minimum calories.
        maxCalories: Maximum calories.
        minFat: Minimum fat in grams.
        maxFat: Maximum fat in grams.
        number: The number of expected results (between 1 and 100).
        offset: The number of results to skip.
    """
    params = {}
    locs = locals()
    for k, v in locs.items():
        if v is not None:
            params[k] = v
            
    return request("GET", "/recipes/findByNutrients", params=params)

def get_recipe_information(
    id: int,
    includeNutrition: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Get full information about a recipe, including ingredients, instructions, and nutrition.
    
    Args:
        id: The recipe ID.
        includeNutrition: Include nutrition data in the recipe information.
    """
    params = {}
    if includeNutrition is not None:
        params["includeNutrition"] = includeNutrition
        
    return request("GET", f"/recipes/{id}/information", params=params)

def get_recipe_instructions(
    id: int,
    stepBreakdown: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Get analyzed instructions for a recipe, broken down into steps, equipment, and ingredients.
    
    Args:
        id: The recipe ID.
        stepBreakdown: Whether to break down steps even more.
    """
    params = {}
    if stepBreakdown is not None:
        params["stepBreakdown"] = stepBreakdown
        
    return request("GET", f"/recipes/{id}/analyzedInstructions", params=params)

def get_similar_recipes(
    id: int,
    number: Optional[int] = None
) -> Dict[str, Any]:
    """
    Find recipes similar to the given recipe ID.
    
    Args:
        id: The recipe ID.
        number: The number of similar recipes to return (default 7).
    """
    params = {}
    if number is not None:
        params["number"] = number
        
    return request("GET", f"/recipes/{id}/similar", params=params)

def get_recipe_equipment(id: int) -> Dict[str, Any]:
    """
    Get a list of equipment used in a recipe.
    
    Args:
        id: The recipe ID.
    """
    return request("GET", f"/recipes/{id}/equipmentWidget.json")

def get_recipe_price_breakdown(id: int) -> Dict[str, Any]:
    """
    Get the price breakdown of a recipe's ingredients.
    
    Args:
        id: The recipe ID.
    """
    return request("GET", f"/recipes/{id}/priceBreakdownWidget.json")

def summarize_recipe(id: int) -> Dict[str, Any]:
    """
    Get a short summary of a recipe, including its key characteristics.
    
    Args:
        id: The recipe ID.
    """
    return request("GET", f"/recipes/{id}/summary")

def extract_recipe(
    url: str,
    forceExtraction: Optional[bool] = None,
    analyze: Optional[bool] = None,
    includeNutrition: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Extract recipe data from any website/web page.
    
    Args:
        url: The URL of the recipe page.
        forceExtraction: Force extraction even if the site is not in the database.
        analyze: Analyze the recipe (extract ingredients, instructions, etc.).
        includeNutrition: Include nutrition data in the response.
    """
    params = {"url": url}
    if forceExtraction is not None:
        params["forceExtraction"] = forceExtraction
    if analyze is not None:
        params["analyze"] = analyze
    if includeNutrition is not None:
        params["includeNutrition"] = includeNutrition
        
    return request("GET", "/recipes/extract", params=params)

def convert_amounts(
    ingredientName: str,
    sourceAmount: float,
    sourceUnit: str,
    targetUnit: str
) -> Dict[str, Any]:
    """
    Convert an amount of an ingredient from one unit to another.
    
    Args:
        ingredientName: The name of the ingredient (e.g., "flour").
        sourceAmount: The amount to convert (e.g., 2.5).
        sourceUnit: The unit to convert from (e.g., "cups").
        targetUnit: The unit to convert to (e.g., "grams").
    """
    params = {
        "ingredientName": ingredientName,
        "sourceAmount": sourceAmount,
        "sourceUnit": sourceUnit,
        "targetUnit": targetUnit
    }
    return request("GET", "/recipes/convert", params=params)

def autocomplete_recipe_search(
    query: str,
    number: Optional[int] = None
) -> Dict[str, Any]:
    """
    Autocomplete a search query for recipes.
    
    Args:
        query: The query to autocomplete.
        number: The number of results to return (default 5).
    """
    params = {"query": query}
    if number is not None:
        params["number"] = number
        
    return request("GET", "/recipes/autocomplete", params=params)
