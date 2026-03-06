@echo off
REM ====================================
REM Data Agent Startup Script
REM ====================================

echo.
echo ========================================
echo   Data Agent - Data System
echo ========================================
echo.
echo Working Directory: knowledge-assistant
echo.
echo Starting Data Agent...
echo.

REM Check if we need to switch to main repo
if exist "..\knowledge-assistant" (
    echo Switching to main repository...
    cd ..\knowledge-assistant
)

REM Check if in correct directory
if not exist "scripts" (
    echo Error: Not in main repository!
    echo Please run this script when knowledge-assistant repo is available.
    pause
    exit /b 1
)

REM Start OpenCode with Data agent
opencode --agent data

pause
