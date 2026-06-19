"""eBay Sell Marketing API tools."""
from typing import Any, Optional
from .client import get_client


# --- Campaigns ---

def get_campaigns(
    campaign_title: Optional[str] = None,
    campaign_status: Optional[str] = None,
    campaign_targeting_types: Optional[str] = None,
    channels: Optional[str] = None,
    end_date_range: Optional[str] = None,
    start_date_range: Optional[str] = None,
    funding_strategy: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Retrieve details for all of the seller's defined campaigns."""
    client = get_client()
    params = {}
    if campaign_title is not None:
        params["campaign_title"] = campaign_title
    if campaign_status is not None:
        params["campaign_status"] = campaign_status
    if campaign_targeting_types is not None:
        params["campaign_targeting_types"] = campaign_targeting_types
    if channels is not None:
        params["channels"] = channels
    if end_date_range is not None:
        params["end_date_range"] = end_date_range
    if start_date_range is not None:
        params["start_date_range"] = start_date_range
    if funding_strategy is not None:
        params["funding_strategy"] = funding_strategy
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/sell/marketing/v1/ad_campaign", params=params)


def get_campaign(campaign_id: str) -> dict:
    """Retrieve the details of a single campaign by campaign ID."""
    client = get_client()
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def get_campaign_by_name(campaign_name: str) -> dict:
    """Retrieve a campaign by its name."""
    client = get_client()
    return client.request("GET", "/sell/marketing/v1/ad_campaign/get_campaign_by_name", params={"campaign_name": campaign_name})


def delete_campaign(campaign_id: str) -> dict:
    """Delete the specified campaign (only ended campaigns can be deleted)."""
    client = get_client()
    return client.request("DELETE", f"/sell/marketing/v1/ad_campaign/{campaign_id}")


def clone_campaign(campaign_id: str, body: dict) -> dict:
    """Clone a campaign's criterion (campaign must be ENDED and rules-based)."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/clone", json=body)


def find_campaign_by_ad_reference(
    inventory_reference_id: Optional[str] = None,
    inventory_reference_type: Optional[str] = None,
    listing_id: Optional[str] = None,
) -> dict:
    """Find a campaign associated with a specific ad reference."""
    client = get_client()
    params = {}
    if inventory_reference_id is not None:
        params["inventory_reference_id"] = inventory_reference_id
    if inventory_reference_type is not None:
        params["inventory_reference_type"] = inventory_reference_type
    if listing_id is not None:
        params["listing_id"] = listing_id
    return client.request("GET", "/sell/marketing/v1/ad_campaign/find_campaign_by_ad_reference", params=params)


def suggest_budget(marketplace_id: str = "EBAY_US") -> dict:
    """Retrieve the suggested budget for an offsite campaign."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("GET", "/sell/marketing/v1/ad_campaign/suggest_budget", headers=headers)


# --- Ads ---

def get_ads(
    campaign_id: str,
    ad_group_ids: Optional[str] = None,
    ad_status: Optional[str] = None,
    listing_ids: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Retrieve Promoted Listings ads associated with a campaign."""
    client = get_client()
    params = {}
    if ad_group_ids is not None:
        params["ad_group_ids"] = ad_group_ids
    if ad_status is not None:
        params["ad_status"] = ad_status
    if listing_ids is not None:
        params["listing_ids"] = listing_ids
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad", params=params)


def get_ad(campaign_id: str, ad_id: str) -> dict:
    """Retrieve a specific ad from a campaign."""
    client = get_client()
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}")


def create_ad_by_listing_id(campaign_id: str, body: dict) -> dict:
    """Add a listing to an existing Promoted Listings campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad", json=body)


def delete_ad(campaign_id: str, ad_id: str) -> dict:
    """Remove a specific ad from a campaign (CPS funding model only)."""
    client = get_client()
    return client.request("DELETE", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}")


def bulk_create_ads_by_listing_id(campaign_id: str, body: dict) -> dict:
    """Add multiple listings (up to 500) to an existing Promoted Listings campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id", json=body)


def bulk_create_ads_by_inventory_reference(campaign_id: str, body: dict) -> dict:
    """Add multiple ads by inventory reference to an existing campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference", json=body)


def bulk_delete_ads_by_listing_id(campaign_id: str, body: dict) -> dict:
    """Delete multiple ads by listing ID from a campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads_by_listing_id", json=body)


def bulk_delete_ads_by_inventory_reference(campaign_id: str, body: dict) -> dict:
    """Delete multiple ads by inventory reference from a campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_delete_ads_by_inventory_reference", json=body)


def bulk_update_ads_bid_by_listing_id(campaign_id: str, body: dict) -> dict:
    """Update bid percentages for multiple ads by listing ID (CPS only)."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_listing_id", json=body)


def bulk_update_ads_bid_by_inventory_reference(campaign_id: str, body: dict) -> dict:
    """Update bid percentages for multiple ads by inventory reference (CPS only)."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_inventory_reference", json=body)


def bulk_update_ads_status(campaign_id: str, body: dict) -> dict:
    """Update the status of multiple ads in a campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_status", json=body)


def bulk_update_ads_status_by_listing_id(campaign_id: str, body: dict) -> dict:
    """Update the status of multiple ads by listing ID in a campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/bulk_update_ads_status_by_listing_id", json=body)


def update_bid(campaign_id: str, ad_id: str, body: dict) -> dict:
    """Update the bid for a specific ad in a campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad/{ad_id}/update_bid", json=body)


def get_ads_by_inventory_reference(
    campaign_id: str,
    inventory_reference_id: Optional[str] = None,
    inventory_reference_type: Optional[str] = None,
) -> dict:
    """Retrieve ads by inventory reference for a campaign."""
    client = get_client()
    params = {}
    if inventory_reference_id is not None:
        params["inventory_reference_id"] = inventory_reference_id
    if inventory_reference_type is not None:
        params["inventory_reference_type"] = inventory_reference_type
    return client.request("GET", f"/sell/marketing/v1/ad_campaign/{campaign_id}/get_ads_by_inventory_reference", params=params)


def create_ads_by_inventory_reference(campaign_id: str, body: dict) -> dict:
    """Create ads by inventory reference for a campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/create_ads_by_inventory_reference", json=body)


def delete_ads_by_inventory_reference(campaign_id: str, body: dict) -> dict:
    """Delete ads by inventory reference from a campaign."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/delete_ads_by_inventory_reference", json=body)


# --- Ad Groups ---

def get_ad_groups(
    campaign_id: str,
    ad_group_status: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
) -> dict:
    """Retrieve ad groups for a specified campaign."""
    client = get_client()
    params = {}
    if ad_group_status is not None:
        params["ad_group_status"] = ad_group_status
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
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
    """Update an ad group in a campaign."""
    client = get_client()
    return client.request("PUT", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}", json=body)


def suggest_bids(campaign_id: str, ad_group_id: str, body: dict) -> dict:
    """Retrieve suggested bids for input keywords and match type."""
    client = get_client()
    return client.request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_bids", json=body)


def suggest_keywords(campaign_id: str, ad_group_id: str, body: dict) -> dict:
    """Retrieve suggested keywords for an ad group."""
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
