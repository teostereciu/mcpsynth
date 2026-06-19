import os
import requests

def search_menu_items(params):
    """
    Search menu items from fast food and chain restaurants.
    Corresponds to GET /food/menuItems/search
    Accepts params as a dict of query parameters.
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/food/menuItems/search"
        params = params.copy()
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_menu_item_information(menu_item_id):
    """
    Get all available information about a menu item by ID.
    Corresponds to GET /food/menuItems/{id}
    Accepts menu_item_id (int).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = f"https://api.spoonacular.com/food/menuItems/{menu_item_id}"
        params = {'apiKey': api_key}
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def autocomplete_menu_item_search(query, number=10):
    """
    Generate suggestions for menu items based on a (partial) query.
    Corresponds to GET /food/menuItems/suggest
    Accepts query (str), number (int, default 10).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/food/menuItems/suggest"
        params = {'apiKey': api_key, 'query': query, 'number': number}
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
