from typing import Any, Dict

from server import _request


def search_recipes(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/recipes/complexSearch", params=params)


def search_recipes_by_nutrients(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/recipes/findByNutrients", params=params)


def search_recipes_by_ingredients(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/recipes/findByIngredients", params=params)


def get_recipe_information(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/recipes/{id}/information", params=params)


def get_recipe_information_bulk(ids: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", "/recipes/informationBulk", params={**params, "ids": ids})


def get_similar_recipes(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/recipes/{id}/similar", params=params)


def get_random_recipes(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/recipes/random", params=params)


def autocomplete_recipe_search(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/recipes/autocomplete", params=params)


def get_recipe_taste(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/recipes/{id}/tasteWidget.json", params=params)


def get_recipe_equipment(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/recipes/{id}/equipmentWidget.json", params=params)


def get_recipe_price_breakdown(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/recipes/{id}/priceBreakdownWidget.json", params=params)


def get_recipe_ingredients(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/recipes/{id}/ingredientWidget.json", params=params)


def get_recipe_nutrition_by_id(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/recipes/{id}/nutritionWidget.json", params=params)


def get_analyzed_recipe_instructions(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/recipes/{id}/analyzedInstructions", params=params)


def extract_recipe_from_website(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/recipes/extract", params=params)


def analyze_recipe(**params: Any) -> Dict[str, Any]:
    return _request("POST", "/recipes/analyze", data=params)


def summarize_recipe(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/recipes/summary", params=params)


def analyze_recipe_instructions(**params: Any) -> Dict[str, Any]:
    return _request("POST", "/recipes/analyzeInstructions", data=params)


def classify_cuisine(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/recipes/cuisine", params=params)


def analyze_recipe_search_query(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/recipes/queries/analyze", params=params)
