from typing import Any, Dict, Optional

from .http_client import EbayHttpClient


class TaxonomyTools:
    def __init__(self, client: Optional[EbayHttpClient] = None):
        self.client = client or EbayHttpClient()

    def get_default_category_tree_id(self, marketplace_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            "/commerce/taxonomy/v1/get_default_category_tree_id",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            params={"marketplace_id": marketplace_id},
        )

    def get_category_tree(self, category_tree_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
        )

    def get_category_subtree(self, category_tree_id: str, category_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            params={"category_id": category_id},
        )

    def get_category_suggestions(self, category_tree_id: str, q: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            params={"q": q},
        )

    def get_item_aspects_for_category(self, category_tree_id: str, category_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            params={"category_id": category_id},
        )

    def fetch_item_aspects(self, category_tree_id: str, category_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            params={"category_id": category_id},
        )

    def get_expired_categories(self, category_tree_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
        )

    def get_compatibility_properties(self, category_tree_id: str, category_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            params={"category_id": category_id},
        )

    def get_compatibility_property_values(
        self,
        category_tree_id: str,
        category_id: str,
        compatibility_property: str,
        *,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {"category_id": category_id, "compatibility_property": compatibility_property}
        if filter is not None:
            params["filter"] = filter
        return self.client.request(
            "GET",
            f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            params=params,
        )
