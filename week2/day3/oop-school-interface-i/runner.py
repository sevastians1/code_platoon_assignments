from classes.school import School 
from classes.student import Student 
import random

# print(Student.all_students())


def school_interface(is_student = False, active=True):
    school = School('Ridgemont High') 

    while active:
        print('Ridgemont High Student Interface')
        print('_________________________________')

        user_name_input = input('Please enter your name: ')
        user_is_student_input = input('Are you a student? ')

        if user_is_student_input == 'yes':
            student_info = school.get_student_info(user_name_input)
            # print(student_info)
            
            print(f"Welcome, {user_name_input}. Your access level is {student_info['role']}.")

            while active:
            
                task_select_input = input("What would you like to do?\n1 View Your Information\n2 Quit\nEnter the task number: ")
                
                if int(task_select_input) == 1:
                    print(student_info)

                elif int(task_select_input) == 2:
                    active = False

        elif user_is_student_input == 'no':
            employee_info = school.get_employee_info(user_name_input)
            # print(employee_info)
            
            print(f"Welcome, {user_name_input}. Your access level is {employee_info['role']}.")

            while active:
            
                task_select_input = input("What would you like to do?\n1 Lists All Students\n2 View Individual Student\n3 Add a Student\n4 Remove a Student\n5 Quit\nEnter the task number: ")

                if int(task_select_input) == 1:
                    print(school.students)
                
                elif int(task_select_input) == 2:
                    print(employee_info)

                elif int(task_select_input) == 3:
                    new_student_name = input("Enter the student's name: ")
                    new_student_age = input("Enter the student's age: ")
                    new_student_password = input("Enter a password: ")

                    new_student = {'name':new_student_name, 'age':new_student_age, 'password':new_student_password, 'school_id':random.randint(10000,99999), 'role':'Student'}

                    new_student_name = Student(**new_student)
                    print(vars(new_student_name))

                elif int(task_select_input) == 4:
                    delete_user = input("Enter the name of the student to be removed: ")
                    Student.del_student(delete_user)

                elif int(task_select_input) == 5:
                    active = False

        active=False

# school_interface()

# student_new = {'name': 'Lisa', 'age': '25', 'role': 'Student', 'school_id': '13345', 'password': 'xx '}
# john = Student(dict['name'], dict['age'],dict['role'],dict['password'],dict['school_id'])

# Student.all_students()
# print(Student.create_students())
# print(Lisa.name)