from typing import Any, Dict, Optional

from .http_client import request_json


def ingredient_search(
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
) -> Any:
    """GET /food/ingredients/search"""
    params: Dict[str, Any] = {
        "query": query,
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
    }
    return request_json("GET", "/food/ingredients/search", params=params)


def get_ingredient_information(
    id: int,
    amount: Optional[float] = None,
    unit: Optional[str] = None,
    locale: Optional[str] = None,
) -> Any:
    """GET /food/ingredients/{id}/information"""
    params = {"amount": amount, "unit": unit, "locale": locale}
    return request_json("GET", f"/food/ingredients/{id}/information", params=params)


def compute_ingredient_amount(
    id: int,
    nutrient: str,
    target: float,
    unit: Optional[str] = None,
) -> Any:
    """GET /food/ingredients/{id}/amount"""
    params = {"nutrient": nutrient, "target": target, "unit": unit}
    return request_json("GET", f"/food/ingredients/{id}/amount", params=params)


def convert_amounts(
    ingredientName: str,
    sourceAmount: float,
    sourceUnit: str,
    targetUnit: str,
) -> Any:
    """GET /recipes/convert"""
    params = {
        "ingredientName": ingredientName,
        "sourceAmount": sourceAmount,
        "sourceUnit": sourceUnit,
        "targetUnit": targetUnit,
    }
    return request_json("GET", "/recipes/convert", params=params)


def parse_ingredients(
    ingredientList: str,
    servings: int,
    includeNutrition: Optional[bool] = None,
    language: Optional[str] = None,
) -> Any:
    """POST /recipes/parseIngredients

    Note: Docs specify x-www-form-urlencoded; Spoonacular also accepts query params.
    We send as query params for simplicity.
    """
    params = {
        "ingredientList": ingredientList,
        "servings": servings,
        "includeNutrition": includeNutrition,
        "language": language,
    }
    return request_json("POST", "/recipes/parseIngredients", params=params)
