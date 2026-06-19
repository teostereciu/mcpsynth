from typing import Any, Dict, Optional

from .client import SpoonacularClient


def wine_pairing(food: str, maxPrice: Optional[float] = None, minRating: Optional[float] = None) -> Any:
    client = SpoonacularClient()
    params: Dict[str, Any] = {"food": food}
    if maxPrice is not None:
        params["maxPrice"] = maxPrice
    if minRating is not None:
        params["minRating"] = minRating
    return client.get("/food/wine/pairing", params=params)


def wine_description(wine: str) -> Any:
    client = SpoonacularClient()
    return client.get("/food/wine/description", params={"wine": wine})
