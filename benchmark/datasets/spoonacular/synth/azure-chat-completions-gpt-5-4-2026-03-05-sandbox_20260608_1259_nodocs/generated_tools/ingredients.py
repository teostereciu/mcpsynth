from typing import Any, List, Optional

from generated_tools.common import spoonacular_request


def search_ingredients(query: str, number: Optional[int] = None, offset: Optional[int] = None, meta_information: Optional[bool] = None) -> Any:
    return spoonacular_request(
        "GET",
        "/food/ingredients/search",
        {
            "query": query,
            "number": number,
            "offset": offset,
            "metaInformation": meta_information,
        },
    )


def get_ingredient_information(ingredient_id: int, amount: Optional[float] = None, unit: Optional[str] = None) -> Any:
    return spoonacular_request(
        "GET",
        f"/food/ingredients/{ingredient_id}/information",
        {"amount": amount, "unit": unit},
    )


def parse_ingredients(ingredient_list: List[str], servings: Optional[int] = None) -> Any:
    return spoonacular_request(
        "GET",
        "/recipes/parseIngredients",
        {
            "ingredientList": "\n".join(ingredient_list),
            "servings": servings,
        },
    )


def autocomplete_ingredient_search(query: str, number: Optional[int] = None, meta_information: Optional[bool] = None, intolerances: Optional[List[str]] = None) -> Any:
    return spoonacular_request(
        "GET",
        "/food/ingredients/autocomplete",
        {
            "query": query,
            "number": number,
            "metaInformation": meta_information,
            "intolerances": intolerances,
        },
    )
