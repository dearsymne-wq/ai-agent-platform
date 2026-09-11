# 🎯 MIKE AI Agent - Quick Start Guide

## ⚡ 5-Minute Quick Start

### Step 1: Open Command Prompt
```
Press: Win + R
Type: cmd
Press: Enter
```

### Step 2: Navigate to Project Folder
```bash
cd C:\Users\YourName\Documents\ai-agent-platform
```
*(Replace YourName with your actual Windows username)*

### Step 3: Activate Virtual Environment
```bash
venv\Scripts\activate
```
You should see `(venv)` at the beginning of your command line.

### Step 4: Run MIKE
```bash
python -m src.mike --text
```

### Step 5: Give Commands
```
👤 You: Open notepad
🤖 MIKE: ✅ Opened notepad

👤 You: Help
🤖 MIKE: [Shows help text]

👤 You: exit
```

**That's it! MIKE is running!** 🎉

---

## 📋 All Available Commands

### 🖥️ Application Commands
- `Open notepad` - Opens Notepad
- `Open calculator` - Opens Calculator
- `Open paint` - Opens Paint
- `Open explorer` - Opens File Explorer
- `Open chrome` - Opens Chrome (if installed)
- `Open firefox` - Opens Firefox (if installed)
- `Open word` - Opens Word (if installed)
- `Open excel` - Opens Excel (if installed)

### ℹ️ Information Commands
- `Help` - Shows all commands
- `What can you do?` - Lists capabilities
- `How do you work?` - Explains how MIKE works

### 🛑 Exit Commands
- `Exit` - Stops MIKE
- `Quit` - Stops MIKE

---

## 🎤 Voice Mode Commands

Same as text mode, but speak them:

```
(Speak): "Open notepad"
(MIKE responds): "✅ Opened notepad"

(Speak): "Open calculator"  
(MIKE responds): "✅ Opened calculator"

(Speak): "Help"
(MIKE responds): [Reads help text]
```

---

## 🚀 Running Modes

### Text Mode (Recommended for First Time)
```bash
python -m src.mike --text
```
- Type commands
- No microphone needed
- Easiest to troubleshoot

### Voice Mode (Requires Microphone)
```bash
python -m src.mike --voice
```
- Speak commands
- Requires working microphone
- MIKE responds with voice

### Debug Mode
```bash
python -m src.mike --text --debug
```
- Shows detailed logs
- Helpful for troubleshooting

---

## 📂 Project Files Explained

```
ai-agent-platform/
│
├── src/                          # Source code folder
│   ├── mike.py                   # Main MIKE agent
│   ├── digital_clock.py          # Clock with time zones
│   ├── todo_list.py              # To-do list manager
│   └── agents/                   # Agent modules
│       ├── base_agent.py         # Base class for all agents
│       ├── automation_agent.py   # App automation
│       ├── assistant_agent.py    # General assistant
│       └── clock_agent.py        # Clock operations
│
├── docs/                         # Documentation
│   ├── SETUP_GUIDE.md           # Detailed setup guide
│   └── QUICK_START.md           # This file
│
├── data/                         # Data storage (created automatically)
│   └── tasks.json               # Saved to-do tasks
│
├── requirements.txt              # List of dependencies
├── .env.example                  # Configuration template
├── .gitignore                    # Git ignore rules
└── README.md                     # Main documentation
```

---

## 🔧 Installation Checklist

- [ ] Python 3.9+ installed
- [ ] Repository downloaded/cloned
- [ ] Virtual environment created: `python -m venv venv`
- [ ] Virtual environment activated: `venv\Scripts\activate`
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] MIKE runs: `python -m src.mike --text`

---

## ⚠️ Common Issues & Quick Fixes

### Issue: "python is not recognized"
**Fix:** Reinstall Python and check "Add Python to PATH"

### Issue: "ModuleNotFoundError"
**Fix:** 
```bash
venv\Scripts\activate
pip install -r requirements.txt --force-reinstall
```

### Issue: Virtual environment won't activate
**Fix:**
```bash
python -m venv venv
venv\Scripts\activate.bat
```

### Issue: Microphone not working (voice mode)
**Fix:** Use text mode instead or check Windows Sound Settings

### Issue: Application won't open
**Fix:** 
- Make sure application is installed
- Use correct name (e.g., "chrome" not "Google Chrome")
- Try different application

---

## 💾 Saving Your Session

### Create a Batch File to Run MIKE Easily

**1. Open Notepad**
```
Press: Win + R
Type: notepad
Press: Enter
```

