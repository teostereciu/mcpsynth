import os
import base64
import time
import requests
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
app = FastMCP("eBay Commerce API")

def get_basic_auth_header(client_id: str, client_secret: str) -> str:
    credentials = f"{client_id}:{client_secret}"
    encoded = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return f"Basic {encoded}"

class EBayAuthManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EBayAuthManager, cls).__new__(cls)
            cls._instance._init_manager()
        return cls._instance

    def _init_manager(self):
        self.client_id = os.environ.get("EBAY_APP_ID")
        self.client_secret = os.environ.get("EBAY_CERT_ID")
        self.refresh_token = os.environ.get("EBAY_REFRESH_TOKEN")
        self.env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
        
        self.app_token = None
        self.app_token_expires_at = 0
        
        self.user_token = None
        self.user_token_expires_at = 0

    def get_base_url(self, is_media: bool = False) -> str:
        if self.env == "PRODUCTION":
            return "https://apim.ebay.com" if is_media else "https://api.ebay.com"
        else:
            return "https://apim.sandbox.ebay.com" if is_media else "https://api.sandbox.ebay.com"

    def get_app_token(self) -> str:
        if self.app_token and time.time() < self.app_token_expires_at - 60:
            return self.app_token
            
        if not self.client_id or not self.client_secret:
            raise ValueError("EBAY_APP_ID and EBAY_CERT_ID environment variables are required.")
            
        base_url = self.get_base_url(is_media=False)
        url = f"{base_url}/identity/v1/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": get_basic_auth_header(self.client_id, self.client_secret)
        }
        data = {
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope"
        }
        
        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            raise Exception(f"Failed to obtain App Token: {response.status_code} {response.text}")
            
        res_json = response.json()
        self.app_token = res_json["access_token"]
        self.app_token_expires_at = time.time() + int(res_json.get("expires_in", 7200))
        return self.app_token

    def get_user_token(self) -> str:
        if self.user_token and time.time() < self.user_token_expires_at - 60:
            return self.user_token
            
        if not self.client_id or not self.client_secret or not self.refresh_token:
            raise ValueError("EBAY_APP_ID, EBAY_CERT_ID, and EBAY_REFRESH_TOKEN environment variables are required.")
            
        base_url = self.get_base_url(is_media=False)
        url = f"{base_url}/identity/v1/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": get_basic_auth_header(self.client_id, self.client_secret)
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }
        
        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            raise Exception(f"Failed to obtain User Token: {response.status_code} {response.text}")
            
        res_json = response.json()
        self.user_token = res_json["access_token"]
        self.user_token_expires_at = time.time() + int(res_json.get("expires_in", 7200))
        return self.user_token

def make_request(method: str, path: str, is_media: bool = False, use_user_token: bool = False, params: dict = None, json_data: dict = None, headers: dict = None, files: dict = None):
    try:
        auth_manager = EBayAuthManager()
        base_url = auth_manager.get_base_url(is_media=is_media)
        url = f"{base_url}{path}"
        
        token = auth_manager.get_user_token() if use_user_token else auth_manager.get_app_token()
        
        req_headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json"
        }
        if json_data is not None:
            req_headers["Content-Type"] = "application/json"
        if headers:
            req_headers.update(headers)
            
        response = requests.request(method, url, headers=req_headers, params=params, json=json_data, files=files)
        
        # If 401, maybe token expired, try to clear cache and retry once
        if response.status_code == 401:
            if use_user_token:
                auth_manager.user_token = None
                token = auth_manager.get_user_token()
            else:
                auth_manager.app_token = None
                token = auth_manager.get_app_token()
            req_headers["Authorization"] = f"Bearer {token}"
            response = requests.request(method, url, headers=req_headers, params=params, json=json_data, files=files)
            
        if response.status_code in [200, 201, 202, 204]:
            if response.status_code == 204 or not response.text:
                return {"success": True}
            try:
                return response.json()
            except ValueError:
                return {"text": response.text}
        else:
            try:
                err_json = response.json()
                return {"error": f"HTTP {response.status_code}", "details": err_json}
            except ValueError:
                return {"error": f"HTTP {response.status_code}", "details": response.text}
    except Exception as e:
        return {"error": str(e)}

# --- Catalog API ---

@app.tool()
def get_product(product_id: str) -> dict:
    """
    Retrieve details of a specific product in the eBay catalog.
    
    Args:
        product_id: The unique identifier of the product.
    """
    return make_request("GET", f"/commerce/catalog/v1/product/{product_id}", use_user_token=False)

