"""
This module contains all the grading related functionalities.
"""

from __future__ import annotations

def grade_from_percentage(pct: float) -> str:
    if pct >= 90:
        return "A"
    elif pct >= 80:
        return "B"
    elif pct >= 70:
        return "C"
    elif pct >= 60:
        return "D"
    else:
        return "F"
