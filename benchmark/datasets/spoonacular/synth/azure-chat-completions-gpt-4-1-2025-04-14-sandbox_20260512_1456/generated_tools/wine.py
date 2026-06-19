import os
import requests

def dish_pairing_for_wine(wine):
    """
    Find a dish that goes well with a given wine.
    Corresponds to GET /food/wine/dishes
    Accepts wine (str).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/food/wine/dishes"
        params = {'apiKey': api_key, 'wine': wine}
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def wine_pairing(food, max_price=None):
    """
    Find a wine that goes well with a food.
    Corresponds to GET /food/wine/pairing
    Accepts food (str), max_price (optional number).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/food/wine/pairing"
        params = {'apiKey': api_key, 'food': food}
        if max_price is not None:
            params['maxPrice'] = max_price
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def wine_description(wine):
    """
    Get a simple description of a certain wine.
    Corresponds to GET /food/wine/description
    Accepts wine (str).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/food/wine/description"
        params = {'apiKey': api_key, 'wine': wine}
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def wine_recommendation(wine, max_price=None, min_rating=None, number=None):
    """
    Get a specific wine recommendation for a given wine type.
    Corresponds to GET /food/wine/recommendation
    Accepts wine (str), max_price (optional number), min_rating (optional float), number (optional int).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/food/wine/recommendation"
        params = {'apiKey': api_key, 'wine': wine}
        if max_price is not None:
            params['maxPrice'] = max_price
        if min_rating is not None:
            params['minRating'] = min_rating
        if number is not None:
            params['number'] = number
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
