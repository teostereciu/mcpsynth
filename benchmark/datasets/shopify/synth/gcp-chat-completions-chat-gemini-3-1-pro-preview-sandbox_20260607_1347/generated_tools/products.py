from generated_tools.utils import make_request

def register(mcp):
    @mcp.tool()
    def get_products(limit: int = 50, title: str = None):
        """Retrieve a list of products."""
        params = {"limit": limit}
        if title:
            params["title"] = title
        return make_request("GET", "/products.json", params=params)

    @mcp.tool()
    def get_product(product_id: int):
        """Retrieve a single product by ID."""
        return make_request("GET", f"/products/{product_id}.json")

    @mcp.tool()
    def create_product(product: dict):
        """Create a new product."""
        return make_request("POST", "/products.json", json_data={"product": product})

    @mcp.tool()
    def update_product(product_id: int, product: dict):
        """Update an existing product."""
        return make_request("PUT", f"/products/{product_id}.json", json_data={"product": product})

    @mcp.tool()
    def delete_product(product_id: int):
        """Delete a product."""
        return make_request("DELETE", f"/products/{product_id}.json")

    @mcp.tool()
    def get_product_variants(product_id: int):
        """Retrieve a list of product variants."""
        return make_request("GET", f"/products/{product_id}/variants.json")

    @mcp.tool()
    def get_product_variant(variant_id: int):
        """Retrieve a single product variant by ID."""
        return make_request("GET", f"/variants/{variant_id}.json")

    @mcp.tool()
    def create_product_variant(product_id: int, variant: dict):
        """Create a new product variant."""
        return make_request("POST", f"/products/{product_id}/variants.json", json_data={"variant": variant})

    @mcp.tool()
    def update_product_variant(variant_id: int, variant: dict):
        """Update an existing product variant."""
        return make_request("PUT", f"/variants/{variant_id}.json", json_data={"variant": variant})

    @mcp.tool()
    def delete_product_variant(product_id: int, variant_id: int):
        """Delete a product variant."""
        return make_request("DELETE", f"/products/{product_id}/variants/{variant_id}.json")

    @mcp.tool()
    def get_product_images(product_id: int):
        """Retrieve a list of product images."""
        return make_request("GET", f"/products/{product_id}/images.json")

    @mcp.tool()
    def create_product_image(product_id: int, image: dict):
        """Create a new product image."""
        return make_request("POST", f"/products/{product_id}/images.json", json_data={"image": image})

    @mcp.tool()
    def delete_product_image(product_id: int, image_id: int):
        """Delete a product image."""
        return make_request("DELETE", f"/products/{product_id}/images/{image_id}.json")

    @mcp.tool()
    def get_custom_collections():
        """Retrieve a list of custom collections."""
        return make_request("GET", "/custom_collections.json")

    @mcp.tool()
    def get_smart_collections():
        """Retrieve a list of smart collections."""
        return make_request("GET", "/smart_collections.json")
