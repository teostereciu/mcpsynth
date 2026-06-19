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


def _get(path: str, params: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        r = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def get_dish_pairing_for_wine(wine: str) -> dict:
    """Find dishes that go well with a given wine type (e.g. 'malbec', 'riesling', 'merlot')."""
    return _get("/food/wine/dishes", {"wine": wine})


def get_wine_pairing(food: str, max_price: Optional[float] = None) -> dict:
    """Find wines that pair well with a food. Food can be a dish name ('steak'),
    an ingredient ('salmon'), or a cuisine ('italian')."""
    return _get("/food/wine/pairing", {
        "food": food,
        "maxPrice": max_price,
    })


def get_wine_description(wine: str) -> dict:
    """Get a simple description of a wine type, e.g. 'malbec', 'riesling', or 'merlot'."""
    return _get("/food/wine/description", {"wine": wine})


def get_wine_recommendation(
    wine: str,
    max_price: Optional[float] = None,
    min_rating: Optional[float] = None,
    number: Optional[int] = None,
) -> dict:
    """Get specific wine product recommendations for a given wine type.
    min_rating: between 0 and 1 (e.g. 0.8 = 4 out of 5 stars)."""
    return _get("/food/wine/recommendation", {
        "wine": wine,
        "maxPrice": max_price,
        "minRating": min_rating,
        "number": number,
    })
