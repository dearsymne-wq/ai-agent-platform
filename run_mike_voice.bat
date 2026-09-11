@echo off
REM MIKE AI Agent - Voice Mode Startup Script
REM This script runs MIKE AI Agent in voice mode (requires microphone)

echo.
echo ========================================
echo   MIKE AI AGENT - VOICE MODE
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
echo   MICROPHONE CHECK
echo ========================================
echo.
echo Please make sure:
echo   1. Microphone is connected and working
echo   2. Microphone is not muted
echo   3. Volume is turned up
echo.
echo To test microphone:
echo   - Right-click Volume icon (bottom-right)
echo   - Click "Open Volume mixer"
echo   - Check microphone level
echo.

REM Ask user to proceed
set /p proceed="Ready to start MIKE in voice mode? (Y/N): "
if /i not "%proceed%"=="Y" (
    echo Cancelled.
    pause
    exit /b 0
)

echo.
echo ========================================
echo   STARTING MIKE AI AGENT - VOICE MODE
echo ========================================
echo.
echo MIKE is listening for voice commands...
echo.
echo You can say:
echo   - "Open notepad"
echo   - "Open calculator"
echo   - "Open chrome"
echo   - "Help"
echo.
echo Press Ctrl+C to stop
echo.
echo ========================================
echo.

REM Run MIKE in voice mode
python -m src.mike --voice

REM On exit
echo.
echo ========================================
echo   MIKE AI AGENT VOICE MODE STOPPED
echo ========================================
echo.
pause
