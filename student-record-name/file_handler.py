import csv
import json
from student import Student

class FileHandle:
    @staticmethod
    def load_txt(file_path):
        students = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",") if p.strip()]
                if len(parts) >= 7:
                    try:
                        s_id = int(parts[0])
                        name = parts[1]
                        dept = parts[2]
                        sem = int(parts[3])
                        m1 = float(parts[4])
                        m2 = float(parts[5])
                        m3 = float(parts[6])
                        students.append(Student(s_id, name, dept, sem, [m1, m2, m3]))
                    except ValueError:
                        continue
        return students

    @staticmethod
    def save_txt(file_path, students):
        with open(file_path, "w", encoding="utf-8") as file:
            for s in students:
                file.write(f"{s.student_id}, {s.name}, {s.department}, {s.semester}, "
                           f"{s.marks[0]}, {s.marks[1]}, {s.marks[2]}\n")

    @staticmethod
    def load_csv(file_path):
        students = []
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            for row in reader:
                if len(row) >= 7:
                    s_id, name, dept, sem, m1, m2, m3 = row[:7]
                    students.append(Student(s_id, name.strip(), dept.strip(), sem, [m1, m2, m3]))
        return students

    @staticmethod
    def save_csv(file_path, students):
        header = ["Student ID", "Name", "Department", "Semester", "Subject1", "Subject2", "Subject3"]
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for s in students:
                writer.writerow([s.student_id, s.name, s.department, s.semester,
                                 s.marks[0], s.marks[1], s.marks[2]])

    @staticmethod
    def load_json(file_path):
        students = []
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                students.append(Student(
                    student_id=item["student_id"],
                    name=item["name"],
                    department=item["department"],
                    semester=item["semester"],
                    marks=item["marks"]
                ))
        return students

    @staticmethod
    def save_json(file_path, students):
        data = [s.convert_dict() for s in students]
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)