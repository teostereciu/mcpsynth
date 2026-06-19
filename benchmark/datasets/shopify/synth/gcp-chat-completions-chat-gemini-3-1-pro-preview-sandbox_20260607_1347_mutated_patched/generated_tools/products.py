import json

def register_tools(mcp, make_request):
    @mcp.tool()
    def get_products(limit: int = 50, since_id: int = None, title: str = None, vendor: str = None, product_type: str = None, collection_id: int = None, status: str = None):
        """Retrieve a list of products."""
        params = {"limit": limit}
        if since_id: params["since_id"] = since_id
        if title: params["title"] = title
        if vendor: params["vendor"] = vendor
        if product_type: params["product_type"] = product_type
        if collection_id: params["collection_id"] = collection_id
        if status: params["status"] = status
        return make_request("GET", "/products.json", params=params)

    @mcp.tool()
    def get_product(product_id: int):
        """Retrieve a single product by ID."""
        return make_request("GET", f"/products/{product_id}.json")

    @mcp.tool()
    def create_product(title: str, body_html: str = None, vendor: str = None, product_type: str = None, tags: str = None, status: str = "active"):
        """Create a new product."""
        product = {"title": title, "status": status}
        if body_html: product["body_html"] = body_html
        if vendor: product["vendor"] = vendor
        if product_type: product["product_type"] = product_type
        if tags: product["tags"] = tags
        return make_request("POST", "/products.json", json_data={"product": product})

    @mcp.tool()
    def update_product(product_id: int, title: str = None, body_html: str = None, vendor: str = None, product_type: str = None, tags: str = None, status: str = None):
        """Update an existing product."""
        product = {"id": product_id}
        if title: product["title"] = title
        if body_html: product["body_html"] = body_html
        if vendor: product["vendor"] = vendor
        if product_type: product["product_type"] = product_type
        if tags: product["tags"] = tags
        if status: product["status"] = status
        return make_request("PUT", f"/products/{product_id}.json", json_data={"product": product})

    @mcp.tool()
    def delete_product(product_id: int):
        """Delete a product."""
        return make_request("DELETE", f"/products/{product_id}.json")

    # Product Variants
    @mcp.tool()
    def get_product_variants(product_id: int):
        """Retrieve a list of variants for a product."""
        return make_request("GET", f"/products/{product_id}/variants.json")

    @mcp.tool()
    def get_product_variant(variant_id: int):
        """Retrieve a single product variant by ID."""
        return make_request("GET", f"/variants/{variant_id}.json")

    @mcp.tool()
    def create_product_variant(product_id: int, price: str, option1: str, sku: str = None, inventory_quantity: int = None):
        """Create a new product variant."""
        variant = {"price": price, "option1": option1}
        if sku: variant["sku"] = sku
        if inventory_quantity is not None: variant["inventory_quantity"] = inventory_quantity
        return make_request("POST", f"/products/{product_id}/variants.json", json_data={"variant": variant})

    @mcp.tool()
    def update_product_variant(variant_id: int, price: str = None, option1: str = None, sku: str = None):
        """Update an existing product variant."""
        variant = {"id": variant_id}
        if price: variant["price"] = price
        if option1: variant["option1"] = option1
        if sku: variant["sku"] = sku
        return make_request("PUT", f"/variants/{variant_id}.json", json_data={"variant": variant})

    @mcp.tool()
    def delete_product_variant(product_id: int, variant_id: int):
        """Delete a product variant."""
        return make_request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")

    # Product Images
    @mcp.tool()
    def get_product_images(product_id: int):
        """Retrieve a list of images for a product."""
        return make_request("GET", f"/products/{product_id}/images.json")

    @mcp.tool()
    def create_product_image(product_id: int, src: str = None, attachment: str = None, alt: str = None):
        """Create a new product image. Provide either src (URL) or attachment (base64)."""
        image = {}
        if src: image["src"] = src
        if attachment: image["attachment"] = attachment
        if alt: image["alt"] = alt
        return make_request("POST", f"/products/{product_id}/images.json", json_data={"image": image})

    @mcp.tool()
    def delete_product_image(product_id: int, image_id: int):
        """Delete a product image."""
        return make_request("DELETE", f"/products/{product_id}/images/{image_id}.json")

    # Collections (Custom and Smart)
    @mcp.tool()
    def get_custom_collections(limit: int = 50, title: str = None):
        """Retrieve a list of custom collections."""
        params = {"limit": limit}
        if title: params["title"] = title
        return make_request("GET", "/custom_collections.json", params=params)

    @mcp.tool()
    def get_smart_collections(limit: int = 50, title: str = None):
        """Retrieve a list of smart collections."""
        params = {"limit": limit}
        if title: params["title"] = title
        return make_request("GET", "/smart_collections.json", params=params)
