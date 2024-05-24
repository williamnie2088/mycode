#!/usr/bin/python3

# imports from Django
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('welcome/', views.welcome),
]

# NEW - Add this to the end of your code
urlpatterns += [
        path('sleepy/', views.sleepy),
        ]
# clock/ is the path to trigger our function
urlpatterns += [path('clock/', views.current_datetime),]

urlpatterns += [path('rand/', views.rand),]

urlpatterns += [path('greetings/', views.greetings),]

urlpatterns += [path('cake/', views.cake),]

