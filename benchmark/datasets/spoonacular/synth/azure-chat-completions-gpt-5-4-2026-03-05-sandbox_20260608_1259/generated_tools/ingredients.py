from typing import Any, Optional

from generated_tools.recipes import _request


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
    return _request("GET", "/food/ingredients/search", locals())


def get_ingredient_information(id: int, amount: Optional[float] = None, unit: Optional[str] = None, locale: Optional[str] = None) -> Any:
    return _request("GET", f"/food/ingredients/{id}/information", {"amount": amount, "unit": unit, "locale": locale})


def compute_ingredient_amount(id: int, nutrient: str, target: float, unit: Optional[str] = None) -> Any:
    return _request("GET", f"/food/ingredients/{id}/amount", {"nutrient": nutrient, "target": target, "unit": unit})


def convert_amounts(ingredientName: str, sourceAmount: float, sourceUnit: str, targetUnit: str) -> Any:
    return _request("GET", "/recipes/convert", locals())


def parse_ingredients(ingredientList: str, servings: float, includeNutrition: Optional[bool] = None, language: Optional[str] = None) -> Any:
    params = {"includeNutrition": includeNutrition, "language": language}
    data = {"ingredientList": ingredientList, "servings": servings}
    return _request("POST", "/recipes/parseIngredients", params, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})


def autocomplete_ingredient_search(query: str, number: Optional[int] = None, metaInformation: Optional[bool] = None, intolerances: Optional[str] = None) -> Any:
    return _request("GET", "/food/ingredients/autocomplete", locals())


def get_ingredient_substitutes(ingredientName: str) -> Any:
    return _request("GET", "/food/ingredients/substitutes", locals())


def get_ingredient_substitutes_by_id(id: int) -> Any:
    return _request("GET", f"/food/ingredients/{id}/substitutes")
