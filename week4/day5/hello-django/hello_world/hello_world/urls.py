"""hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def index(request):
    response = HttpResponse("<h1>Hello World</h1>")
    return response


def get_rectangle_area(request, height, width):
    area = height * width

    response = HttpResponse(f"The area of the rectangle with a height of {height} and a width of {width} is {area}.")

    return response


def get_rectangle_perimeter(request, height, width):

    num_of_sides = 2

    perimeter = height * num_of_sides + width * num_of_sides

    response = HttpResponse(f"The perimeter of the rectangle with a height of {height} and a width of {width} is {perimeter}.")
    
    return response


def get_circle_area(request, radius):

    area = (radius ** 2) * 3.14

    response = HttpResponse(f"The area of the circl with a radius of {radius} is {area}")

    return response


def get_circle_perimeter(request, radius):

    perimeter = 2 * 3.14 * radius

    response = HttpResponse(f"The perimeter of the circl with a radius of {radius} is {perimeter}")

    return response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('rectangle/area/<int:height>/<int:width>', get_rectangle_area),
    path('rectangle/perimeter/<int:height>/<int:width>', get_rectangle_perimeter),
    path('circle/area/<int:radius>', get_circle_area),
    path('circle/parimeter/<int:radius>', get_circle_perimeter),
]
