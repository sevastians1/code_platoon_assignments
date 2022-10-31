from django.shortcuts import render
from .models import School # import our School class
from .models import Student

my_school = School("Django School") # create a school instance


def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):

    all_staff = my_school.staff
    
    return render(request, "pages/staff.html", {"all_staff":all_staff})
    


def staff_detail(request, employee_id):
    all_staff = my_school.staff

    for staff in all_staff:
        if staff.employee_id == employee_id:
            selected_staff = staff

    return render(request, "pages/staff_detail.html", {"selected_staff":selected_staff})


def list_students(request):

    all_students = my_school.students
    
    return render(request, "pages/student.html", {"all_students":all_students})


def student_detail(request, student_id):
    all_students = my_school.students

    for student in all_students:
        if student.school_id == student_id:
            selected_student = student

    return render(request, "pages/student_detail.html", {"selected_student":selected_student})