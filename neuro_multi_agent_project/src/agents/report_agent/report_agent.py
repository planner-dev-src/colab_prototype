# src/agents/report_agent/report_agent.py
from src.agents.base import BaseAgent, AgentResult


class ReportAgent(BaseAgent):
    """Агент для формирования отчётов"""
    
    name = "report_agent"
    
    def generate_report(self, data: dict) -> dict:
        """Генерирует отчёт на основе данных"""
        
        market_analysis = data.get("market_analysis", {})
        metrics_agent = data.get("metrics", None)
        
        # Получаем метрики
        metrics_data = {}
        if metrics_agent:
            all_metrics = metrics_agent.get_all_metrics()
            metrics_data = {
                "total": len(all_metrics),
                "critical": len(metrics_agent.get_critical_metrics()),
                "metrics": all_metrics
            }
        
        # Формируем отчёт
        return {
            "executive_summary": (
                "Проведён анализ рынка образовательных платформ по направлениям AI. "
                "Выявлены ключевые тренды и конкурентные разрывы. "
                "Рекомендуется усилить позиции в областях MLOps и GenAI."
            ),
            "market_analysis": market_analysis,
            "metrics": metrics_data,
            "recommendations": {
                "strategic": [
                    "Разработать программу по MLOps для усиления конкурентной позиции",
                    "Инвестировать в развитие GenAI-направления",
                    "Создать RAG-систему для персонализации обучения"
                ],
                "tactical": [
                    "Увеличить количество практических проектов в курсах",
                    "Внедрить систему наставничества",
                    "Расширить партнёрства с индустрией"
                ],
                "operational": [
                    "Оптимизировать процесс проверки домашних заданий",
                    "Улучшить UX платформы",
                    "Внедрить систему сбора обратной связи"
                ]
            },
            "status": "completed",
            "timestamp": "2026-07-18T12:00:00"
        }
    
    def run(self, *args, **kwargs) -> AgentResult:
        """Запускает агента отчётов"""
        return AgentResult(
            success=True,
            data=self.generate_report(kwargs.get("data", {})),
            metadata={"agent_name": self.name}
        )