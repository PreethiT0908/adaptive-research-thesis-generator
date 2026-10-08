# Adaptive Thesis Generator - Development Server Starter
# PowerShell version for Windows users

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Starting Adaptive Thesis Generator" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Check if Node.js is installed
try {
    $nodeVersion = node --version 2>&1
    Write-Host "✓ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Node.js not found. Please install Node.js" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Starting Backend API on port 8001..." -ForegroundColor Yellow

# Start backend in a new window
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd app; python api.py" -WindowStyle Normal

Write-Host "✓ Backend process started" -ForegroundColor Green

# Wait for backend to initialize
Write-Host "Waiting 3 seconds for backend to initialize..." -ForegroundColor Yellow
Start-Sleep -Seconds 3

Write-Host ""
Write-Host "Starting Frontend on port 5173..." -ForegroundColor Yellow

# Start frontend in a new window
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd thesis-frontend; npm run dev" -WindowStyle Normal

Write-Host "✓ Frontend process started" -ForegroundColor Green

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Services are starting..." -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 Backend API:   http://localhost:8001" -ForegroundColor Blue
Write-Host "📊 API Docs:      http://localhost:8001/docs" -ForegroundColor Blue
Write-Host "📘 Frontend:      http://localhost:5173" -ForegroundColor Blue
Write-Host ""
Write-Host "Press any key to close this window..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
