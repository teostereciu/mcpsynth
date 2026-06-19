# Confluence MCP Server - OAuth 2.0 Setup Guide

## Getting Started

This guide will help you set up OAuth 2.0 authentication for your Confluence MCP server.

## Step 1: Create an Atlassian Account

If you don't already have an Atlassian account:

1. Go to [Atlassian Account](https://id.atlassian.com/)
2. Click "Create account"
3. Follow the instructions

## Step 2: Create an App

1. Go to [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/)
2. Click "Create new app"
3. Fill in the app details:
   - App name: `Confluence MCP Server`
   - App type: `Server-to-server OAuth 2.0`
   - App name: Your organization name
4. Click "Create"

## Step 3: Configure Scopes

In your app configuration, add the following scopes:

### Required Scopes

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
- `write:space.permission:confluence` - Manage space permissions
- `read:space.permission:confluence` - Read space permissions
- `read:relation:confluence` - Read relations

### Optional Scopes

- `read:custom-content:confluence` - Read custom content
- `write:custom-content:confluence` - Create and update custom content
- `delete:custom-content:confluence` - Delete custom content
- `read:whiteboard:confluence` - Read whiteboards
- `write:whiteboard:confluence` - Create and update whiteboards
- `delete:whiteboard:confluence` - Delete whiteboards
- `read:database:confluence` - Read databases
- `write:database:confluence` - Create and update databases
- `read:folder:confluence` - Read folders

## Step 4: Generate Access Token

### Option 1: Generate Token Directly

1. In your app console, go to "API tokens"
2. Click "Create API token"
3. Copy the token
4. Set it as the `CONFLUENCE_ACCESS_TOKEN` environment variable

### Option 2: Use OAuth 2.0 Flow

1. Get the authorization URL from the app console
2. Visit the URL in your browser
3. Authorize the app
4. Get the authorization code
5. Exchange the code for an access token:

```bash
curl -X POST https://auth.atlassian.com/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "authorization_code",
    "client_id": "your-client-id",
    "client_secret": "your-client-secret",
    "code": "your-authorization-code",
    "redirect_uri": "https://example.com/callback"
  }'
```

## Step 5: Set Up Environment Variables

Create a `.env` file in your project root:

```bash
CONFLUENCE_BASE_URL=https://api.atlassian.com/ex/confluence
CONFLUENCE_ACCESS_TOKEN=your-oauth2-token
API_VERSION=2
PORT=8000
HOST=0.0.0.0
```

Or set them directly:

```bash
export CONFLUENCE_ACCESS_TOKEN="your-oauth2-token"
```

## Step 6: Test the Setup

1. Run the server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

2. Test the health endpoint:
```bash
curl http://localhost:8000/health
```

3. Test a Confluence endpoint:
```bash
curl http://localhost:8000/wiki/api/v2/spaces
```

## Troubleshooting

### Invalid Token

- Generate a new token
- Check the token has the required scopes
- Verify the token hasn't expired

### Permission Denied

- Check the user has the required permissions in Confluence
- Add more scopes if needed
- Verify the user has access to the requested resources

### Connection Issues

- Verify the Confluence Base URL is correct
- Check your network connectivity
- Ensure the Confluence instance is accessible

## Security Best Practices

1. **Store tokens securely**: Use environment variables or a secrets manager
2. **Rotate tokens regularly**: Generate new tokens periodically
3. **Use HTTPS**: Always use TLS in production
4. **Limit scopes**: Only request the minimum scopes needed
5. **Monitor access**: Regularly review token access
6. **Revoke unused tokens**: Remove tokens from apps you no longer use

## Token Management

### Viewing Token Scopes

1. Go to [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/)
2. Find your app
3. Check the scopes

### Revoking a Token

1. Go to [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/)
2. Find your app
3. Revoke the token

## Advanced Configuration

### Token Refresh

OAuth 2.0 tokens can be refreshed using the refresh token:

```bash
curl -X POST https://auth.atlassian.com/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "refresh_token",
    "client_id": "your-client-id",
    "client_secret": "your-client-secret",
    "refresh_token": "your-refresh-token"
  }'
```

### Token Expiration

Access tokens typically expire after 3600 seconds (1 hour). Refresh tokens can be used to obtain new access tokens.

## Support

For more information, see:
- [Atlassian OAuth 2.0 Documentation](https://developer.atlassian.com/cloud/confluence/oauth-2-3lo/)
- [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/)
- [Confluence REST API Documentation](https://developer.atlassian.com/cloud/confluence/rest/)
