from typing import Any, Dict

from server import _request


def ingredient_search(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/ingredients/search", params=params)


def get_ingredient_information(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/food/ingredients/{id}/information", params=params)


def compute_ingredient_amount(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/food/ingredients/{id}/amount", params=params)


def convert_amounts(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/recipes/convert", params=params)


def parse_ingredients(**params: Any) -> Dict[str, Any]:
    return _request("POST", "/recipes/parseIngredients", data=params)


def autocomplete_ingredient_search(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/ingredients/autocomplete", params=params)


def get_ingredient_substitutes(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/ingredients/substitutes", params=params)


def get_ingredient_substitutes_by_id(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/food/ingredients/{id}/substitutes", params=params)
