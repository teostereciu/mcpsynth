from typing import Dict, Any

from generated_tools.catalog import client


def get_user() -> Dict[str, Any]:
    return client.request(
        "GET",
        "/commerce/identity/v1/user/",
        token_type="user_identity",
        base_url=("https://apiz.sandbox.ebay.com" if client.base_url.endswith("sandbox.ebay.com") else "https://apiz.ebay.com"),
    )
