# Confluence Cloud REST API Endpoints

This document provides a comprehensive list of all endpoints implemented in the MCP server based on the Confluence Cloud REST API documentation.

## Implemented Endpoints

### Pages API (v2)

#### GET /wiki/api/v2/pages
- Get all pages
- Parameters: `limit`, `cursor`, `space-id`, `status`, `title`, `sort`
- Returns: List of pages

#### POST /wiki/api/v2/pages
- Create a new page
- Request body: `spaceId`, `status`, `title`, `parentId`, `body`, `subtype`
- Returns: Created page

#### GET /wiki/api/v2/pages/{id}
- Get a specific page by ID
- Parameters: `body-format`, `get-draft`, `status`, `version`, `include-labels`, `include-properties`, `include-operations`, `include-likes`, `include-versions`
- Returns: Page details

#### PUT /wiki/api/v2/pages/{id}
- Update a page
- Request body: `id`, `status`, `title`, `spaceId`, `body`, `version`
- Returns: Updated page

#### DELETE /wiki/api/v2/pages/{id}
- Delete a page
- Parameters: `purge`, `draft`
- Returns: 204 No Content

### Spaces API (v2)

#### GET /wiki/api/v2/spaces
- Get all spaces
- Parameters: `limit`, `cursor`, `ids`, `keys`, `type`, `status`, `labels`, `favorited-by`, `not-favorited-by`, `sort`
- Returns: List of spaces

#### POST /wiki/api/v2/spaces
- Create a new space
- Request body: `name`, `key`, `alias`, `description`, `roleAssignments`, `copySpaceAccessConfiguration`, `createPrivateSpace`, `templateKey`
- Returns: Created space

#### GET /wiki/api/v2/spaces/{id}
- Get a specific space by ID
- Returns: Space details

### Users API (v2)

#### POST /wiki/api/v2/users-bulk
- Get user details for multiple account IDs
- Request body: `accountIds` (array)
- Returns: List of users

### Search API (v2)

#### GET /wiki/api/v2/search
- Search content using CQL
- Parameters: `cql`, `limit`, `cursor`
- Returns: Search results

### Attachments API (v2)

#### GET /wiki/api/v2/attachments
- Get all attachments
- Parameters: `limit`, `cursor`, `status`, `mediaType`, `filename`, `sort`
- Returns: List of attachments

#### GET /wiki/api/v2/attachments/{id}
- Get a specific attachment by ID
- Returns: Attachment details

#### DELETE /wiki/api/v2/attachments/{id}
- Delete an attachment
- Parameters: `purge`
- Returns: 204 No Content

### Comments API (v2)

#### GET /wiki/api/v2/footer-comments
- Get all footer comments
- Parameters: `limit`, `cursor`, `sort`
- Returns: List of footer comments

#### POST /wiki/api/v2/footer-comments
- Create a footer comment
- Request body: `blogPostId`, `pageId`, `parentCommentId`, `attachmentId`, `customContentId`, `body`
- Returns: Created comment

### Labels API (v2)

#### GET /wiki/api/v2/labels
- Get all labels
- Parameters: `limit`, `cursor`, `prefix`, `sort`
- Returns: List of labels

### Tasks API (v2)

#### GET /wiki/api/v2/tasks
- Get all tasks
- Parameters: `limit`, `cursor`, `status`, `task-id`, `space-id`, `page-id`, `blogpost-id`, `created-by`, `assigned-to`, `completed-by`
- Returns: List of tasks

#### GET /wiki/api/v2/tasks/{id}
- Get a specific task by ID
- Returns: Task details

#### PUT /wiki/api/v2/tasks/{id}
- Update a task
- Request body: `id`, `localId`, `spaceId`, `pageId`, `blogPostId`, `status`, etc.
- Returns: Updated task

### Blog Posts API (v2)

#### GET /wiki/api/v2/blogposts
- Get all blog posts
- Parameters: `limit`, `cursor`, `space-id`, `status`, `title`, `sort`
- Returns: List of blog posts

#### POST /wiki/api/v2/blogposts
- Create a new blog post
- Request body: `spaceId`, `status`, `title`, `body`, `createdAt`
- Returns: Created blog post

#### GET /wiki/api/v2/blogposts/{id}
- Get a specific blog post by ID
- Returns: Blog post details

#### PUT /wiki/api/v2/blogposts/{id}
- Update a blog post
- Request body: `id`, `status`, `title`, `spaceId`, `body`, `version`, `createdAt`
- Returns: Updated blog post

#### DELETE /wiki/api/v2/blogposts/{id}
- Delete a blog post
- Parameters: `purge`, `draft`
- Returns: 204 No Content

### Whiteboards API (v2)

#### POST /wiki/api/v2/whiteboards
- Create a new whiteboard
- Request body: `spaceId`, `title`, `parentId`, `templateKey`, `locale`
- Returns: Created whiteboard

