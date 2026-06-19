"""
Spoonacular Wine tools — pairing, description, and recommendation.
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
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def get_wine_pairing(
    food: str,
    max_price: float = None,
) -> dict:
    """
    Get wine pairing suggestions for a specific dish or food type.

    Args:
        food: The food or dish to pair wine with (e.g. 'steak', 'salmon',
              'pasta carbonara', 'cheese').
        max_price: Maximum price (USD) for the recommended wines.

    Returns:
        dict with 'pairedWines' list, 'pairingText' description, and
        'productMatches' with specific purchasable wine products.
    """
    return _get("/food/wine/pairing", {"food": food, "maxPrice": max_price})


def get_wine_description(wine: str) -> dict:
    """
    Get a description of a wine type including taste profile and food pairings.

    Args:
        wine: Wine variety name (e.g. 'merlot', 'chardonnay', 'pinot noir',
              'sauvignon blanc', 'riesling').

    Returns:
        dict with 'wineDescription' text describing the wine's characteristics.
    """
    return _get("/food/wine/description", {"wine": wine})


def get_wine_recommendation(
    wine: str,
    max_price: float = None,
    min_rating: float = None,
    number: int = 10,
) -> dict:
    """
    Get specific wine product recommendations for a given wine variety.

    Args:
        wine: Wine variety to recommend (e.g. 'merlot', 'chardonnay',
              'cabernet sauvignon', 'pinot grigio').
        max_price: Maximum price (USD) per bottle.
        min_rating: Minimum rating (0.0 to 1.0) for recommended wines.
        number: Number of recommendations to return (default 10).

    Returns:
        dict with 'recommendedWines' list of specific wine products with
        prices, ratings, and descriptions.
    """
    return _get("/food/wine/recommendation", {
        "wine": wine,
        "maxPrice": max_price,
        "minRating": min_rating,
        "number": number,
    })


def get_dish_pairing_for_wine(wine: str) -> dict:
    """
    Get food/dish pairing suggestions for a given wine variety.

    Args:
        wine: Wine variety name (e.g. 'merlot', 'chardonnay', 'pinot noir').

    Returns:
        dict with 'pairings' list of dishes that pair well with the wine
        and a 'text' description of the pairing rationale.
    """
    return _get("/food/wine/dishes", {"wine": wine})
