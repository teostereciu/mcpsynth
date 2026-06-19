from typing import Any, Optional

from .common import spoonacular_request


def get_dish_pairing_for_wine(wine: str) -> Any:
    return spoonacular_request("GET", "/food/wine/dishes", params=locals())


def get_wine_pairing(food: str, maxPrice: Optional[float] = None) -> Any:
    return spoonacular_request("GET", "/food/wine/pairing", params=locals())


def get_wine_description(wine: str) -> Any:
    return spoonacular_request("GET", "/food/wine/description", params=locals())


def get_wine_recommendation(wine: str, maxPrice: Optional[float] = None, minRating: Optional[float] = None, number: Optional[int] = None) -> Any:
    return spoonacular_request("GET", "/food/wine/recommendation", params=locals())