@app.tool()
def search_products(
    q: str = None,
    gtin: str = None,
    upc: str = None,
    mpn: str = None,
    isbn: str = None,
    limit: int = 10,
    offset: int = 0
) -> dict:
    """
    Search for products in the eBay catalog by query, GTIN, UPC, MPN, or ISBN.
    
    Args:
        q: The search query string.
        gtin: The Global Trade Item Number of the product.
        upc: The Universal Product Code of the product.
        mpn: The Manufacturer Part Number of the product.
        isbn: The International Standard Book Number of the product.
        limit: The number of results to return (default 10).
        offset: The number of results to skip (default 0).
    """
    params = {}
    if q: params["q"] = q
    if gtin: params["gtin"] = gtin
    if upc: params["upc"] = upc
    if mpn: params["mpn"] = mpn
    if isbn: params["isbn"] = isbn
    params["limit"] = limit
    params["offset"] = offset
    return make_request("GET", "/commerce/catalog/v1/product_summary", use_user_token=False, params=params)

# --- Taxonomy API ---

@app.tool()
def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieve the default category tree ID for a given marketplace.
    
    Args:
        marketplace_id: The eBay marketplace ID (default: EBAY_US).
    """
    params = {"marketplace_id": marketplace_id}
    return make_request("GET", "/commerce/taxonomy/v1/get_default_category_tree_id", use_user_token=False, params=params)

@app.tool()
def get_category_tree(category_tree_id: str) -> dict:
    """
    Retrieve the category tree structure for a given category tree ID.
    
    Args:
        category_tree_id: The unique identifier of the category tree.
    """
    return make_request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}", use_user_token=False)

@app.tool()
def get_category_suggestions(category_tree_id: str, q: str) -> dict:
    """
    Retrieve category suggestions for a given query string.
    
    Args:
        category_tree_id: The unique identifier of the category tree.
        q: The query string to get suggestions for.
    """
    params = {"q": q}
    return make_request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions", use_user_token=False, params=params)

@app.tool()
def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve item aspects (attributes) for a given category.
    
    Args:
        category_tree_id: The unique identifier of the category tree.
        category_id: The unique identifier of the category.
    """
    params = {"category_id": category_id}
    return make_request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category", use_user_token=False, params=params)

# --- Identity API ---

@app.tool()
def get_user_profile() -> dict:
    """
    Retrieve the profile and identity information of the authenticated user.
    """
    return make_request("GET", "/commerce/identity/v1/user", use_user_token=True)

# --- Media API ---

@app.tool()
def create_video(title: str, description: str = None, classification: str = "PRODUCT_VIDEO") -> dict:
    """
    Initiate a video upload by creating a video resource.
    
    Args:
        title: The title of the video.
        description: A description of the video.
        classification: The classification of the video (default: PRODUCT_VIDEO).
    """
    json_data = {
        "title": title,
        "classification": classification
    }
    if description:
        json_data["description"] = description
    return make_request("POST", "/commerce/media/v1/video", is_media=True, use_user_token=True, json_data=json_data)

@app.tool()
def get_video(video_id: str) -> dict:
    """
    Retrieve details of a specific video resource.
    
    Args:
        video_id: The unique identifier of the video.
    """
    return make_request("GET", f"/commerce/media/v1/video/{video_id}", is_media=True, use_user_token=True)

@app.tool()
def upload_video_document(video_id: str, file_path: str) -> dict:
    """
    Upload the actual video file content for a created video resource.
    
    Args:
        video_id: The unique identifier of the video resource.
        file_path: The local path to the video file to upload.
    """
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}
        
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            return make_request("POST", f"/commerce/media/v1/video/{video_id}/upload_document", is_media=True, use_user_token=True, files=files)
    except Exception as e:
        return {"error": f"Failed to upload file: {str(e)}"}

# --- Notification API ---

@app.tool()
def list_subscriptions(limit: int = 10, offset: int = 0) -> dict:
    """
    List notification subscriptions.
    
    Args:
        limit: The number of results to return (default 10).
        offset: The number of results to skip (default 0).
    """
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/commerce/notification/v1/subscription", use_user_token=True, params=params)

@app.tool()
def get_subscription(subscription_id: str) -> dict:
    """
    Retrieve details of a specific notification subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription.
    """
    return make_request("GET", f"/commerce/notification/v1/subscription/{subscription_id}", use_user_token=True)

@app.tool()
def create_subscription(destination_id: str, payload_format: str, event_type: str) -> dict:
    """
    Create a new notification subscription.
    
    Args:
        destination_id: The unique identifier of the destination.
        payload_format: The payload format (e.g., JSON).
        event_type: The event type to subscribe to (e.g., MARKETPLACE_ACCOUNT_DELETION).
    """
    json_data = {
        "destinationId": destination_id,
        "payloadFormat": payload_format,
        "eventType": event_type
    }
    return make_request("POST", "/commerce/notification/v1/subscription", use_user_token=True, json_data=json_data)

