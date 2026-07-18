# src/agents/metrics_agent/metrics_agent.py
from src.agents.base import BaseAgent, AgentResult
from .metrics_registry import MetricsRegistry, Metric


class MetricsAgent(BaseAgent):
    """Агент для работы с метриками"""
    
    name = "metrics_agent"
    
    def __init__(self):
        self.registry = MetricsRegistry()
    
    def run(self, *args, **kwargs) -> AgentResult:
        """Запускает агента метрик"""
        metrics = self.get_all_metrics()
        
        return AgentResult(
            success=True,
            data={
                "metrics": [m.to_dict() for m in metrics],
                "total": len(metrics),
                "critical": len(self.get_critical_metrics()),
                "warning": len(self.get_warning_metrics()),
                "summary": self.registry.get_summary()
            },
            metadata={
                "agent_name": self.name,
                "status": "completed"
            }
        )
    
    def get_all_metrics(self) -> list:
        """Возвращает все метрики"""
        return self.registry.get_all_metrics()
    
    def get_critical_metrics(self) -> list:
        """Возвращает критические метрики"""
        return self.registry.get_critical_metrics()
    
    def get_warning_metrics(self) -> list:
        """Возвращает метрики с предупреждением"""
        return self.registry.get_warning_metrics()
    
    def get_metric(self, metric_id: str) -> Metric:
        """Возвращает метрику по ID"""
        return self.registry.get_metric(metric_id)
    
    def update_metric(self, metric_id: str, value: float) -> bool:
        """Обновляет значение метрики"""
        return self.registry.update_metric(metric_id, value)
    
    def get_summary(self) -> dict:
        """Возвращает сводку по метрикам"""
        return self.registry.get_summary()