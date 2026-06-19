from typing import Any, Dict
from generated_tools.spoonacular_client import request


def get_meal_plan_week(username: str, start_date: str, **kwargs) -> Dict[str, Any]:
    return request("GET", f"/mealplanner/{username}/week/{start_date}", params=kwargs)


def get_meal_plan_day(username: str, date: str, **kwargs) -> Dict[str, Any]:
    return request("GET", f"/mealplanner/{username}/day/{date}", params=kwargs)


def generate_meal_plan(**kwargs) -> Dict[str, Any]:
    return request("GET", "/mealplanner/generate", params=kwargs)
