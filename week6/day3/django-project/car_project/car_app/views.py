from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponseRedirect


def index_brand(request):
    brands = Brand.objects.all()

    data = {}
    data['brands_list'] = brands

    return render(request, 'index.html', data)
    
    
def add_brand(request):


    new_brand_name = request.POST['brand-name']
    new_brand_img = request.POST['brand-img']

    new_brand = Brand(brand_name=new_brand_name, brand_img=new_brand_img)

    new_brand.save()

    return HttpResponseRedirect(f"/brands/")


def detail_brand(request, brand_id):
    
    brand = Brand.objects.get(id=brand_id)

    data = {'brand':brand}

    return render(request, 'detail.html', data)


def edit_brand(request):
    return HttpResponse('<h1>hello</h1>')


def del_brand(request, brand_id):

    brand = Brand.objects.get(id=brand_id)
    
    brand.delete()

    return HttpResponseRedirect(f"/brands/")




def index_car(request, brand_id):

    brand = Brand.objects.get(id=brand_id)

    # cars = []

    # for car in brand.cars.all:
    #     cars.append()


    cars = brand.cars.all
    
    data = {'cars':cars, 'brand':brand}

    return render(request, 'index-car.html', data)


def add_car(request, brand_id):

    new_car_name = request.POST['car-name']
    new_car_model = request.POST['car-model']
    new_car_color = request.POST['car-color']
    new_car_year_created = request.POST['car-year-created']
    new_car_img = request.POST['car-img']
    new_car_brand = Brand.objects.get(id=brand_id)

    new_car = Car(
        car_name=new_car_name, 
        car_model=new_car_model, 
        car_color=new_car_color, 
        car_year_created=new_car_year_created, 
        car_img=new_car_img,
        brand=new_car_brand,
        )

    new_car.save()
    
    return HttpResponseRedirect(f"/brands/{brand_id}/cars")


def detail_car(request):
    return HttpResponse('<h1>hello</h1>')

def edit_car(request):
    return HttpResponse('<h1>hello</h1>')