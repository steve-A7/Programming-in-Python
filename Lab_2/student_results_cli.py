"""
Docstring for student_results_cli
This is an application for calculating and storing students results.
This will run in CLI.
If possible we will also save it in a .csv file.
"""

from __future__ import annotations
from data_processor import add_student


def print_menu() -> None:
   print("---- Student Result Calculator ----")
   print("1) Add student result + calculate results")
   print("2) List all student results")
   print("3) Search student by Id")
   print("4) Delete student by Id")
   print("5) Save results to .csv file")
   print("6) Exit")

def main() -> None:
   students: list[dict] = []
   while True:
      print_menu()
      choice: str = input("Enter your choice (1-6): ").strip()
      # Match case is only available after python 3.10
      match choice:
         case "1":
            add_student(students)
         case "2":
            print("Listing all student results...")
            #Here list all student results logic will be implemented
            pass
         case "3":
            print("Searching student by Id...")
            #Here search student by Id logic will be implemented
            pass
         case "4":
            print("Deleting student by Id...")
            #Here delete student by Id logic will be implemented
            pass
         case "5":
            print("Saving results to .csv file...")
            #Here save results to .csv file logic will be implemented
            pass
         case "6":
            print("Exiting the application...")
            break
         case _:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
   main()