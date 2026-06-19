import os
import requests

def search_grocery_products(params):
    """
    Search packaged food products.
    Corresponds to GET /food/products/search
    Accepts params as a dict of query parameters.
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/food/products/search"
        params = params.copy()
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_grocery_products_by_upc(upc):
    """
    Get information about a packaged food using its UPC.
    Corresponds to GET /food/products/upc/{upc}
    Accepts upc (str or int).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = f"https://api.spoonacular.com/food/products/upc/{upc}"
        params = {'apiKey': api_key}
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_product_information(product_id):
    """
    Get full information about a product by ID.
    Corresponds to GET /food/products/{id}
    Accepts product_id (int).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = f"https://api.spoonacular.com/food/products/{product_id}"
        params = {'apiKey': api_key}
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
