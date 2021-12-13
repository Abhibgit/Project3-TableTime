from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Restaurant, Profile
from django import forms
from .models import Reviews

# Note that parens are optional if not inheriting from another class
 
# Create your views here.

def home(request):
  return render(request,'homepage.html')

def restaurant_index(request):
  restaurants = Restaurant.objects.all() 
  return render(request,'restaurantpage/restaurant.html', {'restaurant': restaurants})

def user_profile_index(request):
  print("profile", request.user)
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
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = ProfileForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def restaurant_detail(request, restaurant_id):
  restaurant = Restaurant.objects.get(id=restaurant_id)
  return render(request, 'restaurantpage/restaurant_detail.html', {'restaurant':restaurant})

class ReviewsCreate(CreateView):
  model = Reviews
  fields = '__all__'
  success_url = '/savedrestaurants/'
  
# class ReviewsDelete(DeleteView):
#   model = Reviews
#   fields = '__all__'