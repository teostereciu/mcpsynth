# Notion API MCP Server

A comprehensive Model Context Protocol (MCP) server implementation for the Notion API, providing tools for managing pages, databases, blocks, comments, users, and search operations.

## Features

This MCP server exposes 34 tools covering the most important Notion API operations:

### Pages
- **create_page** - Create a new page with properties and optional content
- **retrieve_page** - Get a page by ID with optional property filtering
- **update_page** - Update page properties, icon, cover, or trash status
- **trash_page** - Move a page to trash
- **restore_page** - Restore a page from trash
- **move_page** - Move a page to a new parent location
- **retrieve_page_property** - Get a specific property of a page
- **retrieve_page_markdown** - Get a page's content as Notion-flavored Markdown
- **update_page_markdown** - Update a page's content using Markdown

### Databases
- **create_database** - Create a new database with schema
- **retrieve_database** - Get a database by ID
- **update_database** - Update database properties, icon, cover, or trash status
- **query_database** - Query a database with filters and sorts

### Data Sources
- **create_data_source** - Create a new data source within a database
- **retrieve_data_source** - Get a data source by ID
- **update_data_source** - Update a data source's properties
- **query_data_source** - Query a data source with filters and sorts

### Blocks
- **retrieve_block** - Get a block by ID
- **get_block_children** - List child blocks of a parent block
- **append_block_children** - Add child blocks to a parent block
- **update_block** - Update a block's content
- **delete_block** - Delete a block

### Comments
- **create_comment** - Create a comment on a page or block
- **retrieve_comment** - Get a comment by ID
- **list_comments** - List comments on a page or block

### Views
- **create_view** - Create a new view in a database or dashboard
- **retrieve_view** - Get a view by ID
- **update_view** - Update a view's properties
- **delete_view** - Delete a view
- **list_views** - List all views in a database

### File Uploads
- **create_file_upload** - Create a file upload session
- **retrieve_file_upload** - Get a file upload by ID
- **list_file_uploads** - List all file uploads
- **complete_file_upload** - Complete a file upload session

### Users
- **list_users** - List all users in the workspace
- **retrieve_user** - Get a user by ID
- **get_self** - Get the bot user associated with the API token

### Search
- **search** - Search for pages and databases by title and properties

## Installation

### Prerequisites
- Python 3.8+
- A Notion integration token (from https://www.notion.so/my-integrations)

### Setup

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your Notion API key:
   ```bash
   export NOTION_API_KEY="your_integration_token_here"
   ```

## Running the Server

Start the MCP server:

```bash
python server.py
```

The server will start listening on stdio and expose all tools via the MCP protocol.

## Usage Examples

### Creating a Page

```python
# Create a page in a database
create_page(
    parent={"database_id": "d9824bdc-8445-4327-be8b-5b47500af6ce"},
    properties={
        "Name": {
            "title": [{"text": {"content": "My New Page"}}]
        }
    }
)
```

### Querying a Database

```python
# Query a database with a filter
query_database(
    database_id="d9824bdc-8445-4327-be8b-5b47500af6ce",
    filter={
        "property": "Status",
        "select": {"equals": "Done"}
    },
    sorts=[{
        "property": "Created",
        "direction": "descending"
    }]
)
```

### Adding Blocks to a Page

```python
# Append a paragraph block to a page
append_block_children(
    block_id="c02fc1d3-db8b-45c5-a222-27595b15aea7",
    children=[{
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{"text": {"content": "Hello, world!"}}]
        }
    }]
)
```

### Creating a Comment

```python
# Create a comment on a page
create_comment(
    parent={"page_id": "b55c9c91-384d-452b-81db-d1ef79372b75"},
    rich_text=[{"text": {"content": "This is a comment"}}]
)
```

### Searching

```python
# Search for pages
search(
    query="meeting notes",
    query_filter={"property": "object", "value": "page"},
    sort={"direction": "descending", "timestamp": "last_edited_time"}
)
```

## API Documentation

For detailed information about each tool's parameters and return values, refer to the official Notion API documentation at https://developers.notion.com/reference.

The `grounding.json` file maps each tool to its source documentation file.

## Error Handling

The server returns errors as JSON objects with an "error" key:

```json
{"error": "HTTP 404: Page not found"}
```

Expected errors (404s, invalid IDs, etc.) are returned as error objects rather than raising exceptions, allowing the client to handle them gracefully.

## Authentication

The server uses Bearer token authentication with the Notion API. The token is read from the `NOTION_API_KEY` environment variable.

All requests include the required `Notion-Version` header set to `2026-03-11`.

## Limitations

- Maximum 100 results per page for paginated endpoints
- Some complex operations may require multiple API calls
- File content upload via HTTP PUT is not directly exposed (use the upload_url from create_file_upload)
- View query operations are not yet implemented

## Implementation Details

- **Language**: Python 3.8+
- **Framework**: FastMCP (MCP SDK for Python)
- **HTTP Client**: httpx
- **API Base URL**: https://api.notion.com/v1
- **API Version**: 2026-03-11

## License

This implementation is provided as-is for use with the Notion API.
