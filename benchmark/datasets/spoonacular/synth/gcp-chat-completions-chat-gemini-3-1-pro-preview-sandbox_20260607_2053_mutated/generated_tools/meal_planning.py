from typing import Optional, Dict, Any
from .recipes import make_request

def generate_meal_plan(timeFrame: str = "day", targetCalories: Optional[int] = None, diet: Optional[str] = None, exclude: Optional[str] = None) -> Any:
    """Generate a meal plan (daily or weekly). timeFrame must be 'day' or 'week'."""
    params = {"timeFrame": timeFrame}
    if targetCalories is not None: params["targetCalories"] = targetCalories
    if diet: params["diet"] = diet
    if exclude: params["exclude"] = exclude
    return make_request("GET", "/mealplanner/generate", params=params)

def get_meal_plan_week(username: str, start_date: str, hash: str) -> Any:
    """Get a meal plan for a week. start_date format: YYYY-MM-DD."""
    params = {"hash": hash}
    return make_request("GET", f"/mealplanner/{username}/week/{start_date}", params=params)

def get_meal_plan_day(username: str, date: str, hash: str) -> Any:
    """Get a meal plan for a day. date format: YYYY-MM-DD."""
    params = {"hash": hash}
    return make_request("GET", f"/mealplanner/{username}/day/{date}", params=params)
