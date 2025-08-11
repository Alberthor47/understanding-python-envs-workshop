# Complete Container Guide - Python Environments Workshop

## Overview

This guide demonstrates how to containerize Python applications using Docker, covering the concepts discussed in Part 2 of the Python Environments workshop.

## What You'll Learn

- How to create a Docker container for a Python application
- Best practices for containerizing Python apps
- When to choose containers vs virtual environments
- Multi-service setup with docker-compose

## Prerequisites

- Docker installed on your system
- Basic understanding of Python virtual environments (from Part 1)
- Familiarity with command line

## Files Explained

### `app.py`
A Flask web application that demonstrates:
- Environment variable configuration
- Health check endpoints
- Logging setup
- API endpoints for testing

### `requirements.txt`
Python dependencies for the application:
- Flask for web framework
- Requests for HTTP client functionality
- Python-dotenv for environment management

### `Dockerfile`
The container definition following best practices:
- Multi-stage build potential
- Non-root user for security
- Health checks
- Proper caching layers

### `docker-compose.yml`
Orchestration file showing:
- Multi-service setup
- Environment configuration
- Volume mounting for development
- Network configuration

### `.dockerignore`
Files to exclude from Docker build context (similar to `.gitignore`)

## Step-by-Step Tutorial

### 1. Build the Container

```bash
# Navigate to the container directory
cd container

# Build the Docker image
docker build -t python-env-demo .

# Check the image was created
docker images | grep python-env-demo
```

### 2. Run the Container

```bash
# Run the container
docker run -p 8000:8000 python-env-demo

# Run in background (detached mode)
docker run -d -p 8000:8000 --name my-python-app python-env-demo

# Check running containers
docker ps
```

### 3. Test the Application

```bash
# Test the home endpoint
curl http://localhost:8000/

# Test the health check
curl http://localhost:8000/health

# Test environment info
curl http://localhost:8000/env
```

### 4. Using Docker Compose

```bash
# Start all services
docker-compose up

# Start in background
docker-compose up -d

# Start with development profile
docker-compose --profile dev up

# Stop services
docker-compose down
```

## Development Workflow

### For Development
```bash
# Mount source code for live reload
docker run -p 8000:8000 -v $(pwd):/app python-env-demo

# Or use docker-compose with development profile
docker-compose --profile dev up
```

### For Production
```bash
# Build production image
docker build -t python-env-demo:prod .

# Run with production settings
docker run -p 8000:8000 -e FLASK_ENV=production python-env-demo:prod
```

## Best Practices Demonstrated

1. **Security**: Non-root user in container
2. **Efficiency**: Multi-layer caching in Dockerfile
3. **Monitoring**: Health check endpoints
4. **Configuration**: Environment variables
5. **Development**: Volume mounting for live reload
6. **Production**: Separate production configuration

## Next Steps

- Try modifying the application and rebuilding
- Experiment with different base images
- Add database connectivity
- Deploy to a cloud platform
- Set up CI/CD pipeline with containers

## Resources

- [Docker Python Guide](https://docs.docker.com/language/python/)
- [Flask in Docker](https://flask.palletsprojects.com/en/2.3.x/deploying/docker/)
- [Docker Compose Reference](https://docs.docker.com/compose/)
- [Python Docker Best Practices](https://pythonspeed.com/docker/)
