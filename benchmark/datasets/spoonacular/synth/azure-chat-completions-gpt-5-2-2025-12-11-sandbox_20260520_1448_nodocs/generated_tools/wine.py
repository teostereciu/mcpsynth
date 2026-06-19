from typing import Any, Dict

from .http import request_json


def wine_pairing(*, food: str, maxPrice: int | None = None, minRating: float | None = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"food": food}
    if maxPrice is not None:
        params["maxPrice"] = maxPrice
    if minRating is not None:
        params["minRating"] = minRating
    return request_json("GET", "/food/wine/pairing", params=params)


def wine_description(*, wine: str) -> Dict[str, Any]:
    return request_json("GET", "/food/wine/description", params={"wine": wine})
