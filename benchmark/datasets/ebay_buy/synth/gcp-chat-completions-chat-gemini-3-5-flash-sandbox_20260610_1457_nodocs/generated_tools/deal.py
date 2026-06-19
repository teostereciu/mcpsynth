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
    Helper function to make requests to the eBay Deal API.
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

def get_deals(
    category_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Retrieve details of eBay deals (discounts, sales, promotions).
    
    Args:
        category_ids: A comma-separated list of eBay category IDs.
        limit: Number of deals to return.
        offset: Number of deals to skip (for pagination).
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    params = {}
    if category_ids is not None: params["category_ids"] = category_ids
    if limit is not None: params["limit"] = limit
    if offset is not None: params["offset"] = offset
    
    return _make_request(
        method="GET",
        path="/buy/deal/v1/deal",
        params=params,
        marketplace_id=marketplace_id
    )

def get_event(
    event_id: str,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Retrieve details of a specific eBay event (e.g., Black Friday, Cyber Monday).
    
    Args:
        event_id: The event ID.
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    return _make_request(
        method="GET",
        path=f"/buy/deal/v1/event/{event_id}",
        marketplace_id=marketplace_id
    )

def get_events(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Retrieve details of active eBay events.
    
    Args:
        limit: Number of events to return.
        offset: Number of events to skip (for pagination).
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    params = {}
    if limit is not None: params["limit"] = limit
    if offset is not None: params["offset"] = offset
    
    return _make_request(
        method="GET",
        path="/buy/deal/v1/event",
        params=params,
        marketplace_id=marketplace_id
    )
