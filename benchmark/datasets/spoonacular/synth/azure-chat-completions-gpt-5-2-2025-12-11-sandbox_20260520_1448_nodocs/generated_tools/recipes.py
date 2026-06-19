from typing import Any, Dict, Optional

from .http import request_json


def recipes_complex_search(
    *,
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
    sort: Optional[str] = None,
    sortDirection: Optional[str] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    number: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        k: v
        for k, v in {
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
            "sort": sort,
            "sortDirection": sortDirection,
            "minCalories": minCalories,
            "maxCalories": maxCalories,
            "minCarbs": minCarbs,
            "maxCarbs": maxCarbs,
            "minProtein": minProtein,
            "maxProtein": maxProtein,
            "minFat": minFat,
            "maxFat": maxFat,
            "number": number,
            "offset": offset,
        }.items()
        if v is not None
    }
    return request_json("GET", "/recipes/complexSearch", params=params)


def recipes_find_by_ingredients(
    *,
    ingredients: str,
    number: Optional[int] = None,
    ranking: Optional[int] = None,
    ignorePantry: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"ingredients": ingredients}
    if number is not None:
        params["number"] = number
    if ranking is not None:
        params["ranking"] = ranking
    if ignorePantry is not None:
        params["ignorePantry"] = ignorePantry
    return request_json("GET", "/recipes/findByIngredients", params=params)


def recipes_search_by_nutrients(
    *,
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    number: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        k: v
        for k, v in {
            "minCarbs": minCarbs,
            "maxCarbs": maxCarbs,
            "minProtein": minProtein,
            "maxProtein": maxProtein,
            "minCalories": minCalories,
            "maxCalories": maxCalories,
            "minFat": minFat,
            "maxFat": maxFat,
            "number": number,
            "offset": offset,
        }.items()
        if v is not None
    }
    return request_json("GET", "/recipes/findByNutrients", params=params)


def recipes_autocomplete(*, query: str, number: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"query": query}
    if number is not None:
        params["number"] = number
    return request_json("GET", "/recipes/autocomplete", params=params)


def recipes_get_information(
    *,
    id: int,
    includeNutrition: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if includeNutrition is not None:
        params["includeNutrition"] = includeNutrition
    return request_json("GET", f"/recipes/{id}/information", params=params)


def recipes_get_analyzed_instructions(*, id: int, stepBreakdown: Optional[bool] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if stepBreakdown is not None:
        params["stepBreakdown"] = stepBreakdown
    return request_json("GET", f"/recipes/{id}/analyzedInstructions", params=params)


def recipes_get_similar(*, id: int, number: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if number is not None:
        params["number"] = number
    return request_json("GET", f"/recipes/{id}/similar", params=params)


def recipes_get_ingredient_widget(*, id: int, defaultCss: Optional[bool] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if defaultCss is not None:
        params["defaultCss"] = defaultCss
    return request_json("GET", f"/recipes/{id}/ingredientWidget.json", params=params)


def recipes_get_nutrition_widget(*, id: int, defaultCss: Optional[bool] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if defaultCss is not None:
        params["defaultCss"] = defaultCss
    return request_json("GET", f"/recipes/{id}/nutritionWidget.json", params=params)
