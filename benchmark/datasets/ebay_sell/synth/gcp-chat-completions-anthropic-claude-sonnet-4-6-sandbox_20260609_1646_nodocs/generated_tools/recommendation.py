"""
eBay Sell Recommendation API tools.
Covers: listing recommendations (quality improvements, pricing, etc.).
"""

from typing import Optional
from auth import api_get, api_post


def get_listing_recommendations(
    filter: Optional[str] = None,
    limit: int = 100,
    offset: int = 0,
) -> dict:
    """
    Get listing recommendations for the seller's active listings.

    filter: e.g. "listingIds:{123456789|987654321}"
             or "recommendationTypes:{PRICE_RECOMMENDATION|AD_RATE_RECOMMENDATION}"
    """
    params: dict = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return api_get("/sell/recommendation/v1/listing_recommendation", params=params)


def find_listing_recommendations(body: dict) -> dict:
    """
    Find listing recommendations for specific listing IDs.

    body fields:
      listingIds: list of str (up to 500)
      recommendationTypes: list of str (optional)
    """
    return api_post("/sell/recommendation/v1/listing_recommendation/find", body=body)
