# Confluence Cloud MCP Server

A Model Context Protocol (MCP) server for Confluence Cloud REST API, enabling autonomous agents to interact with Confluence spaces, pages, blog posts, comments, attachments, and more.

## Features

- **Spaces**: List, get, create spaces
- **Pages**: Create, read, update, delete pages with version support
- **Blog Posts**: Create, read, update, delete blog posts
- **Search**: CQL-based search across content
- **Comments**: Manage footer and inline comments on pages and blog posts
- **Attachments**: Upload, list, delete attachments
- **Labels**: Add, remove, and list labels on content
- **Content Properties**: Manage custom properties on content
- **Versions**: View page versions and restore previous versions
- **Users**: Get current user and user details by account ID

## Prerequisites

- Python 3.8+
- Confluence Cloud account
- Atlassian API token
- Atlassian account email

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Set the following environment variables before running the server:

```bash
export CONFLUENCE_BASE_URL="https://your-site.atlassian.net/wiki"
export CONFLUENCE_SPACE_KEY="SYNTH"  # Default space for operations
export JIRA_EMAIL="your-email@domain.com"
export JIRA_API_TOKEN="your-api-token"
```

### Getting API Token

1. Go to [Atlassian API tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Create a new API token
3. Use your Atlassian account email and the generated token

## Running the Server

```bash
python server.py
```

The server will start and listen on stdio for MCP protocol messages.

## Available Tools

### Space Operations

- `confluence_list_spaces` - List all spaces
- `confluence_get_space` - Get space by ID
- `confluence_get_space_by_key` - Get space by key
- `confluence_create_space` - Create a new space

### Page Operations

- `confluence_list_pages` - List pages across all spaces
- `confluence_get_page` - Get page by ID
- `confluence_create_page` - Create a new page
- `confluence_update_page` - Update an existing page
- `confluence_delete_page` - Delete a page
- `confluence_list_page_versions` - List page versions
- `confluence_list_space_pages` - List pages in a specific space
- `confluence_list_default_space_pages` - List pages in default space

### Blog Post Operations

- `confluence_list_blog_posts` - List blog posts in a space
- `confluence_get_blog_post` - Get blog post by ID
- `confluence_create_blog_post` - Create a new blog post
- `confluence_update_blog_post` - Update a blog post
- `confluence_delete_blog_post` - Delete a blog post

### Search Operations

- `confluence_search` - Search content using CQL
- `confluence_search_users` - Search users using CQL

### Comment Operations

- `confluence_get_page_comments` - Get footer comments for a page
- `confluence_create_comment` - Create a comment
- `confluence_update_comment` - Update a comment
- `confluence_delete_comment` - Delete a comment
- `confluence_get_inline_comments` - Get inline comments for a page

### Attachment Operations

- `confluence_list_attachments` - List attachments for a page or blog post
- `confluence_get_attachment` - Get attachment by ID
- `confluence_upload_attachment` - Upload an attachment
- `confluence_delete_attachment` - Delete an attachment

### Label Operations

- `confluence_get_labels` - Get labels for content
- `confluence_add_label` - Add a label to content
- `confluence_remove_label` - Remove a label from content

### Content Properties Operations

- `confluence_get_content_properties` - Get content properties
- `confluence_create_content_property` - Create a content property
- `confluence_update_content_property` - Update a content property
- `confluence_delete_content_property` - Delete a content property

### Version Operations

- `confluence_get_page_version` - Get specific page version
- `confluence_restore_page_version` - Restore page to a previous version

### User Operations

- `confluence_get_current_user` - Get current user details
- `confluence_get_user_by_account_id` - Get user by account ID
- `confluence_get_users_by_ids` - Get multiple users by IDs

### Helper Operations

- `confluence_get_space_id` - Get space ID from space key
- `confluence_list_default_space_pages` - List pages in default space
- `confluence_create_page_in_default_space` - Create page in default space

## Usage Example

```python
from mcp import ClientSession, StdioServerParameters, create_stdio_client
import asyncio

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )
    
    async with create_stdio_client(server_params) as session:
        await session.initialize()
        
        # List spaces
        result = await session.call_tool("confluence_list_spaces")
        print(result)
        
        # Create a page
        result = await session.call_tool("confluence_create_page_in_default_space", {
            "title": "My New Page",
            "body": "<p>This is my page content</p>",
            "parent_title": "Parent Page"
        })
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

## API Version

The server uses both v1 and v2 Confluence Cloud REST APIs:

- **v2 API** (`/wiki/api/v2/`): Used for most operations (pages, blog posts, comments, attachments, spaces, labels)
- **v1 API** (`/wiki/rest/api/`): Used for search and user operations where v2 equivalents are not available

## Authentication

The server uses HTTP Basic authentication with:
- Username: Atlassian account email (from `JIRA_EMAIL` env var)
- Password: Atlassian API token (from `JIRA_API_TOKEN` env var)

## Error Handling

All tools return error responses as dictionaries with an `"error"` key. The server handles HTTP errors gracefully and returns descriptive error messages.

## Rate Limiting

Confluence Cloud has rate limits (100 requests per minute for Cloud). The server does not implement automatic rate limiting - consider adding this if needed for high-volume usage.

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python server.py
```

## License

MIT
