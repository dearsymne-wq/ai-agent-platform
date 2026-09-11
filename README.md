# 🤖 MIKE AI Agent - Personal AI Assistant Platform

## ⚡ Quick Start (30 seconds)

### For Windows Users:
1. **Download** the repository
2. **Double-click** `setup.bat`
3. **Follow** the wizard
4. **Done!** MIKE is running 🎉

---

## 📋 Table of Contents

- [What is MIKE?](#what-is-mike)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Running MIKE](#running-mike)
- [Available Commands](#available-commands)
- [Documentation](#documentation)
- [Modules](#modules)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 What is MIKE?

**MIKE** (Multi-Intelligent Knowledge Engine) is your personal AI assistant that runs on your Windows computer.

MIKE can:
- 🖥️ **Open applications** - Launch any Windows app with voice or text
- 🎤 **Listen to voice commands** - Hands-free operation
- 💬 **Understand intent** - Know what you want to do
- 🌍 **Manage multiple time zones** - View world clocks
- 📝 **Track tasks** - To-do list with local storage
- 🤖 **Multi-agent system** - Specialized agents for different tasks
- 🔄 **Remember interactions** - Conversation history

---

## ✨ Features

### Core Features
✅ **Voice Recognition** - Speak commands naturally  
✅ **Text Commands** - Type instructions  
✅ **Application Launcher** - Open any Windows app  
✅ **Intent Recognition** - Understands what you want  
✅ **Desktop Automation** - Control your PC  
✅ **Conversation History** - Remembers interactions  

### Additional Features
✅ **Digital Clock** - View time in 15+ time zones  
✅ **To-Do List** - Manage tasks with local storage  
✅ **Multi-Agent System** - Specialized agents for tasks  
✅ **Business Hours Checker** - See working hours globally  
✅ **Task Statistics** - Track completion rate  

---

## 🖥️ System Requirements

### Hardware
- **Processor**: Dual-core or better
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 2GB free space
- **Microphone**: Optional (for voice mode)
- **Speakers**: Optional (for voice feedback)

### Software
- **OS**: Windows 10 or Windows 11
- **Python**: 3.9 or higher
- **Internet**: Required for speech recognition

---

## 📥 Installation

### Method 1: Automatic Setup (EASIEST)

**1. Download Repository**
- Visit https://github.com/dearsymne-wq/ai-agent-platform
- Click "Code" → "Download ZIP"
- Extract the folder

**2. Run Setup**
- Double-click `setup.bat`
- Follow the wizard
- Choose your preferred mode

**That's it!** ✨

### Method 2: Manual Setup

```bash
# 1. Clone repository
git clone https://github.com/dearsymne-wq/ai-agent-platform.git
cd ai-agent-platform

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run MIKE
python -m src.mike --text
```

---

## 🚀 Running MIKE

### Quick Start Scripts

**Text Mode (Recommended for First Time)**
```bash
Double-click: run_mike.bat
```

**Voice Mode (Requires Microphone)**
```bash
Double-click: run_mike_voice.bat
```

### Manual Command Line

**Text Mode**
```bash
python -m src.mike --text
```

**Voice Mode**
```bash
python -m src.mike --voice
```

**Debug Mode**
```bash
python -m src.mike --text --debug
```

---

## 💬 Available Commands

### Opening Applications
```
Open notepad          → Opens Notepad
Open calculator       → Opens Calculator  
Open paint            → Opens Paint
Open explorer         → Opens File Explorer
Open chrome           → Opens Google Chrome
Open firefox          → Opens Firefox
Open word             → Opens Microsoft Word
Open excel            → Opens Microsoft Excel
```

### Information
```
Help                  → Shows all commands
What can you do?      → Lists capabilities
How do you work?      → Explains MIKE
```

### Exit
```
Exit                  → Stops MIKE
Quit                  → Stops MIKE
```

---

## 📚 Documentation

### Available Guides

1. **SETUP_GUIDE.md** - Detailed step-by-step setup instructions
2. **QUICK_START.md** - Fast reference guide
3. **This file (README.md)** - Project overview

### Reading the Documentation

1. **First time?** → Read `QUICK_START.md`
2. **Need detailed help?** → Read `docs/SETUP_GUIDE.md`
3. **Troubleshooting?** → Check troubleshooting section in SETUP_GUIDE.md

---

## 🏗️ Project Structure

```
ai-agent-platform/
│
├── src/                          # Source code
│   ├── mike.py                   # Main MIKE agent
│   ├── digital_clock.py          # Time zone management
│   ├── todo_list.py              # Task management
│   └── agents/                   # Agent modules
│       ├── base_agent.py         # Base agent class
│       ├── automation_agent.py   # App automation
│       ├── assistant_agent.py    # General assistant
│       └── clock_agent.py        # Clock agent
│
├── docs/                         # Documentation
│   ├── SETUP_GUIDE.md           # Detailed setup guide
│   ├── QUICK_START.md           # Quick reference
│   └── TROUBLESHOOTING.md       # Common issues & fixes
│
├── data/                         # Data storage
│   └── tasks.json               # Saved to-do tasks
│
├── setup.bat                     # Automatic setup wizard
├── run_mike.bat                  # Run text mode
├── run_mike_voice.bat            # Run voice mode
├── requirements.txt              # Python dependencies
├── .env.example                  # Configuration template
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

---

## 📦 Modules

### MIKE Agent (`src/mike.py`)
Core agent that processes commands and manages other agents.

**Key Features:**
- Processes voice and text commands
- Integrates with automation agent
- Manages conversation history
- Handles intent recognition

### Digital Clock (`src/digital_clock.py`)
Displays current time in multiple time zones.

**Supported Zones:**
- UTC, EST, CST, MST, PST
- GMT, CET, IST, JST, AEST
- SGT, HKT, NZST, Dubai, BRT

**Features:**
- View all time zones at once
- Get time in specific zone
- Calculate time differences
- Check business hours globally

### To-Do List (`src/todo_list.py`)
Local task management with persistent storage.

**Features:**
- Add/edit/delete tasks
- Mark tasks complete
- Set priority levels
- Filter by status or priority
- View statistics
- Save to local JSON file

### Clock Agent (`src/agents/clock_agent.py`)
MIKE integration for clock functionality.

**Commands:**
- Show all clocks
- View time in specific zone
- Display business hours
- Switch time formats

### Automation Agent (`src/agents/automation_agent.py`)
Handles Windows application launching and control.

**Features:**
- Launch applications
- Automate user actions
- Control keyboard/mouse
- Window management

---

## 🎮 Usage Examples

### Example 1: Basic Commands

```
👤 You: Open notepad
🤖 MIKE: ✅ Opened notepad

👤 You: Open calculator
🤖 MIKE: ✅ Opened calculator

👤 You: Help
🤖 MIKE: [Shows available commands]
```

### Example 2: Using Digital Clock

```python
from src.digital_clock import DigitalClock

clock = DigitalClock()
print(clock.display_all_clocks())
```

### Example 3: Using To-Do List

```python
from src.todo_list import TodoListManager

todo = TodoListManager()
todo.add_task("Complete MIKE setup", priority="high")
print(todo.display_all_tasks())
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file (copy from `.env.example`):

```env
# Optional API keys
OPENAI_API_KEY=your_key_here
GOOGLE_CLOUD_KEY=path/to/key.json

# MIKE Configuration
MIKE_NAME=MIKE
MIKE_VOICE_ENABLED=true
MIKE_DEBUG_MODE=false
```

*(MIKE works without these - they're for advanced features)*

---

## 🐛 Troubleshooting

### Common Issues

**Python not found**
- Reinstall Python with "Add Python to PATH" checked
- Restart your computer

**Modules not found**
- Activate virtual environment: `venv\Scripts\activate`
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

**Microphone not working**
- Check Windows Sound Settings
- Test microphone is working
- Use text mode instead

**Application won't open**
- Make sure application is installed
- Try different application
- Check if app name is correct

**See detailed troubleshooting:** `docs/SETUP_GUIDE.md`

---

## 📈 Performance Tips

- **Faster startup**: Use `.bat` files instead of typing
- **Better voice**: Use a quality microphone
- **Less lag**: Close unnecessary programs
- **Stable**: Keep internet connection active

---

## 🤝 Contributing

Want to help improve MIKE?

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** a pull request

---

## 📖 Learning Resources

### Getting Started
- [Python Official Site](https://www.python.org)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

### Libraries Used
- [PyAutoGUI](https://pyautogui.readthedocs.io/) - Desktop automation
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) - Voice input
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [Pydantic](https://docs.pydantic.dev/) - Data validation

---

## 🎓 Next Steps

After getting MIKE running:

1. ✅ Try all application commands
2. ✅ Experiment with voice mode
3. ✅ Add custom commands
4. ✅ Use digital clock features
5. ✅ Create a to-do list
6. ✅ Explore advanced features
7. ✅ Contribute to the project!

---

## 📞 Support

### Need Help?

1. **Check Documentation**
   - `docs/SETUP_GUIDE.md` - Detailed guide
   - `docs/QUICK_START.md` - Quick reference

2. **Common Issues**
   - See "Troubleshooting" section above
   - Check SETUP_GUIDE.md for detailed solutions

3. **Report Issues**
   - Create an issue on GitHub
   - Include error messages and steps to reproduce

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🙌 Credits

**MIKE AI Agent** was created by the AI Agent Development Team.

### Technologies Used
- Python 3.9+
- PyAutoGUI
- SpeechRecognition
- FastAPI
- PyTorch
- Transformers

---

## 🚀 Getting Started Right Now

### Option 1: Super Easy (Recommended)
```bash
# Just double-click this file:
setup.bat
```

### Option 2: Manual
```bash
python -m src.mike --text
```

### Option 3: Voice Mode
```bash
python -m src.mike --voice
```

---

## 📊 Project Status

- ✅ Core Features: Complete
- ✅ Digital Clock: Complete
- ✅ To-Do List: Complete
- ✅ Documentation: Complete
- 🔄 Voice Improvements: Ongoing
- 🔄 Web Dashboard: In Progress

---

## 🎯 Roadmap

### Version 2.0 (Next)
- [ ] Web Dashboard
- [ ] REST API
- [ ] Database Support
- [ ] Email Integration
- [ ] Calendar Integration
- [ ] Advanced Automation

### Version 3.0 (Future)
- [ ] Mobile App
- [ ] Cloud Sync
- [ ] AI Chat Integration
- [ ] Advanced ML Models
- [ ] Cross-Platform Support

---

## 💡 Pro Tips

1. **Keep MIKE running** in background while working
2. **Use batch files** for quick startup
3. **Test commands** before automating them
4. **Monitor logs** for errors
5. **Back up your data** (tasks.json)
6. **Keep dependencies updated** regularly
7. **Use voice mode** for hands-free operation

---

## 🎉 Success!

You now have MIKE AI Agent installed and ready to use!

**Start Now:**
```bash
python -m src.mike --text
```

**Questions?** Check the documentation files in the `docs/` folder.

**Happy coding!** 🚀✨

---

## 📫 Stay Updated

- Star ⭐ this repository
- Watch 👀 for updates
- Follow for new features
- Contribute 🤝 to the project

---

**MIKE AI Agent - Your Personal Desktop Assistant** 🤖

*Making Windows automation easy and fun!*
