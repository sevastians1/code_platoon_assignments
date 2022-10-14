from .person import Person
import csv

class Student(Person):
    student_list = []

    def __init__(self, name, age, role, password, school_id):
        super().__init__(name, age, role, password)

        self.school_id = school_id

        Student.student_list.append(vars(self))

        

    def all_students():

        with open("./data/students.csv", "r") as csvfile:
            students_data = csv.DictReader(csvfile, delimiter=',')

            for student in students_data:
                # print(student)
                Student.student_list.append(student)

        return Student.student_list

    def del_student(name):
        for index in range(len(Student.student_list)):
            if Student.student_list[index]['name'] == name:
                del Student.student_list[index]
                break

                #make this work!
    # def create_students():
    #     for student in Student.student_list:
    #         student['name'] = Student(**student)
           
        