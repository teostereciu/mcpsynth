"""MCP Server for Shopify Admin REST API"""
import os
import requests
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("shopify-admin")

# Base URL for Shopify Admin API
BASE_URL = "https://{store_url}/admin/api/2026-01"

def get_headers():
    """Get authentication headers for Shopify API"""
    access_token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    store_url = os.environ.get("SHOPIFY_STORE_URL")
    return {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }

def get_base_url():
    """Get the base URL for the Shopify store"""
    store_url = os.environ.get("SHOPIFY_STORE_URL")
    if not store_url:
        return None
    return f"https://{store_url}/admin/api/2026-01"

def make_request(method, endpoint, params=None, data=None):
    """Make a request to the Shopify Admin API"""
    base_url = get_base_url()
    if not base_url:
        return {"error": "SHOPIFY_STORE_URL environment variable not set"}
    
    url = f"{base_url}{endpoint}"
    headers = get_headers()
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {"error": f"Resource not found: {endpoint}"}
        elif e.response.status_code == 401:
            return {"error": "Authentication failed. Check SHOPIFY_ACCESS_TOKEN"}
        elif e.response.status_code == 429:
            return {"error": "Rate limit exceeded"}
        else:
            return {"error": f"API error: {e.response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# ====================
# Product Endpoints
# ====================

@mcp.tool()
def get_products(limit=None, ids=None, since_id=None):
    """
    Retrieve a list of products.
    
    Args:
        limit: Number of products to return (default: 50, max: 250)
        ids: Comma-separated list of product IDs
        since_id: Return products with ID greater than this value
        
    Returns:
        List of products
    """
    params = {}
    if limit:
        params["limit"] = limit
    if ids:
        params["ids"] = ids
    if since_id:
        params["since_id"] = since_id
    
    return make_request("GET", "/products.json", params=params)

@mcp.tool()
def get_product(product_id):
    """
    Retrieve a single product by ID.
    
    Args:
        product_id: The ID of the product to retrieve
        
    Returns:
        Product details
    """
    return make_request("GET", f"/products/{product_id}.json")

@mcp.tool()
def create_product(title, body_html=None, vendor=None, product_type=None, 
                   status="draft", tags=None, handle=None, published=None):
    """
    Create a new product.
    
    Args:
        title: The name of the product (required)
        body_html: HTML description of the product
        vendor: Name of the product's vendor
        product_type: Category for the product
        status: Product status (active, draft, archived)
        tags: Comma-separated tags for filtering
        handle: Unique human-friendly string for the product
        published: Whether to publish the product (True/False/None)
        
    Returns:
        Created product details
    """
    product = {"title": title}
    if body_html:
        product["body_html"] = body_html
    if vendor:
        product["vendor"] = vendor
    if product_type:
        product["product_type"] = product_type
    if status:
        product["status"] = status
    if tags:
        product["tags"] = tags
    if handle:
        product["handle"] = handle
    if published is not None:
        product["published"] = published
    
    return make_request("POST", "/products.json", data={"product": product})

@mcp.tool()
def update_product(product_id, title=None, body_html=None, vendor=None, 
                   product_type=None, status=None, tags=None, handle=None):
    """
    Update an existing product.
    
    Args:
        product_id: The ID of the product to update (required)
        title: Updated product name
        body_html: Updated HTML description
        vendor: Updated vendor name
        product_type: Updated product category
        status: Updated status (active, draft, archived)
        tags: Updated comma-separated tags
        handle: Updated unique string identifier
        
    Returns:
        Updated product details
    """
    product = {}
    if title:
        product["title"] = title
    if body_html:
        product["body_html"] = body_html
    if vendor:
        product["vendor"] = vendor
    if product_type:
        product["product_type"] = product_type
    if status:
        product["status"] = status
    if tags:
        product["tags"] = tags
    if handle:
        product["handle"] = handle
    
    return make_request("PUT", f"/products/{product_id}.json", data={"product": product})

@mcp.tool()
def delete_product(product_id):
    """
    Delete a product.
    
    Args:
        product_id: The ID of the product to delete
        
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/products/{product_id}.json")

@mcp.tool()
def get_product_count():
    """
    Retrieve a count of all products.
    
    Returns:
        Count of products
    """
    return make_request("GET", "/products/count.json")

# ====================
# Product Variant Endpoints
# ====================

@mcp.tool()
def get_product_variants(product_id, limit=None):
    """
    Retrieve a list of variants for a product.
    
    Args:
        product_id: The ID of the product
        limit: Number of variants to return (default: 50, max: 250)
        
    Returns:
        List of product variants
    """
    params = {}
    if limit:
        params["limit"] = limit
    
    return make_request("GET", f"/products/{product_id}/variants.json", params=params)

@mcp.tool()
def get_variant(variant_id):
    """
    Retrieve a single product variant by ID.
    
    Args:
        variant_id: The ID of the variant to retrieve
        
    Returns:
        Variant details
    """
    return make_request("GET", f"/variants/{variant_id}.json")

@mcp.tool()
def create_variant(product_id, price, option1=None, option2=None, option3=None,
                   sku=None, barcode=None, weight=None, weight_unit="lb",
                   inventory_management=None, inventory_policy="deny",
                   inventory_quantity=0):
    """
    Create a new product variant.
    
    Args:
        product_id: The ID of the product (required)
        price: The price of the variant (required)
        option1: First option value (e.g., "Small")
        option2: Second option value
        option3: Third option value
        sku: Stock keeping unit
        barcode: Barcode, UPC, or ISBN
        weight: Weight of the variant
        weight_unit: Unit of weight ("lb" or "kg")
        inventory_management: Whether Shopify tracks inventory ("shopify" or null)
        inventory_policy: Whether customers can order when out of stock
        inventory_quantity: Initial inventory quantity
        
    Returns:
        Created variant details
    """
    variant = {
        "price": price,
        "inventory_management": inventory_management,
        "inventory_policy": inventory_policy
    }
    if option1:
        variant["option1"] = option1
    if option2:
        variant["option2"] = option2
    if option3:
        variant["option3"] = option3
    if sku:
        variant["sku"] = sku
    if barcode:
        variant["barcode"] = barcode
    if weight is not None:
        variant["weight"] = weight
    variant["weight_unit"] = weight_unit
    
    return make_request("POST", f"/products/{product_id}/variants.json", data={"variant": variant})

@mcp.tool()
def update_variant(variant_id, price=None, option1=None, option2=None, option3=None,
                   sku=None, barcode=None, weight=None, weight_unit=None,
                   inventory_management=None, inventory_policy=None, inventory_quantity=None):
    """
    Update an existing product variant.
    
    Args:
        variant_id: The ID of the variant to update (required)
        price: Updated price
        option1: Updated first option value
        option2: Updated second option value
        option3: Updated third option value
        sku: Updated SKU
        barcode: Updated barcode
        weight: Updated weight
        weight_unit: Updated weight unit
        inventory_management: Updated inventory management setting
        inventory_policy: Updated inventory policy
        inventory_quantity: Updated inventory quantity (deprecated, use inventory_levels endpoint)
        
    Returns:
        Updated variant details
    """
    variant = {}
    if price is not None:
        variant["price"] = price
    if option1 is not None:
        variant["option1"] = option1
    if option2 is not None:
        variant["option2"] = option2
    if option3 is not None:
        variant["option3"] = option3
    if sku is not None:
        variant["sku"] = sku
    if barcode is not None:
        variant["barcode"] = barcode
    if weight is not None:
        variant["weight"] = weight
    if weight_unit:
        variant["weight_unit"] = weight_unit
    if inventory_management is not None:
        variant["inventory_management"] = inventory_management
    if inventory_policy is not None:
        variant["inventory_policy"] = inventory_policy
    if inventory_quantity is not None:
        variant["inventory_quantity"] = inventory_quantity
    
    return make_request("PUT", f"/variants/{variant_id}.json", data={"variant": variant})

@mcp.tool()
def delete_variant(product_id, variant_id):
    """
    Delete a product variant.
    
    Args:
        product_id: The ID of the product
        variant_id: The ID of the variant to delete
        
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")

# ====================
# Product Image Endpoints
# ====================

@mcp.tool()
def get_product_images(product_id, limit=None):
    """
    Retrieve a list of images for a product.
    
    Args:
        product_id: The ID of the product
        limit: Number of images to return (default: 50, max: 250)
        
    Returns:
        List of product images
    """
    params = {}
    if limit:
        params["limit"] = limit
    
    return make_request("GET", f"/products/{product_id}/images.json", params=params)

@mcp.tool()
def get_product_image(product_id, image_id):
    """
    Retrieve a single product image by ID.
    
    Args:
        product_id: The ID of the product
        image_id: The ID of the image
        
    Returns:
        Image details
    """
    return make_request("GET", f"/products/{product_id}/images/{image_id}.json")

@mcp.tool()
def create_product_image(product_id, src=None, attachment=None, position=1, alt=None):
    """
    Create a new product image.
    
    Args:
        product_id: The ID of the product (required)
        src: URL of the image to download
        attachment: Base64 encoded image data (use instead of src for direct upload)
        position: Position in the image list (default: 1)
        alt: Alternative text for the image
        
    Returns:
        Created image details
    """
    image = {"position": position}
    if src:
        image["src"] = src
    if attachment:
        image["attachment"] = attachment
    if alt:
        image["alt"] = alt
    
    return make_request("POST", f"/products/{product_id}/images.json", data={"image": image})

@mcp.tool()
def update_product_image(product_id, image_id, src=None, position=None, alt=None):
    """
    Update an existing product image.
    
    Args:
        product_id: The ID of the product
        image_id: The ID of the image
        src: Updated image URL
        position: Updated position in list
        alt: Updated alternative text
        
    Returns:
        Updated image details
    """
    image = {}
    if src:
        image["src"] = src
    if position is not None:
        image["position"] = position
    if alt:
        image["alt"] = alt
    
    return make_request("PUT", f"/products/{product_id}/images/{image_id}.json", 
                       data={"image": image})

@mcp.tool()
def delete_product_image(product_id, image_id):
    """
    Delete a product image.
    
    Args:
        product_id: The ID of the product
        image_id: The ID of the image to delete
        
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/products/{product_id}/images/{image_id}.json")

# ====================
# Product Collection Endpoints
# ====================

@mcp.tool()
def get_custom_collections(limit=None, since_id=None):
    """
    Retrieve a list of custom collections.
    
    Args:
        limit: Number of collections to return (default: 50, max: 250)
        since_id: Return collections with ID greater than this value
        
    Returns:
        List of custom collections
    """
    params = {}
    if limit:
        params["limit"] = limit
    if since_id:
        params["since_id"] = since_id
    
    return make_request("GET", "/custom_collections.json", params=params)

@mcp.tool()
def get_custom_collection(collection_id):
    """
    Retrieve a single custom collection by ID.
    
    Args:
        collection_id: The ID of the collection to retrieve
        
    Returns:
        Collection details
    """
    return make_request("GET", f"/custom_collections/{collection_id}.json")

@mcp.tool()
def create_custom_collection(title, body_html=None, handle=None, image=None, 
                             published=None, sort_order="manual"):
    """
    Create a new custom collection.
    
    Args:
        title: The name of the collection (required)
        body_html: HTML description of the collection
        handle: Unique human-friendly string for the collection
        image: Image URL for the collection
        published: Whether to publish the collection
        sort_order: How products are sorted ("manual", "best-selling", etc.)
        
    Returns:
        Created collection details
    """
    collection = {"title": title, "sort_order": sort_order}
    if body_html:
        collection["body_html"] = body_html
    if handle:
        collection["handle"] = handle
    if image:
        collection["image"] = image
    if published is not None:
        collection["published"] = published
    
    return make_request("POST", "/custom_collections.json", data={"collection": collection})

@mcp.tool()
def update_custom_collection(collection_id, title=None, body_html=None, handle=None,
                             image=None, published=None, sort_order=None):
    """
    Update an existing custom collection.
    
    Args:
        collection_id: The ID of the collection to update (required)
        title: Updated collection name
        body_html: Updated HTML description
        handle: Updated handle
        image: Updated image URL
        published: Updated published status
        sort_order: Updated sort order
        
    Returns:
        Updated collection details
    """
    collection = {}
    if title:
        collection["title"] = title
    if body_html:
        collection["body_html"] = body_html
    if handle:
        collection["handle"] = handle
    if image:
        collection["image"] = image
    if published is not None:
        collection["published"] = published
    if sort_order:
        collection["sort_order"] = sort_order
    
    return make_request("PUT", f"/custom_collections/{collection_id}.json", 
                       data={"collection": collection})

@mcp.tool()
def delete_custom_collection(collection_id):
    """
    Delete a custom collection.
    
    Args:
        collection_id: The ID of the collection to delete
        
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/custom_collections/{collection_id}.json")

@mcp.tool()
def add_product_to_collection(collection_id, product_id):
    """
    Add a product to a custom collection.
    
    Args:
        collection_id: The ID of the collection
        product_id: The ID of the product to add
        
    Returns:
        Create collect response
    """
    return make_request("POST", "/collects.json", data={"collect": {
        "collection_id": collection_id,
        "product_id": product_id
    }})

@mcp.tool()
def remove_product_from_collection(collect_id):
    """
    Remove a product from a custom collection.
    
    Args:
        collect_id: The ID of the collect relationship
        
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/collects/{collect_id}.json")

# ====================
# Smart Collection Endpoints
# ====================

@mcp.tool()
def get_smart_collections(limit=None, since_id=None):
    """
    Retrieve a list of smart collections.
    
    Args:
        limit: Number of collections to return (default: 50, max: 250)
        since_id: Return collections with ID greater than this value
        
    Returns:
        List of smart collections
    """
    params = {}
    if limit:
        params["limit"] = limit
    if since_id:
        params["since_id"] = since_id
    
    return make_request("GET", "/smart_collections.json", params=params)

@mcp.tool()
def get_smart_collection(collection_id):
    """
    Retrieve a single smart collection by ID.
    
    Args:
        collection_id: The ID of the collection to retrieve
        
    Returns:
        Collection details
    """
    return make_request("GET", f"/smart_collections/{collection_id}.json")

@mcp.tool()
def update_smart_collection_rules(collection_id, rules):
    """
    Update the rules for a smart collection.
    
    Args:
        collection_id: The ID of the smart collection (required)
        rules: List of rule objects with condition, relation, and value
        
    Returns:
        Updated collection details
    """
    return make_request("PUT", f"/smart_collections/{collection_id}.json", 
                       data={"collection": {"rules": rules}})

# ====================
# Order Endpoints
# ====================

@mcp.tool()
def get_orders(limit=None, status="open", since_id=None, created_at_min=None, 
               created_at_max=None, updated_at_min=None, updated_at_max=None):
    """
    Retrieve a list of orders.
    
    Args:
        limit: Number of orders to return (default: 50, max: 250)
        status: Filter by status (open, closed, cancelled, any)
        since_id: Return orders with ID greater than this value
        created_at_min: Filter orders created after this datetime (ISO 8601)
        created_at_max: Filter orders created before this datetime (ISO 8601)
        updated_at_min: Filter orders updated after this datetime (ISO 8601)
        updated_at_max: Filter orders updated before this datetime (ISO 8601)
        
    Returns:
        List of orders
    """
    params = {"status": status}
    if limit:
        params["limit"] = limit
    if since_id:
        params["since_id"] = since_id
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if updated_at_min:
        params["updated_at_min"] = updated_at_min
    if updated_at_max:
        params["updated_at_max"] = updated_at_max
    
    return make_request("GET", "/orders.json", params=params)

@mcp.tool()
def get_order(order_id):
    """
    Retrieve a single order by ID.
    
    Args:
        order_id: The ID of the order to retrieve
        
    Returns:
        Order details
    """
    return make_request("GET", f"/orders/{order_id}.json")

@mcp.tool()
def create_order(customer, line_items, shipping_address=None, billing_address=None,
                 email=None, currency="USD", payment_gateway=None, fulfillments=None):
    """
    Create a new order.
    
    Args:
        customer: Customer information object
        line_items: List of line items with product_id, variant_id, quantity, price
        shipping_address: Shipping address object
        billing_address: Billing address object
        email: Customer email
        currency: Currency code (default: "USD")
        payment_gateway: Payment gateway name
        fulfillments: List of fulfillment objects
        
    Returns:
        Created order details
    """
    order = {
        "line_items": line_items,
        "currency": currency
    }
    if customer:
        order["customer"] = customer
    if shipping_address:
        order["shipping_address"] = shipping_address
    if billing_address:
        order["billing_address"] = billing_address
    if email:
        order["email"] = email
    if payment_gateway:
        order["payment_gateway"] = payment_gateway
    if fulfillments:
        order["fulfillments"] = fulfillments
    
    return make_request("POST", "/orders.json", data={"order": order})

@mcp.tool()
def update_order(order_id, **kwargs):
    """
    Update an existing order.
    
    Args:
        order_id: The ID of the order to update (required)
        **kwargs: Fields to update (email, shipping_address, line_items, etc.)
        
    Returns:
        Updated order details
    """
    order = kwargs
    return make_request("PUT", f"/orders/{order_id}.json", data={"order": order})

@mcp.tool()
def cancel_order(order_id, reason=None):
    """
    Cancel an order.
    
    Args:
        order_id: The ID of the order to cancel (required)
        reason: Reason for cancellation (e.g., "customer", "fraud", "inventory")
        
    Returns:
        Cancelled order details
    """
    data = {}
    if reason:
        data["reason"] = reason
    
    return make_request("POST", f"/orders/{order_id}/cancel.json", data=data)

@mcp.tool()
def close_order(order_id):
    """
    Close an order.
    
    Args:
        order_id: The ID of the order to close (required)
        
    Returns:
        Closed order details
    """
    return make_request("POST", f"/orders/{order_id}/close.json")

@mcp.tool()
def open_order(order_id):
    """
    Reopen a closed order.
    
    Args:
        order_id: The ID of the order to reopen (required)
        
    Returns:
        Reopened order details
    """
    return make_request("POST", f"/orders/{order_id}/open.json")

# ====================
# Customer Endpoints
# ====================

@mcp.tool()
def get_customers(limit=None, since_id=None, email=None, field=None):
    """
    Retrieve a list of customers.
    
    Args:
        limit: Number of customers to return (default: 50, max: 250)
        since_id: Return customers with ID greater than this value
        email: Filter by email address
        field: Filter by custom field
        
    Returns:
        List of customers
    """
    params = {}
    if limit:
        params["limit"] = limit
    if since_id:
        params["since_id"] = since_id
    if email:
        params["email"] = email
    if field:
        params["field"] = field
    
    return make_request("GET", "/customers.json", params=params)

@mcp.tool()
def get_customer(customer_id):
    """
    Retrieve a single customer by ID.
    
    Args:
        customer_id: The ID of the customer to retrieve
        
    Returns:
        Customer details
    """
    return make_request("GET", f"/customers/{customer_id}.json")

@mcp.tool()
def create_customer(first_name=None, last_name=None, email=None, phone=None,
                    password=None, password_confirmation=None, verified_email=True,
                    groups="default", send_email_welcome=False):
    """
    Create a new customer.
    
    Args:
        first_name: Customer's first name
        last_name: Customer's last name
        email: Customer's email address (required for account creation)
        phone: Customer's phone number
        password: Password for customer account
        password_confirmation: Confirm password
        verified_email: Whether email is verified
        groups: Customer group(s)
        send_email_welcome: Whether to send welcome email
        
    Returns:
        Created customer details
    """
    customer = {}
    if first_name:
        customer["first_name"] = first_name
    if last_name:
        customer["last_name"] = last_name
    if email:
        customer["email"] = email
    if phone:
        customer["phone"] = phone
    if password:
        customer["password"] = password
    if password_confirmation:
        customer["password_confirmation"] = password_confirmation
    customer["verified_email"] = verified_email
    customer["tags"] = groups
    if send_email_welcome:
        customer["send_email_welcome"] = send_email_welcome
    
    return make_request("POST", "/customers.json", data={"customer": customer})

@mcp.tool()
def update_customer(customer_id, **kwargs):
    """
    Update an existing customer.
    
    Args:
        customer_id: The ID of the customer to update (required)
        **kwargs: Fields to update (first_name, last_name, email, phone, etc.)
        
    Returns:
        Updated customer details
    """
    customer = kwargs
    return make_request("PUT", f"/customers/{customer_id}.json", data={"customer": customer})

@mcp.tool()
def delete_customer(customer_id):
    """
    Delete a customer.
    
    Args:
        customer_id: The ID of the customer to delete
        
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/customers/{customer_id}.json")

@mcp.tool()
def get_customer_account_activation_url(customer_id):
    """
    Generate an account activation URL for a customer.
    
    Args:
        customer_id: The ID of the customer
        
    Returns:
        Account activation URL
    """
    return make_request("POST", f"/customers/{customer_id}/account_activation_url.json")

@mcp.tool()
def send_customer_invite(customer_id):
    """
    Send an account invite to a customer.
    
    Args:
        customer_id: The ID of the customer
        
    Returns:
        Invite confirmation
    """
    return make_request("POST", f"/customers/{customer_id}/send_invite.json")

# ====================
# Customer Address Endpoints
# ====================

@mcp.tool()
def get_customer_addresses(customer_id, limit=None):
    """
    Retrieve a list of addresses for a customer.
    
    Args:
        customer_id: The ID of the customer
        limit: Number of addresses to return (default: 50, max: 250)
        
    Returns:
        List of customer addresses
    """
    params = {}
    if limit:
        params["limit"] = limit
    
    return make_request("GET", f"/customers/{customer_id}/addresses.json", params=params)

@mcp.tool()
def get_customer_address(customer_id, address_id):
    """
    Retrieve a single customer address by ID.
    
    Args:
        customer_id: The ID of the customer
        address_id: The ID of the address
        
    Returns:
        Address details
    """
    return make_request("GET", f"/customers/{customer_id}/addresses/{address_id}.json")

@mcp.tool()
def create_customer_address(customer_id, address1, city, province, country, 
                            zip_code, first_name=None, last_name=None, phone=None,
                            company=None, default=False):
    """
    Create a new customer address.
    
    Args:
        customer_id: The ID of the customer (required)
        address1: First line of the address (required)
        city: City name (required)
        province: Province/state name (required)
        country: Country name (required)
        zip_code: ZIP/postal code (required)
        first_name: First name for the address
        last_name: Last name for the address
        phone: Phone number
        company: Company name
        default: Whether this is the default address
        
    Returns:
        Created address details
    """
    address = {
        "address1": address1,
        "city": city,
        "province": province,
        "country": country,
        "zip": zip_code
    }
    if first_name:
        address["first_name"] = first_name
    if last_name:
        address["last_name"] = last_name
    if phone:
        address["phone"] = phone
    if company:
        address["company"] = company
    address["default"] = default
    
    return make_request("POST", f"/customers/{customer_id}/addresses.json", 
                       data={"address": address})

@mcp.tool()
def update_customer_address(customer_id, address_id, **kwargs):
    """
    Update an existing customer address.
    
    Args:
        customer_id: The ID of the customer
        address_id: The ID of the address to update (required)
        **kwargs: Fields to update (address1, city, province, country, zip, etc.)
        
    Returns:
        Updated address details
    """
    address = kwargs
    return make_request("PUT", f"/customers/{customer_id}/addresses/{address_id}.json", 
                       data={"address": address})

@mcp.tool()
def delete_customer_address(customer_id, address_id):
    """
    Delete a customer address.
    
    Args:
        customer_id: The ID of the customer
        address_id: The ID of the address to delete
        
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/customers/{customer_id}/addresses/{address_id}.json")

# ====================
# Fulfillment Endpoints
# ====================

@mcp.tool()
def get_fulfillments(order_id, limit=None):
    """
    Retrieve fulfillments for an order.
    
    Args:
        order_id: The ID of the order
        limit: Number of fulfillments to return (default: 50, max: 250)
        
    Returns:
        List of fulfillments
    """
    params = {}
    if limit:
        params["limit"] = limit
    
    return make_request("GET", f"/orders/{order_id}/fulfillments.json", params=params)

@mcp.tool()
def get_fulfillment(order_id, fulfillment_id):
    """
    Retrieve a single fulfillment by ID.
    
    Args:
        order_id: The ID of the order
        fulfillment_id: The ID of the fulfillment
        
    Returns:
        Fulfillment details
    """
    return make_request("GET", f"/orders/{order_id}/fulfillments/{fulfillment_id}.json")

@mcp.tool()
def create_fulfillment(order_id, location_id, tracking_number=None, tracking_url=None,
                       tracking_company=None, lines=None):
    """
    Create a fulfillment for an order.
    
    Args:
        order_id: The ID of the order (required)
        location_id: The ID of the fulfillment location (required)
        tracking_number: Tracking number for the shipment
        tracking_url: URL for tracking the shipment
        tracking_company: Name of the tracking company
        lines: List of line items to fulfill with quantity
        
    Returns:
        Created fulfillment details
    """
    fulfillment = {"location_id": location_id}
    if tracking_number:
        fulfillment["tracking_number"] = tracking_number
    if tracking_url:
        fulfillment["tracking_url"] = tracking_url
    if tracking_company:
        fulfillment["tracking_company"] = tracking_company
    if lines:
        fulfillment["lines"] = lines
    
    return make_request("POST", f"/orders/{order_id}/fulfillments.json", 
                       data={"fulfillment": fulfillment})

@mcp.tool()
def update_fulfillment_tracking(order_id, fulfillment_id, tracking_number=None,
                                tracking_url=None, tracking_company=None):
    """
    Update tracking information for a fulfillment.
    
    Args:
        order_id: The ID of the order
        fulfillment_id: The ID of the fulfillment
        tracking_number: Tracking number for the shipment
        tracking_url: URL for tracking the shipment
        tracking_company: Name of the tracking company
        
    Returns:
        Updated fulfillment details
    """
    fulfillment = {}
    if tracking_number:
        fulfillment["tracking_number"] = tracking_number
    if tracking_url:
        fulfillment["tracking_url"] = tracking_url
    if tracking_company:
        fulfillment["tracking_company"] = tracking_company
    
    return make_request("POST", f"/orders/{order_id}/fulfillments/{fulfillment_id}/update_tracking.json", 
                       data={"fulfillment": fulfillment})

@mcp.tool()
def cancel_fulfillment(order_id, fulfillment_id):
    """
    Cancel a fulfillment.
    
    Args:
        order_id: The ID of the order
        fulfillment_id: The ID of the fulfillment to cancel
        
    Returns:
        Cancelled fulfillment details
    """
    return make_request("POST", f"/orders/{order_id}/fulfillments/{fulfillment_id}/cancel.json")

# ====================
# Refund Endpoints
# ====================

@mcp.tool()
def calculate_refund(order_id, line_items=None, shipping=None, restock_type="return"):
    """
    Calculate refund transactions.
    
    Args:
        order_id: The ID of the order (required)
        line_items: List of line items to refund with quantity
        shipping: Whether to refund shipping costs (True/False)
        restock_type: How to restock items ("return", "cancel", "never")
        
    Returns:
        Calculated refund transactions
    """
    refund = {"restock_type": restock_type}
    if line_items:
        refund["line_items"] = line_items
    if shipping is not None:
        refund["shipping"] = {"restock": shipping}
    
    return make_request("POST", f"/orders/{order_id}/refunds/calculate.json", 
                       data={"refund": refund})

@mcp.tool()
def create_refund(order_id, refund):
    """
    Create a refund for an order.
    
    Args:
        order_id: The ID of the order (required)
        refund: Refund object with line_items, shipping, transactions, etc.
        
    Returns:
        Created refund details
    """
    return make_request("POST", f"/orders/{order_id}/refunds.json", 
                       data={"refund": refund})

@mcp.tool()
def get_order_refunds(order_id, limit=None):
    """
    Retrieve refunds for an order.
    
    Args:
        order_id: The ID of the order
        limit: Number of refunds to return (default: 50, max: 250)
        
    Returns:
        List of refunds
    """
    params = {}
    if limit:
        params["limit"] = limit
    
    return make_request("GET", f"/orders/{order_id}/refunds.json", params=params)

# ====================
# Transaction Endpoints
# ====================

@mcp.tool()
def get_order_transactions(order_id, limit=None):
    """
    Retrieve transactions for an order.
    
    Args:
        order_id: The ID of the order
        limit: Number of transactions to return (default: 50, max: 250)
        
    Returns:
        List of transactions
    """
    params = {}
    if limit:
        params["limit"] = limit
    
    return make_request("GET", f"/orders/{order_id}/transactions.json", params=params)

@mcp.tool()
def get_transaction(order_id, transaction_id):
    """
    Retrieve a single transaction by ID.
    
    Args:
        order_id: The ID of the order
        transaction_id: The ID of the transaction
        
    Returns:
        Transaction details
    """
    return make_request("GET", f"/orders/{order_id}/transactions/{transaction_id}.json")

@mcp.tool()
def create_transaction(order_id, amount, kind="authorization", gateway=None,
                       status=None, message=None, payment_details=None):
    """
    Create a transaction for an order.
    
    Args:
        order_id: The ID of the order (required)
        amount: Transaction amount (required)
        kind: Transaction type ("authorization", "capture", "sale", "refund", "void")
        gateway: Payment gateway name
        status: Transaction status ("pending", "success", "failure", "error")
        message: Transaction message
        payment_details: Payment details object
        
    Returns:
        Created transaction details
    """
    transaction = {
        "amount": amount,
        "kind": kind
    }
    if gateway:
        transaction["gateway"] = gateway
    if status:
        transaction["status"] = status
    if message:
        transaction["message"] = message
    if payment_details:
        transaction["payment_details"] = payment_details
    
    return make_request("POST", f"/orders/{order_id}/transactions.json", 
                       data={"transaction": transaction})

# ====================
# Inventory Endpoints
# ====================

@mcp.tool()
def get_inventory_items(limit=None, since_id=None):
    """
    Retrieve a list of inventory items.
    
    Args:
        limit: Number of items to return (default: 50, max: 250)
        since_id: Return items with ID greater than this value
        
    Returns:
        List of inventory items
    """
    params = {}
    if limit:
        params["limit"] = limit
    if since_id:
        params["since_id"] = since_id
    
    return make_request("GET", "/inventory_items.json", params=params)

@mcp.tool()
def get_inventory_item(inventory_item_id):
    """
    Retrieve a single inventory item by ID.
    
    Args:
        inventory_item_id: The ID of the inventory item
        
    Returns:
        Inventory item details
    """
    return make_request("GET", f"/inventory_items/{inventory_item_id}.json")

@mcp.tool()
def get_inventory_levels(location_id=None, inventory_item_ids=None, limit=None):
    """
    Retrieve inventory levels.
    
    Args:
        location_id: Filter by location ID
        inventory_item_ids: Filter by inventory item IDs (comma-separated)
        limit: Number of levels to return (default: 50, max: 250)
        
    Returns:
        List of inventory levels
    """
    params = {}
    if location_id:
        params["location_id"] = location_id
    if inventory_item_ids:
        params["inventory_item_ids"] = inventory_item_ids
    if limit:
        params["limit"] = limit
    
    return make_request("GET", "/inventory_levels.json", params=params)

@mcp.tool()
def adjust_inventory_level(inventory_item_id, location_id, quantity_adjustment):
    """
    Adjust inventory level for an item.
    
    Args:
        inventory_item_id: The ID of the inventory item (required)
        location_id: The ID of the location (required)
        quantity_adjustment: Amount to adjust by (positive or negative)
        
    Returns:
        Updated inventory level
    """
    return make_request("POST", "/inventory_levels/adjust.json", data={
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "quantity_adjustment": quantity_adjustment
    })

@mcp.tool()
def connect_inventory_level(inventory_item_id, location_id):
    """
    Connect an inventory item to a location.
    
    Args:
        inventory_item_id: The ID of the inventory item (required)
        location_id: The ID of the location (required)
        
    Returns:
        Connected inventory level
    """
    return make_request("POST", "/inventory_levels/connect.json", data={
        "inventory_item_id": inventory_item_id,
        "location_id": location_id
    })

@mcp.tool()
def set_inventory_level(inventory_item_id, location_id, available):
    """
    Set inventory level for an item.
    
    Args:
        inventory_item_id: The ID of the inventory item (required)
        location_id: The ID of the location (required)
        available: Available quantity (required)
        
    Returns:
        Set inventory level
    """
    return make_request("POST", "/inventory_levels/set.json", data={
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available": available
    })

# ====================
# Discount Endpoints
# ====================

@mcp.tool()
def get_price_rules(limit=None, since_id=None):
    """
    Retrieve a list of price rules.
    
    Args:
        limit: Number of rules to return (default: 50, max: 250)
        since_id: Return rules with ID greater than this value
        
    Returns:
        List of price rules
    """
    params = {}
    if limit:
        params["limit"] = limit
    if since_id:
        params["since_id"] = since_id
    
    return make_request("GET", "/price_rules.json", params=params)

@mcp.tool()
def get_price_rule(price_rule_id):
    """
    Retrieve a single price rule by ID.
    
    Args:
        price_rule_id: The ID of the price rule
        
    Returns:
        Price rule details
    """
    return make_request("GET", f"/price_rules/{price_rule_id}.json")

@mcp.tool()
def create_price_rule(title, target_type="line_item", target_selection="all",
                      allocation_method="across", value_type="percentage", value=-10.0,
                      customer_selection="all", starts_at=None):
    """
    Create a new price rule.
    
    Args:
        title: Name of the price rule (required)
        target_type: What the discount applies to ("line_item", "shipping_line")
        target_selection: Which items get the discount ("all", "selected")
        allocation_method: How the discount is allocated ("across", "each", "maximum_order_quantity")
        value_type: Type of value ("percentage", "fixed_amount")
        value: Discount value (negative for percentage, positive for fixed)
        customer_selection: Which customers get the discount ("all", "specific")
        starts_at: When the rule starts (ISO 8601 format)
        
    Returns:
        Created price rule details
    """
    price_rule = {
        "title": title,
        "target_type": target_type,
        "target_selection": target_selection,
        "allocation_method": allocation_method,
        "value_type": value_type,
        "value": value,
        "customer_selection": customer_selection
    }
    if starts_at:
        price_rule["starts_at"] = starts_at
    
    return make_request("POST", "/price_rules.json", data={"price_rule": price_rule})

@mcp.tool()
def update_price_rule(price_rule_id, **kwargs):
    """
    Update an existing price rule.
    
    Args:
        price_rule_id: The ID of the price rule to update (required)
        **kwargs: Fields to update (title, target_type, value, etc.)
        
    Returns:
        Updated price rule details
    """
    price_rule = kwargs
    return make_request("PUT", f"/price_rules/{price_rule_id}.json", 
                       data={"price_rule": price_rule})

@mcp.tool()
def delete_price_rule(price_rule_id):
    """
    Delete a price rule.
    
    Args:
        price_rule_id: The ID of the price rule to delete
        
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/price_rules/{price_rule_id}.json")

@mcp.tool()
def create_discount_code(price_rule_id, code, usage_limit=None):
    """
    Create a discount code for a price rule.
    
    Args:
        price_rule_id: The ID of the price rule (required)
        code: The discount code (required)
        usage_limit: Maximum number of times the code can be used
        
    Returns:
        Created discount code details
    """
    discount_code = {"code": code}
    if usage_limit:
        discount_code["usage_limit"] = usage_limit
    
    return make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", 
                       data={"discount_code": discount_code})

