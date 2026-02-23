"""
This module contains all the data processing functionalities.
"""

from __future__ import annotations

#import utils
#from utils import *
# from hudai.utilis import prompt_non_empty, prompt_int, prompt_float, format_name
from utils import prompt_non_empty, prompt_int, prompt_float, format_name

def add_student(students: list[dict]) -> None:
    sid = prompt_non_empty("Enter student Id: ")
    name = format_name(prompt_non_empty("Enter student name: "))

    n = prompt_int("Enter number of subjects: ", min_value=1)

    subjects: list[str] = []
    marks: list[float] = []

    for i in range(n):
        sub = prompt_non_empty(f"Enter name of subject {i+1}: ")
        sub = sub.strip().title()
        subjects.append(sub)

        mk = prompt_float(f"Enter marks for {sub}: ", min_value=0.0, max_value=100.0)
        marks.append(mk)