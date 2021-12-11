from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

# Add the Restaurant class & list and view function below the imports
class Restaurant:
    def __init__(self, name, city, cuisine, cost,): 

        self.name = name
        self.city = city
        self.cuisine = cuisine 
        self.cost = cost 

restaurant = [ 
     Restaurant('Burgers & Fries', 'Toronto', 'American', 2),
     Restaurant('Kobe', 'Toronto', 'Japanese', 3),
]

     # Note that parens are optional if not inheriting from another class
 
# Create your views here.

def home(request):
  return render(request,'homepage.html')

def restaurant_index(request):
    restaurant = []
    return render(request,'restaurantpage/restaurant.html', {'restaurant': 'restaurant'})

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