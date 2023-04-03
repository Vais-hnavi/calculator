from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.calc, name="display"),
    path('add/',views.add, name='add')
]