# src/agents/metrics_agent/metrics_registry.py
# Упрощенная версия реестра метрик для прототипа

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Metric:
    """Модель метрики"""
    id: str
    name: str
    level: str
    value: Any
    target: Any = None
    unit: str = ""
    status: str = "data_missing"
    interpretation: str = ""
    last_updated: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
            "value": self.value,
            "target": self.target,
            "unit": self.unit,
            "status": self.status,
            "interpretation": self.interpretation,
            "last_updated": self.last_updated
        }


class MetricsRegistry:
    """Реестр метрик для прототипа"""
    
    def __init__(self):
        self._metrics: Dict[str, Metric] = {}
        self._init_default_metrics()
    
    def _init_default_metrics(self):
        """Инициализирует дефолтные метрики"""
        default_metrics = [
            Metric(
                id="market_share",
                name="Доля рынка",
                level="market",
                value=15.0,
                target=20.0,
                unit="%",
                status="warning",
                interpretation="Доля рынка ниже целевого значения"
            ),
            Metric(
                id="user_growth",
                name="Рост пользователей",
                level="market",
                value=25.0,
                target=30.0,
                unit="%",
                status="warning",
                interpretation="Темп роста ниже планового"
            ),
            Metric(
                id="course_completion",
                name="Завершаемость курсов",
                level="products",
                value=68.0,
                target=75.0,
                unit="%",
                status="critical",
                interpretation="Критически низкая завершаемость курсов"
            ),
            Metric(
                id="nps_score",
                name="NPS (Net Promoter Score)",
                level="products",
                value=42.0,
                target=50.0,
                unit="",
                status="warning",
                interpretation="NPS ниже целевого значения"
            ),
            Metric(
                id="competitive_gap",
                name="Конкурентный разрыв",
                level="strategic",
                value=35.0,
                target=20.0,
                unit="%",
                status="critical",
                interpretation="Существенный конкурентный разрыв, требуется усиление позиций"
            ),
            Metric(
                id="market_trend_alignment",
                name="Соответствие рыночным трендам",
                level="strategic",
                value=70.0,
                target=85.0,
                unit="%",
                status="warning",
                interpretation="Недостаточное соответствие рыночным трендам"
            ),
            Metric(
                id="mlops_maturity",
                name="Зрелость MLOps",
                level="technical",
                value=2,
                target=4,
                unit="уровень",
                status="critical",
                interpretation="Низкий уровень зрелости MLOps"
            ),
            Metric(
                id="genai_coverage",
                name="Покрытие GenAI направлений",
                level="products",
                value=40.0,
                target=70.0,
                unit="%",
                status="critical",
                interpretation="Недостаточное покрытие GenAI направлений"
            ),
            Metric(
                id="rag_implementation",
                name="Внедрение RAG",
                level="technical",
                value=1,
                target=3,
                unit="уровень",
                status="critical",
                interpretation="RAG система на начальном этапе внедрения"
            ),
            Metric(
                id="team_competency",
                name="Компетенции команды",
                level="competency",
                value=65.0,
                target=80.0,
                unit="%",
                status="warning",
                interpretation="Требуется усиление компетенций команды"
            )
        ]
        
        for metric in default_metrics:
            self._metrics[metric.id] = metric
    
    def get_all_metrics(self) -> List[Metric]:
        """Возвращает все метрики"""
        return list(self._metrics.values())
    
    def get_all_metrics_dict(self) -> List[Dict[str, Any]]:
        """Возвращает все метрики в виде словарей"""
        return [m.to_dict() for m in self._metrics.values()]
    
    def get_metric(self, metric_id: str) -> Optional[Metric]:
        """Возвращает метрику по ID"""
        return self._metrics.get(metric_id)
    
    def get_critical_metrics(self) -> List[Metric]:
        """Возвращает критические метрики"""
        return [m for m in self._metrics.values() if m.status == "critical"]
    
    def get_warning_metrics(self) -> List[Metric]:
        """Возвращает метрики с предупреждением"""
        return [m for m in self._metrics.values() if m.status == "warning"]
    
    def get_metrics_by_level(self, level: str) -> List[Metric]:
        """Возвращает метрики по уровню"""
        return [m for m in self._metrics.values() if m.level == level]
    
    def update_metric(self, metric_id: str, value: Any) -> bool:
        """Обновляет значение метрики"""
        if metric_id in self._metrics:
            self._metrics[metric_id].value = value
            self._metrics[metric_id].last_updated = datetime.now().isoformat()
            # Пересчитываем статус
            self._update_status(self._metrics[metric_id])
            return True
        return False
    
    def _update_status(self, metric: Metric):
        """Обновляет статус метрики на основе значения и цели"""
        if metric.target is None:
            metric.status = "met"
            return
        
        # Проверяем, что оба значения числовые
        if not isinstance(metric.value, (int, float)) or not isinstance(metric.target, (int, float)):
            metric.status = "data_missing"
            return
        
        if metric.target == 0:
            metric.status = "met"
            return
        
        ratio = metric.value / metric.target
        
        if ratio >= 1.1:
            metric.status = "exceeded"
        elif ratio >= 0.95:
            metric.status = "met"
        elif ratio >= 0.75:
            metric.status = "warning"
        else:
            metric.status = "critical"
    
    def get_summary(self) -> Dict[str, Any]:
        """Возвращает сводку по метрикам"""
        status_counts = {}
        level_counts = {}
        
        for metric in self._metrics.values():
            status_counts[metric.status] = status_counts.get(metric.status, 0) + 1
            level_counts[metric.level] = level_counts.get(metric.level, 0) + 1
        
        return {
            "total": len(self._metrics),
            "by_status": status_counts,
            "by_level": level_counts,
            "critical_count": len(self.get_critical_metrics()),
            "warning_count": len(self.get_warning_metrics())
        }
    
    def add_metric(self, metric: Metric) -> bool:
        """Добавляет новую метрику"""
        if metric.id in self._metrics:
            return False
        self._metrics[metric.id] = metric
        return True
    
    def remove_metric(self, metric_id: str) -> bool:
        """Удаляет метрику"""
        if metric_id in self._metrics:
            del self._metrics[metric_id]
            return True
        return False
    
    def get_status_distribution(self) -> Dict[str, int]:
        """Возвращает распределение статусов"""
        distribution = {}
        for metric in self._metrics.values():
            distribution[metric.status] = distribution.get(metric.status, 0) + 1
        return distribution