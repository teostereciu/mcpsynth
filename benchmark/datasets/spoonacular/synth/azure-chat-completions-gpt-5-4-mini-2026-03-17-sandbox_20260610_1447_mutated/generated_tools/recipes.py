from typing import Any, Dict
from generated_tools.spoonacular_client import request


def search_recipes(**kwargs) -> Dict[str, Any]:
    return request("GET", "/recipes/complexSearch", params=kwargs)


def search_recipes_by_nutrients(**kwargs) -> Dict[str, Any]:
    return request("GET", "/recipes/findByNutrients", params=kwargs)


def search_recipes_by_ingredients(**kwargs) -> Dict[str, Any]:
    return request("GET", "/recipes/findByIngredients", params=kwargs)


def get_recipe_information(recipe_id: int, **kwargs) -> Dict[str, Any]:
    return request("GET", f"/recipes/{recipe_id}/information", params=kwargs)


def get_similar_recipes(recipe_id: int, **kwargs) -> Dict[str, Any]:
    return request("GET", f"/recipes/{recipe_id}/similar", params=kwargs)


def autocomplete_recipe_search(**kwargs) -> Dict[str, Any]:
    return request("GET", "/recipes/autocomplete", params=kwargs)


def get_analyzed_recipe_instructions(recipe_id: int, **kwargs) -> Dict[str, Any]:
    return request("GET", f"/recipes/{recipe_id}/analyzedInstructions", params=kwargs)


def get_recipe_nutrition_by_id(recipe_id: int, **kwargs) -> Dict[str, Any]:
    return request("GET", f"/recipes/{recipe_id}/nutritionWidget.json", params=kwargs)
