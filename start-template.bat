@echo off
REM ====================================
REM Template Agent Startup Script
REM ====================================

echo.
echo ========================================
echo   Template Agent - Template System
echo ========================================
echo.
echo Working Directory: knowledge-assistant
echo.
echo Starting Template Agent...
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

REM Start OpenCode with Template agent
opencode --agent template

pause
