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
    params["apiKey"] = _api_key()
    url = f"{BASE_URL}{path}"
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# Wine pairing for a dish
# ---------------------------------------------------------------------------

def get_dish_pairing_for_wine(wine: str) -> dict:
    """
    Get dishes that pair well with a given wine type.

    Args:
        wine: The wine type to find dish pairings for
              (e.g. 'merlot', 'chardonnay', 'pinot noir').

    Returns:
        dict with 'pairings' list of dish names and 'text' description.
    """
    try:
        params = {"wine": wine}
        return _get("/food/wine/dishes", params)
    except Exception as exc:
        return {"error": str(exc)}


def get_wine_pairing(food: str, max_price: float = None) -> dict:
    """
    Get wine pairings for a given food or dish.

    Args:
        food: The food or dish to find wine pairings for
              (e.g. 'steak', 'salmon', 'pasta carbonara').
        max_price: Maximum price (USD) for the recommended wine.

    Returns:
        dict with 'pairedWines' list, 'pairingText' description, and
        'productMatches' with specific purchasable wine products.
    """
    try:
        params: dict = {"food": food}
        if max_price is not None:
            params["maxPrice"] = max_price
        return _get("/food/wine/pairing", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Wine description
# ---------------------------------------------------------------------------

def get_wine_description(wine: str) -> dict:
    """
    Get a description of a wine type including taste profile and food pairings.

    Args:
        wine: The wine type to describe
              (e.g. 'merlot', 'chardonnay', 'sauvignon blanc').

    Returns:
        dict with 'wineDescription' text.
    """
    try:
        params = {"wine": wine}
        return _get("/food/wine/description", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Wine recommendation
# ---------------------------------------------------------------------------

def get_wine_recommendation(
    wine: str,
    max_price: float = None,
    min_rating: float = 0.7,
    number: int = 10,
) -> dict:
    """
    Get specific wine product recommendations for a given wine type.

    Args:
        wine: The wine type to recommend (e.g. 'merlot', 'chardonnay').
        max_price: Maximum price (USD) for the wine.
        min_rating: Minimum rating (0–1) for the wine (default 0.7).
        number: Number of wine recommendations to return.

    Returns:
        dict with 'recommendedWines' list of wine products with prices and ratings.
    """
    try:
        params: dict = {"wine": wine, "minRating": min_rating, "number": number}
        if max_price is not None:
            params["maxPrice"] = max_price
        return _get("/food/wine/recommendation", params)
    except Exception as exc:
        return {"error": str(exc)}
