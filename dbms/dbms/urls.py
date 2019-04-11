"""dbms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('userlogin/', include('userlogin.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='userlogin/index.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='login/home.html'),name='logout'),
    path(r'^reset-password/$', PasswordResetView.as_view(template_name='userlogin/password_reset_form.html',
                                                        email_template_name="userlogin/reset_password_email.html",
                                                        success_url="done/"), name="password_reset"),
    path(r'^reset-password/done/$', PasswordResetDoneView.as_view(template_name='userlogin/password_reset_done.html'),
        name="password_reset_done"),
    path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(template_name="userlogin/password_reset_confirm.html"),
        name="password_reset_confirm"),
    path(r'^reset-password/complete/$',
        PasswordResetCompleteView.as_view(template_name="userlogin/password_reset_complete.html"),
        name="password_reset_complete"),

]
