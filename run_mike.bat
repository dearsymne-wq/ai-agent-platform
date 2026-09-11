@echo off
REM MIKE AI Agent - Startup Script
REM This script sets up and runs MIKE AI Agent automatically

echo.
echo ========================================
echo   MIKE AI AGENT - STARTUP
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo IMPORTANT: Check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [✓] Python found
python --version
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo [*] Creating virtual environment...
    python -m venv venv
    echo [✓] Virtual environment created
    echo.
)

REM Activate virtual environment
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat
echo [✓] Virtual environment activated
echo.

REM Check if requirements are installed
echo [*] Checking dependencies...
pip show pyautogui >nul 2>&1
if errorlevel 1 (
    echo [*] Installing dependencies (this may take 5-10 minutes)...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Failed to install dependencies
        echo Try running: pip install -r requirements.txt
        pause
        exit /b 1
    )
    echo [✓] Dependencies installed
) else (
    echo [✓] Dependencies already installed
)

echo.
echo ========================================
echo   STARTING MIKE AI AGENT
echo ========================================
echo.
echo Type commands to control MIKE:
echo   - "Open notepad" (or calculator, chrome, explorer, etc.)
echo   - "Help" (to see all available commands)
echo   - "exit" (to quit)
echo.
echo ========================================
echo.

REM Run MIKE
python -m src.mike --text

REM On exit
echo.
echo ========================================
echo   MIKE AI AGENT STOPPED
echo ========================================
echo.
pause
