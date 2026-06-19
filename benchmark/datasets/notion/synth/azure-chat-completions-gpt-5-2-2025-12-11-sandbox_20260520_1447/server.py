from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools.pages import (
    pages_archive,
    pages_create,
    pages_move,
    pages_restore,
    pages_retrieve,
    pages_retrieve_property_item,
    pages_update,
)
from generated_tools.databases import (
    databases_create,
    databases_list,
    databases_query,
    databases_retrieve,
    databases_update,
)
from generated_tools.blocks import (
    blocks_children_append,
    blocks_children_list,
    blocks_delete,
    blocks_retrieve,
    blocks_update,
)
from generated_tools.comments import comments_create, comments_list, comments_retrieve
from generated_tools.users import users_list, users_me, users_retrieve
from generated_tools.search import search
from generated_tools.data_sources import (
    data_sources_create,
    data_sources_list_templates,
    data_sources_query,
    data_sources_retrieve,
    data_sources_update,
)
from generated_tools.file_uploads import (
    file_uploads_complete,
    file_uploads_create,
    file_uploads_list,
    file_uploads_retrieve,
    file_uploads_send,
)


mcp = FastMCP("notion")


@mcp.tool()
def pages_get(page_id: str, filter_properties: Any = None) -> Dict[str, Any]:
    return pages_retrieve(page_id, filter_properties=filter_properties)


