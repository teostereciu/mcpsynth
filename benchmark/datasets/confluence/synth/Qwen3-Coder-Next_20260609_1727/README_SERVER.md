# MCP Server for Confluence Cloud

## Implementation Complete ✅

This MCP server implementation provides REST API endpoints for Confluence Cloud operations.

## Files Created

1. **server.py** - Main server implementation
2. **main.py** - Server entry point
3. **requirements.txt** - Python dependencies

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
export CONFLUENCE_ACCESS_TOKEN="your-oauth2-token"

# Run server
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### Pages
- `GET /wiki/api/v2/pages` - Get all pages
- `POST /wiki/api/v2/pages` - Create a page
- `GET /wiki/api/v2/pages/{id}` - Get a page
- `PUT /wiki/api/v2/pages/{id}` - Update a page
- `DELETE /wiki/api/v2/pages/{id}` - Delete a page

### Spaces
- `GET /wiki/api/v2/spaces` - Get all spaces
- `POST /wiki/api/v2/spaces` - Create a space
- `GET /wiki/api/v2/spaces/{id}` - Get a space

### Users
- `POST /wiki/api/v2/users-bulk` - Get users by IDs

### Search
- `GET /wiki/api/v2/search` - Search content

### Attachments
- `GET /wiki/api/v2/attachments` - Get all attachments

### Comments
- `GET /wiki/api/v2/footer-comments` - Get footer comments

### Labels
- `GET /wiki/api/v2/labels` - Get all labels

### Tasks
- `GET /wiki/api/v2/tasks` - Get all tasks

### Blog Posts
- `GET /wiki/api/v2/blogposts` - Get all blog posts
- `POST /wiki/api/v2/blogposts` - Create a blog post

### Whiteboards
- `POST /wiki/api/v2/whiteboards` - Create a whiteboard

### Custom Content
- `GET /wiki/api/v2/custom-content` - Get custom content
- `POST /wiki/api/v2/custom-content` - Create custom content

### Versions
- `GET /wiki/api/v2/pages/{id}/versions` - Get page versions

### Content Properties
- `GET /wiki/api/v2/pages/{id}/properties` - Get properties
- `POST /wiki/api/v2/pages/{id}/properties` - Create property

### Space Permissions
- `GET /wiki/api/v2/spaces/{id}/permissions` - Get permissions

### Data Policies
- `GET /wiki/api/v2/data-policies/metadata` - Get metadata
- `GET /wiki/api/v2/data-policies/spaces` - Get spaces with data policies

### Long-running Tasks
- `GET /wiki/api/v2/longtask` - Get tasks
- `GET /wiki/api/v2/longtask/{id}` - Get task by ID

### Operations
- `GET /wiki/api/v2/pages/{id}/operations` - Get page operations

### Archiving
- `POST /wiki/api/v1/content/archive` - Archive pages

## Dependencies

- fastapi>=0.104.0
- uvicorn>=0.24.0
- httpx>=0.25.0
- pydantic>=2.5.0
- python-dotenv>=1.0.0

## Configuration

Environment variables:
- `CONFLUENCE_BASE_URL` - Base URL for Confluence Cloud API
- `CONFLUENCE_ACCESS_TOKEN` - OAuth 2.0 access token
- `API_VERSION` - API version (default: 2)
- `PORT` - Server port (default: 8000)
- `HOST` - Server host (default: 0.0.0.0)
