"""
Spoonacular Wine API tools.
Endpoints covered:
  - GET /food/wine/dishes
  - GET /food/wine/pairing
  - GET /food/wine/description
  - GET /food/wine/recommendation
"""

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
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ---------------------------------------------------------------------------
# Dish Pairing for Wine
# ---------------------------------------------------------------------------

def get_dish_pairing_for_wine(wine: str) -> dict:
    """Find dishes that pair well with a given wine type (e.g. 'malbec', 'riesling')."""
    return _get("/food/wine/dishes", {"wine": wine})


# ---------------------------------------------------------------------------
# Wine Pairing
# ---------------------------------------------------------------------------

def get_wine_pairing(food: str, max_price: Optional[float] = None) -> dict:
    """Find wines that pair well with a food (dish name, ingredient, or cuisine)."""
    return _get("/food/wine/pairing", {
        "food": food,
        "maxPrice": max_price,
    })


# ---------------------------------------------------------------------------
# Wine Description
# ---------------------------------------------------------------------------

def get_wine_description(wine: str) -> dict:
    """Get a simple description of a wine type (e.g. 'malbec', 'riesling', 'merlot')."""
    return _get("/food/wine/description", {"wine": wine})


# ---------------------------------------------------------------------------
# Wine Recommendation
# ---------------------------------------------------------------------------

def get_wine_recommendation(
    wine: str,
    max_price: Optional[float] = None,
    min_rating: Optional[float] = None,
    number: Optional[int] = None,
) -> dict:
    """Get specific wine product recommendations for a given wine type."""
    return _get("/food/wine/recommendation", {
        "wine": wine,
        "maxPrice": max_price,
        "minRating": min_rating,
        "number": number,
    })
