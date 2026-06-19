from typing import Any, Dict, Optional

from .http_client import request_json


def search_recipes_complex(
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
    addRecipeInstructions: Optional[bool] = None,
    addRecipeNutrition: Optional[bool] = None,
    author: Optional[str] = None,
    tags: Optional[str] = None,
    recipeBoxId: Optional[int] = None,
    titleMatch: Optional[str] = None,
    maxReadyTime: Optional[int] = None,
    minServings: Optional[int] = None,
    maxServings: Optional[int] = None,
    ignorePantry: Optional[bool] = None,
    sort: Optional[str] = None,
    sortDirection: Optional[str] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
    **nutrient_filters: Any,
) -> Any:
    """GET /recipes/complexSearch

    Supports the documented parameters plus any nutrient filters (e.g. minCalories, maxProtein).
    """

    params: Dict[str, Any] = {
        "query": query,
        "cuisine": cuisine,
        "excludeCuisine": excludeCuisine,
        "diet": diet,
        "intolerances": intolerances,
        "equipment": equipment,
        "includeIngredients": includeIngredients,
        "excludeIngredients": excludeIngredients,
        "type": type,
        "instructionsRequired": instructionsRequired,
        "fillIngredients": fillIngredients,
        "addRecipeInformation": addRecipeInformation,
        "addRecipeInstructions": addRecipeInstructions,
        "addRecipeNutrition": addRecipeNutrition,
        "author": author,
        "tags": tags,
        "recipeBoxId": recipeBoxId,
        "titleMatch": titleMatch,
        "maxReadyTime": maxReadyTime,
        "minServings": minServings,
        "maxServings": maxServings,
        "ignorePantry": ignorePantry,
        "sort": sort,
        "sortDirection": sortDirection,
        "offset": offset,
        "number": number,
    }
    params.update(nutrient_filters)
    return request_json("GET", "/recipes/complexSearch", params=params)


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
    number: Optional[int] = None,
    **micronutrients: Any,
) -> Any:
    """GET /recipes/findByNutrients

    Supports the documented macro parameters plus any micronutrient filters.
    """

    params: Dict[str, Any] = {
        "minCarbs": minCarbs,
        "maxCarbs": maxCarbs,
        "minProtein": minProtein,
        "maxProtein": maxProtein,
        "minCalories": minCalories,
        "maxCalories": maxCalories,
        "minFat": minFat,
        "maxFat": maxFat,
        "offset": offset,
        "number": number,
    }
    params.update(micronutrients)
    return request_json("GET", "/recipes/findByNutrients", params=params)
