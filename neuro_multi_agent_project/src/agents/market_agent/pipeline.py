# src/agents/market_agent/pipeline.py
from src.agents.base import BaseAgent, AgentResult


class MarketAgent(BaseAgent):
    """Агент для сбора данных о рынке"""
    
    name = "market_agent"
    
    def __init__(self):
        self.platforms_count = 0
        self.total_courses = 0
        self._initialized = True
    
    def run(self, *args, **kwargs) -> AgentResult:
        """Запускает сбор данных о рынке"""
        # Здесь будет реальная логика сбора данных
        # Пока возвращаем заглушку для прототипа
        
        self.platforms_count = 6  # ЯндексПрактикум, OTUS, Karpov-courses, NETOLOGY, SKILLBOX, HSE
        self.total_courses = 150  # примерное количество курсов
        
        return AgentResult(
            success=True,
            data={
                "platforms_count": self.platforms_count,
                "total_courses": self.total_courses,
                "platforms": [
                    "ЯндексПрактикум",
                    "OTUS",
                    "Karpov-courses",
                    "NETOLOGY",
                    "SKILLBOX",
                    "HSE"
                ]
            },
            metadata={
                "agent_name": self.name,
                "status": "completed"
            }
        )