@mcp.tool()
def get_discount_codes(price_rule_id, limit=None):
    """
    Retrieve discount codes for a price rule.
    
    Args:
        price_rule_id: The ID of the price rule
        limit: Number of codes to return (default: 50, max: 250)
        
    Returns:
        List of discount codes
    """
    params = {}
    if limit:
        params["limit"] = limit
    
    return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json", params=params)

# ====================
# Metafield Endpoints
# ====================

@mcp.tool()
def get_metafields(resource_type, resource_id, limit=None, fields=None):
    """
    Retrieve metafields for a resource.
    
    Args:
        resource_type: Type of resource ("products", "variants", "customers", etc.)
        resource_id: ID of the resource
        limit: Number of metafields to return (default: 50, max: 250)
        fields: Comma-separated list of fields to return
        
    Returns:
        List of metafields
    """
    params = {}
    if limit:
        params["limit"] = limit
    if fields:
        params["fields"] = fields
    
    return make_request("GET", f"/{resource_type}/{resource_id}/metafields.json", params=params)

@mcp.tool()
def get_metafield(resource_type, resource_id, metafield_id):
    """
    Retrieve a single metafield by ID.
    
    Args:
        resource_type: Type of resource ("products", "variants", "customers", etc.)
        resource_id: ID of the resource
        metafield_id: ID of the metafield
        
    Returns:
        Metafield details
    """
    return make_request("GET", f"/{resource_type}/{resource_id}/metafields/{metafield_id}.json")

