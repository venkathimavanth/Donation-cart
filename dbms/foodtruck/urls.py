from django.urls import path,include, re_path
from . import views

urlpatterns = [

    path('', views.foodrequest, name='foodtruck.foodrequest'),
]
