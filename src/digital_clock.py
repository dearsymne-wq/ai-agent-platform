"""
Digital Clock with Multiple Time Zones
A comprehensive time zone display system for MIKE agent
"""

import datetime
import pytz
from typing import List, Dict, Optional, Any
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class TimeFormat(Enum):
    """Time format options"""
    TWELVE_HOUR = "12h"  # 3:45:30 PM
    TWENTY_FOUR_HOUR = "24h"  # 15:45:30


class TimeZoneInfo:
    """Represents a time zone with current time"""
    
    def __init__(self, zone_name: str, display_name: str = None, emoji: str = "🌍"):
        self.zone_name = zone_name
        self.display_name = display_name or zone_name
        self.emoji = emoji
        self.timezone = pytz.timezone(zone_name)
    
    def get_current_time(self) -> datetime.datetime:
        """Get current time in this timezone"""
        return datetime.datetime.now(self.timezone)
    
    def get_time_string(self, format_type: TimeFormat = TimeFormat.TWELVE_HOUR) -> str:
        """Get formatted time string"""
        current_time = self.get_current_time()
        
        if format_type == TimeFormat.TWELVE_HOUR:
            return current_time.strftime("%I:%M:%S %p")
        else:
            return current_time.strftime("%H:%M:%S")
    
    def get_date_string(self) -> str:
        """Get formatted date string"""
        current_time = self.get_current_time()
        return current_time.strftime("%A, %B %d, %Y")
    
    def get_full_datetime(self, format_type: TimeFormat = TimeFormat.TWELVE_HOUR) -> str:
        """Get full date and time"""
        return f"{self.get_date_string()} {self.get_time_string(format_type)}"
    
    def get_offset(self) -> str:
        """Get UTC offset"""
        current_time = self.get_current_time()
        offset = current_time.strftime("%z")
        # Format as +HH:MM or -HH:MM
        if offset:
            return f"{offset[:3]}:{offset[3:]}"
        return "UTC"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'zone_name': self.zone_name,
            'display_name': self.display_name,
            'emoji': self.emoji,
            'time': self.get_time_string(),
            'date': self.get_date_string(),
            'offset': self.get_offset()
        }
    
    def __str__(self) -> str:
        return f"{self.emoji} {self.display_name}: {self.get_time_string()}"


