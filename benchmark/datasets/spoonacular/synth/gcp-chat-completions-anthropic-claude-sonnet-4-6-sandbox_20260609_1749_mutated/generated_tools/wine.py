"""Spoonacular Wine API tools."""
import os
import requests
from typing import Optional

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable not set")
    return key


def _get(path: str, params: dict) -> dict:
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_dish_pairing_for_wine(wine: str) -> dict:
    """Find dishes that go well with a given wine type (e.g. 'malbec', 'riesling')."""
    return _get("/food/wine/dishes", {"wine": wine})


def get_wine_pairing(food: str, max_price: Optional[float] = None) -> dict:
    """Find wines that pair well with a food (dish name, ingredient, or cuisine)."""
    params: dict = {"food": food}
    if max_price is not None:
        params["maxPrice"] = max_price
    return _get("/food/wine/pairing", params)


def get_wine_description(wine: str) -> dict:
    """Get a simple description of a wine type (e.g. 'malbec', 'riesling', 'merlot')."""
    return _get("/food/wine/description", {"wine": wine})


def get_wine_recommendation(
    wine: str,
    max_price: Optional[float] = None,
    min_rating: Optional[float] = None,
    number: int = 3,
) -> dict:
    """Get specific wine product recommendations for a given wine type."""
    params: dict = {"wine": wine, "number": number}
    if max_price is not None:
        params["maxPrice"] = max_price
    if min_rating is not None:
        params["minRating"] = min_rating
    return _get("/food/wine/recommendation", params)
