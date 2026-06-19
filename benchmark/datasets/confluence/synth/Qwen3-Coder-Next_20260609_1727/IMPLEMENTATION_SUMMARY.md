# Confluence MCP Server

## Implementation Summary

This MCP server implementation provides REST API endpoints for Confluence Cloud operations, supporting:

### Core Endpoints

- **Pages**: GET, POST, PUT, DELETE
- **Spaces**: GET, POST
- **Users**: GET bulk user details
- **Search**: CQL-based search
- **Attachments**: GET
- **Comments**: GET footer comments
- **Labels**: GET
- **Tasks**: GET
- **Blog Posts**: GET, POST
- **Whiteboards**: GET, POST
- **Custom Content**: GET, POST
- **Versions**: GET
- **Content Properties**: GET, POST
- **Space Permissions**: GET
- **Data Policies**: GET metadata and spaces
- **Long-running Tasks**: GET status
- **Operations**: GET permitted operations

### MCP Server Features

1. **Health Check**: `/health` endpoint for server health monitoring
2. **Async Support**: All endpoints use async HTTP clients
3. **Error Handling**: Proper HTTP status codes and error responses
4. **Validation**: Pydantic models for request/response validation
5. **Documentation**: Auto-generated OpenAPI docs at `/docs`

### Configuration

Environment variables:
- `CONFLUENCE_BASE_URL` - Base URL for Confluence Cloud API
- `CONFLUENCE_ACCESS_TOKEN` - OAuth 2.0 access token
- `API_VERSION` - API version (default: 2)
- `PORT` - Server port (default: 8000)
- `HOST` - Server host (default: 0.0.0.0)

### Files Created

1. `server.py` - Main server implementation with FastAPI
2. `main.py` - Server entry point
3. `requirements.txt` - Python dependencies
4. `README.md` - Documentation
5. `setup.sh` - Setup script

### Dependencies

- fastapi>=0.104.0
- uvicorn>=0.24.0
- httpx>=0.25.0
- pydantic>=2.5.0
- python-dotenv>=1.0.0

### API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
