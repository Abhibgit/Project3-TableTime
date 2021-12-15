from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Restaurant, Profile
from django import forms
from .forms import ReviewForm
from .models import Reviews
import requests
import os
#from geocodio import GeocodioClient
 
YELP_KEY = os.environ['YELP_KEY']
#Client = GeocodioClient('GEOCODIO_API')


# Note that parens are optional if not inheriting from another class
#PARAMETERS = {'term':'coffee', 'limit': 50, 'radius': 10000, 'location':'San Diego'}
# Create your views here.

def home(request):
  return render(request,'homepage.html')

def user_profile_index(request):
  user_profile = Profile.objects.get(user=request.user)
  return render(request,'userprofile/index.html', {'user_profile': user_profile})

def restaurant_reservation(request):
  return render(request,'reservation.html')

def account_settings(request):
  return render(request,'accountsettings/account_settings.html')

def saved_restaurants_index(request):
  savedrestaurants=[]
  return render(request, 'savedrestaurants/index.html/', {'savedrestaurants':savedrestaurants})    

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = ProfileForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = ProfileForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def restaurant_detail(request, restaurant_id):
  restaurant = Restaurant.objects.get(id=restaurant_id)
  reviews_form = ReviewForm()
  return render(request, 'restaurantpage/restaurant_detail.html', {'restaurant':restaurant, 'reviews_form': reviews_form})

def add_review(request, restaurant_id):
    # create a ModelForm instance using the data in request.POST
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.restaurant_id = restaurant_id
    new_review.save()
  return redirect('detail', restaurant_id=restaurant_id)

def search_restaurant(request):
  r=requests.get("https://api.yelp.com/v3/businesses/search", params = {'location': request.POST['location'], 'categories': request.POST['categories']}, headers={'Authorization':f'Bearer {YELP_KEY}'})
  business_data = r.json()
  return render(request, "restaurantpage/restaurant.html", {'business_data': business_data['businesses']})