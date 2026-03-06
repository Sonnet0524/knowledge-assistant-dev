@echo off
REM ====================================
REM PM Agent Startup Script
REM ====================================

echo.
echo ========================================
echo   PM Agent - Project Manager
echo ========================================
echo.
echo Working Directory: knowledge-assistant-dev
echo.
echo Starting PM Agent...
echo.

REM Check if in correct directory
if not exist "opencode.json" (
    echo Error: opencode.json not found!
    echo Please run this script from the dev repository root.
    pause
    exit /b 1
)

REM Start OpenCode with PM agent
opencode --agent pm

pause
