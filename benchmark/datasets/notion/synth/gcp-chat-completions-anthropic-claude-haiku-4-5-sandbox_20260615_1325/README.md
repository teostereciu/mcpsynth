# Notion API MCP Server

A comprehensive Model Context Protocol (MCP) server implementation for the Notion API, enabling autonomous agents to interact with Notion workspaces programmatically.

## Features

This MCP server provides 38 tools covering all major Notion API operations:

### Pages
- **create_page** - Create new pages with properties, content, icons, and covers
- **retrieve_page** - Get page details with optional property filtering
- **update_page** - Update page properties, icons, covers, and lock status
- **archive_page** - Move pages to trash
- **restore_page** - Restore pages from trash
- **move_page** - Move pages to new parents
- **retrieve_page_property** - Get specific page properties with pagination

### Databases
- **create_database** - Create new databases with schemas
- **retrieve_database** - Get database details
- **update_database** - Update database properties and schema
- **query_database** - Query databases with filters, sorts, and pagination

### Blocks
- **retrieve_block** - Get block details
- **get_block_children** - List child blocks with pagination
- **append_block_children** - Add child blocks with position control
- **update_block** - Update block content
- **delete_block** - Delete blocks

### Comments
- **create_comment** - Create comments with rich text and attachments
- **retrieve_comment** - Get comment details
- **list_comments** - List comments on pages/blocks with pagination

### Users
- **list_users** - List workspace users with pagination
- **retrieve_user** - Get user details
- **get_bot_user** - Get the bot user associated with the API token

### Search
- **search** - Search for pages and databases with filters and sorting

### Data Sources
- **create_data_source** - Create new data sources
- **retrieve_data_source** - Get data source details
- **query_data_source** - Query data sources with filters and sorts
- **update_data_source** - Update data source properties
- **list_data_source_templates** - List available templates

### Views
- **create_view** - Create views (table, gallery, calendar, etc.)
- **retrieve_view** - Get view details
- **update_view** - Update view configuration
- **delete_view** - Delete views
- **list_views** - List views for a data source
- **create_view_query** - Create view queries
- **get_view_query_results** - Get view query results
- **delete_view_query** - Delete view queries

### File Uploads
- **create_file_upload** - Create file upload sessions
- **retrieve_file_upload** - Get upload status
- **list_file_uploads** - List file uploads
- **complete_file_upload** - Complete file uploads

## Installation

### Prerequisites
- Python 3.8+
- Notion API token (integration token)

### Setup

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your Notion API key:
```bash
export NOTION_API_KEY="your-integration-token-here"
```

## Usage

### Running the Server

```bash
python server.py
```

The server will start and listen on stdio, ready to receive MCP protocol messages.

### Example: Creating a Page

```python
# Via MCP client
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "create_page",
    "arguments": {
      "parent_type": "database_id",
      "parent_id": "d9824bdc-8445-4327-be8b-5b47500af6ce",
      "properties": {
        "Name": {
          "title": [
            {
              "text": {
                "content": "My New Page"
              }
            }
          ]
        }
      }
    }
  }
}
```

### Example: Querying a Database

```python
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "query_database",
    "arguments": {
      "database_id": "d9824bdc-8445-4327-be8b-5b47500af6ce",
      "filter": {
        "property": "Status",
        "select": {
          "equals": "Done"
        }
      },
      "sorts": [
        {
          "property": "Name",
          "direction": "ascending"
        }
      ]
    }
  }
}
```

## API Documentation

For detailed information about each tool and its parameters, see `grounding.json` which maps each tool to its source documentation file.

### Authentication

The server uses Bearer token authentication with the Notion API. The token is read from the `NOTION_API_KEY` environment variable.

All requests include the required `Notion-Version: 2026-03-11` header.

### Error Handling

The server returns errors as JSON objects with an `error` field:

```json
{
  "error": "API error 404",
  "details": "..."
}
```

Expected errors (404s, invalid IDs, etc.) are returned as JSON responses rather than raising exceptions, allowing graceful handling by clients.

### Rate Limiting

The Notion API has rate limits. See the official Notion API documentation for current limits.

## Tool Categories

### CRUD Operations
All major resources support standard CRUD operations:
- **Create**: `create_*` tools
- **Read**: `retrieve_*` and `list_*` tools
- **Update**: `update_*` tools
- **Delete**: `delete_*` tools

### Pagination
Tools that return lists support pagination:
- `start_cursor`: Continue from a previous result set
- `page_size`: Number of results per page (max 100)
- Response includes `has_more` and `next_cursor` for pagination

### Filtering and Sorting
Database and data source queries support:
- **Filters**: Complex filter objects with AND/OR logic
- **Sorts**: Multiple sort criteria with direction control

## Architecture

The server is built using FastMCP, which provides:
- Automatic tool registration via decorators
- JSON-RPC 2.0 protocol handling
- Stdio transport for MCP communication

### Request Flow

1. MCP client sends tool call request
2. Server routes to appropriate tool function
3. Tool function constructs API request
4. `make_request()` helper handles HTTP communication
5. Response is returned as JSON

## Development

### Adding New Tools

To add a new tool:

1. Create a function decorated with `@mcp.tool()`
2. Add docstring with parameter descriptions
3. Call `make_request()` with appropriate HTTP method and endpoint
4. Update `grounding.json` with tool mapping

Example:
```python
@mcp.tool()
def my_new_tool(param1: str, param2: Optional[int] = None) -> dict:
    """Description of what this tool does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    """
    body = {"key": param1}
    if param2 is not None:
        body["count"] = param2
    
    return make_request("POST", "/endpoint", data=body)
```

### Testing

Test tools by sending MCP protocol messages to the running server:

```bash
# Start server
python server.py

# In another terminal, send test requests
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | python -m mcp.client.stdio python server.py
```

## Limitations

- File upload requires separate handling of file content (not included in this server)
- Some advanced features like webhooks are not exposed as tools
- Markdown content updates are not directly supported (use block updates instead)

## Resources

- [Notion API Documentation](https://developers.notion.com/reference)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/modelcontextprotocol/python-sdk)

## License

This implementation is provided as-is for use with the Notion API.

## Support

For issues with:
- **Notion API**: See [Notion Developer Docs](https://developers.notion.com/)
- **MCP Protocol**: See [MCP Documentation](https://modelcontextprotocol.io/)
- **This Server**: Check the grounding.json for endpoint mappings