@mcp.tool()
def create_metafield(resource_type, resource_id, namespace, key, value, type="string"):
    """
    Create a new metafield.
    
    Args:
        resource_type: Type of resource ("products", "variants", "customers", etc.)
        resource_id: ID of the resource
        namespace: Namespace for the metafield (required)
        key: Key for the metafield (required)
        value: Value for the metafield (required)
        type: Data type ("string", "integer", "json_string", "boolean", "decimal")
        
    Returns:
        Created metafield details
    """
    metafield = {
        "namespace": namespace,
        "key": key,
        "value": value,
        "type": type
    }
    
    return make_request("POST", f"/{resource_type}/{resource_id}/metafields.json", 
                       data={"metafield": metafield})

@mcp.tool()
def update_metafield(resource_type, resource_id, metafield_id, **kwargs):
    """
    Update an existing metafield.
    
    Args:
        resource_type: Type of resource ("products", "variants", "customers", etc.)
        resource_id: ID of the resource
        metafield_id: ID of the metafield to update (required)
        **kwargs: Fields to update (value, type, etc.)
        
    Returns:
        Updated metafield details
    """
    metafield = kwargs
    return make_request("PUT", f"/{resource_type}/{resource_id}/metafields/{metafield_id}.json", 
                       data={"metafield": metafield})

