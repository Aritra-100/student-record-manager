import argparse
from student import Student
from manager import StuManager

def main():
    parser = argparse.ArgumentParser(
        description="Student Record Management and Search System (AI/ML Lab - Assignment X_01)"
    )

    parser.add_argument("--file", type=str, required=True, help="Path to the input data file")
    parser.add_argument("--format", type=str, required=True, choices=["txt", "csv", "json"], help="Data file format (txt, csv, or json)")
    parser.add_argument("--action", type=str, default="display", choices=["display", "add", "search_id", "search_name", "search_dept", "filter_avg", "search_complex", "update_marks"], help="Action to execute on student database")

    parser.add_argument("--id", type=int, help="Student ID parameter for search/update actions")
    parser.add_argument("--name", type=str, help="Name parameter for search or student creation")
    parser.add_argument("--dept", type=str, help="Department parameter for search or student creation")
    parser.add_argument("--sem", type=int, default=1, help="Semester parameter for student creation")
    parser.add_argument("--marks", type=float, nargs=3, help="Three subject marks space-separated")
    parser.add_argument("--min_avg", type=float, help="Minimum average threshold for filter_avg action")
    parser.add_argument("--out", type=str, help="Output file path to save updated records")

    args = parser.parse_args()

    manager = StuManager()
    try:
        manager.get_from_file(args.file, args.format)
        print(f"\n[INFO] Successfully loaded {len(manager.students)} record(s) from '{args.file}'.")
    except Exception as e:
        print(f"[ERROR] Failed to load file: {e}")
        return

    if args.action == "display":
        print("\n--- ALL STUDENT RECORDS ---")
        manager.display_students()

    elif args.action == "add":
        if not (args.id and args.name and args.dept and args.marks):
            print("[ERROR] Adding a student requires --id, --name, --dept, and --marks.")
            return
        new_student = Student(args.id, args.name, args.dept, args.sem, args.marks)
        if manager.add_student(new_student):
            print(f"[SUCCESS] Student {args.name} added successfully.")

    elif args.action == "search_id":
        if args.id is None:
            print("[ERROR] Please specify --id for search_id.")
            return
        res = manager.search_by_id(args.id)
        print(f"\n--- SEARCH RESULT (ID: {args.id}) ---")
        if res:
            res.display_student()
        else:
            print("No matching student record found.")

    elif args.action == "search_name":
        if not args.name:
            print("[ERROR] Please specify --name for search_name.")
            return
        results = manager.search_name(args.name)
        print(f"\n--- SEARCH RESULTS (Name: '{args.name}') ---")
        for s in results:
            s.display_student()
        if not results:
            print("No matching student records found.")

    elif args.action == "search_dept":
        if not args.dept:
            print("[ERROR] Please specify --dept for search_dept.")
            return
        results = manager.search_department(args.dept)
        print(f"\n--- SEARCH RESULTS (Department: '{args.dept}') ---")
        for s in results:
            s.display_student()
        if not results:
            print("No matching student records found.")

    elif args.action == "filter_avg":
        if args.min_avg is None:
            print("[ERROR] Please specify --min_avg for filter_avg.")
            return
        results = manager.search_by_average_above(args.min_avg)
        print(f"\n--- STUDENTS WITH AVERAGE MARKS > {args.min_avg} ---")
        for s in results:
            s.display_student()
        if not results:
            print("No students met the criteria.")

    elif args.action == "search_complex":
        if not args.dept or args.min_avg is None:
            print("[ERROR] Complex search requires both --dept and --min_avg.")
            return
        results = manager.search_complex(args.dept, args.min_avg)
        print(f"\n--- SEARCH RESULTS (Dept: '{args.dept}' AND Average > {args.min_avg}) ---")
        for s in results:
            s.display_student()
        if not results:
            print("No matching student records found.")

    elif args.action == "update_marks":
        if args.id is None or not args.marks:
            print("[ERROR] Updating marks requires --id and --marks (3 float values).")
            return
        s = manager.search_by_id(args.id)
        if s:
            s.update(args.marks)
            print(f"[SUCCESS] Marks updated for Student ID {args.id}.")
            s.display_student()
        else:
            print(f"[ERROR] Student ID {args.id} not found.")

    if args.out:
        out_fmt = args.format
        if "." in args.out:
            out_fmt = args.out.split(".")[-1]
        manager.save_to_file(args.out, out_fmt)
        print(f"[INFO] Saved updated records to '{args.out}'.")

if __name__ == "__main__":
    main()