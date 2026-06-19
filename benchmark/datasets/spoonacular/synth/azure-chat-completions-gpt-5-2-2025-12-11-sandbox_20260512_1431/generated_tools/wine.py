from typing import Any, Dict, Optional

from .http_client import request_json


def wine_dish_pairing(wine: str) -> Dict[str, Any]:
    """GET /food/wine/dishes"""
    return request_json("GET", "/food/wine/dishes", params={"wine": wine})


def wine_pairing(food: str, maxPrice: Optional[float] = None) -> Dict[str, Any]:
    """GET /food/wine/pairing"""
    params: Dict[str, Any] = {"food": food}
    if maxPrice is not None:
        params["maxPrice"] = maxPrice
    return request_json("GET", "/food/wine/pairing", params=params)


def wine_description(wine: str) -> Dict[str, Any]:
    """GET /food/wine/description"""
    return request_json("GET", "/food/wine/description", params={"wine": wine})


def wine_recommendation(
    wine: str,
    number: Optional[int] = None,
    maxPrice: Optional[float] = None,
    minRating: Optional[float] = None,
) -> Dict[str, Any]:
    """GET /food/wine/recommendation"""
    params: Dict[str, Any] = {"wine": wine}
    for k, v in {"number": number, "maxPrice": maxPrice, "minRating": minRating}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/food/wine/recommendation", params=params)
