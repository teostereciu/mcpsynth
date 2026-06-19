# Confluence MCP Server - Development Guide

## Project Structure

```
confluence-mcp-server/
├── server.py              # Main server implementation
├── main.py                # Server entry point
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── ENDPOINTS.md           # API endpoint documentation
├── CONFIGURATION.md       # Configuration guide
├── DEVELOPMENT.md         # This file
├── setup.sh               # Setup script
└── .env                   # Environment variables (not included)
```

## Development Setup

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### Installation Steps

1. Clone the repository:
```bash
git clone <repository-url>
cd confluence-mcp-server
```

2. Create a virtual environment:
```bash
python3 -m venv venv
```

3. Activate the virtual environment:
```bash
# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Set up environment variables:
```bash
echo "CONFLUENCE_ACCESS_TOKEN=your-token" > .env
```

6. Run the server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_pages.py

# Run with coverage
pytest --cov=. --cov-report=html
```

### Code Style

The project follows PEP 8 style guidelines:

- Use 4 spaces for indentation
- Limit lines to 79 characters
- Use blank lines to separate functions and classes
- Use docstrings for all public functions and classes

### Running Linters

```bash
# Run flake8
flake8 .

# Run mypy for type checking
mypy --package server

# Run black for formatting
black .
```

### Auto-formatting

```bash
# Format with black
black server.py main.py

# Sort imports with isort
isort server.py main.py
```

## Testing

### Unit Tests

Create test files in the `tests/` directory:

```python
# tests/test_pages.py
import pytest
from server import get_pages

@pytest.mark.asyncio
async def test_get_pages():
    result = await get_pages(limit=25)
    assert isinstance(result, list)
```

### Integration Tests

```python
# tests/test_integration.py
import pytest
from server import app

@pytest.fixture
def client():
    return TestClient(app)

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
```

## Documentation

### Updating API Documentation

The API documentation is auto-generated from the FastAPI endpoints. To update:

1. Modify the endpoint definitions in `server.py`
2. Run the server to see updated docs: `http://localhost:8000/docs`
3. Check the OpenAPI schema: `http://localhost:8000/openapi.json`

### Documentation Generation

```bash
# Generate OpenAPI schema
python -m fastapi dev server.py --generate-docs

# Generate HTML documentation
fastapi OpenAPI.json > docs.html
```

## Debugging

### Using Print Statements

```python
logger.debug(f"Request params: {params}")
```

### Using pdb

```python
import pdb; pdb.set_trace()
```

### Using IDE Debugger

Configure your IDE to:
1. Set breakpoints in the code
2. Run the server with debug mode
3. Step through the code

## Common Tasks

### Adding a New Endpoint

1. Add the endpoint to `server.py`:
```python
@app.get("/new-endpoint")
async def new_endpoint():
    return {"message": "New endpoint"}
```

2. Test the endpoint:
```bash
curl http://localhost:8000/new-endpoint
```

3. Update documentation in `ENDPOINTS.md`

### Modifying Existing Endpoints

1. Locate the endpoint in `server.py`
2. Make the necessary changes
3. Test the endpoint
4. Update documentation if needed

### Adding New Models

1. Add the Pydantic model to `server.py`:
```python
class NewModel(BaseModel):
    field: str
```

2. Use the model in endpoints:
```python
@app.post("/endpoint")
async def create_model(model: NewModel):
    return model
```

## Performance Optimization

### Async/Await

Use async/await for I/O operations:

```python
async def get_pages():
    response = await http_client.get(url)
    return response.json()
```

### Connection Pooling

The HTTPX client uses connection pooling by default.

### Caching

Consider adding caching for frequently accessed data:

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def cached_function(param):
    # Expensive operation
    return result
```

## Deployment

### Docker Deployment

1. Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

2. Build and run:
```bash
docker build -t confluence-mcp-server .
docker run -p 8000:8000 confluence-mcp-server
```

### Cloud Deployment

#### AWS

1. Use AWS ECS or EKS
2. Configure environment variables
3. Set up load balancer

#### Google Cloud

1. Use Cloud Run or GKE
2. Configure environment variables
3. Set up HTTPS

#### Azure

1. Use Azure Container Instances or AKS
2. Configure environment variables
3. Set up HTTPS

## Troubleshooting

### Common Issues

1. **Port already in use**:
   ```bash
   lsof -i :8000
   kill -9 <PID>
   ```

2. **Module not found**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Access token invalid**:
   - Generate a new token
   - Check token scopes

### Debug Mode

```bash
uvicorn main:app --reload --log-level debug
```

### Logging

```bash
# Set log level
export LOG_LEVEL=DEBUG
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

MIT License - See LICENSE file for details.
