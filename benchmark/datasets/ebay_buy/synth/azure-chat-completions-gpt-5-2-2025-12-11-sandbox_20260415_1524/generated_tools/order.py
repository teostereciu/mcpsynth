from typing import Any, Dict, List, Optional

from .ebay_client import EbayClient


ORDER_V2_BASE = "https://apix.sandbox.ebay.com"  # overridden in client via base_url; kept for doc clarity


def initiate_guest_checkout_session(
    client: EbayClient,
    *,
    marketplace_id: str,
    contact_email: str,
    line_items: List[Dict[str, Any]],
    shipping_address: Dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {
        "Content-Type": "application/json",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {
        "contactEmail": contact_email,
        "lineItemInputs": line_items,
        "shippingAddress": shipping_address,
    }
    # Note: docs mention apix.* host; in practice, /buy/order/v2 is on api.* for many apps.
    # We'll call via client's base_url; users can set EBAY_ENVIRONMENT accordingly.
    return client.request("POST", "/buy/order/v2/guest_checkout_session/initiate", json=payload, headers=headers)
