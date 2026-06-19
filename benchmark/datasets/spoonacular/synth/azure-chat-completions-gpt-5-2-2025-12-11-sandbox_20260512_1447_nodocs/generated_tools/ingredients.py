from typing import Any, Dict, Optional

from .client import SpoonacularClient


def ingredients_search(query: str, number: int = 10, offset: int = 0) -> Any:
    client = SpoonacularClient()
    return client.get(
        "/food/ingredients/search",
        params={"query": query, "number": number, "offset": offset},
    )


def ingredient_information(ingredient_id: int, amount: Optional[float] = None, unit: Optional[str] = None) -> Any:
    client = SpoonacularClient()
    params: Dict[str, Any] = {}
    if amount is not None:
        params["amount"] = amount
    if unit is not None:
        params["unit"] = unit
    return client.get(f"/food/ingredients/{ingredient_id}/information", params=params)


def ingredients_autocomplete(query: str, number: int = 10, metaInformation: bool = True) -> Any:
    client = SpoonacularClient()
    return client.get(
        "/food/ingredients/autocomplete",
        params={"query": query, "number": number, "metaInformation": metaInformation},
    )


def parse_ingredients(ingredientList: str, servings: Optional[int] = None, includeNutrition: bool = False) -> Any:
    client = SpoonacularClient()
    params: Dict[str, Any] = {"ingredientList": ingredientList, "includeNutrition": includeNutrition}
    if servings is not None:
        params["servings"] = servings
    return client.post("/recipes/parseIngredients", params=params)
