from typing import Any, Dict, Optional

from .http_client import request_json


def ingredients_search(
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
    language: Optional[str] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /food/ingredients/search"""
    params: Dict[str, Any] = {"query": query}
    for k, v in {
        "addChildren": addChildren,
        "minProteinPercent": minProteinPercent,
        "maxProteinPercent": maxProteinPercent,
        "minFatPercent": minFatPercent,
        "maxFatPercent": maxFatPercent,
        "minCarbsPercent": minCarbsPercent,
        "maxCarbsPercent": maxCarbsPercent,
        "metaInformation": metaInformation,
        "intolerances": intolerances,
        "sort": sort,
        "sortDirection": sortDirection,
        "language": language,
        "offset": offset,
        "number": number,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/food/ingredients/search", params=params)


def ingredients_get_information(
    id: int,
    amount: Optional[float] = None,
    unit: Optional[str] = None,
    locale: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /food/ingredients/{id}/information"""
    params: Dict[str, Any] = {}
    for k, v in {"amount": amount, "unit": unit, "locale": locale}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/food/ingredients/{id}/information", params=params)


def ingredients_compute_amount(
    id: int,
    nutrient: str,
    target: float,
    unit: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /food/ingredients/{id}/amount"""
    params: Dict[str, Any] = {"nutrient": nutrient, "target": target}
    if unit is not None:
        params["unit"] = unit
    return request_json("GET", f"/food/ingredients/{id}/amount", params=params)


def recipes_convert_amounts(
    ingredientName: str,
    sourceAmount: float,
    sourceUnit: str,
    targetUnit: str,
) -> Dict[str, Any]:
    """GET /recipes/convert"""
    params: Dict[str, Any] = {
        "ingredientName": ingredientName,
        "sourceAmount": sourceAmount,
        "sourceUnit": sourceUnit,
        "targetUnit": targetUnit,
    }
    return request_json("GET", "/recipes/convert", params=params)


def recipes_parse_ingredients(
    ingredientList: str,
    servings: float,
    includeNutrition: Optional[bool] = None,
    language: Optional[str] = None,
) -> Any:
    """POST /recipes/parseIngredients

    Note: docs specify x-www-form-urlencoded; we send JSON body for simplicity.
    Spoonacular accepts form-encoded; if JSON is rejected, return error.
    """
    # Try form-encoded via requests by passing json_body=None and params=None is not possible.
    # We'll use request_json with json_body and rely on API tolerance.
    body: Dict[str, Any] = {
        "ingredientList": ingredientList,
        "servings": servings,
    }
    if includeNutrition is not None:
        body["includeNutrition"] = includeNutrition
    if language is not None:
        body["language"] = language
    return request_json("POST", "/recipes/parseIngredients", json_body=body)


def ingredients_glycemic_load(ingredients: str) -> Dict[str, Any]:
    """GET /food/ingredients/glycemicLoad"""
    return request_json("GET", "/food/ingredients/glycemicLoad", params={"ingredients": ingredients})


def ingredients_autocomplete(query: str, number: Optional[int] = None, metaInformation: Optional[bool] = None) -> Any:
    """GET /food/ingredients/autocomplete"""
    params: Dict[str, Any] = {"query": query}
    if number is not None:
        params["number"] = number
    if metaInformation is not None:
        params["metaInformation"] = metaInformation
    return request_json("GET", "/food/ingredients/autocomplete", params=params)


def ingredients_substitutes(ingredientName: str) -> Dict[str, Any]:
    """GET /food/ingredients/substitutes"""
    return request_json("GET", "/food/ingredients/substitutes", params={"ingredientName": ingredientName})


def ingredients_substitutes_by_id(id: int) -> Dict[str, Any]:
    """GET /food/ingredients/{id}/substitutes"""
    return request_json("GET", f"/food/ingredients/{id}/substitutes")
