from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_brand, name='index-brand'),
    path('new/', views.add_brand, name='add-brand'),
    path('<int:brand_id>/', views.detail_brand, name='detail-brand'),
    path('<int:brand_id>/delete', views.del_brand, name='del-brand'),
    # path('brands/<:id>/edit/', views.edit_brand),
    path('<int:brand_id>/cars/', views.index_car, name='index-car'),
    path('<int:brand_id>/cars/new/', views.add_car, name='add-car'),
    # path('brands/<:brand_id>/cars/<:car_id>/', views.detail_car),
    # path('brands/<:brand_id>/cars/<:car_id>/edit/', views.edit_car),
]
