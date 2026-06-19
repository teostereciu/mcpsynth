from typing import Any, Dict, Optional

from .client import SpoonacularClient


def meal_plan_generate(
    timeFrame: str = "day",
    targetCalories: Optional[int] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None,
) -> Any:
    client = SpoonacularClient()
    params: Dict[str, Any] = {"timeFrame": timeFrame}
    if targetCalories is not None:
        params["targetCalories"] = targetCalories
    if diet is not None:
        params["diet"] = diet
    if exclude is not None:
        params["exclude"] = exclude
    return client.get("/mealplanner/generate", params=params)
