# Confluence MCP Server - Docker Guide

## Quick Start

```bash
# Build the image
docker build -t confluence-mcp-server .

# Run the container
docker run -p 8000:8000 \
  -e CONFLUENCE_ACCESS_TOKEN=your-oauth2-token \
  confluence-mcp-server
```

## Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Docker Compose

```yaml
version: '3.8'

services:
  confluence-mcp:
    build: .
    ports:
      - "8000:8000"
    environment:
      - CONFLUENCE_ACCESS_TOKEN=your-oauth2-token
      - CONFLUENCE_BASE_URL=https://api.atlassian.com/ex/confluence
      - API_VERSION=2
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

## Kubernetes

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
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

## Deployment Checklist

- [ ] Create OAuth 2.0 access token
- [ ] Set up environment variables
- [ ] Configure CORS (if needed)
- [ ] Set up health checks
- [ ] Configure logging
- [ ] Set up monitoring
- [ ] Configure TLS/SSL
- [ ] Set up backup strategy

## Troubleshooting

### Container won't start

```bash
# Check logs
docker logs confluence-mcp-server

# Check environment variables
docker exec -it confluence-mcp-server env
```

### Connection issues

```bash
# Check network
docker exec -it confluence-mcp-server ping api.atlassian.com
```

### Resource limits

Adjust memory and CPU limits based on your needs:

```yaml
resources:
  requests:
    memory: "512Mi"
    cpu: "500m"
  limits:
    memory: "1Gi"
    cpu: "1000m"
```

## Scaling

### Horizontal Pod Scaling (Kubernetes)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: confluence-mcp-server-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: confluence-mcp-server
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

## Security Best Practices

1. Use secrets for sensitive data
2. Enable TLS/SSL
3. Set up network policies
4. Configure pod security policies
5. Use read-only root filesystem
6. Run as non-root user

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Monitoring

### Prometheus Metrics

Add Prometheus metrics to your endpoints:

```python
from prometheus_fastapi_instrumentator import Instrumentator

Instrumentator().instrument(app).expose(app)
```

### Health Check

The server provides a health check endpoint:

```bash
curl http://localhost:8000/health
```

## Backup and Recovery

1. Regularly back up your OAuth 2.0 tokens
2. Keep a record of your Confluence instance URL
3. Document your deployment configuration
4. Test disaster recovery procedures

## Updates

1. Update the Docker image
2. Test in staging environment
3. Deploy to production
4. Verify functionality
5. Monitor logs

## Support

For support, see the main README.md file.
