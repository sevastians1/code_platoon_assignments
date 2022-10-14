from .student import Student
from .staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()
        
    def get_student_info(self, name):
        for student in self.students:
            if student.get('name') == name:
                student_info = student
                return student_info
            else:
                return "Student does not exist at this school."

    def get_employee_info(self, name):
        for employee in self.staff:
            if employee.get('name') == name:
                employee_info = employee
                print(employee_info)
                return employee_info
            else:
                return "Employee does not exist at this school."