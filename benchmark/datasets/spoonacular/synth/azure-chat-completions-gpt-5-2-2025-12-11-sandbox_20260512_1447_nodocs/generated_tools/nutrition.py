from typing import Any

from .client import SpoonacularClient


def guess_nutrition_by_dish_name(title: str) -> Any:
    client = SpoonacularClient()
    return client.get("/recipes/guessNutrition", params={"title": title})
