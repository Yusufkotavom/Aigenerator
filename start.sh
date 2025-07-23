#!/bin/bash

echo "🤖 AI Generator - Startup Script"
echo "================================"

# Check if Node.js is available
if command -v node &> /dev/null; then
    echo "✅ Node.js found - Starting full server..."
    
    # Install dependencies if not exists
    if [ ! -d "node_modules" ]; then
        echo "📦 Installing dependencies..."
        npm install
    fi
    
    echo "🚀 Starting server on http://localhost:3000"
    npm start
    
elif command -v python3 &> /dev/null; then
    echo "✅ Python3 found - Starting simple server..."
    echo "🚀 Starting server on http://localhost:8000"
    echo "⚠️  Note: Use Node.js for full API proxy features"
    python3 -m http.server 8000
    
elif command -v php &> /dev/null; then
    echo "✅ PHP found - Starting simple server..."
    echo "🚀 Starting server on http://localhost:8000"
    echo "⚠️  Note: Use Node.js for full API proxy features"
    php -S localhost:8000
    
else
    echo "❌ No suitable server found!"
    echo "Please install one of the following:"
    echo "- Node.js (recommended): https://nodejs.org/"
    echo "- Python3: https://python.org/"
    echo "- PHP: https://php.net/"
    exit 1
fi