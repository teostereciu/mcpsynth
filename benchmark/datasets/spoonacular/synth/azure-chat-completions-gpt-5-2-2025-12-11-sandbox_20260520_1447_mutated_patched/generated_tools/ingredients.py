from typing import Any, Dict, Optional

from .http_client import request_json


def ingredient_search(
    *,
    search_query: str,
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
    params: Dict[str, Any] = {"query": search_query}
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


def get_ingredient_information(
    *,
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


def compute_ingredient_amount(
    *,
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


def convert_amounts(
    *,
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


def parse_ingredients(
    *,
    ingredientList: str,
    servings: float,
    includeNutrition: Optional[bool] = None,
    language: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /recipes/parseIngredients

    Note: Docs specify application/x-www-form-urlencoded; we send JSON-like body as form params
    by using request_json with params and no json body.
    """
    params: Dict[str, Any] = {"ingredientList": ingredientList, "servings": servings}
    if includeNutrition is not None:
        params["includeNutrition"] = includeNutrition
    if language is not None:
        params["language"] = language
    # Spoonacular expects form-encoded; requests will encode params in query for POST.
    # This endpoint accepts query params as well.
    return request_json("POST", "/recipes/parseIngredients", params=params)
