from django.urls import path,include, re_path
from . import views

urlpatterns = [
    path('', views.index, name="userlogin.index"),
    path('signup/',views.signup,name="userlogin.signup"),
    path('accounts/',views.login,name="userlogin.login"),

]
