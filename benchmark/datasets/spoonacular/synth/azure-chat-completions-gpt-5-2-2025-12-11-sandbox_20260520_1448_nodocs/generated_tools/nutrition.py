from typing import Any, Dict, Optional

from .http import request_json


def nutrition_guess_by_dish_name(*, title: str) -> Dict[str, Any]:
    return request_json("GET", "/recipes/guessNutrition", params={"title": title})


def nutrition_visualize_recipe_nutrition(*, id: int, defaultCss: Optional[bool] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if defaultCss is not None:
        params["defaultCss"] = defaultCss
    return request_json("GET", f"/recipes/{id}/nutritionWidget", params=params)
