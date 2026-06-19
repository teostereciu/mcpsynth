from typing import Any, Dict, Optional

from .http_client import request_json


def search_recipes_complex(
    *,
    search_query: Optional[str] = None,
    cuisine: Optional[str] = None,
    excludeCuisine: Optional[str] = None,
    diet_type: Optional[str] = None,
    intolerances: Optional[str] = None,
    equipment: Optional[str] = None,
    ingredients: Optional[str] = None,
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
) -> Dict[str, Any]:
    """GET /recipes/complexSearch

    Supports the documented parameters plus any nutrient filters via **nutrient_filters
    (e.g. minCalories=..., maxProtein=...).
    """
    params: Dict[str, Any] = {}
    for k, v in {
        "search_query": search_query,
        "cuisine": cuisine,
        "excludeCuisine": excludeCuisine,
        "diet_type": diet_type,
        "intolerances": intolerances,
        "equipment": equipment,
        "ingredients": ingredients,
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
    }.items():
        if v is not None:
            params[k] = v

    for k, v in nutrient_filters.items():
        if v is not None:
            params[k] = v

    return request_json("GET", "/recipes/complexSearch", params=params)
