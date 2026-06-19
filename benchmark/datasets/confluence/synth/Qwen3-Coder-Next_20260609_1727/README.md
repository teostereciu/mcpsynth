# MCP Server for Confluence Cloud

This is an MCP (Model Context Protocol) server implementation for Confluence Cloud, providing REST API endpoints for common Confluence operations.

## Features

The server provides endpoints for:

- **Pages**: Get, create, update, delete pages
- **Spaces**: Get, create spaces
- **Users**: Get user details
- **Search**: Search content using CQL
- **Attachments**: Get attachments
- **Comments**: Get footer comments
- **Labels**: Get labels
- **Tasks**: Get tasks
- **Blog Posts**: Get, create blog posts
- **Whiteboards**: Get, create whiteboards
- **Custom Content**: Get, create custom content
- **Versions**: Get page versions
- **Content Properties**: Get, create content properties
- **Space Permissions**: Get space permissions
- **Data Policies**: Get data policy metadata and spaces
- **Long-running Tasks**: Get long-running task status
- **Operations**: Get permitted operations for content

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- HTTPX
- Pydantic

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd confluence-mcp-server

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Set the following environment variables:

```bash
export CONFLUENCE_BASE_URL="https://api.atlassian.com/ex/confluence"
export CONFLUENCE_ACCESS_TOKEN="your-oauth2-token"
export API_VERSION="2"
export PORT="8000"
export HOST="0.0.0.0"
```

## Running the Server

```bash
# Method 1: Direct Python
python main.py

# Method 2: Using Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

# Method 3: Using the setup script
chmod +x setup.sh
./setup.sh
```

## API Documentation

Once the server is running, visit:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Usage

### Health Check

```bash
curl http://localhost:8000/health
```

### Get Pages

```bash
curl http://localhost:8000/wiki/api/v2/pages?limit=25
```

### Create Page

```bash
curl -X POST http://localhost:8000/wiki/api/v2/pages \
  -H "Content-Type: application/json" \
  -d '{
    "spaceId": "<space-id>",
    "status": "current",
    "title": "My Page",
    "parentId": "<parent-id>",
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

## MCP Server Configuration

The server can be configured using the following environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `CONFLUENCE_BASE_URL` | Base URL for Confluence Cloud API | `https://api.atlassian.com/ex/confluence` |
| `CONFLUENCE_ACCESS_TOKEN` | OAuth 2.0 access token for Confluence API | None (required for API endpoints) |
| `API_VERSION` | API version to use | `2` |
| `PORT` | Port to run the server on | `8000` |
| `HOST` | Host to bind to | `0.0.0.0` |

## Error Handling

The server returns standard HTTP status codes:

- `200`: Success
- `201`: Created
- `204`: No content
- `400`: Bad request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not found
- `500`: Internal server error

## Authentication

The server uses OAuth 2.0 for authentication. The access token should be provided via the `CONFLUENCE_ACCESS_TOKEN` environment variable.

## Development

```bash
# Run with auto-reload for development
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Run tests (if available)
pytest
```

## License

This project is licensed under the MIT License.

## Acknowledgments

- Based on [Confluence Cloud REST API documentation](https://developer.atlassian.com/cloud/confluence/rest/)
- Built with FastAPI and Uvicorn
