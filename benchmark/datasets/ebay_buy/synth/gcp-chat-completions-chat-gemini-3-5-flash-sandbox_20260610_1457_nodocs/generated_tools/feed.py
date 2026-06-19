import requests
from typing import Optional, Dict, Any
from .auth import auth_manager

def _make_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Helper function to make requests to the eBay Feed API.
    """
    url = f"{auth_manager.base_url}{path}"
    try:
        headers = auth_manager.get_headers()
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            timeout=20
        )
        
        if response.status_code in (200, 201):
            try:
                return response.json()
            except ValueError:
                return {"status": "success", "status_code": response.status_code}
                
        try:
            error_detail = response.json()
        except ValueError:
            error_detail = response.text
            
        return {
            "error": f"HTTP {response.status_code} Error",
            "details": error_detail
        }
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}

def get_feed_files(
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Retrieve details of available feed files for bulk item downloads.
    
    Args:
        feed_scope: The scope of the feed (e.g., "ALL_ACTIVE", "NEWLY_LISTED").
        category_id: The eBay category ID.
        date: The date of the feed file (format: YYYYMMDD, e.g., "20231024").
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    params = {
        "feed_scope": feed_scope,
        "category_id": category_id
    }
    if date is not None:
        params["date"] = date
        
    return _make_request(
        method="GET",
        path="/buy/feed/v1/feed_file",
        params=params,
        marketplace_id=marketplace_id
    )
