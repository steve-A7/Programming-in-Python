"""
This module contains the function for exporting student results to CSV files.
"""

from __future__ import annotations
from csv import DictWriter

def export_students_to_csv(students: list[dict], filename: str) -> None:
   fields=["Id", "Name","Subjects", "Marks", "Total", "Percentage", "Grade", "Status"]

   with open(filename, mode="w", newline="") as f:
      writer = DictWriter(f, fieldnames=fields)
      writer.writeheader()
      for student in students:
         row = student.copy()
         row["Subjects"] = ",".join(student["Subjects"])
         row["Marks"] = ",".join(str(m) for m in student["Marks"])
         writer.writerow(row)
   
   print(f"Student results exported to {filename} successfully.")

