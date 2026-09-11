"""
MIKE Agent - Automation Agent Implementation
Handles Windows desktop automation and system control
"""

import logging
import subprocess
from typing import Any, Dict
from .base_agent import BaseAgent


class AutomationAgent(BaseAgent):
    """Agent for Windows automation and system control"""
    
    def __init__(self):
        super().__init__(
            name="AutomationAgent",
            description="Handles Windows automation, application launching, and system control"
        )
        
        self.applications = {
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'paint': 'mspaint.exe',
            'word': 'winword.exe',
            'excel': 'excel.exe',
            'chrome': 'chrome.exe',
            'firefox': 'firefox.exe',
            'explorer': 'explorer.exe',
            'cmd': 'cmd.exe',
            'powershell': 'powershell.exe',
        }
    
    async def process(self, command: str) -> Dict[str, Any]:
        """Process automation command"""
        self.logger.info(f"Processing automation: {command}")
        
        if not self.enabled:
            return {
                'success': False,
                'response': 'Automation agent is disabled',
                'agent': self.name
            }
        
        try:
            # Parse command
            parts = command.lower().split()
            
            if parts[0] in ['open', 'launch', 'start'] and len(parts) > 1:
                app_name = parts[1]
                success = await self.open_application(app_name)
                return {
                    'success': success,
                    'response': f"{'✅ Opened' if success else '❌ Could not open'} {app_name}",
                    'agent': self.name
                }
            
            return {
                'success': False,
                'response': f"Unknown automation command: {command}",
                'agent': self.name
            }
            
        except Exception as e:
            self.logger.error(f"Automation error: {e}")
            return {
                'success': False,
                'response': f"Error: {str(e)}",
                'agent': self.name
            }
    
    async def open_application(self, app_name: str) -> bool:
        """Open a Windows application"""
        try:
            app_path = self.applications.get(app_name.lower())
            if app_path:
                subprocess.Popen(app_path)
                self.logger.info(f"Opened {app_name}")
                return True
            else:
                self.logger.warning(f"Application {app_name} not found")
                return False
        except Exception as e:
            self.logger.error(f"Failed to open {app_name}: {e}")
            return False
