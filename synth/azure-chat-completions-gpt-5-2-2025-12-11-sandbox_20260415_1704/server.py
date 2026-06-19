from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.client import TikTokShopClient
from generated_tools import products


mcp = FastMCP("tiktok-shop-partner-open-api")


def _client() -> TikTokShopClient:
    return TikTokShopClient.from_env()


@mcp.tool()
def tts_create_product_202309(product: Dict[str, Any], shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """Create a product (local listing) using Product API v202309."""
    return products.create_product_202309(_client(), product=product, shop_cipher=shop_cipher)


@mcp.tool()
def tts_get_product_202309(
    product_id: str,
    return_under_review_version: Optional[bool] = None,
    return_draft_version: Optional[bool] = None,
    locale: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Get product details using Product API v202309."""
    return products.get_product_202309(
        _client(),
        product_id=product_id,
        return_under_review_version=return_under_review_version,
        return_draft_version=return_draft_version,
        locale=locale,
        shop_cipher=shop_cipher,
    )


if __name__ == "__main__":
    mcp.run()
