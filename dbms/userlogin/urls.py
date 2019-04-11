from django.urls import path,include, re_path
from . import views

urlpatterns = [
    path('', views.index, name="userlogin.index"),
    path('signup/',views.signup,name="userlogin.signup"),

    path('profile/edit/', views.edit_profile, name='userlogin.edit_profile'),
    path('password/', views.change_password, name='userlogin.change_password'),
]