@app.tool()
def update_subscription(subscription_id: str, destination_id: str = None, payload_format: str = None, status: str = None) -> dict:
    """
    Update an existing notification subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription.
        destination_id: The unique identifier of the destination.
        payload_format: The payload format.
        status: The status of the subscription (e.g., ENABLED, DISABLED).
    """
    json_data = {}
    if destination_id: json_data["destinationId"] = destination_id
    if payload_format: json_data["payloadFormat"] = payload_format
    if status: json_data["status"] = status
    return make_request("PUT", f"/commerce/notification/v1/subscription/{subscription_id}", use_user_token=True, json_data=json_data)

@app.tool()
def delete_subscription(subscription_id: str) -> dict:
    """
    Delete a notification subscription.
    
    Args:
        subscription_id: The unique identifier of the subscription.
    """
    return make_request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}", use_user_token=True)

@app.tool()
def list_destinations(limit: int = 10, offset: int = 0) -> dict:
    """
    List notification destinations.
    
    Args:
        limit: The number of results to return (default 10).
        offset: The number of results to skip (default 0).
    """
    params = {"limit": limit, "offset": offset}
    return make_request("GET", "/commerce/notification/v1/destination", use_user_token=True, params=params)

@app.tool()
def get_destination(destination_id: str) -> dict:
    """
    Retrieve details of a specific notification destination.
    
    Args:
        destination_id: The unique identifier of the destination.
    """
    return make_request("GET", f"/commerce/notification/v1/destination/{destination_id}", use_user_token=True)

@app.tool()
def create_destination(name: str, delivery_config: dict) -> dict:
    """
    Create a new notification destination.
    
    Args:
        name: The name of the destination.
        delivery_config: The delivery configuration dictionary (containing endpoint, verificationToken, etc.).
    """
    json_data = {
        "name": name,
        "deliveryConfig": delivery_config
    }
    return make_request("POST", "/commerce/notification/v1/destination", use_user_token=True, json_data=json_data)

@app.tool()
def update_destination(destination_id: str, name: str = None, delivery_config: dict = None) -> dict:
    """
    Update an existing notification destination.
    
    Args:
        destination_id: The unique identifier of the destination.
        name: The name of the destination.
        delivery_config: The delivery configuration dictionary.
    """
    json_data = {}
    if name: json_data["name"] = name
    if delivery_config: json_data["deliveryConfig"] = delivery_config
    return make_request("PUT", f"/commerce/notification/v1/destination/{destination_id}", use_user_token=True, json_data=json_data)

@app.tool()
def delete_destination(destination_id: str) -> dict:
    """
    Delete a notification destination.
    
    Args:
        destination_id: The unique identifier of the destination.
    """
    return make_request("DELETE", f"/commerce/notification/v1/destination/{destination_id}", use_user_token=True)

# --- Charity API ---

@app.tool()
def get_charity_org(charity_org_id: str) -> dict:
    """
    Retrieve details of a specific charity organization.
    
    Args:
        charity_org_id: The unique identifier of the charity organization.
    """
    return make_request("GET", f"/commerce/charity/v1/charity_org/{charity_org_id}", use_user_token=False)

@app.tool()
def search_charity_orgs(q: str = None, registration_id: str = None, limit: int = 10, offset: int = 0) -> dict:
    """
    Search for charity organizations.
    
    Args:
        q: The search query string.
        registration_id: The registration ID of the charity organization.
        limit: The number of results to return (default 10).
        offset: The number of results to skip (default 0).
    """
    params = {"limit": limit, "offset": offset}
    if q: params["q"] = q
    if registration_id: params["registration_id"] = registration_id
    return make_request("GET", "/commerce/charity/v1/charity_org", use_user_token=False, params=params)

# --- Translation API ---

@app.tool()
def translate_text(text: str, source_language: str, target_language: str, translation_context: str = "ITEM") -> dict:
    """
    Translate text from one language to another.
    
    Args:
        text: The text to translate.
        source_language: The language code of the source text (e.g., en).
        target_language: The language code of the target translation (e.g., es).
        translation_context: The context of the translation (default: ITEM).
    """
    json_data = {
        "translationContext": translation_context,
        "text": [text],
        "sourceLanguage": source_language,
        "targetLanguage": target_language
    }
    return make_request("POST", "/commerce/translation/v1/translate", use_user_token=False, json_data=json_data)

if __name__ == "__main__":
    app.run()
