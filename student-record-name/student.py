class Student:
    def __init__(self, student_id, name, department, semester, marks):
        self.student_id = int(student_id)
        self.name = str(name)
        self.department = str(department)
        self.semester = int(semester)

        if isinstance(marks, dict):
            self.marks = [float(marks.get(f"subject{i}", 0)) for i in range(1,4)]
        else:
            self.marks = [float(m) for m in marks]

    def calculate(self):
        total = 0.0
        for mark in self.marks: 
            total += mark
        return total

    def calc_avg(self):
        return self.calculate()/len(self.marks) if self.marks else 0.0

    def get_res(self):
        for mark in self.marks:
            if mark < 40.0: 
                return "Fail"
        return "Passed"

    def update(self, new_marks):
        if isinstance(new_marks, dict):
            self.marks = [float(new_marks.get(f"subject{i}", 0)) for i in range (1,4)]
        else:
            self.marks = [float(m) for m in new_marks]

    def display_student(self):
        total = self.calculate()
        avg = self.calc_avg()
        status = self.get_res()
        print(f"ID: {self.student_id} | Name: {self.name:<12} | Dept: {self.department:<18} "
              f"| Sem: {self.semester} | Marks: {self.marks} | Total: {total:.1f} | Avg: {avg:.2f} | Status: {status}")
    
    def convert_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "department": self.department,
            "semester": self.semester,
            "marks": {
                "subject1": self.marks[0],
                "subject2": self.marks[1],
                "subject3": self.marks[2]
            }
        }