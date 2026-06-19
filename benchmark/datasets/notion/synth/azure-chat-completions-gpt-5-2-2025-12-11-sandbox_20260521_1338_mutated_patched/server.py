from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.pages import (
    pages_create,
    pages_retrieve,
    pages_update,
    pages_retrieve_property_item,
    pages_move,
)
from generated_tools.databases import (
    databases_create,
    databases_retrieve,
    databases_update,
    databases_query,
)
from generated_tools.data_sources import (
    data_sources_create,
    data_sources_retrieve,
    data_sources_update,
    data_sources_query,
)
from generated_tools.blocks import (
    blocks_retrieve,
    blocks_children_list,
    blocks_children_append,
    blocks_update,
    blocks_delete,
)
from generated_tools.comments import (
    comments_create,
    comments_retrieve,
    comments_list,
)
from generated_tools.users import (
    users_list,
    users_retrieve,
    users_me,
)
from generated_tools.search import search
from generated_tools.file_uploads import (
    file_uploads_create,
    file_uploads_send,
    file_uploads_complete,
    file_uploads_retrieve,
    file_uploads_list,
)


mcp = FastMCP("notion")


@mcp.tool()
def notion_pages_create(parent: Dict[str, Any], properties: Dict[str, Any], children: Optional[list[Dict[str, Any]]] = None,
                       content_markdown: Optional[str] = None, icon: Optional[Dict[str, Any]] = None,
                       cover: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return pages_create(parent, properties, children=children, content_markdown=content_markdown, icon=icon, cover=cover)


@mcp.tool()
def notion_pages_retrieve(page_id: str, filter_properties: Optional[list[str]] = None) -> Dict[str, Any]:
    return pages_retrieve(page_id, filter_properties=filter_properties)


@mcp.tool()
def notion_pages_update(page_id: str, properties: Optional[Dict[str, Any]] = None, icon: Optional[Dict[str, Any]] = None,
                       cover: Optional[Dict[str, Any]] = None, in_trash: Optional[bool] = None,
                       is_locked: Optional[bool] = None, erase_content: Optional[bool] = None,
                       children: Optional[list[Dict[str, Any]]] = None, content_markdown: Optional[str] = None,
                       template: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return pages_update(
        page_id,
        properties=properties,
        icon=icon,
        cover=cover,
        in_trash=in_trash,
        is_locked=is_locked,
        erase_content=erase_content,
        children=children,
        content_markdown=content_markdown,
        template=template,
    )


@mcp.tool()
def notion_pages_retrieve_property_item(page_id: str, property_id: str, page_cursor: Optional[str] = None,
                                       results_per_page: Optional[int] = None) -> Dict[str, Any]:
    return pages_retrieve_property_item(page_id, property_id, page_cursor=page_cursor, results_per_page=results_per_page)


@mcp.tool()
def notion_pages_move(page_id: str, parent: Dict[str, Any]) -> Dict[str, Any]:
    return pages_move(page_id, parent)


@mcp.tool()
def notion_databases_create(parent: Dict[str, Any], title: Any, description: Optional[Any] = None,
                           is_inline: Optional[bool] = None, data_source: Optional[Dict[str, Any]] = None,
                           icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return databases_create(parent, title, description=description, is_inline=is_inline, data_source=data_source, icon=icon, cover=cover)


@mcp.tool()
def notion_databases_retrieve(database_id: str) -> Dict[str, Any]:
    return databases_retrieve(database_id)


@mcp.tool()
def notion_databases_update(database_id: str, parent: Optional[Dict[str, Any]] = None, title: Optional[Any] = None,
                           description: Optional[Any] = None, is_inline: Optional[bool] = None,
                           icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None,
                           in_trash: Optional[bool] = None, is_locked: Optional[bool] = None) -> Dict[str, Any]:
    return databases_update(
        database_id,
        parent=parent,
        title=title,
        description=description,
        is_inline=is_inline,
        icon=icon,
        cover=cover,
        in_trash=in_trash,
        is_locked=is_locked,
    )


@mcp.tool()
def notion_databases_query(database_id: str, query_filter: Optional[Dict[str, Any]] = None,
                          sorts: Optional[list[Dict[str, Any]]] = None,
                          start_cursor: Optional[str] = None, page_size: Optional[int] = None,
                          filter_properties: Optional[list[str]] = None) -> Dict[str, Any]:
    return databases_query(
        database_id,
        query_filter=query_filter,
        sorts=sorts,
        start_cursor=start_cursor,
        page_size=page_size,
        filter_properties=filter_properties,
    )


@mcp.tool()
def notion_data_sources_create(parent: Dict[str, Any], title: Any, properties: Dict[str, Any]) -> Dict[str, Any]:
    return data_sources_create(parent, title, properties)


@mcp.tool()
def notion_data_sources_retrieve(data_source_id: str) -> Dict[str, Any]:
    return data_sources_retrieve(data_source_id)


@mcp.tool()
def notion_data_sources_update(data_source_id: str, title: Optional[Any] = None, properties: Optional[Dict[str, Any]] = None,
                              in_trash: Optional[bool] = None, parent: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return data_sources_update(data_source_id, title=title, properties=properties, in_trash=in_trash, parent=parent)


@mcp.tool()
def notion_data_sources_query(data_source_id: str, query_filter: Optional[Dict[str, Any]] = None,
                             sort_rules: Optional[list[Dict[str, Any]]] = None,
                             page_cursor: Optional[str] = None, results_per_page: Optional[int] = None,
                             filter_properties: Optional[list[str]] = None,
                             result_type_filter: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return data_sources_query(
        data_source_id,
        query_filter=query_filter,
        sort_rules=sort_rules,
        page_cursor=page_cursor,
        results_per_page=results_per_page,
        filter_properties=filter_properties,
        result_type_filter=result_type_filter,
    )


@mcp.tool()
def notion_blocks_retrieve(block_id: str) -> Dict[str, Any]:
    return blocks_retrieve(block_id)


@mcp.tool()
def notion_blocks_children_list(block_id: str, page_cursor: Optional[str] = None,
                               results_per_page: Optional[int] = None) -> Dict[str, Any]:
    return blocks_children_list(block_id, page_cursor=page_cursor, results_per_page=results_per_page)


@mcp.tool()
def notion_blocks_children_append(block_id: str, children: list[Dict[str, Any]], position: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return blocks_children_append(block_id, children, position=position)


@mcp.tool()
def notion_blocks_update(block_id: str, block: Dict[str, Any]) -> Dict[str, Any]:
    return blocks_update(block_id, block)


@mcp.tool()
def notion_blocks_delete(block_id: str) -> Dict[str, Any]:
    return blocks_delete(block_id)


@mcp.tool()
def notion_comments_create(parent: Dict[str, Any], rich_text: list[Dict[str, Any]],
                          attachments: Optional[list[Dict[str, Any]]] = None,
                          display_name: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return comments_create(parent, rich_text, attachments=attachments, display_name=display_name)


@mcp.tool()
def notion_comments_retrieve(comment_id: str) -> Dict[str, Any]:
    return comments_retrieve(comment_id)


@mcp.tool()
def notion_comments_list(block_id: Optional[str] = None, page_id: Optional[str] = None,
                        page_cursor: Optional[str] = None, results_per_page: Optional[int] = None) -> Dict[str, Any]:
    return comments_list(block_id=block_id, page_id=page_id, page_cursor=page_cursor, results_per_page=results_per_page)


@mcp.tool()
def notion_users_list(page_cursor: Optional[str] = None, results_per_page: Optional[int] = None) -> Dict[str, Any]:
    return users_list(page_cursor=page_cursor, results_per_page=results_per_page)


@mcp.tool()
def notion_users_retrieve(user_id: str) -> Dict[str, Any]:
    return users_retrieve(user_id)


@mcp.tool()
def notion_users_me() -> Dict[str, Any]:
    return users_me()


@mcp.tool()
def notion_search(query: Optional[str] = None, query_filter: Optional[Dict[str, Any]] = None,
                 sort: Optional[Dict[str, Any]] = None, page_cursor: Optional[str] = None,
                 results_per_page: Optional[int] = None) -> Dict[str, Any]:
    return search(query, query_filter=query_filter, sort=sort, page_cursor=page_cursor, results_per_page=results_per_page)


@mcp.tool()
def notion_file_uploads_create(mode: Optional[str] = None, filename: Optional[str] = None,
                              content_type: Optional[str] = None, number_of_parts: Optional[int] = None,
                              external_url: Optional[str] = None) -> Dict[str, Any]:
    return file_uploads_create(mode=mode, filename=filename, content_type=content_type, number_of_parts=number_of_parts, external_url=external_url)


@mcp.tool()
def notion_file_uploads_send(file_upload_id: str, file_path: Optional[str] = None, data: Optional[bytes] = None,
                            filename: Optional[str] = None, content_type: Optional[str] = None,
                            part_number: Optional[int] = None) -> Dict[str, Any]:
    return file_uploads_send(
        file_upload_id,
        file_path=file_path,
        data=data,
        filename=filename,
        content_type=content_type,
        part_number=part_number,
    )


@mcp.tool()
def notion_file_uploads_complete(file_upload_id: str) -> Dict[str, Any]:
    return file_uploads_complete(file_upload_id)


@mcp.tool()
def notion_file_uploads_retrieve(file_upload_id: str) -> Dict[str, Any]:
    return file_uploads_retrieve(file_upload_id)


@mcp.tool()
def notion_file_uploads_list(status: Optional[str] = None, page_cursor: Optional[str] = None,
                            results_per_page: Optional[int] = None) -> Dict[str, Any]:
    return file_uploads_list(status=status, page_cursor=page_cursor, results_per_page=results_per_page)


if __name__ == "__main__":
    mcp.run()