@mcp.tool()
def pages_create_tool(
    parent: Dict[str, Any],
    properties: Dict[str, Any],
    children: Any = None,
    content_markdown: str | None = None,
    icon: Dict[str, Any] | None = None,
    cover: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    return pages_create(parent, properties, children=children, content_markdown=content_markdown, icon=icon, cover=cover)


@mcp.tool()
def pages_update_tool(
    page_id: str,
    properties: Dict[str, Any] | None = None,
    icon: Dict[str, Any] | None = None,
    cover: Dict[str, Any] | None = None,
    in_trash: bool | None = None,
    archived: bool | None = None,
    locked: bool | None = None,
    erase_content: bool | None = None,
    children: Any = None,
    content_markdown: str | None = None,
    template: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    return pages_update(
        page_id,
        properties=properties,
        icon=icon,
        cover=cover,
        in_trash=in_trash,
        archived=archived,
        locked=locked,
        erase_content=erase_content,
        children=children,
        content_markdown=content_markdown,
        template=template,
    )


@mcp.tool()
def pages_trash(page_id: str) -> Dict[str, Any]:
    return pages_archive(page_id)


@mcp.tool()
def pages_restore_tool(page_id: str) -> Dict[str, Any]:
    return pages_restore(page_id)


@mcp.tool()
def pages_move_tool(page_id: str, parent: Dict[str, Any]) -> Dict[str, Any]:
    return pages_move(page_id, parent)


@mcp.tool()
def pages_get_property_item(
    page_id: str,
    property_id: str,
    start_cursor: str | None = None,
    page_size: int | None = None,
) -> Dict[str, Any]:
    return pages_retrieve_property_item(page_id, property_id, start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def databases_create_tool(
    parent: Dict[str, Any],
    title: Any,
    description: Any = None,
    is_inline: bool | None = None,
    data_sources: Any = None,
    icon: Dict[str, Any] | None = None,
    cover: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    return databases_create(
        parent,
        title,
        description=description,
        is_inline=is_inline,
        data_sources=data_sources,
        icon=icon,
        cover=cover,
    )


@mcp.tool()
def databases_get(database_id: str) -> Dict[str, Any]:
    return databases_retrieve(database_id)


@mcp.tool()
def databases_list_tool(start_cursor: str | None = None, page_size: int | None = None) -> Dict[str, Any]:
    return databases_list(start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def databases_update_tool(
    database_id: str,
    parent: Dict[str, Any] | None = None,
    title: Any = None,
    description: Any = None,
    is_inline: bool | None = None,
    icon: Dict[str, Any] | None = None,
    cover: Dict[str, Any] | None = None,
    in_trash: bool | None = None,
    locked: bool | None = None,
) -> Dict[str, Any]:
    return databases_update(
        database_id,
        parent=parent,
        title=title,
        description=description,
        is_inline=is_inline,
        icon=icon,
        cover=cover,
        in_trash=in_trash,
        locked=locked,
    )


@mcp.tool()
def databases_query_tool(
    database_id: str,
    filter: Dict[str, Any] | None = None,
    sorts: Any = None,
    start_cursor: str | None = None,
    page_size: int | None = None,
    filter_properties: Any = None,
) -> Dict[str, Any]:
    return databases_query(
        database_id,
        filter=filter,
        sorts=sorts,
        start_cursor=start_cursor,
        page_size=page_size,
        filter_properties=filter_properties,
    )


@mcp.tool()
def blocks_get(block_id: str) -> Dict[str, Any]:
    return blocks_retrieve(block_id)


@mcp.tool()
def blocks_children_list_tool(block_id: str, start_cursor: str | None = None, page_size: int | None = None) -> Dict[str, Any]:
    return blocks_children_list(block_id, start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def blocks_children_append_tool(block_id: str, children: Any, position: Dict[str, Any] | None = None) -> Dict[str, Any]:
    return blocks_children_append(block_id, children, position=position)


@mcp.tool()
def blocks_update_tool(block_id: str, **block_fields: Any) -> Dict[str, Any]:
    return blocks_update(block_id, **block_fields)


@mcp.tool()
def blocks_delete_tool(block_id: str) -> Dict[str, Any]:
    return blocks_delete(block_id)


@mcp.tool()
def comments_create_tool(parent: Dict[str, Any], rich_text: Any, attachments: Any = None, display_name: Any = None) -> Dict[str, Any]:
    return comments_create(parent, rich_text, attachments=attachments, display_name=display_name)


@mcp.tool()
def comments_list_tool(block_id: str | None = None, start_cursor: str | None = None, page_size: int | None = None) -> Dict[str, Any]:
    return comments_list(block_id=block_id, start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def comments_get(comment_id: str) -> Dict[str, Any]:
    return comments_retrieve(comment_id)


@mcp.tool()
def users_me_tool() -> Dict[str, Any]:
    return users_me()


@mcp.tool()
def users_list_tool(start_cursor: str | None = None, page_size: int | None = None) -> Dict[str, Any]:
    return users_list(start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def users_get(user_id: str) -> Dict[str, Any]:
    return users_retrieve(user_id)


@mcp.tool()
def search_tool(
    query: str | None = None,
    filter: Dict[str, Any] | None = None,
    sort: Dict[str, Any] | None = None,
    start_cursor: str | None = None,
    page_size: int | None = None,
) -> Dict[str, Any]:
    return search(query=query, filter=filter, sort=sort, start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def data_sources_create_tool(parent: Dict[str, Any], title: Any, properties: Dict[str, Any]) -> Dict[str, Any]:
    return data_sources_create(parent, title, properties)


@mcp.tool()
def data_sources_get(data_source_id: str) -> Dict[str, Any]:
    return data_sources_retrieve(data_source_id)


@mcp.tool()
def data_sources_update_tool(
    data_source_id: str,
    title: Any = None,
    properties: Dict[str, Any] | None = None,
    in_trash: bool | None = None,
    parent: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    return data_sources_update(data_source_id, title=title, properties=properties, in_trash=in_trash, parent=parent)


@mcp.tool()
def data_sources_query_tool(
    data_source_id: str,
    filter: Dict[str, Any] | None = None,
    sorts: Any = None,
    start_cursor: str | None = None,
    page_size: int | None = None,
    filter_properties: Any = None,
    result_type: str | None = None,
) -> Dict[str, Any]:
    return data_sources_query(
        data_source_id,
        filter=filter,
        sorts=sorts,
        start_cursor=start_cursor,
        page_size=page_size,
        filter_properties=filter_properties,
        result_type=result_type,
    )


@mcp.tool()
def data_sources_list_templates_tool(
    data_source_id: str,
    name: str | None = None,
    start_cursor: str | None = None,
    page_size: int | None = None,
) -> Dict[str, Any]:
    return data_sources_list_templates(data_source_id, name=name, start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def file_uploads_create_tool(
    mode: str | None = None,
    filename: str | None = None,
    content_type: str | None = None,
    number_of_parts: int | None = None,
    external_url: str | None = None,
) -> Dict[str, Any]:
    return file_uploads_create(
        mode=mode,
        filename=filename,
        content_type=content_type,
        number_of_parts=number_of_parts,
        external_url=external_url,
    )


@mcp.tool()
def file_uploads_send_tool(
    file_upload_id: str,
    file_path: str | None = None,
    file_bytes_b64: str | None = None,
    part_number: int | None = None,
    content_type: str | None = None,
    filename: str | None = None,
) -> Dict[str, Any]:
    return file_uploads_send(
        file_upload_id,
        file_path=file_path,
        file_bytes_b64=file_bytes_b64,
        part_number=part_number,
        content_type=content_type,
        filename=filename,
    )


@mcp.tool()
def file_uploads_complete_tool(file_upload_id: str) -> Dict[str, Any]:
    return file_uploads_complete(file_upload_id)


@mcp.tool()
def file_uploads_get(file_upload_id: str) -> Dict[str, Any]:
    return file_uploads_retrieve(file_upload_id)


@mcp.tool()
def file_uploads_list_tool(status: str | None = None, start_cursor: str | None = None, page_size: int | None = None) -> Dict[str, Any]:
    return file_uploads_list(status=status, start_cursor=start_cursor, page_size=page_size)


if __name__ == "__main__":
    mcp.run()
