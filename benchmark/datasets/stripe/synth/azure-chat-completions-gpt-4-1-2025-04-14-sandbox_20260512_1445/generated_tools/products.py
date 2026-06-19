import os
import requests
from fastmcp import tool

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

@tool("create_product")
def create_product(name: str, active: bool = True, description: str = None, id: str = None, metadata: dict = None, tax_code: str = None, default_price_data: dict = None, images: list = None, marketing_features: list = None, package_dimensions: dict = None, shippable: bool = None, statement_descriptor: str = None, unit_label: str = None, url: str = None):
    """
    Create a Product object.
    """
    data = {
        "name": name,
        "active": "true" if active else "false"
    }
    if description:
        data["description"] = description
    if id:
        data["id"] = id
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if tax_code:
        data["tax_code"] = tax_code
    if default_price_data:
        for k, v in default_price_data.items():
            data[f"default_price_data[{k}]"] = v
    if images:
        for i, img in enumerate(images):
            data[f"images[{i}]"] = img
    if marketing_features:
        for i, feat in enumerate(marketing_features):
            data[f"marketing_features[{i}]"] = feat
    if package_dimensions:
        for k, v in package_dimensions.items():
            data[f"package_dimensions[{k}]"] = v
    if shippable is not None:
        data["shippable"] = "true" if shippable else "false"
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    if unit_label:
        data["unit_label"] = unit_label
    if url:
        data["url"] = url
    try:
        resp = requests.post(f"{BASE_URL}/products", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("retrieve_product")
def retrieve_product(product_id: str):
    """
    Retrieve a Product object.
    """
    try:
        resp = requests.get(f"{BASE_URL}/products/{product_id}", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("update_product")
def update_product(product_id: str, active: bool = None, default_price: str = None, description: str = None, metadata: dict = None, name: str = None, tax_code: str = None, images: list = None, marketing_features: list = None, package_dimensions: dict = None, shippable: bool = None, statement_descriptor: str = None, unit_label: str = None, url: str = None):
    """
    Update a Product object.
    """
    data = {}
    if active is not None:
        data["active"] = "true" if active else "false"
    if default_price:
        data["default_price"] = default_price
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if name:
        data["name"] = name
    if tax_code:
        data["tax_code"] = tax_code
    if images:
        for i, img in enumerate(images):
            data[f"images[{i}]"] = img
    if marketing_features:
        for i, feat in enumerate(marketing_features):
            data[f"marketing_features[{i}]"] = feat
    if package_dimensions:
        for k, v in package_dimensions.items():
            data[f"package_dimensions[{k}]"] = v
    if shippable is not None:
        data["shippable"] = "true" if shippable else "false"
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    if unit_label:
        data["unit_label"] = unit_label
    if url:
        data["url"] = url
    try:
        resp = requests.post(f"{BASE_URL}/products/{product_id}", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}
