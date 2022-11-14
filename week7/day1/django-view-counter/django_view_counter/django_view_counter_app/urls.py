from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_cookie),
    path('home', views.index),
]