@mcp.tool()
def delete_metafield(resource_type, resource_id, metafield_id):
    """
    Delete a metafield.
    
    Args:
        resource_type: Type of resource ("products", "variants", "customers", etc.)
        resource_id: ID of the resource
        metafield_id: ID of the metafield to delete
        
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/{resource_type}/{resource_id}/metafields/{metafield_id}.json")

# ====================
# Shop Endpoints
# ====================

@mcp.tool()
def get_shop():
    """
    Retrieve information about the shop.
    
    Returns:
        Shop details
    """
    return make_request("GET", "/shop.json")

@mcp.tool()
def get_locations(limit=None):
    """
    Retrieve a list of locations.
    
    Args:
        limit: Number of locations to return (default: 50, max: 250)
        
    Returns:
        List of locations
    """
    params = {}
    if limit:
        params["limit"] = limit
    
    return make_request("GET", "/locations.json", params=params)

@mcp.tool()
def get_location(location_id):
    """
    Retrieve a single location by ID.
    
    Args:
        location_id: The ID of the location
        
    Returns:
        Location details
    """
    return make_request("GET", f"/locations/{location_id}.json")

# ====================
# Draft Order Endpoints
# ====================

@mcp.tool()
def get_draft_orders(limit=None, since_id=None, status=None):
    """
    Retrieve a list of draft orders.
    
    Args:
        limit: Number of draft orders to return (default: 50, max: 250)
        since_id: Return draft orders with ID greater than this value
        status: Filter by status (open, completed, cancelled)
        
    Returns:
        List of draft orders
    """
    params = {}
    if limit:
        params["limit"] = limit
    if since_id:
        params["since_id"] = since_id
    if status:
        params["status"] = status
    
    return make_request("GET", "/draft_orders.json", params=params)

@mcp.tool()
def get_draft_order(draft_order_id):
    """
    Retrieve a single draft order by ID.
    
    Args:
        draft_order_id: The ID of the draft order
        
    Returns:
        Draft order details
    """
    return make_request("GET", f"/draft_orders/{draft_order_id}.json")

@mcp.tool()
def create_draft_order(customer=None, line_items=None, shipping_address=None,
                       billing_address=None, note=None, gift_cards=None,
                       email=None):
    """
    Create a new draft order.
    
    Args:
        customer: Customer information
        line_items: List of line items
        shipping_address: Shipping address
        billing_address: Billing address
        note: Order note
        gift_cards: List of gift cards to apply
        email: Customer email
        
    Returns:
        Created draft order details
    """
    draft_order = {}
    if customer:
        draft_order["customer"] = customer
    if line_items:
        draft_order["line_items"] = line_items
    if shipping_address:
        draft_order["shipping_address"] = shipping_address
    if billing_address:
        draft_order["billing_address"] = billing_address
    if note:
        draft_order["note"] = note
    if gift_cards:
        draft_order["gift_cards"] = gift_cards
    if email:
        draft_order["email"] = email
    
    return make_request("POST", "/draft_orders.json", data={"draft_order": draft_order})

@mcp.tool()
def update_draft_order(draft_order_id, **kwargs):
    """
    Update an existing draft order.
    
    Args:
        draft_order_id: The ID of the draft order to update (required)
        **kwargs: Fields to update
        
    Returns:
        Updated draft order details
    """
    draft_order = kwargs
    return make_request("PUT", f"/draft_orders/{draft_order_id}.json", 
                       data={"draft_order": draft_order})

@mcp.tool()
def delete_draft_order(draft_order_id):
    """
    Delete a draft order.
    
    Args:
        draft_order_id: The ID of the draft order to delete
        
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/draft_orders/{draft_order_id}.json")

