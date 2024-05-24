#!/usr/bin/python3
import datetime
# imports from Django
from django.shortcuts import render
from django.http import HttpResponse
import random

# This view will return "Welcome to the Phoenix Cafe!" as text
def welcome(request):
    return HttpResponse("Welcome to the Phoenix Cafe!")
# your custom code will be here
def sleepy(request):
    return HttpResponse("Z-z-z-z-z-z-z!")

# NEW - new view that returns the current date and time
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)  # we are not returning a static string

def rand(request):
    return HttpResponse(random.random())

def greetings(request):
    now = datetime.datetime.now()
    t = now.strftime( '%I:%M:%S %p')
    d = now.strftime('%I')
    d = int(d)
    if 'AM' in t:
        answer = 'Good Morning'
    elif 'PM' in t and d >= 6:
        answer = 'Good Night!'
    else:
        answer = 'Good Noon'
    return HttpResponse(answer)

def cake(request):
    return HttpResponse("""

    1 cup white sugar

    ½ cup unsalted butter

    2 large eggs

    2 teaspoons vanilla extract

    1 ½ cups all-purpose flour

    1 ¾ teaspoons baking powder

    ½ cup milk""" )
