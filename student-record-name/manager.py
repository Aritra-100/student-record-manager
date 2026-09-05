from student import Student
from file_handler import FileHandle

class StuManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.student_id == student.student_id:
                print(f"Error: Student with ID {student.student_id} already exists.")
                return False
        self.students.append(student)  # FIXED: Missing append call
        return True

    def remove_student(self, student_id):
        target_index = -1
        for idx in range(len(self.students)):
            if self.students[idx].student_id == student_id:
                target_index = idx
                break
        if target_index != -1:
            removed = self.students.pop(target_index)
            return removed
        return None

    def display_students(self):
        if not self.students:
            print("No student records found.")
            return
        print("-" * 95)
        for student in self.students:
            student.display_student()
        print("-" * 95)

    def search_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_name(self, name_query):
        results = []
        query = name_query.lower()
        for student in self.students:
            if query in student.name.lower():
                results.append(student)
        return results

    def search_department(self, dept_query):
        results = []
        query = dept_query.lower()
        for student in self.students:
            if query in student.department.lower():
                results.append(student)
        return results

    def search_by_average_above(self, min_avg):
        results = []
        for student in self.students:
            if student.calc_avg() > min_avg:
                results.append(student)
        return results

    def search_complex(self, dept_query, min_avg):
        query = dept_query.lower()
        return [s for s in self.students if query in s.department.lower() and s.calc_avg() > min_avg]

    def get_from_file(self, file_path, file_format):
        format = file_format.lower()
        if format == "txt":
            self.students = FileHandle.load_txt(file_path)
        elif format == "csv":
            self.students = FileHandle.load_csv(file_path)
        elif format == "json":
            self.students = FileHandle.load_json(file_path)
        else:
            raise ValueError(f"Unsupported format: {file_format}")

    def save_to_file(self, file_path, file_format):
        format = file_format.lower()
        if format == "txt":
            FileHandle.save_txt(file_path, self.students)
        elif format == "csv":
            FileHandle.save_csv(file_path, self.students)
        elif format == "json":
            FileHandle.save_json(file_path, self.students)
        else:
            raise ValueError(f"Unsupported format: {file_format}")    

    