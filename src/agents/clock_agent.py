"""
Clock Agent for MIKE
Integrates digital clock with MIKE agent for voice/text commands
"""

import logging
from typing import Any, Dict, Optional
from src.agents.base_agent import BaseAgent
from src.digital_clock import DigitalClock, TimeFormat


class ClockAgent(BaseAgent):
    """Agent for managing time zones and displaying clocks"""
    
    def __init__(self):
        super().__init__(
            name="ClockAgent",
            description="Manages time zones, displays current time, and provides clock utilities"
        )
        self.clock = DigitalClock()
        self.logger = logging.getLogger(__name__)
    
    async def process(self, command: str) -> Dict[str, Any]:
        """Process clock-related commands"""
        self.logger.info(f"Processing clock command: {command}")
        
        if not self.enabled:
            return {
                'success': False,
                'response': 'Clock agent is disabled',
                'agent': self.name
            }
        
        try:
            command_lower = command.lower()
            
            # Show all clocks
            if 'show all' in command_lower or 'all clocks' in command_lower or 'display all' in command_lower:
                response = self.clock.display_all_clocks()
                return {
                    'success': True,
                    'response': response,
                    'agent': self.name,
                    'command_type': 'show_all'
                }
            
            # Show time in specific zone
            elif 'time in' in command_lower or 'what time' in command_lower:
                for zone_code, (zone_name, _, display_name) in self.clock.POPULAR_ZONES.items():
                    if zone_code.lower() in command_lower or zone_name.lower() in command_lower:
                        response = self.clock.display_detailed_clock(zone_name)
                        return {
                            'success': True,
                            'response': response,
                            'agent': self.name,
                            'command_type': 'show_timezone'
                        }
            
            # Business hours status
            elif 'business' in command_lower or 'working hours' in command_lower:
                response = self.clock.display_business_hours()
                return {
                    'success': True,
                    'response': response,
                    'agent': self.name,
                    'command_type': 'business_hours'
                }
            
            # Time difference between zones
            elif 'difference' in command_lower or 'between' in command_lower:
                response = "Available time zones: UTC, EST, CST, MST, PST, GMT, CET, IST, JST, AEST, SGT, HKT, NZST, Dubai, BRT\n"
                response += "Usage: 'What is the time difference between EST and JST?'"
                return {
                    'success': True,
                    'response': response,
                    'agent': self.name,
                    'command_type': 'help'
                }
            
            # Switch time format
            elif '24 hour' in command_lower or '24h' in command_lower:
                self.clock.set_time_format(TimeFormat.TWENTY_FOUR_HOUR)
                response = "⏱️ Time format switched to 24-hour\n" + self.clock.display_all_clocks()
                return {
                    'success': True,
                    'response': response,
                    'agent': self.name,
                    'command_type': 'format_changed'
                }
            
            elif '12 hour' in command_lower or '12h' in command_lower:
                self.clock.set_time_format(TimeFormat.TWELVE_HOUR)
                response = "⏱️ Time format switched to 12-hour\n" + self.clock.display_all_clocks()
                return {
                    'success': True,
                    'response': response,
                    'agent': self.name,
                    'command_type': 'format_changed'
                }
            
            # Add timezone
            elif 'add' in command_lower or 'add timezone' in command_lower:
                response = "Available zones to add:\n"
                for code, (zone_name, emoji, display_name) in self.clock.POPULAR_ZONES.items():
                    response += f"  • {code}: {display_name}\n"
                return {
                    'success': True,
                    'response': response,
                    'agent': self.name,
                    'command_type': 'help'
                }
            
            # Help
            elif 'help' in command_lower or 'clock help' in command_lower:
                response = self._get_help_text()
                return {
                    'success': True,
                    'response': response,
                    'agent': self.name,
                    'command_type': 'help'
                }
            
            # Default: show all clocks
            else:
                response = self.clock.display_all_clocks()
                return {
                    'success': True,
                    'response': response,
                    'agent': self.name,
                    'command_type': 'show_all'
                }
            
        except Exception as e:
            self.logger.error(f"Clock agent error: {e}")
            return {
                'success': False,
                'response': f"Error: {str(e)}",
                'agent': self.name
            }
    
    def _get_help_text(self) -> str:
        """Get help text for clock commands"""
        return """
🕐 CLOCK AGENT - AVAILABLE COMMANDS:

📋 View Clocks:
  • "Show all clocks" - Display all configured time zones
  • "What time in EST?" - Show time in Eastern timezone
  • "Show clocks" - Display all time zones

⏱️ Format Control:
  • "Switch to 24 hour" - Change to 24-hour format
  • "Switch to 12 hour" - Change to 12-hour format

💼 Business Hours:
  • "Business hours" - Show business hours status (9 AM - 5 PM)
  • "Show working hours" - Display working hours for all zones

🌍 Timezone Management:
  • "Add timezone" - Get list of available zones to add
  • "List all zones" - Show all configured zones

❓ Help:
  • "Clock help" - Show this help message

Available Time Zones:
  UTC, EST, CST, MST, PST, GMT, CET, IST, JST, AEST, SGT, HKT, NZST, Dubai, BRT
        """
    
    def add_timezone(self, zone_code: str) -> bool:
        """Add a timezone from popular zones"""
        if zone_code in self.clock.POPULAR_ZONES:
            zone_name, emoji, display_name = self.clock.POPULAR_ZONES[zone_code]
            return self.clock.add_timezone(zone_name, display_name, emoji)
        return False
    
    def remove_timezone(self, zone_name: str) -> bool:
        """Remove a timezone"""
        return self.clock.remove_timezone(zone_name)
    
    def get_all_timezones(self) -> list:
        """Get all configured timezones"""
        return self.clock.get_available_timezones()
    
    def get_timezone_count(self) -> int:
        """Get number of configured timezones"""
        return self.clock.get_timezone_count()
