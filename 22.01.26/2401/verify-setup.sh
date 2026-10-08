#!/bin/bash
# Verification script for Frontend-Backend Connection
# Run this to verify everything is properly configured

echo "=========================================="
echo "Adaptive Thesis Generator - Verification"
echo "=========================================="
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} $1"
        return 0
    else
        echo -e "${RED}✗${NC} $1 (MISSING)"
        return 1
    fi
}

check_directory() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}✓${NC} $1/"
        return 0
    else
        echo -e "${RED}✗${NC} $1/ (MISSING)"
        return 1
    fi
}

echo "Checking Backend Files:"
check_file "app/api.py"
check_file "app/main.py"
check_directory "app/agents"
check_directory "app/config"
check_directory "app/models"

echo ""
echo "Checking Frontend Files:"
check_file "thesis-frontend/package.json"
check_file "thesis-frontend/vite.config.js"
check_file "thesis-frontend/src/pages/Generate.jsx"
check_file "thesis-frontend/src/styles/Generate.css"
check_file "thesis-frontend/.env.local"

echo ""
echo "Checking Helper Scripts:"
check_file "start-dev.bat"
check_file "start-dev.ps1"
check_file "QUICK_START.txt"
check_file "SETUP_GUIDE.md"
check_file "FRONTEND_BACKEND_CONNECTION.md"

echo ""
echo "Checking Backend Dependencies:"
python -c "import fastapi" 2>/dev/null && echo -e "${GREEN}✓${NC} fastapi" || echo -e "${RED}✗${NC} fastapi (install with: pip install fastapi)"
python -c "import uvicorn" 2>/dev/null && echo -e "${GREEN}✓${NC} uvicorn" || echo -e "${RED}✗${NC} uvicorn (install with: pip install uvicorn)"

echo ""
echo "Checking Frontend Dependencies:"
if [ -d "thesis-frontend/node_modules" ]; then
    echo -e "${GREEN}✓${NC} node_modules/"
else
    echo -e "${YELLOW}⚠${NC} node_modules/ (run: cd thesis-frontend && npm install)"
fi

echo ""
echo "=========================================="
echo "Verification complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Install missing dependencies if needed"
echo "2. Run: start-dev.bat (Windows) or ./start-dev.ps1 (PowerShell)"
echo "3. Open http://localhost:5173 in your browser"
echo "4. Fill in the form and generate your thesis!"
