#!/bin/bash

# Confluence MCP Server Setup Script

# Check Python version
python3 --version || echo "Python 3 not found"

# Create virtual environment if needed
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created"
fi

# Activate virtual environment
source venv/bin/activate || echo "Failed to activate virtual environment"

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run the server
echo "Starting Confluence MCP Server..."
uvicorn main:app --host 0.0.0.0 --port 8000