**2. Copy this code:**
```batch
@echo off
cd /d C:\Users\YourName\Documents\ai-agent-platform
call venv\Scripts\activate
python -m src.mike --text
pause
```

**3. Save as:**
- Name: `run_mike.bat`
- Location: Your `ai-agent-platform` folder
- Type: All Files (*.*)

**4. Run MIKE Anytime:**
- Double-click `run_mike.bat`
- MIKE starts immediately!

---

## 🌍 Using with Digital Clock

Once MIKE is running, you can use the clock feature:

```python
from src.digital_clock import DigitalClock

clock = DigitalClock()
print(clock.display_all_clocks())
```

**Supported Time Zones:**
- UTC, EST, CST, MST, PST
- GMT, CET, IST, JST, AEST
- SGT, HKT, NZST, Dubai, BRT

---

## 📝 Using with To-Do List

Manage your tasks:

```python
from src.todo_list import TodoListManager

todo = TodoListManager()

# Add task
todo.add_task("Complete MIKE setup", priority="high")

# Show tasks
print(todo.display_all_tasks())

# Mark complete
todo.complete_task(task_id)
```

---

## 🎨 Customizing MIKE

### Add Your Own Commands

Edit `src/mike.py` and modify the `_handle_intent` method:

```python
async def _handle_intent(self, intent: str, command: str) -> str:
    # ... existing code ...
    
    elif intent == 'custom':
        return "Your custom response here"
```

### Add Custom Applications

Edit the `apps` dictionary in `src/mike.py`:

```python
apps = {
    'notepad': 'notepad.exe',
    'custom': 'path/to/your/app.exe',  # Add this line
    # ... more apps ...
}
```

---

## 📊 System Requirements Check

Run this to verify everything:

```bash
# Check Python version
python --version

# Check if main libraries are installed
python -c "import pyautogui; print('✅ PyAutoGUI OK')"
python -c "import speech_recognition; print('✅ Speech Recognition OK')"
python -c "import pyttsx3; print('✅ Text-to-Speech OK')"
```

---

## 🔗 Useful Links

- **GitHub Repository**: https://github.com/dearsymne-wq/ai-agent-platform
- **Python Documentation**: https://docs.python.org/3/
- **PyAutoGUI Docs**: https://pyautogui.readthedocs.io/
- **SpeechRecognition Docs**: https://github.com/Uberi/speech_recognition

---

## 📞 Getting Help

### Check These Resources First
1. **docs/SETUP_GUIDE.md** - Detailed setup instructions
2. **README.md** - Project overview
3. **Troubleshooting section** (above)

### If You Find a Bug
1. Check if it's in the troubleshooting section
2. Try reinstalling dependencies
3. Restart your computer
4. Report it on GitHub Issues

---

## 🎯 What's Next?

After you get MIKE running:

1. ✅ Try all application commands
2. ✅ Test voice mode (if you have a microphone)
3. ✅ Create a batch file for easy launching
4. ✅ Add custom commands
5. ✅ Integrate with digital clock
6. ✅ Use the to-do list feature
7. ✅ Explore advanced features

---

## 📈 Performance Tips

- **Faster startup**: Use batch file instead of typing each time
- **Better voice recognition**: Use a better microphone
- **Less lag**: Close unnecessary programs
- **Stable operation**: Keep internet connection active

---

## 🎓 Learning Resources

Want to extend MIKE further?

- **Python Basics**: Learn about variables, functions, loops
- **Async Programming**: Understand `async/await` syntax
- **APIs**: How to integrate external services
- **Databases**: Store data persistently

Start with Python basics at https://www.python.org/about/gettingstarted/

---

## 🎉 Success Checklist

- [ ] Python installed and working
- [ ] Repository downloaded
- [ ] Virtual environment created and activated
- [ ] Dependencies installed
- [ ] MIKE runs in text mode
- [ ] MIKE responds to commands
- [ ] Batch file created for easy launching
- [ ] Voice mode tested (if microphone available)

**Once all checked, you're a MIKE expert!** 🚀

---

## 💡 Pro Tips

1. **Keep MIKE running in background** while working
2. **Use batch file** for fast startup
3. **Test commands** before automating them
4. **Keep dependencies updated**: `pip install -r requirements.txt --upgrade`
5. **Back up your data folder** (contains saved tasks)
6. **Monitor console output** for errors and logs
7. **Use voice mode** for hands-free operation

---

## 🚀 You're All Set!

**Start MIKE Now:**
```bash
python -m src.mike --text
```

**Welcome to your personal AI assistant!** 🤖✨

Questions? Check the SETUP_GUIDE.md or README.md for more details!
