import os
from typing import Optional, Dict, Any, List
from mcp.server.fastmcp import FastMCP

# Import our tool implementations
from generated_tools.browse import (
    search_items as _search_items,
    get_item as _get_item,
    get_item_by_legacy_id as _get_item_by_legacy_id,
    get_items_by_item_group as _get_items_by_item_group,
    check_compatibility as _check_compatibility
)
from generated_tools.deal import (
    get_deals as _get_deals,
    get_event as _get_event,
    get_events as _get_events
)
from generated_tools.feed import (
    get_feed_files as _get_feed_files
)
from generated_tools.order import (
    create_guest_checkout_session as _create_guest_checkout_session,
    get_guest_checkout_session as _get_guest_checkout_session,
    update_guest_quantity as _update_guest_quantity,
    associate_guest_shipping_address as _associate_guest_shipping_address,
    get_guest_shipping_methods as _get_guest_shipping_methods,
    update_guest_shipping_option as _update_guest_shipping_option,
    initiate_guest_payment as _initiate_guest_payment
)

# Initialize FastMCP server
mcp = FastMCP("eBay Buy API")

# ==========================================
# BROWSE API TOOLS
# ==========================================

@mcp.tool()
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
    return _search_items(
        q=q,
        gtin=gtin,
        charity_ids=charity_ids,
        category_ids=category_ids,
        filter=filter,
        sort=sort,
        limit=limit,
        offset=offset,
        aspect_filter=aspect_filter,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id
    )

@mcp.tool()
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
    return _get_item(
        item_id=item_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id
    )

@mcp.tool()
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
    return _get_item_by_legacy_id(
        legacy_item_id=legacy_item_id,
        legacy_variation_id=legacy_variation_id,
        fieldgroups=fieldgroups,
        marketplace_id=marketplace_id
    )

@mcp.tool()
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
    return _get_items_by_item_group(
        item_group_id=item_group_id,
        marketplace_id=marketplace_id
    )

@mcp.tool()
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
    return _check_compatibility(
        item_id=item_id,
        compatibility_properties=compatibility_properties,
        marketplace_id=marketplace_id
    )

# ==========================================
# DEAL API TOOLS
# ==========================================

@mcp.tool()
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
    return _get_deals(
        category_ids=category_ids,
        limit=limit,
        offset=offset,
        marketplace_id=marketplace_id
    )

@mcp.tool()
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
    return _get_event(
        event_id=event_id,
        marketplace_id=marketplace_id
    )

@mcp.tool()
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
    return _get_events(
        limit=limit,
        offset=offset,
        marketplace_id=marketplace_id
    )

# ==========================================
# FEED API TOOLS
# ==========================================

@mcp.tool()
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
    return _get_feed_files(
        feed_scope=feed_scope,
        category_id=category_id,
        date=date,
        marketplace_id=marketplace_id
    )

# ==========================================
# ORDER API TOOLS (GUEST CHECKOUT)
# ==========================================

@mcp.tool()
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
    return _create_guest_checkout_session(
        line_items=line_items,
        contact_email=contact_email,
        contact_first_name=contact_first_name,
        contact_last_name=contact_last_name,
        marketplace_id=marketplace_id
    )

@mcp.tool()
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
    return _get_guest_checkout_session(
        checkout_session_id=checkout_session_id,
        marketplace_id=marketplace_id
    )

@mcp.tool()
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
    return _update_guest_quantity(
        checkout_session_id=checkout_session_id,
        line_item_id=line_item_id,
        quantity=quantity,
        marketplace_id=marketplace_id
    )

@mcp.tool()
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
    return _associate_guest_shipping_address(
        checkout_session_id=checkout_session_id,
        shipping_address=shipping_address,
        marketplace_id=marketplace_id
    )

@mcp.tool()
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
    return _get_guest_shipping_methods(
        checkout_session_id=checkout_session_id,
        marketplace_id=marketplace_id
    )

@mcp.tool()
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
    return _update_guest_shipping_option(
        checkout_session_id=checkout_session_id,
        line_item_id=line_item_id,
        shipping_option_id=shipping_option_id,
        marketplace_id=marketplace_id
    )

@mcp.tool()
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
    return _initiate_guest_payment(
        checkout_session_id=checkout_session_id,
        payment_method=payment_method,
        marketplace_id=marketplace_id
    )

if __name__ == "__main__":
    # Run the FastMCP server over stdio
    mcp.run()
