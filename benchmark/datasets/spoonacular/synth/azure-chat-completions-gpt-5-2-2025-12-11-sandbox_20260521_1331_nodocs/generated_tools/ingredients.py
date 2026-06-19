from typing import Any, Dict, Optional

from .http import request_json


def ingredients_search(query: str, number: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"query": query}
    if number is not None:
        params["number"] = number
    if offset is not None:
        params["offset"] = offset
    return request_json("GET", "/food/ingredients/search", params=params)


def ingredients_get_information(id: int, amount: Optional[float] = None, unit: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if amount is not None:
        params["amount"] = amount
    if unit is not None:
        params["unit"] = unit
    return request_json("GET", f"/food/ingredients/{id}/information", params=params)


def ingredients_autocomplete(query: str, number: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"query": query}
    if number is not None:
        params["number"] = number
    return request_json("GET", "/food/ingredients/autocomplete", params=params)


def ingredients_parse(ingredientList: str, servings: Optional[int] = None, includeNutrition: Optional[bool] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"ingredientList": ingredientList}
    if servings is not None:
        params["servings"] = servings
    if includeNutrition is not None:
        params["includeNutrition"] = includeNutrition
    return request_json("POST", "/recipes/parseIngredients", params=params)
