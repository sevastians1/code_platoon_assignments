from .person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, role, password, employee_id):
        super().__init__(name, age, role, password)

        self.employee_id = employee_id

    def all_staff():
        staff_list = []

        with open("./data/staff.csv", "r") as csvfile:
            staff_data = csv.DictReader(csvfile, delimiter=',')

            for staff in staff_data:
                # print(student)
                staff_list.append(staff)

        return staff_list