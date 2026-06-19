from typing import Any, Dict, List, Optional

from .http_client import request_json


def recipes_complex_search(
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
) -> Dict[str, Any]:
    """GET /recipes/complexSearch

    Supports many nutrient filters via **nutrient_filters (e.g., minCarbs, maxCalories, etc.).
    """
    params: Dict[str, Any] = {}
    for k, v in {
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
    }.items():
        if v is not None:
            params[k] = v

    for k, v in nutrient_filters.items():
        if v is not None:
            params[k] = v

    return request_json("GET", "/recipes/complexSearch", params=params)


def recipes_find_by_nutrients(
    number: Optional[int] = None,
    offset: Optional[int] = None,
    **nutrient_limits: Any,
) -> Any:
    """GET /recipes/findByNutrients

    Nutrient limits via **nutrient_limits (minCarbs, maxCarbs, minCalories, ...).
    """
    params: Dict[str, Any] = {}
    if number is not None:
        params["number"] = number
    if offset is not None:
        params["offset"] = offset
    for k, v in nutrient_limits.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/recipes/findByNutrients", params=params)


def recipes_find_by_ingredients(
    ingredients: str,
    number: Optional[int] = None,
    limitLicense: Optional[bool] = None,
    ranking: Optional[int] = None,
    ignorePantry: Optional[bool] = None,
) -> Any:
    """GET /recipes/findByIngredients"""
    params: Dict[str, Any] = {"ingredients": ingredients}
    for k, v in {
        "number": number,
        "limitLicense": limitLicense,
        "ranking": ranking,
        "ignorePantry": ignorePantry,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/recipes/findByIngredients", params=params)


def recipes_get_information(id: int, includeNutrition: Optional[bool] = None) -> Dict[str, Any]:
    """GET /recipes/{id}/information"""
    params: Dict[str, Any] = {}
    if includeNutrition is not None:
        params["includeNutrition"] = includeNutrition
    return request_json("GET", f"/recipes/{id}/information", params=params)


def recipes_get_information_bulk(ids: List[int], includeNutrition: Optional[bool] = None) -> Any:
    """GET /recipes/informationBulk"""
    params: Dict[str, Any] = {"ids": ",".join(str(i) for i in ids)}
    if includeNutrition is not None:
        params["includeNutrition"] = includeNutrition
    return request_json("GET", "/recipes/informationBulk", params=params)


def recipes_get_similar(id: int, number: Optional[int] = None) -> Any:
    """GET /recipes/{id}/similar"""
    params: Dict[str, Any] = {}
    if number is not None:
        params["number"] = number
    return request_json("GET", f"/recipes/{id}/similar", params=params)


def recipes_random(number: Optional[int] = None, include_tags: Optional[str] = None, exclude_tags: Optional[str] = None) -> Dict[str, Any]:
    """GET /recipes/random"""
    params: Dict[str, Any] = {}
    if number is not None:
        params["number"] = number
    if include_tags is not None:
        params["include-tags"] = include_tags
    if exclude_tags is not None:
        params["exclude-tags"] = exclude_tags
    return request_json("GET", "/recipes/random", params=params)


def recipes_autocomplete(query: str, number: Optional[int] = None) -> Any:
    """GET /recipes/autocomplete"""
    params: Dict[str, Any] = {"query": query}
    if number is not None:
        params["number"] = number
    return request_json("GET", "/recipes/autocomplete", params=params)


def recipes_analyzed_instructions(id: int, stepBreakdown: Optional[bool] = None) -> Any:
    """GET /recipes/{id}/analyzedInstructions"""
    params: Dict[str, Any] = {}
    if stepBreakdown is not None:
        params["stepBreakdown"] = stepBreakdown
    return request_json("GET", f"/recipes/{id}/analyzedInstructions", params=params)


def recipes_extract(url: str, forceExtraction: Optional[bool] = None, analyze: Optional[bool] = None, includeNutrition: Optional[bool] = None) -> Dict[str, Any]:
    """GET /recipes/extract"""
    params: Dict[str, Any] = {"url": url}
    for k, v in {
        "forceExtraction": forceExtraction,
        "analyze": analyze,
        "includeNutrition": includeNutrition,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/recipes/extract", params=params)


def recipes_taste_widget_json(id: int) -> Dict[str, Any]:
    """GET /recipes/{id}/tasteWidget.json"""
    return request_json("GET", f"/recipes/{id}/tasteWidget.json")


def recipes_equipment_widget_json(id: int) -> Dict[str, Any]:
    """GET /recipes/{id}/equipmentWidget.json"""
    return request_json("GET", f"/recipes/{id}/equipmentWidget.json")


def recipes_price_breakdown_widget_json(id: int) -> Dict[str, Any]:
    """GET /recipes/{id}/priceBreakdownWidget.json"""
    return request_json("GET", f"/recipes/{id}/priceBreakdownWidget.json")


def recipes_ingredient_widget_json(id: int) -> Dict[str, Any]:
    """GET /recipes/{id}/ingredientWidget.json"""
    return request_json("GET", f"/recipes/{id}/ingredientWidget.json")


def recipes_nutrition_widget_json(id: int) -> Dict[str, Any]:
    """GET /recipes/{id}/nutritionWidget.json"""
    return request_json("GET", f"/recipes/{id}/nutritionWidget.json")
