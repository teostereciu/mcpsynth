from typing import Any, Dict, Optional

from .http import request_json


def wine_dish_pairing(*, wine: str) -> Any:
    """GET /food/wine/dishes"""
    return request_json("GET", "/food/wine/dishes", params={"wine": wine})


def wine_pairing(*, food: str, maxPrice: Optional[float] = None) -> Any:
    """GET /food/wine/pairing"""
    params: Dict[str, Any] = {"food": food, "maxPrice": maxPrice}
    return request_json("GET", "/food/wine/pairing", params=params)


def wine_description(*, wine: str) -> Any:
    """GET /food/wine/description"""
    return request_json("GET", "/food/wine/description", params={"wine": wine})


def wine_recommendation(*, wine: str, maxPrice: Optional[float] = None, minRating: Optional[float] = None, number: Optional[int] = None) -> Any:
    """GET /food/wine/recommendation"""
    params: Dict[str, Any] = {"wine": wine, "maxPrice": maxPrice, "minRating": minRating, "number": number}
    return request_json("GET", "/food/wine/recommendation", params=params)
