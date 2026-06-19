from typing import Any, Optional

from generated_tools.common import spoonacular_request


def generate_meal_plan(
    time_frame: str,
    target_calories: Optional[int] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None,
) -> Any:
    return spoonacular_request(
        "GET",
        "/mealplanner/generate",
        {
            "timeFrame": time_frame,
            "targetCalories": target_calories,
            "diet": diet,
            "exclude": exclude,
        },
    )


def get_meal_plan_week(username: str, start_date: Optional[str] = None, hash: Optional[str] = None) -> Any:
    return spoonacular_request(
        "GET",
        f"/mealplanner/{username}/week/{start_date or ''}",
        {"hash": hash},
    )
