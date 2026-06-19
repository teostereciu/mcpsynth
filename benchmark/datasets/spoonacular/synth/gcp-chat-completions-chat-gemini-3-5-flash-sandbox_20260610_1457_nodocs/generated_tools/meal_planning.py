from typing import Optional, Dict, Any
from generated_tools.client import request

def generate_meal_plan(
    timeFrame: Optional[str] = None,
    targetCalories: Optional[float] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None
) -> Dict[str, Any]:
    """
    Generate a meal plan for a day or a week based on target calories and dietary preferences.
    
    Args:
        timeFrame: The time frame of the meal plan ('day' or 'week').
        targetCalories: The target calories for the day/week.
        diet: The diet for which the meal plan must be suitable (e.g., "vegetarian", "vegan", "paleo").
        exclude: A comma-separated list of ingredients or allergens to exclude (e.g., "shellfish,olives").
    """
    params = {}
    if timeFrame is not None:
        params["timeFrame"] = timeFrame
    if targetCalories is not None:
        params["targetCalories"] = targetCalories
    if diet is not None:
        params["diet"] = diet
    if exclude is not None:
        params["exclude"] = exclude
        
    return request("GET", "/mealplanner/generate", params=params)