class DigitalClock:
    """Main Digital Clock with multiple time zones"""
    
    # Predefined popular time zones
    POPULAR_ZONES = {
        'UTC': ('UTC', '🌐', 'Coordinated Universal Time'),
        'EST': ('US/Eastern', '🗽', 'Eastern Time (New York)'),
        'CST': ('US/Central', '⭐', 'Central Time (Chicago)'),
        'MST': ('US/Mountain', '⛰️', 'Mountain Time (Denver)'),
        'PST': ('US/Pacific', '🌊', 'Pacific Time (Los Angeles)'),
        'GMT': ('Europe/London', '🇬🇧', 'Greenwich Mean Time (London)'),
        'CET': ('Europe/Paris', '🇫🇷', 'Central European Time (Paris)'),
        'IST': ('Asia/Kolkata', '🇮🇳', 'Indian Standard Time (India)'),
        'JST': ('Asia/Tokyo', '🇯🇵', 'Japan Standard Time (Tokyo)'),
        'AEST': ('Australia/Sydney', '🇦🇺', 'Australian Eastern Time (Sydney)'),
        'SGT': ('Asia/Singapore', '🇸🇬', 'Singapore Time'),
        'HKT': ('Asia/Hong_Kong', '🇭🇰', 'Hong Kong Time'),
        'NZST': ('Pacific/Auckland', '🇳🇿', 'New Zealand Standard Time'),
        'Dubai': ('Asia/Dubai', '🇦🇪', 'Gulf Standard Time (Dubai)'),
        'BRT': ('America/Sao_Paulo', '🇧🇷', 'Brasília Time (São Paulo)'),
    }
    
    def __init__(self):
        self.timezones: Dict[str, TimeZoneInfo] = {}
        self.time_format = TimeFormat.TWELVE_HOUR
        self.logger = logging.getLogger(__name__)
        
        # Add default popular timezones
        self.add_popular_zones(['UTC', 'EST', 'PST', 'GMT', 'IST', 'JST', 'AEST'])
    
    def add_timezone(self, zone_name: str, display_name: str = None, emoji: str = "🌍") -> bool:
        """Add a custom timezone"""
        try:
            tz_info = TimeZoneInfo(zone_name, display_name or zone_name, emoji)
            self.timezones[zone_name] = tz_info
            self.logger.info(f"Added timezone: {zone_name}")
            return True
        except Exception as e:
            self.logger.error(f"Error adding timezone {zone_name}: {e}")
            return False
    
    def add_popular_zones(self, zone_codes: List[str]) -> int:
        """Add multiple popular zones at once"""
        count = 0
        for code in zone_codes:
            if code in self.POPULAR_ZONES:
                zone_name, emoji, display_name = self.POPULAR_ZONES[code]
                if self.add_timezone(zone_name, display_name, emoji):
                    count += 1
        return count
    
    def remove_timezone(self, zone_name: str) -> bool:
        """Remove a timezone"""
        if zone_name in self.timezones:
            del self.timezones[zone_name]
            self.logger.info(f"Removed timezone: {zone_name}")
            return True
        return False
    
    def get_timezone(self, zone_name: str) -> Optional[TimeZoneInfo]:
        """Get a specific timezone"""
        return self.timezones.get(zone_name)
    
    def set_time_format(self, format_type: TimeFormat) -> None:
        """Set the time format for all zones"""
        self.time_format = format_type
        self.logger.info(f"Time format set to: {format_type.value}")
    
    def get_current_time_in_zone(self, zone_name: str) -> Optional[str]:
        """Get current time in a specific zone"""
        tz = self.get_timezone(zone_name)
        if tz:
            return tz.get_time_string(self.time_format)
        return None
    
    def get_all_timezones_data(self) -> Dict[str, Dict[str, Any]]:
        """Get data for all timezones"""
        return {name: tz.to_dict() for name, tz in self.timezones.items()}
    
    def display_all_clocks(self) -> str:
        """Display all clocks in a formatted view"""
        output = "\n⏰ DIGITAL CLOCK - ALL TIMEZONES\n"
        output += "=" * 70 + "\n"
        
        if not self.timezones:
            return output + "No timezones configured\n"
        
        # Sort by offset
        sorted_zones = sorted(
            self.timezones.items(),
            key=lambda x: x[1].get_offset()
        )
        
        for zone_name, tz_info in sorted_zones:
            time_str = tz_info.get_time_string(self.time_format)
            offset = tz_info.get_offset()
            output += f"{tz_info.emoji} {tz_info.display_name:30} | {time_str:12} | {offset}\n"
        
        output += "=" * 70 + "\n"
        return output
    
    def display_detailed_clock(self, zone_name: str) -> str:
        """Display detailed information for a specific timezone"""
        tz = self.get_timezone(zone_name)
        if not tz:
            return f"❌ Timezone {zone_name} not found\n"
        
        output = f"\n⏰ DETAILED CLOCK - {tz.display_name}\n"
        output += "=" * 60 + "\n"
        output += f"Timezone: {tz.zone_name}\n"
        output += f"Date: {tz.get_date_string()}\n"
        output += f"Time: {tz.get_time_string(self.time_format)}\n"
        output += f"UTC Offset: {tz.get_offset()}\n"
        
        # Check if DST is active
        current_time = tz.get_current_time()
        dst_active = bool(current_time.dst())
        output += f"Daylight Saving: {'✅ Active' if dst_active else '❌ Not Active'}\n"
        output += "=" * 60 + "\n"
        
        return output
    
    def display_clock_comparison(self, zone_names: List[str]) -> str:
        """Display clock comparison for specific zones"""
        output = "\n⏰ CLOCK COMPARISON\n"
        output += "=" * 70 + "\n"
        
        for zone_name in zone_names:
            tz = self.get_timezone(zone_name)
            if tz:
                time_str = tz.get_time_string(self.time_format)
                output += f"{tz.emoji} {tz.display_name:30} | {time_str}\n"
            else:
                output += f"❌ {zone_name} not found\n"
        
        output += "=" * 70 + "\n"
        return output
    
    def get_time_difference(self, zone1: str, zone2: str) -> Optional[str]:
        """Calculate time difference between two zones"""
        tz1 = self.get_timezone(zone1)
        tz2 = self.get_timezone(zone2)
        
        if not tz1 or not tz2:
            return None
        
        time1 = tz1.get_current_time()
        time2 = tz2.get_current_time()
        
        diff = time2 - time1
        hours = int(diff.total_seconds() // 3600)
        minutes = int((diff.total_seconds() % 3600) // 60)
        
        if hours > 0:
            return f"{tz2.display_name} is {hours}h {minutes}m ahead of {tz1.display_name}"
        elif hours < 0:
            return f"{tz2.display_name} is {abs(hours)}h {abs(minutes)}m behind {tz1.display_name}"
        else:
            return f"{tz1.display_name} and {tz2.display_name} are in the same time"
    
    def get_noon_times(self) -> Dict[str, str]:
        """Get when it's noon in each timezone"""
        output = {}
        
        for zone_name, tz_info in self.timezones.items():
            # Create a time at noon in the target timezone
            now = tz_info.get_current_time()
            noon = now.replace(hour=12, minute=0, second=0, microsecond=0)
            
            # Get UTC time for that noon
            utc_noon = noon.astimezone(pytz.UTC)
            
            # Show what time it is in other zones when it's noon
            output[zone_name] = f"When it's noon in {tz_info.display_name}, it's {utc_noon.strftime('%H:%M UTC')}"
        
        return output
    
    def get_business_hours_status(self) -> Dict[str, str]:
        """Show business hours status for each timezone (9 AM - 5 PM)"""
        output = {}
        
        for zone_name, tz_info in self.timezones.items():
            current_time = tz_info.get_current_time()
            hour = current_time.hour
            
            if 9 <= hour < 17:
                status = "🟢 Business Hours"
            elif 9 <= hour < 12:
                status = "🟡 Morning"
            elif 12 <= hour < 17:
                status = "🟡 Afternoon"
            else:
                status = "🔴 Off Hours"
            
            output[zone_name] = f"{tz_info.display_name}: {status} ({current_time.strftime('%H:%M')})"
        
        return output
    
    def display_business_hours(self) -> str:
        """Display business hours status for all zones"""
        output = "\n💼 BUSINESS HOURS STATUS (9 AM - 5 PM)\n"
        output += "=" * 70 + "\n"
        
        status = self.get_business_hours_status()
        for zone_name, status_text in status.items():
            output += f"{status_text}\n"
        
        output += "=" * 70 + "\n"
        return output
    
    def get_available_timezones(self) -> List[str]:
        """Get all available timezone names"""
        return sorted(self.timezones.keys())
    
    def get_timezone_count(self) -> int:
        """Get number of configured timezones"""
        return len(self.timezones)


class ClockDisplay:
    """Display utilities for the digital clock"""
    
    @staticmethod
    def ascii_clock(hour: int, minute: int) -> str:
        """Create ASCII art clock representation"""
        clock_face = """
        ┌─────────────────┐
        │  ⏰ DIGITAL CLOCK   │
        ├─────────────────┤
        │                │
        │   {:02d}:{:02d}      │
        │                │
        └─────────────────┘
        """.format(hour, minute)
        return clock_face
    
    @staticmethod
    def create_header(title: str, width: int = 70) -> str:
        """Create a formatted header"""
        padding = (width - len(title) - 2) // 2
        return f"\n{'=' * padding} {title} {'=' * padding}\n"


# Example usage and demonstration
def demo():
    """Demonstrate the digital clock application"""
    
    print("\n🎯 DIGITAL CLOCK WITH MULTIPLE TIMEZONES DEMO\n")
    
    # Initialize the clock
    clock = DigitalClock()
    
    # Set time format
    clock.set_time_format(TimeFormat.TWELVE_HOUR)
    print("⏱️  Time format set to 12-hour\n")
    
    # Display all clocks
    print(clock.display_all_clocks())
    
    # Display detailed clock for a specific timezone
    print(clock.display_detailed_clock('US/Eastern'))
    
    # Compare multiple zones
    print(clock.display_clock_comparison(['US/Eastern', 'US/Pacific', 'Europe/London', 'Asia/Tokyo']))
    
    # Show time differences
    print("\n⏱️  TIME DIFFERENCES:\n")
    diff = clock.get_time_difference('US/Eastern', 'Asia/Tokyo')
    print(f"📌 {diff}\n")
    
    # Business hours status
    print(clock.display_business_hours())
    
    # Change to 24-hour format
    print("\n⏱️  Switching to 24-hour format...\n")
    clock.set_time_format(TimeFormat.TWENTY_FOUR_HOUR)
    print(clock.display_all_clocks())
    
    # Add custom timezone
    print("➕ Adding custom timezone: Australia/Melbourne\n")
    clock.add_timezone('Australia/Melbourne', 'Melbourne', '🦘')
    
    print(clock.display_all_clocks())
    
    return clock


if __name__ == "__main__":
    demo()
