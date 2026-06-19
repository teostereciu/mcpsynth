# Confluence MCP Server

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

MCP (Model Context Protocol) Server for Confluence Cloud API

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Endpoints](#endpoints)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- 🚀 FastAPI-based REST API server
- 📝 Full Confluence Cloud API v2 support
- 🔒 OAuth 2.0 authentication
- 📊 Auto-generated API documentation
- 🔄 Async/await support for better performance
- 🛠️ Comprehensive error handling
- 📱 Health check endpoint
- 🔄 Pagination support
- 🔍 Search functionality

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### Quick Start

```bash
# Clone the repository
git clone https://github.com/your-org/confluence-mcp-server.git
cd confluence-mcp-server

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment
echo "CONFLUENCE_ACCESS_TOKEN=your-oauth2-token" > .env

# Run the server
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Using Docker

```bash
# Build Docker image
docker build -t confluence-mcp-server .

# Run container
docker run -p 8000:8000 \
  -e CONFLUENCE_ACCESS_TOKEN=your-token \
  confluence-mcp-server
```

## Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `CONFLUENCE_BASE_URL` | Base URL for Confluence Cloud API | No | `https://api.atlassian.com/ex/confluence` |
| `CONFLUENCE_ACCESS_TOKEN` | OAuth 2.0 access token | Yes | None |
| `API_VERSION` | API version | No | `2` |
| `PORT` | Server port | No | `8000` |
| `HOST` | Server host | No | `0.0.0.0` |

### .env File

Create a `.env` file in the project root:

```bash
CONFLUENCE_BASE_URL=https://api.atlassian.com/ex/confluence
CONFLUENCE_ACCESS_TOKEN=your-oauth2-token-here
API_VERSION=2
PORT=8000
HOST=0.0.0.0
```

## Usage

### Health Check

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

## API Documentation

Once the server is running, visit:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

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
- `GET /wiki/api/v2/whiteboards` - Get all whiteboards
- `POST /wiki/api/v2/whiteboards` - Create a whiteboard

### Custom Content
- `GET /wiki/api/v2/custom-content` - Get custom content
- `POST /wiki/api/v2/custom-content` - Create custom content

For a complete list of endpoints, see [ENDPOINTS.md](ENDPOINTS.md).

## Development

### Setup for Development

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run linter
flake8 server.py main.py

# Run formatter
black server.py main.py

# Run type checker
mypy server.py main.py
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test
pytest tests/test_pages.py
```

### Code Structure

```
confluence-mcp-server/
├── server.py              # Main server implementation
├── main.py                # Server entry point
├── requirements.txt       # Dependencies
├── requirements-dev.txt   # Development dependencies
├── README.md              # This file
├── ENDPOINTS.md           # API endpoint documentation
├── CONFIGURATION.md       # Configuration guide
├── DEVELOPMENT.md         # Development guide
└── tests/                 # Test files
```

## Testing

### Unit Tests

```bash
pytest tests/
```

### Integration Tests

```bash
pytest tests/integration/
```

### Test Coverage

```bash
pytest --cov=. --cov-report=html
```

## Deployment

### Docker Deployment

```bash
# Build image
docker build -t confluence-mcp-server:latest .

# Run container
docker run -d \
  -p 8000:8000 \
  --name confluence-mcp \
  -e CONFLUENCE_ACCESS_TOKEN=your-token \
  confluence-mcp-server:latest
```

### Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: confluence-mcp-server
spec:
  replicas: 3
  selector:
    matchLabels:
      app: confluence-mcp-server
  template:
    metadata:
      labels:
        app: confluence-mcp-server
    spec:
      containers:
      - name: confluence-mcp-server
        image: confluence-mcp-server:latest
        ports:
        - containerPort: 8000
        env:
        - name: CONFLUENCE_ACCESS_TOKEN
          valueFrom:
            secretKeyRef:
              name: confluence-secrets
              key: access-token
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation as needed
- Ensure all tests pass

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing framework
- [Confluence Cloud API](https://developer.atlassian.com/cloud/confluence/rest/) for the documentation
- [HTTPX](https://www.python-httpx.org/) for the async HTTP client
- [Pydantic](https://docs.pydantic.dev/) for data validation

## Contact

- Project maintainers: [Your Name](mailto:email@example.com)
- Issue tracker: [GitHub Issues](https://github.com/your-org/confluence-mcp-server/issues)

## Support

For support, please:
1. Check the [documentation](README.md)
2. Search [GitHub Issues](https://github.com/your-org/confluence-mcp-server/issues)
3. Open a new issue if needed

---

Made with ❤️ by the Confluence MCP Team
