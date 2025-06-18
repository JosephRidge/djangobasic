from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('base/home/', views.home),
]