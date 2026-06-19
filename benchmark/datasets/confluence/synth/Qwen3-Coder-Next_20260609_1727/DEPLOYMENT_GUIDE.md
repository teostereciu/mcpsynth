# Confluence MCP Server - Deployment Guide

## Deployment Options

### 1. Direct Deployment (Simple)

```bash
# Clone the repository
git clone https://github.com/your-org/confluence-mcp-server.git
cd confluence-mcp-server

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export CONFLUENCE_ACCESS_TOKEN="your-oauth2-token"

# Run the server
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 2. Docker Deployment (Recommended)

#### Build Docker Image

```bash
docker build -t confluence-mcp-server .
```

#### Run Docker Container

```bash
docker run -d \
  -p 8000:8000 \
  --name confluence-mcp \
  -e CONFLUENCE_ACCESS_TOKEN="your-oauth2-token" \
  confluence-mcp-server
```

#### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  confluence-mcp:
    build: .
    ports:
      - "8000:8000"
    environment:
      - CONFLUENCE_ACCESS_TOKEN=${CONFLUENCE_ACCESS_TOKEN}
      - CONFLUENCE_BASE_URL=https://api.atlassian.com/ex/confluence
      - API_VERSION=2
    restart: unless-stopped
```

Run with:

```bash
docker-compose up -d
```

### 3. Kubernetes Deployment

#### Create Kubernetes Manifests

**Deployment** (`k8s/deployment.yaml`):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: confluence-mcp-server
  labels:
    app: confluence-mcp-server
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

**Service** (`k8s/service.yaml`):

```yaml
apiVersion: v1
kind: Service
metadata:
  name: confluence-mcp-server
spec:
  selector:
    app: confluence-mcp-server
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
  type: LoadBalancer
```

**Ingress** (`k8s/ingress.yaml`):

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: confluence-mcp-server
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: confluence.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: confluence-mcp-server
            port:
              number: 80
```

#### Create Secrets

```bash
# Create secret for access token
kubectl create secret generic confluence-secrets \
  --from-literal=access-token="your-oauth2-token"
```

#### Apply Deployments

```bash
# Apply deployments
kubectl apply -f k8s/

# Check status
kubectl get pods
kubectl get services
kubectl get ingresses
```

## Cloud Platform Deployments

### AWS Deployment

#### Using ECS

1. Create an ECR repository:
```bash
aws ecr create-repository --repository-name confluence-mcp-server
```

2. Build and push Docker image:
```bash
# Get login
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

# Build image
docker build -t confluence-mcp-server .

# Tag image
docker tag confluence-mcp-server:latest \
  <account-id>.dkr.ecr.us-east-1.amazonaws.com/confluence-mcp-server:latest

# Push image
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/confluence-mcp-server:latest
```

3. Create ECS task definition:
```json
{
  "family": "confluence-mcp-server",
  "networkMode": "awsvpc",
  "containerDefinitions": [{
    "name": "confluence-mcp-server",
    "image": "<account-id>.dkr.ecr.us-east-1.amazonaws.com/confluence-mcp-server:latest",
    "cpu": 256,
    "memory": 512,
    "essential": true,
    "portMappings": [{
      "containerPort": 8000,
      "hostPort": 8000,
      "protocol": "tcp"
    }],
    "environment": [{
      "name": "CONFLUENCE_ACCESS_TOKEN",
      "value": "your-oauth2-token"
    }]
  }],
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512"
}
```

4. Create ECS service:
```bash
aws ecs create-service \
  --cluster default \
  --service-name confluence-mcp-server \
  --task-definition confluence-mcp-server \
  --desired-count 3 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-12345678],securityGroups=[sg-12345678],assignPublicIp=ENABLED}"
```

### Google Cloud Deployment

#### Using Cloud Run

```bash
# Build and push image
gcloud builds submit --tag gcr.io/PROJECT_ID/confluence-mcp-server

# Deploy to Cloud Run
gcloud run deploy confluence-mcp-server \
  --image gcr.io/PROJECT_ID/confluence-mcp-server \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars CONFLUENCE_ACCESS_TOKEN=your-oauth2-token
```

### Azure Deployment

#### Using Azure Container Instances

```bash
# Build and push image
az acr build --registry <registry-name> --image confluence-mcp-server:latest .

