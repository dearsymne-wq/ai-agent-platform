"""
MIKE - Personal AI Agent
A voice-activated, multi-agent AI platform for Windows automation and personal assistance.
"""

import os
import sys
import asyncio
import logging
from typing import Optional, Dict, Any
from datetime import datetime

try:
    import speech_recognition as sr
    import pyttsx3
except ImportError:
    print("Warning: Voice dependencies not installed. Install with: pip install -r requirements.txt")

from pydantic_settings import BaseSettings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MIKEConfig(BaseSettings):
    """Configuration for MIKE Agent"""
    name: str = "MIKE"
    voice_enabled: bool = True
    auto_start: bool = False
    debug_mode: bool = False
    openai_api_key: Optional[str] = None
    google_cloud_key: Optional[str] = None
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


class VoiceEngine:
    """Handles speech-to-text and text-to-speech"""
    
    def __init__(self, rate: int = 150):
        try:
            self.recognizer = sr.Recognizer()
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('rate', rate)
            self.logger = logging.getLogger(__name__)
            self.available = True
        except Exception as e:
            self.logger = logging.getLogger(__name__)
            self.logger.warning(f"Voice engine not available: {e}")
            self.available = False
    
    def listen(self) -> Optional[str]:
        """
        Listen for voice input and convert to text
        Returns: Transcribed text or None if recognition failed
        """
        if not self.available:
            return None
            
        try:
            with sr.Microphone() as source:
                self.logger.info("🎤 Listening...")
                audio = self.recognizer.listen(source, timeout=5)
                
            # Try Google Speech Recognition
            text = self.recognizer.recognize_google(audio)
            self.logger.info(f"Recognized: {text}")
            return text
            
        except sr.UnknownValueError:
            self.logger.warning("Could not understand audio")
            return None
        except sr.RequestError as e:
            self.logger.error(f"Speech recognition error: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Microphone error: {e}")
            return None
    
    def speak(self, text: str) -> None:
        """Convert text to speech"""
        if not self.available:
            return
            
        try:
            self.logger.info(f"Speaking: {text}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            self.logger.error(f"TTS error: {e}")


class NLPEngine:
    """Natural Language Processing for intent recognition"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.intents = {
            'open': ['open', 'launch', 'start'],
            'close': ['close', 'quit', 'exit', 'stop'],
            'execute': ['run', 'execute', 'do'],
            'search': ['search', 'find', 'look for'],
            'navigate': ['go to', 'navigate'],
            'help': ['help', 'what can you do', 'how do you work'],
        }
    
    def extract_intent(self, text: str) -> Dict[str, Any]:
        """Extract intent from user input"""
        text_lower = text.lower()
        
        for intent, keywords in self.intents.items():
            for keyword in keywords:
                if keyword in text_lower:
                    return {
                        'intent': intent,
                        'confidence': 0.8,
                        'text': text,
                        'timestamp': datetime.now().isoformat()
                    }
        
        return {
            'intent': 'unknown',
            'confidence': 0.0,
            'text': text,
            'timestamp': datetime.now().isoformat()
        }


class WindowsAutomation:
    """Windows desktop automation"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def open_application(self, app_name: str) -> bool:
        """Open a Windows application"""
        try:
            import subprocess
            apps = {
                'notepad': 'notepad.exe',
                'calculator': 'calc.exe',
                'paint': 'mspaint.exe',
                'word': 'winword.exe',
                'excel': 'excel.exe',
                'chrome': 'chrome.exe',
                'firefox': 'firefox.exe',
                'explorer': 'explorer.exe',
            }
            
            app_path = apps.get(app_name.lower())
            if app_path:
                subprocess.Popen(app_path)
                self.logger.info(f"Opened {app_name}")
                return True
            else:
                self.logger.warning(f"Application {app_name} not found")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to open application: {e}")
            return False


class MIKEAgent:
    """
    Main MIKE Agent Class
    Central coordinator for all agent functionalities
    """
    
    def __init__(self, config: Optional[MIKEConfig] = None):
        self.config = config or MIKEConfig()
        self.logger = logging.getLogger(self.config.name)
        
        # Initialize components
        self.voice_engine = VoiceEngine() if self.config.voice_enabled else None
        self.nlp_engine = NLPEngine()
        self.automation = WindowsAutomation()
        
        self.running = False
        self.conversation_history = []
        
        self.logger.info(f"✅ {self.config.name} Agent initialized")
    
    async def process_command(self, command: str) -> str:
        """Process user command and return response"""
        
        # Extract intent
        intent_result = self.nlp_engine.extract_intent(command)
        intent = intent_result['intent']
        
        self.logger.info(f"Intent detected: {intent}")
        
        # Handle intent
        response = await self._handle_intent(intent, command)
        
        # Store in history
        self.conversation_history.append({
            'timestamp': datetime.now().isoformat(),
            'user': command,
            'agent': response,
            'intent': intent
        })
        
        return response
    
    async def _handle_intent(self, intent: str, command: str) -> str:
        """Handle specific intents"""
        
        if intent == 'open':
            parts = command.lower().split()
            if len(parts) > 1:
                app_name = parts[1]
                success = self.automation.open_application(app_name)
                return f"{'✅ Opened' if success else '❌ Could not open'} {app_name}"
            return "Please specify which application to open"
        
        elif intent == 'help':
            return self._get_help_text()
        
        elif intent == 'close':
            return "Closing application"
        
        elif intent == 'search':
            return f"Searching for: {command}"
        
        else:
            return f"I received your command: '{command}'. This feature is being developed."
    
    def _get_help_text(self) -> str:
        """Return help information"""
        return """
🤖 I'm MIKE, your personal AI assistant. I can help you with:

📋 Application Control:
   • 'Open notepad' - Opens Notepad
   • 'Open calculator' - Opens Calculator
   • 'Open chrome' - Launches Chrome browser
   • 'Open explorer' - Opens File Explorer

⚙️ System Control:
   • Desktop automation
   • Window management
   • Application launching

📚 Information:
   • 'Help' - Show this help message

Try saying 'Open notepad' to get started!
        """
    
    async def voice_loop(self) -> None:
        """Main voice interaction loop"""
        if not self.voice_engine or not self.voice_engine.available:
            self.logger.error("Voice engine not available")
            return
        
        self.logger.info("🎤 Voice loop started. Listening...")
        
        while self.running:
            try:
                command = self.voice_engine.listen()
                
                if command:
                    response = await self.process_command(command)
                    self.voice_engine.speak(response)
                
                await asyncio.sleep(0.1)
                
            except KeyboardInterrupt:
                self.logger.info("Voice loop interrupted")
                break
            except Exception as e:
                self.logger.error(f"Voice loop error: {e}")
                await asyncio.sleep(1)
    
    async def text_loop(self) -> None:
        """Text-based interaction loop"""
        self.logger.info("💬 Text mode started. Type 'exit' to quit.")
        
        while self.running:
            try:
                command = input("\n👤 You: ").strip()
                
                if command.lower() in ['exit', 'quit']:
                    break
                
                if command:
                    response = await self.process_command(command)
                    print(f"\n🤖 {self.config.name}: {response}")
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                self.logger.error(f"Text loop error: {e}")
    
    async def start(self, voice_mode: bool = False) -> None:
        """Start MIKE agent"""
        self.running = True
        self.logger.info(f"🚀 Starting {self.config.name} Agent...")
        print(f"\n{'='*50}")
        print(f"🎯 MIKE Agent Started")
        print(f"{'='*50}\n")
        
        try:
            if voice_mode and self.voice_engine and self.voice_engine.available:
                await self.voice_loop()
            else:
                await self.text_loop()
        except Exception as e:
            self.logger.error(f"Agent error: {e}")
        finally:
            self.stop()
    
    def stop(self) -> None:
        """Stop MIKE agent"""
        self.running = False
        print(f"\n{'='*50}")
        print(f"🛑 {self.config.name} Agent stopped")
        print(f"{'='*50}\n")
        self.logger.info(f"🛑 {self.config.name} Agent stopped")


def main():
    """Entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="MIKE - Personal AI Agent")
    parser.add_argument('--voice', action='store_true', help='Start in voice mode')
    parser.add_argument('--text', action='store_true', help='Start in text mode')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    
    args = parser.parse_args()
    
    # Create config
    config = MIKEConfig(debug_mode=args.debug)
    
    # Create agent
    agent = MIKEAgent(config=config)
    
    # Start agent
    try:
        # Default to text mode if neither specified
        voice_mode = args.voice and not args.text
        asyncio.run(agent.start(voice_mode=voice_mode))
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        agent.stop()


if __name__ == "__main__":
    main()
