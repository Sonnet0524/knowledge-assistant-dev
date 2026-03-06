@echo off
REM ====================================
REM Agent Test Startup Script
REM ====================================

echo.
echo ========================================
echo   Agent Test - Quality Assurance
echo ========================================
echo.
echo Working Directory: knowledge-assistant
echo.
echo Starting Agent Test...
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

REM Start OpenCode with Agent Test
opencode --agent test

pause
