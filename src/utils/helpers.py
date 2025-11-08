"""Utility functions for safe conversions and statistical analysis"""

import statistics

def safe_float(x, default=None):
    """Safely convert to float with default fallback"""
    try:
        return float(x)
    except (TypeError, ValueError):
        return default

def safe_int(x, default=None):
    """Safely convert to int with default fallback"""
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return default

def calculate_zscore(series, last_value):
    """Calculate z-score for a series"""
    vals = [v for v in series if v is not None]
    if len(vals) < 10 or last_value is None:
        return None
    mu = statistics.mean(vals)
    sd = statistics.pstdev(vals) if len(vals) > 1 else 0.0
    return None if sd == 0.0 else (last_value - mu) / sd
