# MCP Server Configuration

## Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `CONFLUENCE_BASE_URL` | Base URL for Confluence Cloud API | No | `https://api.atlassian.com/ex/confluence` |
| `CONFLUENCE_ACCESS_TOKEN` | OAuth 2.0 access token for Confluence API | Yes (for API endpoints) | None |
| `API_VERSION` | API version to use | No | `2` |
| `PORT` | Port to run the server on | No | `8000` |
| `HOST` | Host to bind to | No | `0.0.0.0` |

## Environment File (.env)

Create a `.env` file in the project root:

```bash
CONFLUENCE_BASE_URL=https://api.atlassian.com/ex/confluence
CONFLUENCE_ACCESS_TOKEN=your-oauth2-token-here
API_VERSION=2
PORT=8000
HOST=0.0.0.0
```

## OAuth 2.0 Authentication

To authenticate with the Confluence API, you need an OAuth 2.0 access token.

### Getting an Access Token

1. Register your app at [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/)
2. Create a new app and select "Confluence" as the product
3. Configure the app with the required scopes:
   - `read:page:confluence` - Read pages
   - `write:page:confluence` - Create and update pages
   - `read:space:confluence` - Read spaces
   - `read:content-details:confluence` - Read content details
   - `search:confluence` - Search content
   - `read:attachment:confluence` - Read attachments
   - `read:comment:confluence` - Read comments
   - `read:label:confluence` - Read labels
   - `read:task:confluence` - Read tasks
   - `read:user:confluence` - Read users
   - `read:configuration:confluence` - Read configuration
   - `read:group:confluence` - Read groups
   - `write:space:confluence` - Create spaces
   - `delete:page:confluence` - Delete pages
   - `write:page:confluence` - Create and update pages
   - `read:space.permission:confluence` - Read space permissions
   - `write:space.permission:confluence` - Manage space permissions
   - `read:relation:confluence` - Read relations

4. Generate an access token or use the OAuth 2.0 flow

### scopes

The server supports the following scopes:

- **Read Operations**: `read:page:confluence`, `read:space:confluence`, `read:content-details:confluence`, `search:confluence`, `read:attachment:confluence`, `read:comment:confluence`, `read:label:confluence`, `read:task:confluence`, `read:user:confluence`, `read:configuration:confluence`, `read:group:confluence`, `read:relation:confluence`
- **Write Operations**: `write:space:confluence`, `write:page:confluence`, `write:space.permission:confluence`
- **Delete Operations**: `delete:page:confluence`

## Running the Server

### Using Environment Variables

```bash
# Set environment variables
export CONFLUENCE_ACCESS_TOKEN="your-token-here"

# Run the server
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Using .env File

```bash
# Create .env file
echo "CONFLUENCE_ACCESS_TOKEN=your-token-here" > .env

# Run the server
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Using Docker

```bash
# Build Docker image
docker build -t confluence-mcp-server .

# Run container
docker run -p 8000:8000 \
  -e CONFLUENCE_ACCESS_TOKEN="your-token-here" \
  confluence-mcp-server
```

## Configuration Examples

### Example 1: Basic Setup

```bash
export CONFLUENCE_ACCESS_TOKEN="your-oauth2-token"
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Example 2: Development Setup with Reload

```bash
export CONFLUENCE_ACCESS_TOKEN="your-oauth2-token"
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Example 3: Production Setup

```bash
export CONFLUENCE_ACCESS_TOKEN="your-oauth2-token"
export PORT=8080
export HOST=0.0.0.0
uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4
```

## Health Check

The server provides a health check endpoint:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{
  "status": "healthy",
  "server": "confluence-mcp-server",
  "version": "1.0.0",
  "initialized": true
}
```

## Error Handling

### Authentication Errors

If the access token is invalid or missing:

```json
{
  "detail": "Server not initialized"
}
```

### API Errors

The server passes through Confluence API errors:

```json
{
  "detail": "401: Unauthorized"
}
```

### Validation Errors

```json
{
  "detail": [
    {
      "loc": ["body", "field_name"],
      "msg": "Field required",
      "type": "value_error.missing"
    }
  ]
}
```

## Logging

The server uses Python's logging module. Log levels can be configured:

```bash
# Set log level
export LOG_LEVEL=DEBUG
uvicorn main:app --host 0.0.0.0 --port 8000
```

## TLS/SSL

For production deployments, consider using TLS:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 \
  --ssl-keyfile=/path/to/key.pem \
  --ssl-certfile=/path/to/cert.pem
```

## Rate Limiting

The server does not implement rate limiting. For production use, consider:

1. Using a reverse proxy like Nginx with rate limiting
2. Implementing rate limiting in the application
3. Using a cloud provider's rate limiting features

## Monitoring

Monitor the server using:

1. Health check endpoint: `/health`
2. Access logs
3. Application metrics (add Prometheus support as needed)

## Security Best Practices

1. **Store secrets securely**: Use environment variables or a secrets manager
2. **Use HTTPS**: Always use TLS in production
3. **Rate limiting**: Implement rate limiting to prevent abuse
4. **Input validation**: Validate all user inputs
5. **CORS**: Configure CORS properly for your use case
6. **Logging**: Monitor logs for suspicious activity

## Troubleshooting

### Server won't start

- Check if the port is already in use
- Verify the access token is set correctly
- Check the logs for errors

### API endpoints return errors

- Verify the access token has the required scopes
- Check the Confluence API status
- Review the error response details

### Connection issues

- Verify the Confluence Base URL is correct
- Check network connectivity
- Ensure the access token is valid
