"""eBay Sell Marketing API tools."""
from typing import Optional
from .client import get_client


# ── Campaigns ─────────────────────────────────────────────────────────────────

def get_campaigns(campaign_title: Optional[str] = None, campaign_status: Optional[str] = None,
                  campaign_targeting_types: Optional[str] = None, channels: Optional[str] = None,
                  end_date_range: Optional[str] = None, start_date_range: Optional[str] = None,
                  funding_strategy: Optional[str] = None, limit: Optional[str] = None,
                  offset: Optional[str] = None) -> dict:
    """Retrieve details for all of the seller's defined Promoted Listings campaigns."""
    client = get_client()
    params = {}
    if campaign_title:
        params["campaign_title"] = campaign_title
    if campaign_status:
        params["campaign_status"] = campaign_status
    if campaign_targeting_types:
        params["campaign_targeting_types"] = campaign_targeting_types
    if channels:
        params["channels"] = channels
    if end_date_range:
        params["end_date_range"] = end_date_range
    if start_date_range:
        params["start_date_range"] = start_date_range
    if funding_strategy:
        params["funding_strategy"] = funding_strategy
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    return client.request("GET", "/sell/marketing/v1/ad_campaign", params=params)


def get_campaign(campaign_id: str) -> dict:
    """Retrieve the details of a single campaign by campaign ID."""
    client = get_client()
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def get_campaign_by_name(campaign_title: str) -> dict:
    """Retrieve the details of a single campaign by its exact name."""
    client = get_client()
    return client.request("GET", "/sell/marketing/v1/ad_campaign/get_campaign_by_name",
                          params={"campaign_title": campaign_title})


def clone_campaign(campaign_id: str, body: dict) -> dict:
    """Clone a campaign's criterion (campaign must be ENDED and rules-based)."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/clone", json=body)


def delete_campaign(campaign_id: str) -> dict:
    """Delete a campaign (only campaigns that have ended can be deleted)."""
    client = get_client()
    return client.request("DELETE", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def find_campaign_by_ad_reference(reference_id: Optional[str] = None,
                                   reference_type: Optional[str] = None) -> dict:
    """Find a campaign associated with a specific ad reference."""
    client = get_client()
    params = {}
    if reference_id:
        params["reference_id"] = reference_id
    if reference_type:
        params["reference_type"] = reference_type
    return client.request("GET", "/sell/marketing/v1/ad_campaign/find_campaign_by_ad_reference", params=params)


def suggest_budget(marketplace_id: str = "EBAY_US") -> dict:
    """Retrieve the suggested budget for an offsite campaign."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/marketing/v1/ad_campaign/suggest_budget", extra_headers=headers)


# ── Ads ───────────────────────────────────────────────────────────────────────

def get_ads(campaign_id: str, ad_group_ids: Optional[str] = None, ad_status: Optional[str] = None,
            listing_ids: Optional[str] = None, limit: Optional[str] = None,
            offset: Optional[str] = None) -> dict:
    """Retrieve Promoted Listings ads associated with a campaign."""
    client = get_client()
    params = {}
    if ad_group_ids:
        params["ad_group_ids"] = ad_group_ids
    if ad_status:
        params["ad_status"] = ad_status
    if listing_ids:
        params["listing_ids"] = listing_ids
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad", params=params)


def get_ad(campaign_id: str, ad_id: str) -> dict:
    """Retrieve a specific ad from a campaign."""
    client = get_client()
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}")


def create_ad_by_listing_id(campaign_id: str, body: dict) -> dict:
    """Add a listing to an existing Promoted Listings campaign using a listing ID."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad", json=body)


def delete_ad(campaign_id: str, ad_id: str) -> dict:
    """Remove a specific ad from a campaign (CPS funding model only)."""
    client = get_client()
    return client.request("DELETE", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}")


def update_bid(campaign_id: str, ad_id: str, body: dict) -> dict:
    """Update the bid percentage for a specific ad in a campaign (CPS funding model only)."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}/update_bid", json=body)


