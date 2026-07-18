# ============================================================
# src/agents/market_analysis_agent/aggregations.py
# ============================================================

def aggregate_platform_data(platforms_data):
    """
    Агрегирует данные по платформам
    
    Args:
        platforms_data: список данных по платформам
        
    Returns:
        dict: Агрегированные данные
    """
    return {
        "total_platforms": len(platforms_data),
        "total_courses": sum(p.get('courses_count', 0) for p in platforms_data),
        "platforms": platforms_data
    }


def aggregate_trends(trends_data):
    """
    Агрегирует данные по трендам
    
    Args:
        trends_data: список трендов
        
    Returns:
        dict: Агрегированные тренды
    """
    return {
        "total_trends": len(trends_data),
        "trends": trends_data
    }


def aggregate_gaps(gaps_data):
    """
    Агрегирует данные по конкурентным разрывам (GAP)
    
    Args:
        gaps_data: список GAP-зон
        
    Returns:
        dict: Агрегированные GAP-зоны
    """
    return {
        "total_gaps": len(gaps_data),
        "gaps": gaps_data
    }