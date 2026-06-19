"""
Spoonacular Wine tools — pairing, dish recommendations, and wine descriptions.
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
    params["apiKey"] = _api_key()
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def get_wine_pairing(food: str, max_price: float = 0) -> dict:
    """
    Get wine pairing suggestions for a given dish or food type.

    Args:
        food: The food or dish to pair wine with (e.g. "steak", "salmon",
              "pasta carbonara", "cheese").
        max_price: Maximum price (USD) for the wine recommendation. 0 = no limit.

    Returns:
        dict with 'pairedWines' list, 'pairingText' description, and
        'productMatches' with specific purchasable wine products.
    """
    params: dict = {"food": food}
    if max_price > 0:
        params["maxPrice"] = max_price
    return _get("/food/wine/pairing", params)


def get_wine_description(wine: str) -> dict:
    """
    Get a description of a wine type including taste profile and food pairings.

    Args:
        wine: Wine variety name (e.g. "merlot", "chardonnay", "pinot noir",
              "sauvignon blanc", "riesling").

    Returns:
        dict with 'wineDescription' text.
    """
    return _get("/food/wine/description", {"wine": wine})


def get_wine_recommendation(
    wine: str,
    max_price: float = 0,
    min_rating: float = 0,
    number: int = 10,
) -> dict:
    """
    Get specific wine product recommendations for a given wine variety.

    Args:
        wine: Wine variety (e.g. "merlot", "chardonnay", "pinot noir").
        max_price: Maximum price (USD). 0 = no limit.
        min_rating: Minimum rating (0.0–1.0). 0 = no minimum.
        number: Number of recommendations to return.

    Returns:
        dict with 'recommendedWines' list of purchasable wine products.
    """
    params: dict = {"wine": wine, "number": number}
    if max_price > 0:
        params["maxPrice"] = max_price
    if min_rating > 0:
        params["minRating"] = min_rating
    return _get("/food/wine/recommendation", params)


def get_dish_pairing_for_wine(wine: str) -> dict:
    """
    Get dish pairing suggestions for a given wine variety.

    Args:
        wine: Wine variety (e.g. "merlot", "chardonnay", "cabernet sauvignon").

    Returns:
        dict with 'pairings' list of dishes and 'text' description.
    """
    return _get("/food/wine/dishes", {"wine": wine})
