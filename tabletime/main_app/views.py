from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return HttpResponse('<h1>Welcome to Table Time</h1>')

def restaurant(request):
    return render(request,'restaurant.html')

def userprofile(request):
    return HttpResponse('<h1>You the man</h1>')

def restaurant_reservation(request):
    return HttpResponse('<h1>Eat it up</h1>')

def account_settings(request):
    return HttpResponse('<h1>Give me your info</h1>')

def signup(request):
    return HttpResponse('<h1>Welcome to the matrix</h1>')

def login(request):
    return HttpResponse('<h1>So your back huh</h1>')

def savedrestaurants_index(request):
    return render(request, 'savedrestaurants/index.html', {'savedreturants':savedrestaurants})    