#### GET /wiki/api/v2/whiteboards/{id}
- Get a specific whiteboard by ID
- Returns: Whiteboard details

#### DELETE /wiki/api/v2/whiteboards/{id}
- Delete a whiteboard
- Returns: 204 No Content

### Custom Content API (v2)

#### GET /wiki/api/v2/custom-content
- Get custom content by type
- Parameters: `type` (required), `limit`, `cursor`
- Returns: List of custom content

#### POST /wiki/api/v2/custom-content
- Create custom content
- Request body: `type`, `status`, `title`, `spaceId`, `pageId`, `blogPostId`, `customContentId`, `body`
- Returns: Created custom content

#### GET /wiki/api/v2/custom-content/{id}
- Get custom content by ID
- Returns: Custom content details

#### PUT /wiki/api/v2/custom-content/{id}
- Update custom content
- Request body: `id`, `type`, `status`, `spaceId`, `pageId`, `blogPostId`, `customContentId`, `title`, `body`, `version`
- Returns: Updated custom content

#### DELETE /wiki/api/v2/custom-content/{id}
- Delete custom content
- Parameters: `purge`
- Returns: 204 No Content

### Versions API (v2)

#### GET /wiki/api/v2/pages/{id}/versions
- Get page versions
- Parameters: `limit`, `cursor`
- Returns: List of versions

#### GET /wiki/api/v2/blogposts/{id}/versions
- Get blog post versions
- Parameters: `limit`, `cursor`
- Returns: List of versions

### Content Properties API (v2)

#### GET /wiki/api/v2/pages/{id}/properties
- Get content properties for a page
- Parameters: `limit`, `cursor`
- Returns: List of properties

#### POST /wiki/api/v2/pages/{id}/properties
- Create content property for a page
- Request body: `key`, `value`
- Returns: Created property

#### GET /wiki/api/v2/attachments/{id}/properties
- Get content properties for an attachment
- Parameters: `limit`, `cursor`
- Returns: List of properties

### Space Permissions API (v2)

#### GET /wiki/api/v2/spaces/{id}/permissions
- Get space permissions for a space
- Parameters: `limit`, `cursor`
- Returns: List of permissions

#### GET /wiki/api/v2/space-permissions
- Get available space permissions
- Parameters: `limit`, `cursor`
- Returns: List of available permissions

### Data Policies API (v2)

#### GET /wiki/api/v2/data-policies/metadata
- Get data policy metadata for the workspace
- Returns: Data policy metadata

#### GET /wiki/api/v2/data-policies/spaces
- Get spaces with data policies
- Parameters: `limit`, `cursor`
- Returns: List of spaces with data policies

### Long-running Tasks API (v2)

#### GET /wiki/api/v2/longtask
- Get long-running tasks
- Parameters: `key`, `limit`, `cursor`
- Returns: List of long-running tasks

#### GET /wiki/api/v2/longtask/{id}
- Get a specific long-running task
- Returns: Task details

### Operations API (v2)

#### GET /wiki/api/v2/pages/{id}/operations
- Get permitted operations for a page
- Returns: List of permitted operations

#### GET /wiki/api/v2/spaces/{id}/operations
- Get permitted operations for a space
- Returns: List of permitted operations

#### GET /wiki/api/v2/attachments/{id}/operations
- Get permitted operations for an attachment
- Returns: List of permitted operations

#### GET /wiki/api/v2/blogposts/{id}/operations
- Get permitted operations for a blog post
- Returns: List of permitted operations

#### GET /wiki/api/v2/custom-content/{id}/operations
- Get permitted operations for custom content
- Returns: List of permitted operations

#### GET /wiki/api/v2/whiteboards/{id}/operations
- Get permitted operations for a whiteboard
- Returns: List of permitted operations

### Archiving API (v1)

#### POST /wiki/api/v1/content/archive
- Archive pages
- Request body: `pages` (array of page IDs)
- Returns: Long task response

## MCP Server Implementation

The MCP server provides these endpoints through FastAPI, with:

1. **Request Validation**: Pydantic models ensure proper request format
2. **Error Handling**: HTTP exceptions mapped to appropriate status codes
3. **Async Support**: All endpoints use async HTTP clients for better performance
4. **Documentation**: Auto-generated OpenAPI docs at `/docs`
5. **Authentication**: OAuth 2.0 support via Bearer token

## Usage Examples

### Get Pages
```bash
curl http://localhost:8000/wiki/api/v2/pages?limit=25
```

### Create Page
```bash
curl -X POST http://localhost:8000/wiki/api/v2/pages \
  -H "Content-Type: application/json" \
  -d '{
    "spaceId": "SPACE123",
    "status": "current",
    "title": "My Page",
    "body": {
      "storage": {
        "representation": "storage",
        "value": "<p>Page content</p>"
      }
    }
  }'
```

### Search Content
```bash
curl "http://localhost:8000/wiki/api/v2/search?cql=type=page&limit=25"
```

### Health Check
```bash
curl http://localhost:8000/health
```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
