import requests
from typing import Optional, Dict, Any, List
from .auth import auth_manager

def _make_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    json_data: Optional[Dict[str, Any]] = None,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Helper function to make requests to the eBay Browse API.
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
            json=json_data,
            timeout=20
        )
        
        # If response is successful, return JSON
        if response.status_code in (200, 201):
            try:
                return response.json()
            except ValueError:
                return {"status": "success", "status_code": response.status_code}
                
        # Handle error responses gracefully
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

def search_items(
    q: Optional[str] = None,
    gtin: Optional[str] = None,
    charity_ids: Optional[str] = None,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Search for eBay items by keyword, category, GTIN, or other filters.
    
    Args:
        q: The search query keywords (e.g., "iphone 13").
        gtin: The GTIN (UPC, EAN, or ISBN) of the product.
        charity_ids: A comma-separated list of charity IDs.
        category_ids: A comma-separated list of eBay category IDs.
        filter: Filter criteria (e.g., "price:[10..50],conditions:{NEW}").
        sort: Sort order (e.g., "price", "-price", "distance").
        limit: Number of items to return (max 200).
        offset: Number of items to skip (for pagination).
        aspect_filter: Aspect filters (e.g., "categoryId:123,Brand:{Apple}").
        fieldgroups: Field groups to return (e.g., "MATCHING_ITEMS", "ASPECT_REFINEMENTS").
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    params = {}
    if q is not None: params["q"] = q
    if gtin is not None: params["gtin"] = gtin
    if charity_ids is not None: params["charity_ids"] = charity_ids
    if category_ids is not None: params["category_ids"] = category_ids
    if filter is not None: params["filter"] = filter
    if sort is not None: params["sort"] = sort
    if limit is not None: params["limit"] = limit
    if offset is not None: params["offset"] = offset
    if aspect_filter is not None: params["aspect_filter"] = aspect_filter
    if fieldgroups is not None: params["fieldgroups"] = fieldgroups

    return _make_request(
        method="GET",
        path="/buy/browse/v1/item_summary/search",
        params=params,
        marketplace_id=marketplace_id
    )

def get_item(
    item_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Retrieve details of a specific eBay item by its RESTful item ID.
    
    Args:
        item_id: The RESTful item ID (e.g., "v1|123456789012|0").
        fieldgroups: Field groups to return (e.g., "PRODUCT").
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    params = {}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
        
    return _make_request(
        method="GET",
        path=f"/buy/browse/v1/item/{item_id}",
        params=params,
        marketplace_id=marketplace_id
    )

def get_item_by_legacy_id(
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Retrieve details of an eBay item using its legacy item ID.
    
    Args:
        legacy_item_id: The legacy eBay item ID (e.g., "123456789012").
        legacy_variation_id: The legacy variation ID (optional).
        fieldgroups: Field groups to return.
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    params = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id is not None:
        params["legacy_variation_id"] = legacy_variation_id
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
        
    return _make_request(
        method="GET",
        path="/buy/browse/v1/item/get_item_by_legacy_id",
        params=params,
        marketplace_id=marketplace_id
    )

def get_items_by_item_group(
    item_group_id: str,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Retrieve details of all items belonging to a specific item group (e.g., multi-variation listing).
    
    Args:
        item_group_id: The item group ID.
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    return _make_request(
        method="GET",
        path=f"/buy/browse/v1/item_group/{item_group_id}",
        marketplace_id=marketplace_id
    )

def check_compatibility(
    item_id: str,
    compatibility_properties: List[Dict[str, str]],
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Check if a compatible item (like a car part) fits a specific vehicle or product.
    
    Args:
        item_id: The RESTful item ID.
        compatibility_properties: A list of property name-value pairs.
            Example: [{"name": "Year", "value": "2018"}, {"name": "Make", "value": "Toyota"}, {"name": "Model", "value": "Camry"}]
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    json_data = {
        "compatibilityProperties": compatibility_properties
    }
    return _make_request(
        method="POST",
        path=f"/buy/browse/v1/item/{item_id}/check_compatibility",
        json_data=json_data,
        marketplace_id=marketplace_id
    )
