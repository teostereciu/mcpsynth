"""Google Docs API tools for the Google Workspace MCP Server."""

from typing import Any, Optional

import requests

from generated_tools import mcp
from generated_tools.auth import (
    DOCS_BASE,
    api_get,
    api_post,
    handle_http_error,
)


@mcp.tool()
def docs_create_document(title: str) -> dict:
    """Create a new blank Google Document.

    Args:
        title: The title of the new document.
    """
    try:
        return api_post(DOCS_BASE, payload={"title": title})
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def docs_get_document(
    document_id: str,
    suggestions_view_mode: Optional[str] = None,
    include_tabs_content: bool = False,
) -> dict:
    """Get the content and metadata of a Google Document.

    Args:
        document_id: The ID of the document to retrieve.
        suggestions_view_mode: How to view suggestions: 'DEFAULT_FOR_CURRENT_ACCESS',
            'SUGGESTIONS_INLINE', 'PREVIEW_SUGGESTIONS_ACCEPTED', or 'PREVIEW_WITHOUT_SUGGESTIONS'.
        include_tabs_content: Whether to populate Document.tabs instead of legacy body fields.
    """
    try:
        params: dict[str, Any] = {"includeTabsContent": include_tabs_content}
        if suggestions_view_mode:
            params["suggestionsViewMode"] = suggestions_view_mode
        return api_get(f"{DOCS_BASE}/{document_id}", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def docs_batch_update(
    document_id: str,
    doc_requests: list,
    required_revision_id: Optional[str] = None,
    target_revision_id: Optional[str] = None,
) -> dict:
    """Apply one or more updates to a Google Document.

    Common request types:
    - insertText: {'insertText': {'location': {'index': 1}, 'text': 'Hello!'}}
    - replaceAllText: {'replaceAllText': {'containsText': {'text': 'old'}, 'replaceText': 'new'}}
    - deleteContentRange: {'deleteContentRange': {'range': {'startIndex': 1, 'endIndex': 5}}}
    - updateTextStyle: {'updateTextStyle': {'range': {'startIndex': 1, 'endIndex': 5}, 'textStyle': {'bold': True}, 'fields': 'bold'}}
    - insertTable: {'insertTable': {'rows': 3, 'columns': 3, 'location': {'index': 1}}}
    - createHeader: {'createHeader': {'type': 'DEFAULT'}}
    - insertPageBreak: {'insertPageBreak': {'location': {'index': 1}}}

    Args:
        document_id: The ID of the document to update.
        doc_requests: List of request objects to apply to the document.
        required_revision_id: If set, the request fails if this is not the current revision.
        target_revision_id: Apply changes against this revision (collaborative editing).
    """
    try:
        payload: dict[str, Any] = {"requests": doc_requests}
        if required_revision_id or target_revision_id:
            write_control: dict[str, str] = {}
            if required_revision_id:
                write_control["requiredRevisionId"] = required_revision_id
            if target_revision_id:
                write_control["targetRevisionId"] = target_revision_id
            payload["writeControl"] = write_control
        return api_post(f"{DOCS_BASE}/{document_id}:batchUpdate", payload=payload)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def docs_insert_text(
    document_id: str,
    text: str,
    index: int = 1,
    segment_id: Optional[str] = None,
) -> dict:
    """Insert text into a Google Document at a specific index.

    Index 1 is the beginning of the document body. Use docs_get_document to
    find the end index of the document for appending.

    Args:
        document_id: The ID of the document.
        text: The text to insert.
        index: The zero-based index in the document where text will be inserted (default 1).
        segment_id: The ID of the header, footer, or footnote segment (omit for body).
    """
    try:
        location: dict[str, Any] = {"index": index}
        if segment_id:
            location["segmentId"] = segment_id
        request = {"insertText": {"location": location, "text": text}}
        return api_post(
            f"{DOCS_BASE}/{document_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def docs_replace_all_text(
    document_id: str,
    find_text: str,
    replace_text: str,
    match_case: bool = False,
) -> dict:
    """Replace all occurrences of text in a Google Document.

    Args:
        document_id: The ID of the document.
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
            f"{DOCS_BASE}/{document_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def docs_delete_content_range(
    document_id: str,
    start_index: int,
    end_index: int,
    segment_id: Optional[str] = None,
) -> dict:
    """Delete a range of content from a Google Document.

    Args:
        document_id: The ID of the document.
        start_index: The start index of the range to delete (inclusive).
        end_index: The end index of the range to delete (exclusive).
        segment_id: The ID of the header, footer, or footnote segment (omit for body).
    """
    try:
        range_obj: dict[str, Any] = {
            "startIndex": start_index,
            "endIndex": end_index,
        }
        if segment_id:
            range_obj["segmentId"] = segment_id
        request = {"deleteContentRange": {"range": range_obj}}
        return api_post(
            f"{DOCS_BASE}/{document_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def docs_update_text_style(
    document_id: str,
    start_index: int,
    end_index: int,
    bold: Optional[bool] = None,
    italic: Optional[bool] = None,
    underline: Optional[bool] = None,
    strikethrough: Optional[bool] = None,
    font_size_pt: Optional[float] = None,
    foreground_color_hex: Optional[str] = None,
    segment_id: Optional[str] = None,
) -> dict:
    """Update the text style for a range in a Google Document.

    Args:
        document_id: The ID of the document.
        start_index: The start index of the range.
        end_index: The end index of the range.
        bold: Whether the text is bold.
        italic: Whether the text is italic.
        underline: Whether the text is underlined.
        strikethrough: Whether the text has strikethrough.
        font_size_pt: Font size in points.
        foreground_color_hex: Hex color string for text color (e.g. '#FF0000').
        segment_id: The ID of the header, footer, or footnote segment.
    """
    try:
        text_style: dict[str, Any] = {}
        fields_list = []

        if bold is not None:
            text_style["bold"] = bold
            fields_list.append("bold")
        if italic is not None:
            text_style["italic"] = italic
            fields_list.append("italic")
        if underline is not None:
            text_style["underline"] = underline
            fields_list.append("underline")
        if strikethrough is not None:
            text_style["strikethrough"] = strikethrough
            fields_list.append("strikethrough")
        if font_size_pt is not None:
            text_style["fontSize"] = {"magnitude": font_size_pt, "unit": "PT"}
            fields_list.append("fontSize")
        if foreground_color_hex is not None:
            hex_color = foreground_color_hex.lstrip("#")
            r = int(hex_color[0:2], 16) / 255.0
            g = int(hex_color[2:4], 16) / 255.0
            b = int(hex_color[4:6], 16) / 255.0
            text_style["foregroundColor"] = {"color": {"rgbColor": {"red": r, "green": g, "blue": b}}}
            fields_list.append("foregroundColor")

        range_obj: dict[str, Any] = {"startIndex": start_index, "endIndex": end_index}
        if segment_id:
            range_obj["segmentId"] = segment_id

        request = {
            "updateTextStyle": {
                "range": range_obj,
                "textStyle": text_style,
                "fields": ",".join(fields_list) if fields_list else "*",
            }
        }
        return api_post(
            f"{DOCS_BASE}/{document_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def docs_insert_table(
    document_id: str,
    rows: int,
    columns: int,
    index: int = 1,
) -> dict:
    """Insert a table into a Google Document.

    Args:
        document_id: The ID of the document.
        rows: Number of rows in the table.
        columns: Number of columns in the table.
        index: The index in the document where the table will be inserted.
    """
    try:
        request = {
            "insertTable": {
                "rows": rows,
                "columns": columns,
                "location": {"index": index},
            }
        }
        return api_post(
            f"{DOCS_BASE}/{document_id}:batchUpdate",
            payload={"requests": [request]},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)
