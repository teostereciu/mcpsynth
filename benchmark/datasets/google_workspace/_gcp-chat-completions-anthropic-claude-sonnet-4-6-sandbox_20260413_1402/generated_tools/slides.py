"""Google Slides API tools for the Google Workspace MCP Server."""

from typing import Any, Optional

import requests

from generated_tools import mcp
from generated_tools.auth import (
    SLIDES_BASE,
    api_get,
    api_post,
    handle_http_error,
)


@mcp.tool()
def slides_create_presentation(title: str) -> dict:
    """Create a new blank Google Slides presentation.

    Args:
        title: The title of the new presentation.
    """
    try:
        return api_post(SLIDES_BASE, payload={"title": title})
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def slides_get_presentation(presentation_id: str) -> dict:
    """Get the content and metadata of a Google Slides presentation.

    Args:
        presentation_id: The ID of the presentation to retrieve.
    """
    try:
        return api_get(f"{SLIDES_BASE}/{presentation_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def slides_batch_update(
    presentation_id: str,
    slide_requests: list,
    required_revision_id: Optional[str] = None,
) -> dict:
    """Apply one or more updates to a Google Slides presentation.

    Common request types:
    - createSlide: {'createSlide': {'insertionIndex': 1, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}}
    - deleteObject: {'deleteObject': {'objectId': 'slide_id'}}
    - insertText: {'insertText': {'objectId': 'shape_id', 'insertionIndex': 0, 'text': 'Hello!'}}
    - replaceAllText: {'replaceAllText': {'containsText': {'text': '{{name}}'}, 'replaceText': 'Alice'}}
    - createShape: {'createShape': {'objectId': 'my_shape', 'shapeType': 'TEXT_BOX', 'elementProperties': {'pageObjectId': 'slide_id', 'size': {'width': {'magnitude': 3000000, 'unit': 'EMU'}, 'height': {'magnitude': 3000000, 'unit': 'EMU'}}, 'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': 350000, 'translateY': 1700000, 'unit': 'EMU'}}}}
    - updateSlidesPosition: {'updateSlidesPosition': {'slideObjectIds': ['slide_id'], 'insertionIndex': 0}}
    - duplicateObject: {'duplicateObject': {'objectId': 'slide_id'}}

    Args:
        presentation_id: The ID of the presentation to update.
        slide_requests: List of request objects to apply to the presentation.
        required_revision_id: If set, the request fails if this is not the current revision.
    """
    try:
        payload: dict[str, Any] = {"requests": slide_requests}
        if required_revision_id:
            payload["writeControl"] = {"requiredRevisionId": required_revision_id}
        return api_post(f"{SLIDES_BASE}/{presentation_id}:batchUpdate", payload=payload)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def slides_get_page(presentation_id: str, page_object_id: str) -> dict:
    """Get a specific slide (page) from a Google Slides presentation.

    Args:
        presentation_id: The ID of the presentation.
        page_object_id: The object ID of the slide/page to retrieve.
    """
    try:
        return api_get(f"{SLIDES_BASE}/{presentation_id}/pages/{page_object_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def slides_get_page_thumbnail(
    presentation_id: str,
    page_object_id: str,
    mime_type: str = "PNG",
    thumbnail_size: str = "MEDIUM",
) -> dict:
    """Get a thumbnail image URL for a specific slide.

    Args:
        presentation_id: The ID of the presentation.
        page_object_id: The object ID of the slide/page.
        mime_type: Thumbnail MIME type: 'PNG' (default).
        thumbnail_size: Thumbnail size: 'SMALL' (200px), 'MEDIUM' (800px), or 'LARGE' (1600px).
    """
    try:
        params: dict[str, Any] = {
            "thumbnailProperties.mimeType": mime_type,
            "thumbnailProperties.thumbnailSize": thumbnail_size,
        }
        return api_get(
            f"{SLIDES_BASE}/{presentation_id}/pages/{page_object_id}/thumbnail",
            params=params,
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def slides_add_slide(
    presentation_id: str,
    insertion_index: Optional[int] = None,
    predefined_layout: str = "BLANK",
    slide_object_id: Optional[str] = None,
) -> dict:
    """Add a new slide to a Google Slides presentation.

    Args:
        presentation_id: The ID of the presentation.
        insertion_index: Zero-based index where the slide will be inserted.
            If omitted, the slide is appended at the end.
        predefined_layout: Layout for the new slide. Options: 'BLANK', 'CAPTION_ONLY',
            'TITLE', 'TITLE_AND_BODY', 'TITLE_AND_TWO_COLUMNS', 'TITLE_ONLY',
            'SECTION_HEADER', 'SECTION_TITLE_AND_DESCRIPTION', 'ONE_COLUMN_TEXT',
            'MAIN_POINT', 'BIG_NUMBER'.
        slide_object_id: Optional custom object ID for the new slide.
    """
    try:
        create_slide: dict[str, Any] = {
            "slideLayoutReference": {"predefinedLayout": predefined_layout}
        }
        if insertion_index is not None:
            create_slide["insertionIndex"] = insertion_index
        if slide_object_id:
            create_slide["objectId"] = slide_object_id

        return api_post(
            f"{SLIDES_BASE}/{presentation_id}:batchUpdate",
            payload={"requests": [{"createSlide": create_slide}]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def slides_insert_text(
    presentation_id: str,
    object_id: str,
    text: str,
    insertion_index: int = 0,
) -> dict:
    """Insert text into a shape or table cell in a Google Slides presentation.

    Args:
        presentation_id: The ID of the presentation.
        object_id: The object ID of the shape or table cell to insert text into.
        text: The text to insert.
        insertion_index: The index in the text where the text will be inserted (default 0).
    """
    try:
        request = {
            "insertText": {
                "objectId": object_id,
                "insertionIndex": insertion_index,
                "text": text,
            }
        }
        return api_post(
            f"{SLIDES_BASE}/{presentation_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def slides_replace_all_text(
    presentation_id: str,
    find_text: str,
    replace_text: str,
    match_case: bool = False,
) -> dict:
    """Replace all occurrences of text in a Google Slides presentation.

    Args:
        presentation_id: The ID of the presentation.
        find_text: The text to find and replace.
        replace_text: The replacement text.
        match_case: Whether the search is case-sensitive.
    """
    try:
        request = {
            "replaceAllText": {
                "containsText": {"text": find_text, "matchCase": match_case},
                "replaceText": replace_text,
            }
        }
        return api_post(
            f"{SLIDES_BASE}/{presentation_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def slides_delete_object(presentation_id: str, object_id: str) -> dict:
    """Delete an object (slide, shape, image, etc.) from a Google Slides presentation.

    Args:
        presentation_id: The ID of the presentation.
        object_id: The object ID of the element to delete.
    """
    try:
        request = {"deleteObject": {"objectId": object_id}}
        return api_post(
            f"{SLIDES_BASE}/{presentation_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def slides_duplicate_object(
    presentation_id: str,
    object_id: str,
    object_id_mappings: Optional[dict] = None,
) -> dict:
    """Duplicate a slide or page element in a Google Slides presentation.

    Args:
        presentation_id: The ID of the presentation.
        object_id: The object ID of the element to duplicate.
        object_id_mappings: Optional mapping of old object IDs to new object IDs for the duplicate.
    """
    try:
        duplicate_request: dict[str, Any] = {"objectId": object_id}
        if object_id_mappings:
            duplicate_request["objectIds"] = object_id_mappings
        request = {"duplicateObject": duplicate_request}
        return api_post(
            f"{SLIDES_BASE}/{presentation_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)
