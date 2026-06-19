from typing import Any

from generated_tools.common import spoonacular_request


def get_recipe_nutrition_by_id(recipe_id: int) -> Any:
    return spoonacular_request("GET", f"/recipes/{recipe_id}/nutritionWidget.json")


def visualize_recipe_nutrition(recipe_id: int, default_css: bool = True) -> Any:
    return spoonacular_request(
        "GET",
        f"/recipes/{recipe_id}/nutritionWidget",
        {"defaultCss": default_css},
    )
