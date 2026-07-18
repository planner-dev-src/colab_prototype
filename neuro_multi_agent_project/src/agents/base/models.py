# src/agents/base/models.py
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AgentResult:
    """Результат работы агента"""
    success: bool = True
    data: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "data": self.data,
            "error": self.error,
            "metadata": self.metadata
        }