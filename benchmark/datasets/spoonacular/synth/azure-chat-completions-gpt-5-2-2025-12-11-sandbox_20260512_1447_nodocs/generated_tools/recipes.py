from typing import Any, Dict, List, Optional

from .client import SpoonacularClient


def recipes_complex_search(
    query: Optional[str] = None,
    cuisine: Optional[str] = None,
    diet: Optional[str] = None,
    intolerances: Optional[str] = None,
    includeIngredients: Optional[str] = None,
    excludeIngredients: Optional[str] = None,
    type: Optional[str] = None,
    instructionsRequired: Optional[bool] = None,
    fillIngredients: Optional[bool] = None,
    addRecipeInformation: Optional[bool] = None,
    addRecipeNutrition: Optional[bool] = None,
    maxReadyTime: Optional[int] = None,
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    sort: Optional[str] = None,
    sortDirection: Optional[str] = None,
    number: Optional[int] = 10,
    offset: Optional[int] = 0,
) -> Any:
    """Search recipes with Spoonacular complexSearch."""
    client = SpoonacularClient()
    params: Dict[str, Any] = {
        "query": query,
        "cuisine": cuisine,
        "diet": diet,
        "intolerances": intolerances,
        "includeIngredients": includeIngredients,
        "excludeIngredients": excludeIngredients,
        "type": type,
        "instructionsRequired": instructionsRequired,
        "fillIngredients": fillIngredients,
        "addRecipeInformation": addRecipeInformation,
        "addRecipeNutrition": addRecipeNutrition,
        "maxReadyTime": maxReadyTime,
        "minCarbs": minCarbs,
        "maxCarbs": maxCarbs,
        "minProtein": minProtein,
        "maxProtein": maxProtein,
        "minCalories": minCalories,
        "maxCalories": maxCalories,
        "minFat": minFat,
        "maxFat": maxFat,
        "sort": sort,
        "sortDirection": sortDirection,
        "number": number,
        "offset": offset,
    }
    params = {k: v for k, v in params.items() if v is not None}
    return client.get("/recipes/complexSearch", params=params)


def recipes_find_by_ingredients(
    ingredients: str,
    number: int = 10,
    ranking: int = 1,
    ignorePantry: bool = True,
) -> Any:
    """Find recipes by ingredients (comma-separated list)."""
    client = SpoonacularClient()
    params = {
        "ingredients": ingredients,
        "number": number,
        "ranking": ranking,
        "ignorePantry": ignorePantry,
    }
    return client.get("/recipes/findByIngredients", params=params)


def recipes_find_by_nutrients(
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    number: int = 10,
    random: Optional[bool] = None,
) -> Any:
    """Find recipes by macro nutrients."""
    client = SpoonacularClient()
    params: Dict[str, Any] = {
        "minCarbs": minCarbs,
        "maxCarbs": maxCarbs,
        "minProtein": minProtein,
        "maxProtein": maxProtein,
        "minCalories": minCalories,
        "maxCalories": maxCalories,
        "minFat": minFat,
        "maxFat": maxFat,
        "number": number,
        "random": random,
    }
    params = {k: v for k, v in params.items() if v is not None}
    return client.get("/recipes/findByNutrients", params=params)


def recipes_autocomplete(query: str, number: int = 10) -> Any:
    """Autocomplete recipe search."""
    client = SpoonacularClient()
    return client.get("/recipes/autocomplete", params={"query": query, "number": number})


def recipe_information(recipe_id: int, includeNutrition: bool = False) -> Any:
    """Get recipe information."""
    client = SpoonacularClient()
    return client.get(f"/recipes/{recipe_id}/information", params={"includeNutrition": includeNutrition})


def recipe_ingredients_widget(recipe_id: int) -> Any:
    """Get ingredients widget JSON."""
    client = SpoonacularClient()
    return client.get(f"/recipes/{recipe_id}/ingredientWidget.json")


def recipe_nutrition_widget(recipe_id: int) -> Any:
    """Get nutrition widget JSON."""
    client = SpoonacularClient()
    return client.get(f"/recipes/{recipe_id}/nutritionWidget.json")


def recipe_analyzed_instructions(recipe_id: int, stepBreakdown: bool = True) -> Any:
    """Get analyzed instructions."""
    client = SpoonacularClient()
    return client.get(f"/recipes/{recipe_id}/analyzedInstructions", params={"stepBreakdown": stepBreakdown})


def recipe_similar(recipe_id: int, number: int = 10) -> Any:
    """Get similar recipes."""
    client = SpoonacularClient()
    return client.get(f"/recipes/{recipe_id}/similar", params={"number": number})
