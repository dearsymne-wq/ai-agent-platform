# 🚀 MIKE AI Agent - Complete Setup & Usage Guide

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation Steps](#installation-steps)
3. [Running MIKE](#running-mike)
4. [Commands Reference](#commands-reference)
5. [Voice Mode Setup](#voice-mode-setup)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Features](#advanced-features)

---

## System Requirements

### Hardware Requirements
- **Processor**: Intel/AMD dual-core or better
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 2GB free space
- **Microphone**: Optional (only needed for voice mode)
- **Speakers**: Optional (for voice feedback)

### Software Requirements
- **Operating System**: Windows 10 or Windows 11
- **Python**: Version 3.9 or higher
- **Internet Connection**: Required for speech recognition

### Check Your Windows Version
1. Press `Win + R`
2. Type `winver` and press Enter
3. Check your Windows version

### Check if Python is Installed
1. Press `Win + R`
2. Type `cmd` and press Enter
3. Type `python --version` and press Enter
4. Should show: `Python 3.x.x`

If not installed, download from [python.org](https://www.python.org/downloads/)

---

## Installation Steps

### Step 1: Download & Install Python (If Not Already Installed)

**1.1 Visit Python Website**
- Go to https://www.python.org/downloads/
- Click "Download Python 3.11" (or latest 3.9+)

**1.2 Run the Installer**
- Double-click the downloaded `.exe` file
- **IMPORTANT**: Check the box "Add Python to PATH"
- Click "Install Now"
- Wait for installation to complete

**1.3 Verify Installation**
```bash
python --version
```
Should show: `Python 3.11.x` (or your version)

---

### Step 2: Download MIKE Repository

**Option A: Using Git (Recommended)**

**2.1 Install Git** (if not already installed)
- Download from https://git-scm.com/download/win
- Run the installer and accept defaults
- Restart your computer

**2.2 Clone the Repository**
```bash
# Open Command Prompt (Win + R, type cmd, press Enter)
git clone https://github.com/dearsymne-wq/ai-agent-platform.git
cd ai-agent-platform
```

**Option B: Download as ZIP**

**2.1 Download ZIP File**
- Visit https://github.com/dearsymne-wq/ai-agent-platform
- Click "Code" button (green button)
- Click "Download ZIP"

**2.2 Extract the ZIP**
- Right-click the downloaded ZIP file
- Select "Extract All"
- Choose a location (e.g., `C:\Users\YourName\Documents`)
- Open the extracted folder

---

### Step 3: Open Command Prompt in the Project Directory

**Method 1: Using File Explorer**
1. Open File Explorer
2. Navigate to `ai-agent-platform` folder
3. Click the address bar at the top
4. Type `cmd` and press Enter
5. Command Prompt will open in that directory

**Method 2: Using Command Prompt**
```bash
# Open Command Prompt
cd C:\Users\YourName\Documents\ai-agent-platform
# (Replace YourName with your actual username)
```

---

### Step 4: Create Virtual Environment (Recommended)

A virtual environment keeps dependencies isolated from your system Python.

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# You should see (venv) at the start of your command prompt
```

---

### Step 5: Install All Dependencies

```bash
# Make sure virtual environment is activated (you see (venv) in prompt)

# Install all required packages
pip install -r requirements.txt
```

**What's Being Installed:**
- 🎤 **Voice Processing**: SpeechRecognition, pyttsx3, google-cloud libraries
- 🤖 **AI/NLP**: transformers, torch, spacy, openai
- 🖥️ **Windows Automation**: pyautogui, pywinauto, keyboard, mouse
- 🌐 **Web Framework**: fastapi, uvicorn, websockets
- 💾 **Database**: sqlalchemy, psycopg2, redis
- 📊 **Data Tools**: numpy, pandas, requests

**Installation Time**: 5-15 minutes (depending on internet speed)

**If Installation Fails:**
```bash
# Try upgrading pip first
python -m pip install --upgrade pip

# Then try again
pip install -r requirements.txt
```

---

### Step 6: Configure Environment Variables (Optional)

```bash
# Copy the example environment file
copy .env.example .env

# Edit .env with Notepad (optional - only if you have API keys)
notepad .env
```

**What to Configure:**
```env
# Only edit if you have these API keys:
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_CLOUD_KEY=path/to/google_cloud_key.json
```

*(MIKE works perfectly fine without these - they're for advanced features)*

---

## Running MIKE

### Method 1: Text Mode (EASIEST - RECOMMENDED FOR FIRST TIME)

Text mode is the safest way to test MIKE without a microphone.

**1. Make sure you're in the project directory**
```bash
cd C:\Users\YourName\Documents\ai-agent-platform
```

**2. Activate virtual environment (if you created one)**
```bash
venv\Scripts\activate
```

**3. Run MIKE in text mode**
```bash
python -m src.mike --text
```

**4. You should see:**
```
==================================================
🎯 MIKE Agent Started
==================================================

💬 Text mode started. Type 'exit' to quit.

👤 You: _
```

**5. Type a command:**
```
👤 You: Open notepad
🤖 MIKE: ✅ Opened notepad

👤 You: exit
🤖 MIKE: 
==================================================
🛑 MIKE Agent stopped
==================================================
```

---

### Method 2: Voice Mode (Requires Microphone)

**1. Make sure you have a working microphone**
- Test microphone in Windows Sound Settings
- Volume should be turned up

**2. Run MIKE in voice mode**
```bash
python -m src.mike --voice
```

**3. You should hear:**
- "🎤 Listening..." message
- MIKE waiting for voice input

**4. Speak clearly into the microphone:**
```
(You speak): "Open notepad"
(MIKE responds): "✅ Opened notepad"
```

---

## Commands Reference

### Application Launching Commands

```
Open notepad          → Opens Windows Notepad
Open calculator       → Opens Windows Calculator
Open paint            → Opens Paint application
Open explorer         → Opens File Explorer
Open word             → Opens Microsoft Word (if installed)
Open excel            → Opens Microsoft Excel (if installed)
Open chrome           → Opens Google Chrome (if installed)
Open firefox          → Opens Firefox (if installed)
```

### Information Commands

```
Help                  → Shows all available commands
What can you do?      → Lists MIKE's capabilities
How do you work?      → Explains MIKE's functionality
```

### Control Commands

```
Exit                  → Stops MIKE
Quit                  → Stops MIKE
```

---

## Voice Mode Setup

### Microphone Setup

**1. Check if Microphone is Connected**
- Plug in USB microphone or use built-in laptop microphone
- Windows should detect it automatically

**2. Test Microphone in Windows**
- Right-click Volume icon (bottom-right corner)
- Click "Open Volume mixer"
- Click "App volume and device preferences"
- Look for your microphone device
- Make sure it's not muted (no red X icon)

**3. Adjust Microphone Volume**
- Right-click Volume icon
- Click "Sound settings"
- Scroll to "Input"
- Under "Microphone", adjust volume slider
- Click "Test your microphone" to test

### Running Voice Mode

```bash
# Make sure virtual environment is activated
venv\Scripts\activate

# Run MIKE in voice mode
python -m src.mike --voice
```

### Voice Mode Tips

- **Speak clearly** - Good microphone quality helps
- **Avoid background noise** - Quiet environment works best
- **Normal volume** - Don't whisper or shout
- **Give commands slowly** - Let it finish listening before speaking again
- **Wait for confirmation** - Let MIKE respond before next command

---

## Troubleshooting

### Problem 1: Python Not Found

**Error Message:**
```
'python' is not recognized as an internal or external command
```

**Solution:**
1. Python might not be in PATH
2. Reinstall Python
3. **During installation, MUST check "Add Python to PATH"**
4. Restart computer after installation
5. Try `python --version` in new Command Prompt

---

### Problem 2: Module Not Found

**Error Message:**
```
ModuleNotFoundError: No module named 'pyautogui'
```

**Solution:**
```bash
# Make sure virtual environment is activated
venv\Scripts\activate

# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall

# If still fails, try:
pip install pyautogui pyttsx3 speech_recognition
```

---

### Problem 3: Virtual Environment Not Activating

**Error Message:**
```
is not recognized as an internal or external command
```

**Solution:**
```bash
# Try full path to activation script
C:\Users\YourName\Documents\ai-agent-platform\venv\Scripts\activate

# Or use different approach:
python -m venv venv
venv\Scripts\activate.bat
```

---

### Problem 4: Microphone Not Working in Voice Mode

**Error Message:**
```
No microphone device found or Microphone error
```

**Solution:**
1. Check microphone is physically connected
2. Check Windows recognizes it (Sound Settings)
3. Give Python microphone permission (Windows 11)
4. Use text mode instead: `python -m src.mike --text`
5. Try different USB port if using USB microphone

---

### Problem 5: Application Not Opening

**Error Message:**
```
Could not open [application name]
```

**Possible Causes:**
- Application not installed on your system
- Wrong application name used
- Application path not in Windows PATH

**Solution:**
- Use applications that come with Windows (notepad, calculator)
- Check application is installed
- Use exact name: "chrome" not "Google Chrome"

---

### Problem 6: Slow Installation

**Why it takes time:**
- torch package is large (~700MB)
- Multiple dependencies to download and install
- Compiling some packages from source

**Speed it up:**
```bash
# Use faster pip installation
pip install -r requirements.txt --use-deprecated=legacy-resolver

# Or install only what you need (minimal):
pip install pyautogui pyttsx3 SpeechRecognition pydantic
```

---

### Problem 7: Port Already in Use

**Error Message:**
```
Address already in use
```

**Solution:**
This only happens with web server. For basic MIKE:
- Close any other MIKE instances running
- Wait 10 seconds and try again
- Restart Command Prompt

---

## Advanced Features

### Creating a Batch File to Run MIKE Easily

**1. Open Notepad**
- Press `Win + R`
- Type `notepad`
- Press Enter

**2. Type this code:**
```batch
@echo off
cd /d C:\Users\YourName\Documents\ai-agent-platform
call venv\Scripts\activate
python -m src.mike --text
pause
```

*(Replace `YourName` with your Windows username)*

**3. Save the file**
- Press `Ctrl + S`
- Name it: `run_mike.bat`
- Save in: `ai-agent-platform` folder
- File type: All Files

**4. Run MIKE**
- Double-click `run_mike.bat`
- MIKE starts immediately!

---

### Adding to Windows Startup

**1. Create the batch file** (see above)

**2. Create Shortcut**
- Right-click `run_mike.bat`
- Select "Create shortcut"
- Name it "MIKE AI Agent"

**3. Add to Startup Folder**
- Press `Win + R`
- Type: `shell:startup`
- Drag the shortcut there
- MIKE will run when you boot your computer

---

### Keeping MIKE Running in Background

**Option 1: Use Windows Task Scheduler**
1. Press `Win + R`
2. Type `taskschd.msc`
3. Click "Create Basic Task"
4. Set to run your `run_mike.bat` file
5. Set to run "On a schedule" or "At startup"

**Option 2: Use a Python Loop**
Create `keep_mike_running.py`:
```python
import subprocess
import time

while True:
    try:
        subprocess.run(["python", "-m", "src.mike", "--text"])
    except Exception as e:
        print(f"Error: {e}, restarting in 5 seconds...")
        time.sleep(5)
```

Run it:
```bash
python keep_mike_running.py
```

---

### Integrating with Digital Clock

```python
from src.digital_clock import DigitalClock, TimeFormat

# Create clock
clock = DigitalClock()

# Show all clocks
print(clock.display_all_clocks())

# Get time in specific zone
time_est = clock.get_current_time_in_zone('US/Eastern')
print(f"Time in EST: {time_est}")
```

---

### Integrating with To-Do List

```python
from src.todo_list import TodoListManager

# Create manager
todo = TodoListManager()

# Add task
task = todo.add_task(
    "Complete MIKE setup",
    priority="high",
    due_date="2026-09-20"
)

# Show tasks
print(todo.display_all_tasks())
```

---

## Quick Reference

### Essential Commands

| Task | Command |
|------|---------|
| Check Python | `python --version` |
| Create venv | `python -m venv venv` |
| Activate venv | `venv\Scripts\activate` |
| Install deps | `pip install -r requirements.txt` |
| Run MIKE (text) | `python -m src.mike --text` |
| Run MIKE (voice) | `python -m src.mike --voice` |
| Deactivate venv | `deactivate` |

---

## Getting Help

### If Something Goes Wrong

1. **Read the error message carefully** - It usually tells you the problem
2. **Check troubleshooting section above**
3. **Try reinstalling dependencies:**
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```
4. **Restart your computer** - Solves many issues
5. **Try text mode first** - Simpler than voice mode

---

## Next Steps

✅ **Installation Complete!**

You can now:
1. Run MIKE in text mode
2. Give it commands to open applications
3. Experiment with voice mode
4. Integrate with digital clock
5. Add tasks to to-do list
6. Customize commands

**Start MIKE Now:**
```bash
python -m src.mike --text
```

---

## Support & Updates

- **Repository**: https://github.com/dearsymne-wq/ai-agent-platform
- **Issues**: Report problems on GitHub
- **Updates**: Pull latest changes with `git pull`

---

**Welcome to MIKE AI Agent!** 🤖✨

Now you're ready to use your personal AI assistant!
