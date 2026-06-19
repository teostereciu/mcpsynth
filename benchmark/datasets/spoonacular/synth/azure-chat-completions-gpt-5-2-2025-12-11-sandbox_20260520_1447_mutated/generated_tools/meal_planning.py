from typing import Any, Dict, Optional

from .http_client import request_json


def get_meal_plan_week(*, username: str, start_date: str, hash: str) -> Dict[str, Any]:
    """GET /mealplanner/{username}/week/{start-date}"""
    return request_json(
        "GET",
        f"/mealplanner/{username}/week/{start_date}",
        params={"hash": hash},
    )


def get_meal_plan_day(*, username: str, date: str, hash: str) -> Dict[str, Any]:
    """GET /mealplanner/{username}/day/{date}"""
    return request_json(
        "GET",
        f"/mealplanner/{username}/day/{date}",
        params={"hash": hash},
    )


def generate_meal_plan(
    *,
    timeFrame: str,
    targetCalories: Optional[int] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /mealplanner/generate"""
    params: Dict[str, Any] = {"timeFrame": timeFrame}
    for k, v in {"targetCalories": targetCalories, "diet": diet, "exclude": exclude}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/mealplanner/generate", params=params)


def connect_user(*, body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /users/connect

    The docs describe a JSON body with user details.
    """
    return request_json("POST", "/users/connect", json=body)