def bulk_create_ads_by_listing_id(campaign_id: str, body: dict) -> dict:
    """Add multiple listings (up to 500) to an existing Promoted Listings campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id", json=body)


def bulk_create_ads_by_inventory_reference(campaign_id: str, body: dict) -> dict:
    """Add multiple listings to a campaign using inventory reference IDs."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference", json=body)


def bulk_delete_ads_by_listing_id(campaign_id: str, body: dict) -> dict:
    """Delete multiple ads from a campaign using listing IDs."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads_by_listing_id", json=body)


def bulk_delete_ads_by_inventory_reference(campaign_id: str, body: dict) -> dict:
    """Delete multiple ads from a campaign using inventory reference IDs."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads_by_inventory_reference", json=body)


def bulk_update_ads_bid_by_listing_id(campaign_id: str, body: dict) -> dict:
    """Update bid percentages for multiple ads using listing IDs (CPS funding model only)."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_listing_id", json=body)


def bulk_update_ads_bid_by_inventory_reference(campaign_id: str, body: dict) -> dict:
    """Update bid percentages for multiple ads using inventory reference IDs."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_inventory_reference", json=body)


def bulk_update_ads_status(campaign_id: str, body: dict) -> dict:
    """Update the status of multiple ads in a campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_status", json=body)


def bulk_update_ads_status_by_listing_id(campaign_id: str, body: dict) -> dict:
    """Update the status of multiple ads using listing IDs."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_status_by_listing_id", json=body)


def create_ads_by_inventory_reference(campaign_id: str, body: dict) -> dict:
    """Add listings to a campaign using inventory reference IDs."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/create_ads_by_inventory_reference", json=body)


def delete_ads_by_inventory_reference(campaign_id: str, body: dict) -> dict:
    """Delete ads from a campaign using inventory reference IDs."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/delete_ads_by_inventory_reference", json=body)


def get_ads_by_inventory_reference(campaign_id: str, inventory_reference_id: Optional[str] = None,
                                    inventory_reference_type: Optional[str] = None) -> dict:
    """Retrieve ads associated with a campaign using inventory reference IDs."""
    client = get_client()
    params = {}
    if inventory_reference_id:
        params["inventory_reference_id"] = inventory_reference_id
    if inventory_reference_type:
        params["inventory_reference_type"] = inventory_reference_type
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}/get_ads_by_inventory_reference", params=params)


# ── Ad Groups ─────────────────────────────────────────────────────────────────

def get_ad_groups(campaign_id: str, ad_group_status: Optional[str] = None,
                  limit: Optional[str] = None, offset: Optional[str] = None) -> dict:
    """Retrieve ad groups for a specified campaign (CPC priority strategy campaigns)."""
    client = get_client()
    params = {}
    if ad_group_status:
        params["ad_group_status"] = ad_group_status
    if limit:
        params["limit"] = limit
    if offset:
        params["offset"] = offset
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group", params=params)


def get_ad_group(campaign_id: str, ad_group_id: str) -> dict:
    """Retrieve a specific ad group from a campaign."""
    client = get_client()
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}")


def create_ad_group(campaign_id: str, body: dict) -> dict:
    """Add an ad group to an existing priority strategy campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group", json=body)


def update_ad_group(campaign_id: str, ad_group_id: str, body: dict) -> dict:
    """Update an existing ad group in a campaign."""
    client = get_client()
    return client.request("PUT", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}", json=body)


def suggest_bids(campaign_id: str, ad_group_id: str, body: dict) -> dict:
    """Retrieve suggested bids for input keywords and match type."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_bids", json=body)


def suggest_keywords(campaign_id: str, ad_group_id: str, body: dict) -> dict:
    """Retrieve suggested keywords for a campaign ad group."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_keywords", json=body)


def update_keyword(campaign_id: str, keyword_id: str, body: dict) -> dict:
    """Update a keyword in a campaign."""
    client = get_client()
    return client.request("PUT", f"/sell/marketing/v1/ad_campaign/{campaign_id}/keyword/{keyword_id}", json=body)


def update_negative_keyword(negative_keyword_id: str, body: dict) -> dict:
    """Update a negative keyword."""
    client = get_client()
    return client.request("PUT", f"/sell/marketing/v1/negative_keyword/{negative_keyword_id}", json=body)
