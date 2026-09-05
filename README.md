# Student Record Management and Search System

**Course:** AI/ML Lab  
**Assignment:** File Operations & Command-Line Systems 
**Author:** Aritra Das  

---

## Overview

The **Student Record Management and Search System** is a Python CLI application designed to manage, search, process, and persist student academic performance data. The system supports multi-format file operations (**TXT**, **CSV**, and **JSON**), allowing seamless import and export of student records.

It evaluates student performance by computing total marks, percentage averages, and pass/fail statuses, while offering single-criterion and combined search capabilities.

---

## Features & Assignment Compliance

1. **Multi-Format Data Persistence**:
   - Reads and writes student records across `.txt`, `.csv`, and `.json` formats.
   - Text files support line-by-line comma-separated parsing.
   - CSV files include standardized column headers (`Student ID`, `Name`, `Department`, `Semester`, `Subject1`, `Subject2`, `Subject3`).
   - JSON files store structured nested objects for subject marks.

2. **Core Performance Computations**:
   - **Total Marks**: Sums marks obtained across all 3 subjects.
   - **Average Marks**: Computes percentage mean score.
   - **Pass/Fail Determination**: Assigns `"Fail"` status if any subject score falls below $40.0$, otherwise `"Passed"`.

3. **Search & Filtering Operations**:
   - **By Student ID**: Exact match query.
   - **By Student Name**: Case-insensitive substring query.
   - **By Department**: Filter records by department name.
   - **By Minimum Average**: Filter students scoring above a specified threshold.
   - **Complex Search**: Combined filtering by department AND minimum average mark threshold.

4. **Data Management**:
   - Add new student records with duplicate ID validation.
   - Update individual student marks.
   - Save modified datasets to new or existing output files.

---

## Project Structure

```text
student-record-name/
│
├── data/
│   ├── students.txt          # Plain text student records
│   ├── students.csv          # Comma-Separated Values dataset
│   └── students.json         # JSON formatted dataset
│
├── student.py                # Student class (attributes & performance calculations)
├── manager.py                # StuManager class (business logic & record collections)
├── file_handler.py           # FileHandle class (TXT, CSV, JSON I/O methods)
├── main.py                   # Argument parser and CLI execution entry point
└── README.md                 # Project documentation
```
---

## Parser commands

1. Display all Records:
python main.py --file data/students.json --format json --action display
python main.py --file data/students.csv --format csv --action display
python main.py --file data/students.txt --format txt --action display

2. Add a new student:
python main.py --file data/students.json --format json --action add --id 6 --name "Rohan" --dept "Electrical Engg" --sem 1 --marks 80 75 88 --out data/updated_students.json

3. Search Student by Id:
python main.py --file data/students.json --format json --action search_id --id 1

4. Search Student by Name:
python main.py --file data/students.csv --format csv --action search_name --name "Aritra"

5. Search Students by Department:
python main.py --file data/students.txt --format txt --action search_dept --dept "Computer Science"

6. Filter by Minimum Average:
python main.py --file data/students.json --format json --action filter_avg --min_avg 70

7. Complex Search: Department and Minimum Avg:
python main.py --file data/students.json --format json --action search_complex --dept "Computer Science" --min_avg 75

8. Update Student Marks:
python main.py --file data/students.csv --format csv --action update_marks --id 3 --marks 85 90 88 --out data/updated_students.csv