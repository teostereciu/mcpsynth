from typing import Any, Dict

from server import _request


def get_meal_plan_week(username: Any, start_date: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/mealplanner/{username}/week/{start_date}", params=params)


def get_meal_plan_day(username: Any, date: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/mealplanner/{username}/day/{date}", params=params)


def generate_meal_plan(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/mealplanner/generate", params=params)


def get_meal_plan_templates(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/mealplanner/templates", params=params)


def get_meal_plan_template(id: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/mealplanner/templates/{id}", params=params)


def get_shopping_list(username: Any, hash_value: Any, **params: Any) -> Dict[str, Any]:
    return _request("GET", f"/mealplanner/{username}/shopping-list/{hash_value}", params=params)
