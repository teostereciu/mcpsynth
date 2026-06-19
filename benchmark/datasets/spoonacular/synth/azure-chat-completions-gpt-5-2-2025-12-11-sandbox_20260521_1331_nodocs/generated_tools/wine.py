from typing import Any, Dict, Optional

from .http import request_json


def wine_pairing(dish: str) -> Dict[str, Any]:
    return request_json("GET", "/food/wine/pairing", params={"food": dish})


def wine_description(wine: str) -> Dict[str, Any]:
    return request_json("GET", "/food/wine/description", params={"wine": wine})


def wine_recommendation(
    wine: str,
    maxPrice: Optional[float] = None,
    minRating: Optional[float] = None,
    number: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"wine": wine}
    if maxPrice is not None:
        params["maxPrice"] = maxPrice
    if minRating is not None:
        params["minRating"] = minRating
    if number is not None:
        params["number"] = number
    return request_json("GET", "/food/wine/recommendation", params=params)