@mcp.tool()
def send_draft_order_invoice(draft_order_id):
    """
    Send an invoice for a draft order.
    
    Args:
        draft_order_id: The ID of the draft order
        
    Returns:
        Invoice confirmation
    """
    return make_request("POST", f"/draft_orders/{draft_order_id}/send_invoice.json")

# ====================
# Webhook Endpoints
# ====================

@mcp.tool()
def get_webhooks(limit=None):
    """
    Retrieve a list of webhooks.
    
    Args:
        limit: Number of webhooks to return (default: 50, max: 250)
        
    Returns:
        List of webhooks
    """
    params = {}
    if limit:
        params["limit"] = limit
    
    return make_request("GET", "/webhooks.json", params=params)

@mcp.tool()
def get_webhook(webhook_id):
    """
    Retrieve a single webhook by ID.
    
    Args:
        webhook_id: The ID of the webhook
        
    Returns:
        Webhook details
    """
    return make_request("GET", f"/webhooks/{webhook_id}.json")

@mcp.tool()
def create_webhook(topic, address, format="json"):
    """
    Create a new webhook.
    
    Args:
        topic: Event topic (e.g., "orders/create", "products/update")
        address: URL where webhook should be delivered
        format: Data format ("json" or "xml")
        
    Returns:
        Created webhook details
    """
    webhook = {
        "topic": topic,
        "address": address,
        "format": format
    }
    
    return make_request("POST", "/webhooks.json", data={"webhook": webhook})

