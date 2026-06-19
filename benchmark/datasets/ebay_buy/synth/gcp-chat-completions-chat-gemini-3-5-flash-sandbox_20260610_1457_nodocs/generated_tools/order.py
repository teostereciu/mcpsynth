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
    Helper function to make requests to the eBay Order API.
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

def create_guest_checkout_session(
    line_items: List[Dict[str, Any]],
    contact_email: Optional[str] = None,
    contact_first_name: Optional[str] = None,
    contact_last_name: Optional[str] = None,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Create a guest checkout session to initiate a purchase.
    
    Args:
        line_items: A list of items to purchase. Each item is a dict with:
            - "itemId": The RESTful item ID (e.g., "v1|123456789012|0")
            - "quantity": The quantity to purchase (integer)
        contact_email: The guest's email address.
        contact_first_name: The guest's first name.
        contact_last_name: The guest's last name.
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    json_data = {
        "lineItems": line_items
    }
    if contact_email is not None: json_data["contactEmail"] = contact_email
    if contact_first_name is not None: json_data["contactFirstName"] = contact_first_name
    if contact_last_name is not None: json_data["contactLastName"] = contact_last_name
    
    return _make_request(
        method="POST",
        path="/buy/order/v1/guest_checkout_session",
        json_data=json_data,
        marketplace_id=marketplace_id
    )

def get_guest_checkout_session(
    checkout_session_id: str,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Retrieve details of an existing guest checkout session.
    
    Args:
        checkout_session_id: The ID of the guest checkout session.
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    return _make_request(
        method="GET",
        path=f"/buy/order/v1/guest_checkout_session/{checkout_session_id}",
        marketplace_id=marketplace_id
    )

def update_guest_quantity(
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Update the quantity of a line item in a guest checkout session.
    
    Args:
        checkout_session_id: The ID of the guest checkout session.
        line_item_id: The ID of the line item in the session.
        quantity: The new quantity.
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    json_data = {
        "lineItemId": line_item_id,
        "quantity": quantity
    }
    return _make_request(
        method="PUT",
        path=f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_quantity",
        json_data=json_data,
        marketplace_id=marketplace_id
    )

def associate_guest_shipping_address(
    checkout_session_id: str,
    shipping_address: Dict[str, Any],
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Associate a shipping address with a guest checkout session.
    
    Args:
        checkout_session_id: The ID of the guest checkout session.
        shipping_address: A dictionary containing shipping address details:
            - "addressLine1": Street address (string)
            - "addressLine2": Suite, unit, etc. (optional, string)
            - "city": City (string)
            - "stateOrProvince": State or province (string)
            - "postalCode": Postal code (string)
            - "country": Two-letter country code (e.g., "US")
            - "recipient": Recipient's full name (string)
            - "phoneNumber": Phone number (string)
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    json_data = {
        "shippingAddress": shipping_address
    }
    return _make_request(
        method="POST",
        path=f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/associate_shipping_address",
        json_data=json_data,
        marketplace_id=marketplace_id
    )

def get_guest_shipping_methods(
    checkout_session_id: str,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Retrieve available shipping methods for a guest checkout session.
    
    Args:
        checkout_session_id: The ID of the guest checkout session.
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    return _make_request(
        method="GET",
        path=f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/shipping_method",
        marketplace_id=marketplace_id
    )

def update_guest_shipping_option(
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str,
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Update the shipping option for a line item in a guest checkout session.
    
    Args:
        checkout_session_id: The ID of the guest checkout session.
        line_item_id: The ID of the line item.
        shipping_option_id: The ID of the selected shipping option.
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    json_data = {
        "lineItemId": line_item_id,
        "shippingOptionId": shipping_option_id
    }
    return _make_request(
        method="POST",
        path=f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/update_shipping_option",
        json_data=json_data,
        marketplace_id=marketplace_id
    )

def initiate_guest_payment(
    checkout_session_id: str,
    payment_method: Dict[str, Any],
    marketplace_id: str = "EBAY_US"
) -> Dict[str, Any]:
    """
    Initiate payment for a guest checkout session.
    
    Args:
        checkout_session_id: The ID of the guest checkout session.
        payment_method: A dictionary containing payment details (e.g., credit card details).
        marketplace_id: eBay Marketplace ID (default: "EBAY_US").
    """
    json_data = {
        "paymentMethod": payment_method
    }
    return _make_request(
        method="POST",
        path=f"/buy/order/v1/guest_checkout_session/{checkout_session_id}/initiate_payment",
        json_data=json_data,
        marketplace_id=marketplace_id
    )
