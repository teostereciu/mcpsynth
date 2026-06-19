from typing import Any, Dict, Optional

from .http_client import request_json


def connect_user(*, username: str, firstName: Optional[str] = None, lastName: Optional[str] = None, email: Optional[str] = None) -> Any:
    """POST /users/connect

    Returns a spoonacular username + hash for meal planner endpoints.
    """
    data: Dict[str, Any] = {"username": username, "firstName": firstName, "lastName": lastName, "email": email}
    return request_json("POST", "/users/connect", data=data)


def get_meal_plan_week(*, username: str, start_date: str, hash: str) -> Any:
    """GET /mealplanner/{username}/week/{start-date}"""
    return request_json("GET", f"/mealplanner/{username}/week/{start_date}", params={"hash": hash})


def get_meal_plan_day(*, username: str, date: str, hash: str) -> Any:
    """GET /mealplanner/{username}/day/{date}"""
    return request_json("GET", f"/mealplanner/{username}/day/{date}", params={"hash": hash})


def generate_meal_plan(
    *,
    timeFrame: str,
    targetCalories: Optional[int] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None,
) -> Any:
    """GET /mealplanner/generate"""
    params: Dict[str, Any] = {
        "timeFrame": timeFrame,
        "targetCalories": targetCalories,
        "diet": diet,
        "exclude": exclude,
    }
    return request_json("GET", "/mealplanner/generate", params=params)
