from typing import Any, Dict, Optional

from .http import request_json


def mealplan_generate(
    *,
    timeFrame: str = "day",
    targetCalories: Optional[int] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"timeFrame": timeFrame}
    if targetCalories is not None:
        params["targetCalories"] = targetCalories
    if diet is not None:
        params["diet"] = diet
    if exclude is not None:
        params["exclude"] = exclude
    return request_json("GET", "/mealplanner/generate", params=params)
