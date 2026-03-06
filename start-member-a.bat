@echo off
REM ====================================
REM Agent A Startup Script
REM ====================================

echo.
echo ========================================
echo   Agent A - Template System Developer
echo ========================================
echo.
echo Working Directory: knowledge-assistant
echo.
echo Starting Agent A...
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

REM Start OpenCode with Agent A
opencode --agent member-a

pause
