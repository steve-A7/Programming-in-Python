"""
This module contains all the grading related functionalities.
"""

from __future__ import annotations

def compute_total_and_percentage(marks: list[float]) -> tuple[float, float]:
    #total = sum(marks)
    total = 0.0
    for m in marks:
        total += m
    percentage = (total / (len(marks) * 100)) * 100
    return total, percentage

def grade_from_percentage(pct: float) -> str:
    if pct >= 90:
        return "A+"
    elif pct >= 85:
        return "A"
    elif pct >= 80:
        return "B+"
    elif pct >= 75:
        return "B"
    elif pct >= 70:
        return "C+"
    elif pct >= 65:
        return "C"
    elif pct >= 60:
        return "D+"
    elif pct >= 50:
        return "D"
    else:
        return "F"
    
def status_from_percentage(pct: float) -> str:
    return "Pass" if pct >= 50 else "Fail"
