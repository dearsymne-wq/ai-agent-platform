"""
Base agent class for all specialized agents
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from datetime import datetime
import logging


class BaseAgent(ABC):
    """Abstract base class for all agents"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.logger = logging.getLogger(name)
        self.enabled = True
        self.created_at = datetime.now()
    
    @abstractmethod
    async def process(self, command: str) -> Dict[str, Any]:
        """
        Process a command and return result
        
        Args:
            command: User command string
            
        Returns:
            Dictionary with result and metadata
        """
        pass
    
    def enable(self) -> None:
        """Enable this agent"""
        self.enabled = True
        self.logger.info(f"{self.name} agent enabled")
    
    def disable(self) -> None:
        """Disable this agent"""
        self.enabled = False
        self.logger.info(f"{self.name} agent disabled")
    
    def get_info(self) -> Dict[str, Any]:
        """Get agent information"""
        return {
            'name': self.name,
            'description': self.description,
            'enabled': self.enabled,
            'created_at': self.created_at.isoformat()
        }
