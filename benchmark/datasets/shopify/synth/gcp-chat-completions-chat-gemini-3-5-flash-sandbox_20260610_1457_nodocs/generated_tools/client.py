import os
import requests
from typing import Any, Dict, Optional

class ShopifyClient:
    def __init__(self):
        self.access_token = os.environ.get("SHOPIFY_ACCESS_TOKEN", "").strip()
        store_url = os.environ.get("SHOPIFY_STORE_URL", "").strip()
        
        # Clean store URL
        if store_url.startswith("https://"):
            store_url = store_url[len("https://"):]
        if store_url.startswith("http://"):
            store_url = store_url[len("http://"):]
        self.store_url = store_url.rstrip("/")
        
        self.base_url = f"https://{self.store_url}/admin/api/2026-01"
        self.session = requests.Session()
        self.session.headers.update({
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json"
        })

    def request(self, method: str, path: str, params: Optional[Dict[str, Any]] = None, json_data: Optional[Dict[str, Any]] = None) -> Any:
        if not self.access_token:
            return {"error": "SHOPIFY_ACCESS_TOKEN environment variable is not set."}
        if not self.store_url:
            return {"error": "SHOPIFY_STORE_URL environment variable is not set."}
            
        url = f"{self.base_url}/{path.lstrip('/')}"
        try:
            response = self.session.request(method, url, params=params, json=json_data, timeout=30)
            if response.status_code in [200, 201]:
                try:
                    return response.json()
                except ValueError:
                    return {"success": True, "status_code": response.status_code, "text": response.text}
            elif response.status_code == 204:
                return {"success": True, "status_code": 204}
            else:
                try:
                    err_json = response.json()
                    return {"error": f"API Error {response.status_code}", "details": err_json}
                except ValueError:
                    return {"error": f"API Error {response.status_code}", "details": response.text}
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self.request("GET", path, params=params)

    def post(self, path: str, json_data: Optional[Dict[str, Any]] = None) -> Any:
        return self.request("POST", path, json_data=json_data)

    def put(self, path: str, json_data: Optional[Dict[str, Any]] = None) -> Any:
        return self.request("PUT", path, json_data=json_data)

    def delete(self, path: str) -> Any:
        return self.request("DELETE", path)

client = ShopifyClient()
