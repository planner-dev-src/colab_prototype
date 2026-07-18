# src/agents/base/agent.py
from abc import ABC, abstractmethod
from .models import AgentResult


class BaseAgent(ABC):
    """Базовый класс для всех агентов"""
    
    name: str = "base_agent"
    
    @abstractmethod
    def run(self, *args, **kwargs) -> AgentResult:
        """Основной метод запуска агента"""
        raise NotImplementedError
    
    def get_status(self) -> dict:
        """Возвращает статус агента"""
        return {
            "name": self.name,
            "status": "initialized",
            "class": self.__class__.__name__
        }