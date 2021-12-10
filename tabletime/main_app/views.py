from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.

def home(request):
  return render(request,'homepage.html')

def restaurant(request):
    return render(request,'restaurant.html')

def userprofile_index(request):
    return render(request,'userprofile/index.html', {'userprofile':'userprofile'})

def restaurant_reservation(request):
    return render(request,'reservation.html')

def account_settings(request):
    return HttpResponse('<h1>Give me your info</h1>')

def signup(request):
    return HttpResponse('<h1>Welcome to the matrix</h1>')

def login(request):
    return HttpResponse('<h1>So your back huh</h1>')

def savedrestaurants_index(request):
    savedrestaurants=[]
    return render(request, 'savedrestaurants/index.html/', {'savedrestaurants':savedrestaurants})    

def login(request):
    return HttpResponse('<h1>So your back huh</h1>')