from typing import Any, Dict, Optional

from .ebay_client import EbayClient


class InventoryTools:
    def __init__(self, client: Optional[EbayClient] = None):
        self.client = client or EbayClient()

    # Inventory Item
    def get_inventory_item(self, sku: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/inventory/v1/inventory_item/{sku}")

    def create_or_replace_inventory_item(self, sku: str, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("PUT", f"/sell/inventory/v1/inventory_item/{sku}", json=inventory_item)

    def delete_inventory_item(self, sku: str) -> Dict[str, Any]:
        return self.client.request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")

    def bulk_get_inventory_item(self, requests: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("POST", "/sell/inventory/v1/bulk_get_inventory_item", json=requests)

    def bulk_create_or_replace_inventory_item(self, requests: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("POST", "/sell/inventory/v1/bulk_create_or_replace_inventory_item", json=requests)

    # Inventory Item - location/availability
    def get_inventory_item_group(self, inventory_item_group_key: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")

    def create_or_replace_inventory_item_group(self, inventory_item_group_key: str, body: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("PUT", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}", json=body)

    def delete_inventory_item_group(self, inventory_item_group_key: str) -> Dict[str, Any]:
        return self.client.request("DELETE", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")

    # Offers
    def get_offer(self, offer_id: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/inventory/v1/offer/{offer_id}")

    def create_offer(self, offer: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("POST", "/sell/inventory/v1/offer", json=offer)

    def update_offer(self, offer_id: str, offer_patch: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json=offer_patch)

    def publish_offer(self, offer_id: str) -> Dict[str, Any]:
        return self.client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")

    def withdraw_offer(self, offer_id: str) -> Dict[str, Any]:
        return self.client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw")

    def delete_offer(self, offer_id: str) -> Dict[str, Any]:
        return self.client.request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")

    def get_offers(self, sku: Optional[str] = None, marketplace_id: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if sku:
            params["sku"] = sku
        if marketplace_id:
            params["marketplace_id"] = marketplace_id
        return self.client.request("GET", "/sell/inventory/v1/offer", params=params)

    # Locations
    def get_inventory_location(self, merchant_location_key: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/inventory/v1/location/{merchant_location_key}")

    def create_inventory_location(self, merchant_location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}", json=location)

    def update_inventory_location(self, merchant_location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("PUT", f"/sell/inventory/v1/location/{merchant_location_key}", json=location)

    def delete_inventory_location(self, merchant_location_key: str) -> Dict[str, Any]:
        return self.client.request("DELETE", f"/sell/inventory/v1/location/{merchant_location_key}")

    def get_inventory_locations(self, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        return self.client.request("GET", "/sell/inventory/v1/location", params={"limit": limit, "offset": offset})
