@echo off
REM MIKE AI Agent - Complete Setup Script
REM Automates the entire installation and setup process

setlocal enabledelayedexpansion

echo.
echo ========================================
echo   MIKE AI AGENT - SETUP WIZARD
echo ========================================
echo.
echo This script will:
echo   1. Check if Python is installed
echo   2. Create virtual environment
echo   3. Install all dependencies
echo   4. Verify installation
echo   5. Start MIKE AI Agent
echo.
echo ========================================
echo.

REM Step 1: Check Python
echo [STEP 1] Checking Python Installation...
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo.
    echo IMPORTANT INSTALLATION STEPS:
    echo   1. Download Python installer from python.org
    echo   2. Run the installer
    echo   3. CHECK THE BOX: "Add Python to PATH"
    echo   4. Click "Install Now"
    echo   5. Wait for installation to complete
    echo   6. Restart your computer
    echo   7. Run this script again
    echo.
    pause
    exit /b 1
)

echo [✓] Python is installed:
python --version
echo.
timeout /t 2 /nobreak

REM Step 2: Create Virtual Environment
echo [STEP 2] Creating Virtual Environment...
echo.

if not exist "venv\" (
    echo Creating venv folder...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment
        echo Try running: python -m venv venv
        pause
        exit /b 1
    )
    echo [✓] Virtual environment created
) else (
    echo [✓] Virtual environment already exists
)
echo.
timeout /t 2 /nobreak

REM Step 3: Activate Virtual Environment
echo [STEP 3] Activating Virtual Environment...
echo.

call venv\Scripts\activate.bat
echo [✓] Virtual environment activated
echo.
timeout /t 2 /nobreak

REM Step 4: Install Dependencies
echo [STEP 4] Installing Dependencies...
echo.
echo This may take 5-15 minutes depending on internet speed...
echo Please wait...
echo.

pip install -q -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    echo.
    echo Trying alternative installation method...
    pip install --upgrade pip
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Installation failed
        echo Try running manually: pip install -r requirements.txt
        pause
        exit /b 1
    )
)

echo [✓] Dependencies installed successfully
echo.
timeout /t 2 /nobreak

REM Step 5: Verify Installation
echo [STEP 5] Verifying Installation...
echo.

python -c "import pyautogui; print('[OK] PyAutoGUI')" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] PyAutoGUI not found
) else (
    echo [✓] PyAutoGUI installed
)

python -c "import speech_recognition; print('[OK] Speech Recognition')" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Speech Recognition not found
) else (
    echo [✓] Speech Recognition installed
)

python -c "import pyttsx3; print('[OK] Text-to-Speech')" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Text-to-Speech not found
) else (
    echo [✓] Text-to-Speech installed
)

echo.
timeout /t 2 /nobreak

REM Step 6: Choose Mode
echo [STEP 6] Choose Operating Mode
echo.
echo Available modes:
echo   1) Text Mode (easiest, recommended for first time)
echo   2) Voice Mode (requires microphone)
echo   3) Skip for now (just finish setup)
echo.

set /p mode="Select mode (1-3): "

if "%mode%"=="1" (
    echo.
    echo ========================================
    echo   STARTING MIKE AI AGENT - TEXT MODE
    echo ========================================
    echo.
    python -m src.mike --text
) else if "%mode%"=="2" (
    echo.
    echo ========================================
    echo   STARTING MIKE AI AGENT - VOICE MODE
    echo ========================================
    echo.
    echo Make sure your microphone is:
    echo   - Connected and working
    echo   - Not muted
    echo   - Volume is turned up
    echo.
    pause
    python -m src.mike --voice
) else (
    echo.
    echo ========================================
    echo   SETUP COMPLETE!
    echo ========================================
    echo.
    echo MIKE AI Agent is ready to use!
    echo.
    echo To run MIKE later:
    echo.
    echo Text Mode:
    echo   - Double-click: run_mike.bat
    echo   - Or type: python -m src.mike --text
    echo.
    echo Voice Mode:
    echo   - Double-click: run_mike_voice.bat
    echo   - Or type: python -m src.mike --voice
    echo.
)

echo.
echo ========================================
echo   SETUP FINISHED
echo ========================================
echo.
pause
