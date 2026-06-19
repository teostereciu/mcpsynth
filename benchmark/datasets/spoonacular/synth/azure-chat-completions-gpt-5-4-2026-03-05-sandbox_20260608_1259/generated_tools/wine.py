from typing import Any, Optional

from generated_tools.recipes import _request


def get_dish_pairing_for_wine(wine: str) -> Any:
    return _request("GET", "/food/wine/dishes", locals())


def get_wine_pairing(food: str, maxPrice: Optional[float] = None) -> Any:
    return _request("GET", "/food/wine/pairing", locals())


def get_wine_description(wine: str) -> Any:
    return _request("GET", "/food/wine/description", locals())


def get_wine_recommendation(wine: str, maxPrice: Optional[float] = None, minRating: Optional[float] = None, number: Optional[int] = None) -> Any:
    return _request("GET", "/food/wine/recommendation", locals())
