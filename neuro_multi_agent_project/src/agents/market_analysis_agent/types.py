# src/agents/market_analysis_agent/types.py
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class OfferFeatures:
    """Особенности предложения (курса)"""
    item_id: Optional[str] = None
    platform_name: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    canonical_url: Optional[str] = None
    topic_clusters: List[str] = field(default_factory=list)
    competency_families: List[str] = field(default_factory=list)
    value_props: List[str] = field(default_factory=list)
    core_signals: List[str] = field(default_factory=list)
    audience_segments: List[str] = field(default_factory=list)
    format_signals: List[str] = field(default_factory=list)
    support_signals: List[str] = field(default_factory=list)
    outcome_signals: List[str] = field(default_factory=list)
    intensity_signals: List[str] = field(default_factory=list)


@dataclass
class PlatformAggregate:
    """Агрегированные данные по платформе"""
    platform_name: str
    offers_count: int = 0
    raw_items_count: int = 0
    deduped_items_count: int = 0
    filtered_items_count: int = 0
    dropped_as_noise_count: int = 0
    dropped_as_duplicates_count: int = 0
    top_topics: List[str] = field(default_factory=list)
    top_competency_families: List[str] = field(default_factory=list)
    top_value_props: List[str] = field(default_factory=list)
    top_core_signals: List[str] = field(default_factory=list)
    top_audiences: List[str] = field(default_factory=list)
    top_format_signals: List[str] = field(default_factory=list)
    evidence_items: List[str] = field(default_factory=list)
    source_items_count: int = 0
    source_items_count_raw: int = 0
    source_items_deduped_removed: int = 0
    source_items_noise_removed: int = 0


@dataclass
class CompetitiveGap:
    """Конкурентный разрыв (GAP-зона)"""
    topic: str
    gap_type: str  # "topic_cluster", "competency_family", "core_signal"
    platforms_count: int
    platform_share: float
    underrepresented_platforms: List[str] = field(default_factory=list)
    opportunity_score: float = 0.0
    interpretation: str = ""
    evidence_item_ids: List[str] = field(default_factory=list)