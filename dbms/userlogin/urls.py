from django.urls import path,include, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name="userlogin.index"),
    path('signup/',views.signup,name="userlogin.signup"),
    url('^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
        name='userlogin.activate'),
    path('profile/edit/', views.edit_profile, name='userlogin.edit_profile'),
    path('password/', views.change_password, name='userlogin.change_password'),
]
