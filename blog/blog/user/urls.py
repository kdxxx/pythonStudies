from django.contrib import admin
from django.urls import path,include
from .views import index

app_name = "user"

urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
]