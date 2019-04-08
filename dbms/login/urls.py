from django.urls import path,include, re_path
from . import views

urlpatterns = [
    re_path('^$', views.home, name="login.home"),
    path('accounts/', views.login, name="login.login"),
]
