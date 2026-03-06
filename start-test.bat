@echo off
REM ====================================
REM Test Agent Startup Script
REM ====================================

echo.
echo ========================================
echo   Test Agent - Quality Assurance
echo ========================================
echo.
echo Working Directory: knowledge-assistant
echo.
echo Starting Test Agent...
echo.

REM Check if we need to switch to main repo
if exist "..\knowledge-assistant" (
    echo Switching to main repository...
    cd ..\knowledge-assistant
)

REM Check if in correct directory
if not exist "tests" (
    echo Error: Not in main repository!
    echo Please run this script when knowledge-assistant repo is available.
    pause
    exit /b 1
)

REM Start OpenCode with Test agent
opencode --agent test

pause
