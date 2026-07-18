# src/agents/market_analysis_agent/market_analysis_agent.py
from src.agents.base import BaseAgent, AgentResult


class MarketAnalysisAgent(BaseAgent):
    """Агент анализа рынка"""
    
    name = "market_analysis_agent"
    
    def run(self, *args, **kwargs) -> AgentResult:
        """Запускает анализ рынка"""
        result = run_market_analysis()
        return AgentResult(
            success=True,
            data=result,
            metadata={"agent_name": self.name}
        )