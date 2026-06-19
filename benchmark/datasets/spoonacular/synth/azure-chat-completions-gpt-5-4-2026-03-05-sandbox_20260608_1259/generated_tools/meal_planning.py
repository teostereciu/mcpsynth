from typing import Any, Optional

from generated_tools.recipes import _request


def get_meal_plan_week(username: str, start_date: str, hash: str) -> Any:
    return _request("GET", f"/mealplanner/{username}/week/{start_date}", {"hash": hash})


def get_meal_plan_day(username: str, date: str, hash: str) -> Any:
    return _request("GET", f"/mealplanner/{username}/day/{date}", {"hash": hash})


def generate_meal_plan(timeFrame: str, targetCalories: Optional[int] = None, diet: Optional[str] = None, exclude: Optional[str] = None) -> Any:
    return _request("GET", "/mealplanner/generate", locals())


def get_shopping_list(username: str, hash: str) -> Any:
    return _request("GET", f"/mealplanner/{username}/shopping-list", {"hash": hash})


def generate_shopping_list(username: str, start_date: str, end_date: str, hash: str) -> Any:
    return _request("GET", f"/mealplanner/{username}/shopping-list/{start_date}/{end_date}", {"hash": hash})


def search_custom_foods(query: str, username: str, hash: str, number: Optional[int] = None) -> Any:
    return _request("GET", "/food/customFoods/search", {"query": query, "username": username, "hash": hash, "number": number})
