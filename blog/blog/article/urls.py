from django.contrib import admin
from django.urls import path
from . import views #from this file

app_name= "article"

urlpatterns = [
    path("create/",views.index,name="index"),
]