@echo off
echo 🤖 AI Generator - Startup Script
echo ================================

:: Check if Node.js is available
where node >nul 2>nul
if %errorlevel% == 0 (
    echo ✅ Node.js found - Starting full server...
    
    :: Install dependencies if not exists
    if not exist "node_modules" (
        echo 📦 Installing dependencies...
        npm install
    )
    
    echo 🚀 Starting server on http://localhost:3000
    npm start
    goto :end
)

:: Check if Python is available
where python >nul 2>nul
if %errorlevel% == 0 (
    echo ✅ Python found - Starting simple server...
    echo 🚀 Starting server on http://localhost:8000
    echo ⚠️  Note: Use Node.js for full API proxy features
    python -m http.server 8000
    goto :end
)

:: Check if PHP is available
where php >nul 2>nul
if %errorlevel% == 0 (
    echo ✅ PHP found - Starting simple server...
    echo 🚀 Starting server on http://localhost:8000
    echo ⚠️  Note: Use Node.js for full API proxy features
    php -S localhost:8000
    goto :end
)

echo ❌ No suitable server found!
echo Please install one of the following:
echo - Node.js (recommended): https://nodejs.org/
echo - Python: https://python.org/
echo - PHP: https://php.net/
pause

:end