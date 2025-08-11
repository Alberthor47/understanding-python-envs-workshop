# Containerizing Python Environments

This folder contains examples and explanations for containerizing Python applications, as discussed in Part 2 of the Python Environments workshop.

## Contents

- `app.py` - Sample Flask application
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container definition
- `docker-compose.yml` - Multi-service setup example
- `README-container.md` - Detailed container guide
- `.dockerignore` - Files to exclude from container build

## Quick Start

1. **Build the container:**
   ```bash
   docker build -t python-env-demo .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 python-env-demo
   ```

3. **Or use docker-compose:**
   ```bash
   docker-compose up
   ```

## Learning Objectives

- Understand when to use containers vs virtual environments
- Learn Docker basics for Python applications
- Practice creating reproducible environments
- Compare development vs production setups

## Comparison: Virtual Envs vs Containers

| Aspect | Virtual Environments | Containers |
|--------|---------------------|------------|
| **Speed** | Fast startup | Slower startup |
| **Isolation** | Python packages only | Full OS isolation |
| **Portability** | Platform dependent | Platform independent |
| **Resource Usage** | Lightweight | More overhead |
| **Use Case** | Local development | Deployment, CI/CD |
| **Learning Curve** | Easy | Moderate |

## When to Choose What?

### Use Virtual Environments when:
- Rapid local development
- Simple Python-only projects
- Quick experimentation
- Team has limited Docker knowledge

### Use Containers when:
- Deploying to production
- Complex system dependencies
- Microservices architecture
- Need exact environment replication
- CI/CD pipelines