@mcp.tool()
def update_webhook(webhook_id, topic=None, address=None, format=None):
    """
    Update an existing webhook.
    
    Args:
        webhook_id: The ID of the webhook to update (required)
        topic: Updated event topic
        address: Updated delivery URL
        format: Updated data format
        
    Returns:
        Updated webhook details
    """
    webhook = {}
    if topic:
        webhook["topic"] = topic
    if address:
        webhook["address"] = address
    if format:
        webhook["format"] = format
    
    return make_request("PUT", f"/webhooks/{webhook_id}.json", data={"webhook": webhook})

@mcp.tool()
def delete_webhook(webhook_id):
    """
    Delete a webhook.
    
    Args:
        webhook_id: The ID of the webhook to delete
        
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/webhooks/{webhook_id}.json")

# ====================
# Application Charge Endpoints
# ====================

@mcp.tool()
def get_application_charges(limit=None):
    """
    Retrieve a list of application charges.
    
    Args:
        limit: Number of charges to return (default: 50, max: 250)
        
    Returns:
        List of application charges
    """
    params = {}
    if limit:
        params["limit"] = limit
    
    return make_request("GET", "/application_charges.json", params=params)

@mcp.tool()
def get_application_charge(charge_id):
    """
    Retrieve a single application charge by ID.
    
    Args:
        charge_id: The ID of the charge
        
    Returns:
        Charge details
    """
    return make_request("GET", f"/application_charges/{charge_id}.json")

@mcp.tool()
def create_application_charge(name, price, return_url, test=None, charged_only_once=None):
    """
    Create a new application charge.
    
    Args:
        name: Name of the charge (required)
        price: Price for the charge (required)
        return_url: URL to redirect to after charge acceptance (required)
        test: Whether this is a test charge
        charged_only_once: Whether the charge can only be used once
        
    Returns:
        Created charge details
    """
    charge = {
        "name": name,
        "price": price,
        "return_url": return_url
    }
    if test is not None:
        charge["test"] = test
    if charged_only_once is not None:
        charge["charged_only_once"] = charged_only_once
    
    return make_request("POST", "/application_charges.json", data={"application_charge": charge})

@mcp.tool()
def get_recurring_application_charges(limit=None):
    """
    Retrieve a list of recurring application charges.
    
    Args:
        limit: Number of charges to return (default: 50, max: 250)
        
    Returns:
        List of recurring application charges
    """
    params = {}
    if limit:
        params["limit"] = limit
    
    return make_request("GET", "/recurring_application_charges.json", params=params)

@mcp.tool()
def get_recurring_application_charge(charge_id):
    """
    Retrieve a single recurring application charge by ID.
    
    Args:
        charge_id: The ID of the charge
        
    Returns:
        Charge details
    """
    return make_request("GET", f"/recurring_application_charges/{charge_id}.json")

@mcp.tool()
def create_recurring_application_charge(name, price, return_url, test=None,
                                        trial_days=None, capped_amount=None,
                                        terms=None):
    """
    Create a new recurring application charge.
    
    Args:
        name: Name of the charge (required)
        price: Price for the charge (required)
        return_url: URL to redirect to after charge acceptance (required)
        test: Whether this is a test charge
        trial_days: Number of trial days
        capped_amount: Maximum amount to charge
        terms: Terms of the recurring charge
        
    Returns:
        Created charge details
    """
    charge = {
        "name": name,
        "price": price,
        "return_url": return_url
    }
    if test is not None:
        charge["test"] = test
    if trial_days:
        charge["trial_days"] = trial_days
    if capped_amount:
        charge["capped_amount"] = capped_amount
    if terms:
        charge["terms"] = terms
    
    return make_request("POST", "/recurring_application_charges.json", 
                       data={"recurring_application_charge": charge})

@mcp.tool()
def activate_recurring_application_charge(charge_id):
    """
    Activate a recurring application charge.
    
    Args:
        charge_id: The ID of the charge to activate
        
    Returns:
        Activated charge details
    """
    return make_request("POST", f"/recurring_application_charges/{charge_id}/activate.json")

@mcp.tool()
def delete_recurring_application_charge(charge_id):
    """
    Delete a recurring application charge.
    
    Args:
        charge_id: The ID of the charge to delete
        
    Returns:
        Deletion confirmation
    """
    return make_request("DELETE", f"/recurring_application_charges/{charge_id}.json")

# ====================
# Shipping Zone Endpoints
# ====================

@mcp.tool()
def get_shipping_zones(limit=None):
    """
    Retrieve a list of shipping zones.
    
    Args:
        limit: Number of zones to return (default: 50, max: 250)
        
    Returns:
        List of shipping zones
    """
    params = {}
    if limit:
        params["limit"] = limit
    
    return make_request("GET", "/shipping_zones.json", params=params)

@mcp.tool()
def get_shipping_zone(shipping_zone_id):
    """
    Retrieve a single shipping zone by ID.
    
    Args:
        shipping_zone_id: The ID of the shipping zone
        
    Returns:
        Shipping zone details
    """
    return make_request("GET", f"/shipping_zones/{shipping_zone_id}.json")

if __name__ == "__main__":
    mcp.run()
