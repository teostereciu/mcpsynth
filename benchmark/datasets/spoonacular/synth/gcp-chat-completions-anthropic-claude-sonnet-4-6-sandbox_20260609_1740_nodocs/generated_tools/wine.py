"""
Spoonacular Wine tools — pairing, description, recommendation.
"""
import os
import requests

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def get_dish_pairing_for_wine(wine: str) -> dict:
    """
    Get dishes that pair well with a given wine type (e.g. 'merlot',
    'chardonnay', 'riesling'). Returns a list of pairing suggestions
    with explanations.
    """
    params = {"wine": wine}
    return _get("/food/wine/dishes", params)


def get_wine_pairing_for_dish(food: str, max_price: float = None) -> dict:
    """
    Get wine recommendations that pair well with a given dish or food type
    (e.g. 'steak', 'salmon', 'pasta carbonara'). Optionally filter by
    maximum price per bottle.
    """
    params = {"food": food, "maxPrice": max_price}
    return _get("/food/wine/pairing", params)


def get_wine_description(wine: str) -> dict:
    """
    Get a description of a wine type (e.g. 'pinot noir', 'sauvignon blanc'),
    including taste profile, typical pairings, and serving suggestions.
    """
    params = {"wine": wine}
    return _get("/food/wine/description", params)


def get_wine_recommendation(
    wine: str,
    max_price: float = None,
    min_rating: float = None,
    number: int = 10,
) -> dict:
    """
    Get specific wine product recommendations for a given wine type.
    Optionally filter by maximum price and minimum rating (0–1 scale).
    Returns a list of recommended wines with prices and ratings.
    """
    params = {
        "wine": wine,
        "maxPrice": max_price,
        "minRating": min_rating,
        "number": number,
    }
    return _get("/food/wine/recommendation", params)
