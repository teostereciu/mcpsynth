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
) -> Any:
    """GET /recipes/complexSearch

    Supports the documented parameters plus any nutrient filters passed via **nutrient_filters
    (e.g. minCalories=..., maxProtein=...).
    """
    params: Dict[str, Any] = {
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
    }
    params.update(nutrient_filters)
    return request_json("GET", "/recipes/complexSearch", params=params)


def search_recipes_by_nutrients(*, minCarbs: Optional[float] = None, maxCarbs: Optional[float] = None, minProtein: Optional[float] = None, maxProtein: Optional[float] = None, minCalories: Optional[float] = None, maxCalories: Optional[float] = None, minFat: Optional[float] = None, maxFat: Optional[float] = None, offset: Optional[int] = None, number: Optional[int] = None, **micros: Any) -> Any:
    """GET /recipes/findByNutrients

    Supports macro params explicitly and any additional micro nutrient filters via **micros.
    """
    params: Dict[str, Any] = {
        "minCarbs": minCarbs,
        "maxCarbs": maxCarbs,
        "minProtein": minProtein,
        "maxProtein": maxProtein,
        "minCalories": minCalories,
        "maxCalories": maxCalories,
        "minFat": minFat,
        "maxFat": maxFat,
        "offset": offset,
        "number": number,
    }
    params.update(micros)
    return request_json("GET", "/recipes/findByNutrients", params=params)


def search_recipes_by_ingredients(*, ingredients: str, number: Optional[int] = None, limitLicense: Optional[bool] = None, ranking: Optional[int] = None, ignorePantry: Optional[bool] = None) -> Any:
    """GET /recipes/findByIngredients"""
    params: Dict[str, Any] = {
        "ingredients": ingredients,
        "number": number,
        "limitLicense": limitLicense,
        "ranking": ranking,
        "ignorePantry": ignorePantry,
    }
    return request_json("GET", "/recipes/findByIngredients", params=params)


def get_recipe_information(*, id: int, includeNutrition: Optional[bool] = None) -> Any:
    """GET /recipes/{id}/information"""
    return request_json("GET", f"/recipes/{id}/information", params={"includeNutrition": includeNutrition})


def get_recipe_information_bulk(*, ids: str, includeNutrition: Optional[bool] = None) -> Any:
    """GET /recipes/informationBulk"""
    return request_json("GET", "/recipes/informationBulk", params={"ids": ids, "includeNutrition": includeNutrition})


def get_similar_recipes(*, id: int, number: Optional[int] = None) -> Any:
    """GET /recipes/{id}/similar"""
    return request_json("GET", f"/recipes/{id}/similar", params={"number": number})


def get_random_recipes(*, number: Optional[int] = None, tags: Optional[str] = None) -> Any:
    """GET /recipes/random"""
    return request_json("GET", "/recipes/random", params={"number": number, "tags": tags})


def autocomplete_recipe_search(*, search_query: str, number: Optional[int] = None) -> Any:
    """GET /recipes/autocomplete"""
    return request_json("GET", "/recipes/autocomplete", params={"search_query": search_query, "number": number})


def taste_by_id(*, id: int, normalize: Optional[bool] = None) -> Any:
    """GET /recipes/{id}/tasteWidget.json"""
    return request_json("GET", f"/recipes/{id}/tasteWidget.json", params={"normalize": normalize})


def equipment_by_id(*, id: int) -> Any:
    """GET /recipes/{id}/equipmentWidget.json"""
    return request_json("GET", f"/recipes/{id}/equipmentWidget.json")


def price_breakdown_by_id(*, id: int) -> Any:
    """GET /recipes/{id}/priceBreakdownWidget.json"""
    return request_json("GET", f"/recipes/{id}/priceBreakdownWidget.json")


def ingredients_by_id(*, id: int) -> Any:
    """GET /recipes/{id}/ingredientWidget.json"""
    return request_json("GET", f"/recipes/{id}/ingredientWidget.json")


def nutrition_by_id(*, id: int) -> Any:
    """GET /recipes/{id}/nutritionWidget.json"""
    return request_json("GET", f"/recipes/{id}/nutritionWidget.json")


def get_analyzed_recipe_instructions(*, id: int, stepBreakdown: Optional[bool] = None) -> Any:
    """GET /recipes/{id}/analyzedInstructions"""
    return request_json("GET", f"/recipes/{id}/analyzedInstructions", params={"stepBreakdown": stepBreakdown})


def extract_recipe_from_website(*, url: str, forceExtraction: Optional[bool] = None, analyze: Optional[bool] = None) -> Any:
    """GET /recipes/extract"""
    return request_json("GET", "/recipes/extract", params={"url": url, "forceExtraction": forceExtraction, "analyze": analyze})


def analyze_recipe(*, title: str, ingredientList: str, servings: int, instructions: Optional[str] = None, language: Optional[str] = None, includeNutrition: Optional[bool] = None, includeTaste: Optional[bool] = None) -> Any:
    """POST /recipes/analyze"""
    params: Dict[str, Any] = {"language": language, "includeNutrition": includeNutrition, "includeTaste": includeTaste}
    data: Dict[str, Any] = {"title": title, "ingredientList": ingredientList, "servings": servings, "instructions": instructions}
    return request_json("POST", "/recipes/analyze", params=params, data=data)


def summarize_recipe(*, id: int) -> Any:
    """GET /recipes/{id}/summary"""
    return request_json("GET", f"/recipes/{id}/summary")


def analyze_recipe_instructions(*, instructions: str) -> Any:
    """POST /recipes/analyzeInstructions"""
    return request_json("POST", "/recipes/analyzeInstructions", data={"instructions": instructions})


def classify_cuisine(*, title: str, ingredientList: str, language: Optional[str] = None) -> Any:
    """POST /recipes/cuisine"""
    return request_json("POST", "/recipes/cuisine", params={"language": language}, data={"title": title, "ingredientList": ingredientList})


def analyze_recipe_search_query(*, q: str) -> Any:
    """GET /recipes/queries/analyze"""
    return request_json("GET", "/recipes/queries/analyze", params={"q": q})
