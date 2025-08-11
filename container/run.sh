#!/bin/bash

# Build and Run Script for Container Demo
# This script automates the build and run process

set -e  # Exit on any error

echo "🐳 Python Environment Container Demo"
echo "====================================="

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

# Build the image
echo "🔨 Building Docker image..."
docker build -t python-env-demo .

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
else
    echo "❌ Build failed!"
    exit 1
fi

# Ask user what to do
echo ""
echo "What would you like to do?"
echo "1) Run the container"
echo "2) Run with docker-compose"
echo "3) Run in development mode"
echo "4) Just build (already done)"
echo ""
read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo "🚀 Running container on port 8000..."
        docker run -p 8000:8000 python-env-demo
        ;;
    2)
        echo "🚀 Starting services with docker-compose..."
        docker-compose up
        ;;
    3)
        echo "🚀 Running in development mode with volume mounting..."
        docker run -p 8000:8000 -v $(pwd):/app -e FLASK_ENV=development -e FLASK_DEBUG=true python-env-demo
        ;;
    4)
        echo "✅ Build complete. You can now run:"
        echo "   docker run -p 8000:8000 python-env-demo"
        ;;
    *)
        echo "❌ Invalid choice. Exiting."
        exit 1
        ;;
esac
