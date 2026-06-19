from typing import Any, Dict
from generated_tools.spoonacular_client import request


def search_ingredients(**kwargs) -> Dict[str, Any]:
    return request("GET", "/food/ingredients/search", params=kwargs)


def get_ingredient_information(ingredient_id: int, **kwargs) -> Dict[str, Any]:
    return request("GET", f"/food/ingredients/{ingredient_id}/information", params=kwargs)


def compute_ingredient_amount(ingredient_id: int, **kwargs) -> Dict[str, Any]:
    return request("GET", f"/food/ingredients/{ingredient_id}/amount", params=kwargs)


def convert_amounts(**kwargs) -> Dict[str, Any]:
    return request("GET", "/recipes/convert", params=kwargs)


def parse_ingredients(**kwargs) -> Dict[str, Any]:
    return request("POST", "/recipes/parseIngredients", data=kwargs)


def autocomplete_ingredient_search(**kwargs) -> Dict[str, Any]:
    return request("GET", "/food/ingredients/autocomplete", params=kwargs)