# Deploy to ACI
az container create \
  --resource-group myResourceGroup \
  --name confluence-mcp-server \
  --image <registry-name>.azurecr.io/confluence-mcp-server:latest \
  --registry-login-server <registry-name>.azurecr.io \
  --registry-username <username> \
  --registry-password <password> \
  --ports 8000 \
  --protocol TCP \
  --dns-name-label confluence-mcp-server \
  --environment-variables CONFLUENCE_ACCESS_TOKEN="your-oauth2-token"
```

## Load Balancer Configuration

### Nginx

```nginx
upstream confluence_mcp {
    server localhost:8000;
}

server {
    listen 80;
    server_name confluence.example.com;

    location / {
        proxy_pass http://confluence_mcp;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### AWS ALB

```hcl
resource "aws_lb" "confluence_mcp" {
  name               = "confluence-mcp-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.confluence_mcp.id]
  subnets            = aws_subnet.private[*].id
}

resource "aws_lb_target_group" "confluence_mcp" {
  name     = "confluence-mcp-tg"
  port     = 8000
  protocol = "HTTP"
  vpc_id   = aws_vpc.main.id

  health_check {
    path                = "/health"
    healthy_threshold   = 2
    unhealthy_threshold = 10
  }
}

resource "aws_lb_listener" "confluence_mcp" {
  load_balancer_arn = aws_lb.confluence_mcp.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.confluence_mcp.arn
  }
}
```

## SSL/TLS Configuration

### Using Let's Encrypt

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d confluence.example.com
```

### AWS Certificate Manager

1. Request certificate in AWS ACM
2. Validate domain ownership
3. Configure ALB listener with HTTPS
4. Attach certificate to listener

## Monitoring and Logging

### Prometheus Metrics

Add Prometheus metrics to your endpoints:

```python
from prometheus_fastapi_instrumentator import Instrumentator

Instrumentator().instrument(app).expose(app)
```

### Logging Configuration

Create `logging.yaml`:

```yaml
version: 1
disable_existing_loggers: False
formatters:
  standard:
    format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: standard
    stream: ext://sys.stdout
loggers:
  uvicorn:
    level: INFO
    handlers: [console]
    propagate: no
  uvicorn.error:
    level: INFO
    handlers: [console]
    propagate: no
  uvicorn.access:
    level: INFO
    handlers: [console]
    propagate: no
root:
  level: DEBUG
  handlers: [console]
```

## Health Check Configuration

### Docker Health Check

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1
```

### Kubernetes Liveness and Readiness Probes

Already configured in the Kubernetes deployment manifest.

## Backup and Recovery

### Database Backup (if applicable)

```bash
# Backup configuration
kubectl get configmap confluence-mcp-config -o yaml > config-backup.yaml

# Backup secrets
kubectl get secret confluence-secrets -o yaml > secret-backup.yaml
```

### Application Backup

1. Keep source code in version control
2. Document deployment procedures
3. Test disaster recovery procedures

## Security Checklist

- [ ] Use HTTPS/TLS
- [ ] Set up authentication
- [ ] Configure CORS properly
- [ ] Enable rate limiting
- [ ] Set up monitoring
- [ ] Configure logging
- [ ] Set up health checks
- [ ] Use secrets management
- [ ] Enable network policies
- [ ] Configure firewall rules
- [ ] Set up backup strategy
- [ ] Document incident response procedures

## Maintenance

### Updating the Deployment

```bash
# Build new image
docker build -t confluence-mcp-server:latest .

# Update deployment
kubectl set image deployment/confluence-mcp-server \
  confluence-mcp-server=confluence-mcp-server:latest
```

### Rolling Back

```bash
# Rollback to previous version
kubectl rollout undo deployment/confluence-mcp-server
```

## Troubleshooting

### Common Issues

1. **Container won't start**: Check logs with `docker logs` or `kubectl logs`
2. **Connection refused**: Verify port configuration
3. **Health check failed**: Check `/health` endpoint manually
4. **API endpoints return errors**: Verify access token and scopes

### Debug Mode

```bash
# Run with debug logging
uvicorn main:app --log-level debug
```

## Support

For support, see the main README.md file and the other documentation files in this repository.
