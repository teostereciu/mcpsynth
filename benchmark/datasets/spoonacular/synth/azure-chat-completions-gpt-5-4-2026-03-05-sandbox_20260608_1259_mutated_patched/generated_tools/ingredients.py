from typing import Any, Optional

from .common import spoonacular_request


def search_ingredients(
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
) -> Any:
    return spoonacular_request("GET", "/food/ingredients/search", params=locals())


def get_ingredient_information(id: int, amount: Optional[float] = None, unit: Optional[str] = None, locale: Optional[str] = None) -> Any:
    return spoonacular_request("GET", f"/food/ingredients/{id}/information", params={"amount": amount, "unit": unit, "locale": locale})


def compute_ingredient_amount(id: int, nutrient: str, target: float, unit: Optional[str] = None) -> Any:
    return spoonacular_request("GET", f"/food/ingredients/{id}/amount", params=locals())


def convert_amounts(ingredientName: str, sourceAmount: float, sourceUnit: str, targetUnit: str) -> Any:
    return spoonacular_request("GET", "/recipes/convert", params=locals())


def parse_ingredients(ingredientList: str, servings: int, includeNutrition: Optional[bool] = None, language: Optional[str] = None) -> Any:
    return spoonacular_request(
        "POST",
        "/recipes/parseIngredients",
        params={"includeNutrition": includeNutrition, "language": language},
        data={"ingredientList": ingredientList, "servings": servings},
    )


def compute_glycemic_load(ingredientList: str) -> Any:
    return spoonacular_request("POST", "/food/ingredients/glycemicLoad", data={"ingredientList": ingredientList})


def autocomplete_ingredient_search(search_query: str, number: Optional[int] = None, metaInformation: Optional[bool] = None, intolerances: Optional[str] = None, language: Optional[str] = None) -> Any:
    return spoonacular_request("GET", "/food/ingredients/autocomplete", params=locals())


def get_ingredient_substitutes(ingredientName: str) -> Any:
    return spoonacular_request("GET", "/food/ingredients/substitutes", params=locals())


def get_ingredient_substitutes_by_id(id: int) -> Any:
    return spoonacular_request("GET", f"/food/ingredients/{id}/substitutes")
