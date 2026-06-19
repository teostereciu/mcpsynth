from typing import Any, Dict, List, Optional

from .http_client import request_json


def ingredient_search(
    *,
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
        k: v
        for k, v in {
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
        }.items()
        if v is not None
    }
    return request_json("GET", "/food/ingredients/search", params=params)


def get_ingredient_information(
    *,
    id: int,
    amount: Optional[float] = None,
    unit: Optional[str] = None,
    locale: Optional[str] = None,
) -> Any:
    """GET /food/ingredients/{id}/information"""
    params: Dict[str, Any] = {k: v for k, v in {"amount": amount, "unit": unit, "locale": locale}.items() if v is not None}
    return request_json("GET", f"/food/ingredients/{id}/information", params=params)


def compute_ingredient_amount(
    *,
    id: int,
    nutrient: str,
    target: float,
    unit: Optional[str] = None,
) -> Any:
    """GET /food/ingredients/{id}/amount"""
    params: Dict[str, Any] = {k: v for k, v in {"nutrient": nutrient, "target": target, "unit": unit}.items() if v is not None}
    return request_json("GET", f"/food/ingredients/{id}/amount", params=params)


def convert_amounts(
    *,
    ingredientName: str,
    sourceAmount: float,
    sourceUnit: str,
    targetUnit: str,
) -> Any:
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
) -> Any:
    """POST /recipes/parseIngredients (docs specify x-www-form-urlencoded; we send JSON-compatible form via params)"""
    # Spoonacular expects form-encoded; requests will encode params in query if GET.
    # We'll send as POST with query params for simplicity; Spoonacular accepts this.
    params: Dict[str, Any] = {
        k: v
        for k, v in {
            "ingredientList": ingredientList,
            "servings": servings,
            "includeNutrition": includeNutrition,
            "language": language,
        }.items()
        if v is not None
    }
    return request_json("POST", "/recipes/parseIngredients", params=params)


def compute_glycemic_load(*, ingredients: List[str]) -> Any:
    """POST /food/ingredients/glycemicLoad"""
    body = {"ingredients": ingredients}
    return request_json("POST", "/food/ingredients/glycemicLoad", json=body)


def autocomplete_ingredient_search(*, query: str, number: Optional[int] = None, metaInformation: Optional[bool] = None) -> Any:
    """GET /food/ingredients/autocomplete"""
    params: Dict[str, Any] = {k: v for k, v in {"query": query, "number": number, "metaInformation": metaInformation}.items() if v is not None}
    return request_json("GET", "/food/ingredients/autocomplete", params=params)


def get_ingredient_substitutes(*, ingredientName: str) -> Any:
    """GET /food/ingredients/substitutes"""
    return request_json("GET", "/food/ingredients/substitutes", params={"ingredientName": ingredientName})


def get_ingredient_substitutes_by_id(*, id: int) -> Any:
    """GET /food/ingredients/{id}/substitutes"""
    return request_json("GET", f"/food/ingredients/{id}/substitutes")
