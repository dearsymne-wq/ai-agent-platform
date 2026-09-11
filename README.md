# MIKE - Personal AI Agent Platform

A sophisticated AI agent platform for Windows automation and personal assistance, inspired by Stonic AI.

## Features

- 🎤 **Voice Activation** - Natural language voice commands
- 🤖 **Multi-Agent System** - Specialized agents for different tasks
- 💻 **Windows Desktop Automation** - Control your PC with AI
- 🔌 **Rich Integrations** - Connect to multiple services
- 🧠 **Intelligent Processing** - Advanced NLP and decision-making
- 📱 **Cross-Platform Support** - Web and desktop interfaces

## Getting Started

### Prerequisites

- Python 3.9+
- Windows 10/11
- 4GB+ RAM
- Internet connection

### Installation

```bash
git clone https://github.com/dearsymne-wq/ai-agent-platform.git
cd ai-agent-platform
pip install -r requirements.txt
```

### Quick Start

```python
from src.mike import MIKEAgent

# Initialize your MIKE agent
mike = MIKEAgent()
asyncio.run(mike.start())
```

## Architecture

```
MIKE Agent Platform
├── Voice Engine (Speech-to-Text/Text-to-Speech)
├── NLP Processing (Intent Recognition)
├── Agent Management (Multi-agent Orchestration)
├── Windows Automation (Desktop Control)
├── Integration Layer (APIs & Services)
└── User Interface (Web Dashboard & Voice)
```

## Core Components

- **Voice Input/Output**: Google Cloud Speech-to-Text, Text-to-Speech
- **NLP Engine**: Transformers, spaCy
- **PC Automation**: PyAutoGUI, pywinauto
- **APIs**: OpenAI GPT, Hugging Face
- **Backend**: FastAPI
- **Frontend**: React/Vue

## Quick Commands

Text Mode:
```bash
python -m src.mike --text
```

Voice Mode:
```bash
python -m src.mike --voice
```

## Available Commands

- `Open notepad` - Open Notepad
- `Open calculator` - Open Calculator
- `Open chrome` - Open Chrome browser
- `Help` - Show available commands
- `Exit` - Quit MIKE

## Documentation

- [Setup Guide](./docs/SETUP.md)
- [Agent Configuration](./docs/AGENT_CONFIG.md)
- [Windows Automation](./docs/AUTOMATION.md)
- [API Reference](./docs/API.md)

## License

MIT License - See LICENSE file for details
