from typing import Any

from generated_tools.common import spoonacular_request


def get_wine_pairing(food: str) -> Any:
    return spoonacular_request("GET", "/food/wine/pairing", {"food": food})


def get_wine_description(wine: str) -> Any:
    return spoonacular_request("GET", "/food/wine/description", {"wine": wine})
