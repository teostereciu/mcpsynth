from typing import Any, Dict, Optional

from .ebay_client import EbayClient


class AccountTools:
    def __init__(self, client: Optional[EbayClient] = None):
        self.client = client or EbayClient()

    # Fulfillment policies
    def get_fulfillment_policies(self, marketplace_id: str) -> Dict[str, Any]:
        return self.client.request("GET", "/sell/account/v1/fulfillment_policy", params={"marketplace_id": marketplace_id})

    def get_fulfillment_policy(self, fulfillment_policy_id: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")

    def create_fulfillment_policy(self, policy: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("POST", "/sell/account/v1/fulfillment_policy", json=policy)

    def update_fulfillment_policy(self, fulfillment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("PUT", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}", json=policy)

    def delete_fulfillment_policy(self, fulfillment_policy_id: str) -> Dict[str, Any]:
        return self.client.request("DELETE", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")

    # Payment policies
    def get_payment_policies(self, marketplace_id: str) -> Dict[str, Any]:
        return self.client.request("GET", "/sell/account/v1/payment_policy", params={"marketplace_id": marketplace_id})

    def get_payment_policy(self, payment_policy_id: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/account/v1/payment_policy/{payment_policy_id}")

    def create_payment_policy(self, policy: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("POST", "/sell/account/v1/payment_policy", json=policy)

    def update_payment_policy(self, payment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("PUT", f"/sell/account/v1/payment_policy/{payment_policy_id}", json=policy)

    def delete_payment_policy(self, payment_policy_id: str) -> Dict[str, Any]:
        return self.client.request("DELETE", f"/sell/account/v1/payment_policy/{payment_policy_id}")

    # Return policies
    def get_return_policies(self, marketplace_id: str) -> Dict[str, Any]:
        return self.client.request("GET", "/sell/account/v1/return_policy", params={"marketplace_id": marketplace_id})

    def get_return_policy(self, return_policy_id: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/account/v1/return_policy/{return_policy_id}")

    def create_return_policy(self, policy: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("POST", "/sell/account/v1/return_policy", json=policy)

    def update_return_policy(self, return_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("PUT", f"/sell/account/v1/return_policy/{return_policy_id}", json=policy)

    def delete_return_policy(self, return_policy_id: str) -> Dict[str, Any]:
        return self.client.request("DELETE", f"/sell/account/v1/return_policy/{return_policy_id}")

    # Sales tax
    def get_sales_taxes(self, marketplace_id: str) -> Dict[str, Any]:
        return self.client.request("GET", "/sell/account/v1/sales_tax", params={"marketplace_id": marketplace_id})

    def get_sales_tax(self, country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")

    def create_or_replace_sales_tax(self, country_code: str, jurisdiction_id: str, body: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("PUT", f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}", json=body)

    def delete_sales_tax(self, country_code: str, jurisdiction_id: str) -> Dict[str, Any]:
        return self.client.request("DELETE", f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")
