from typing import Any, Optional

from generated_tools.common import client, compact_kwargs, parse_json_body


API_BASE = "/sell/marketing/v1"


def get_campaigns(
    campaign_title: Optional[str] = None,
    campaign_status: Optional[str] = None,
    campaign_targeting_types: Optional[str] = None,
    channels: Optional[str] = None,
    end_date_range: Optional[str] = None,
    funding_strategy: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    start_date_range: Optional[str] = None,
) -> Any:
    try:
        return client.request(API_BASE, "GET", "/ad_campaign", params=compact_kwargs(
            campaign_title=campaign_title,
            campaign_status=campaign_status,
            campaign_targeting_types=campaign_targeting_types,
            channels=channels,
            end_date_range=end_date_range,
            funding_strategy=funding_strategy,
            limit=limit,
            offset=offset,
            start_date_range=start_date_range,
        ))
    except Exception as e:
        return {"error": str(e)}


def get_campaign(campaign_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/ad_campaign/{campaign_id}")
    except Exception as e:
        return {"error": str(e)}


def get_campaign_by_name(campaign_name: str) -> Any:
    try:
        return client.request(API_BASE, "GET", "/ad_campaign/get_campaign_by_name", params={"campaign_name": campaign_name})
    except Exception as e:
        return {"error": str(e)}


def create_campaign(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/ad_campaign", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def update_campaign(campaign_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "PUT", f"/ad_campaign/{campaign_id}", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def delete_campaign(campaign_id: str) -> Any:
    try:
        return client.request(API_BASE, "DELETE", f"/ad_campaign/{campaign_id}")
    except Exception as e:
        return {"error": str(e)}


def clone_campaign(campaign_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/ad_campaign/{campaign_id}/clone", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def create_ad_by_listing_id(campaign_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/ad_campaign/{campaign_id}/ad", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def get_ads(campaign_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/ad_campaign/{campaign_id}/ad", params=compact_kwargs(limit=limit, offset=offset))
    except Exception as e:
        return {"error": str(e)}


def get_ad(campaign_id: str, ad_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/ad_campaign/{campaign_id}/ad/{ad_id}")
    except Exception as e:
        return {"error": str(e)}


def delete_ad(campaign_id: str, ad_id: str) -> Any:
    try:
        return client.request(API_BASE, "DELETE", f"/ad_campaign/{campaign_id}/ad/{ad_id}")
    except Exception as e:
        return {"error": str(e)}


def update_bid(campaign_id: str, ad_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/ad_campaign/{campaign_id}/ad/{ad_id}/update_bid", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def create_ad_group(campaign_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/ad_campaign/{campaign_id}/ad_group", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def get_ad_groups(campaign_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/ad_campaign/{campaign_id}/ad_group", params=compact_kwargs(limit=limit, offset=offset))
    except Exception as e:
        return {"error": str(e)}


def get_ad_group(campaign_id: str, ad_group_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/ad_campaign/{campaign_id}/ad_group/{ad_group_id}")
    except Exception as e:
        return {"error": str(e)}


def update_ad_group(campaign_id: str, ad_group_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "PUT", f"/ad_campaign/{campaign_id}/ad_group/{ad_group_id}", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def suggest_bids(campaign_id: str, ad_group_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_bids", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def suggest_keywords(campaign_id: str, ad_group_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_keywords", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def suggest_budget() -> Any:
    try:
        return client.request(API_BASE, "GET", "/ad_campaign/suggest_budget")
    except Exception as e:
        return {"error": str(e)}
