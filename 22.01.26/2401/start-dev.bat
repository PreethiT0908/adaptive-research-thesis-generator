@echo off
echo Starting Adaptive Thesis Generator...
echo.

REM Start backend API on port 8001
echo Starting Backend API on port 8001...
start cmd /k "cd app && python api.py"

REM Wait a moment for the backend to start
timeout /t 3 /nobreak

REM Start frontend on port 5173
echo Starting Frontend on port 5173...
start cmd /k "cd thesis-frontend && npm run dev"

echo.
echo ============================================
echo Backend API: http://localhost:8001
echo Frontend: http://localhost:5173
echo ============================================
pause
