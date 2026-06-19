"""Tools for eBay Commerce Notification API (webhooks)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import EbayApiError, error_dict, get_api_base_url, request_json


# Notification API generally uses application token per docs; some operations may require user.


def get_config() -> Dict[str, Any]:
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path="/commerce/notification/v1/configuration",
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def update_config(payload: Dict[str, Any]) -> Dict[str, Any]:
    try:
        return request_json(
            method="PUT",
            base_url=get_api_base_url(),
            path="/commerce/notification/v1/configuration",
            json_body=payload,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_public_key() -> Dict[str, Any]:
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path="/commerce/notification/v1/public_key/",
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


# Destinations

def create_destination(payload: Dict[str, Any]) -> Dict[str, Any]:
    try:
        return request_json(
            method="POST",
            base_url=get_api_base_url(),
            path="/commerce/notification/v1/destination",
            json_body=payload,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_destinations(limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    try:
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if continuation_token is not None:
            params["continuation_token"] = continuation_token
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path="/commerce/notification/v1/destination",
            params=params or None,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_destination(destination_id: str) -> Dict[str, Any]:
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/destination/{destination_id}",
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def update_destination(destination_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    try:
        return request_json(
            method="PUT",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/destination/{destination_id}",
            json_body=payload,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def delete_destination(destination_id: str) -> Dict[str, Any]:
    try:
        return request_json(
            method="DELETE",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/destination/{destination_id}",
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


# Topics

def get_topics(limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    try:
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if continuation_token is not None:
            params["continuation_token"] = continuation_token
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path="/commerce/notification/v1/topic",
            params=params or None,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_topic(topic_id: str) -> Dict[str, Any]:
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/topic/{topic_id}",
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


# Subscriptions

def create_subscription(payload: Dict[str, Any]) -> Dict[str, Any]:
    try:
        return request_json(
            method="POST",
            base_url=get_api_base_url(),
            path="/commerce/notification/v1/subscription",
            json_body=payload,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_subscriptions(limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    try:
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if continuation_token is not None:
            params["continuation_token"] = continuation_token
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path="/commerce/notification/v1/subscription",
            params=params or None,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_subscription(subscription_id: str) -> Dict[str, Any]:
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/subscription/{subscription_id}",
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def update_subscription(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    try:
        return request_json(
            method="PUT",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/subscription/{subscription_id}",
            json_body=payload,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    try:
        return request_json(
            method="DELETE",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/subscription/{subscription_id}",
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def enable_subscription(subscription_id: str) -> Dict[str, Any]:
    try:
        return request_json(
            method="POST",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/subscription/{subscription_id}/enable",
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def disable_subscription(subscription_id: str) -> Dict[str, Any]:
    try:
        return request_json(
            method="POST",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/subscription/{subscription_id}/disable",
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def test_subscription(subscription_id: str) -> Dict[str, Any]:
    try:
        return request_json(
            method="POST",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/subscription/{subscription_id}/test",
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def test(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Send a test notification."""
    try:
        return request_json(
            method="POST",
            base_url=get_api_base_url(),
            path="/commerce/notification/v1/test",
            json_body=payload,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


# Subscription filters

def create_subscription_filter(subscription_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    try:
        return request_json(
            method="POST",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/subscription/{subscription_id}/filter",
            json_body=payload,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_subscription_filter(subscription_id: str) -> Dict[str, Any]:
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/subscription/{subscription_id}/filter",
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def delete_subscription_filter(subscription_id: str) -> Dict[str, Any]:
    try:
        return request_json(
            method="DELETE",
            base_url=get_api_base_url(),
            path=f"/commerce/notification/v1/subscription/{subscription_id}/filter",
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)
