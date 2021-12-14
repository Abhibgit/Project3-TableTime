from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Restaurant, Profile, Reservations
from django import forms
from .forms import ReviewForm
from .models import Reviews
from .forms import ReservationForm

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
  reservations = Reservations.objects.filter(user_id= user_profile.id)
  return render(request,'userprofile/index.html', {'user_profile': user_profile, 'reservations': reservations})

# def restaurant_reservation(request):
#   user_profile = Profile.objects.get(user=request.user)
#   reservations = Reservations.objects.filter(user= user_profile.id)
#   print("reservation", reservations)
#   # reservations_form = ReservationsForm()
#   return render(request,'reservation.html', {'reservations': reservations})

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
  user_profile = Profile.objects.get(user=request.user)
  reviews_form = ReviewForm()
  return render(request, 'restaurantpage/restaurant_detail.html', {'restaurant':restaurant, 'reviews_form': reviews_form, 'profile_id': user_profile.id})

def add_review(request, restaurant_id):
    # create a ModelForm instance using the data in request.POST
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.restaurant_id = restaurant_id
    new_review.save()
  return redirect('detail', restaurant_id=restaurant_id)


def add_reservations(request, restaurant_id, profile_id):
    # create a ModelForm instance using the data in request.POST
  form = ReservationForm(request.POST)
  if form.is_valid():
    new_reservations = form.save(commit=False)
    new_reservations.user_id = profile_id 
    new_reservations.restaurant_id = restaurant_id
    new_reservations.save()
    # user_profile = Profile.objects.get(user=request.user)
    # reservations = Reservations.objects.filter(user_id= user_profile.id)
    return redirect('user_profile')
  else:
    return render(request, 'reservation.html', {'restaurant_id': restaurant_id, 'profile_id': profile_id, 'reservation_form' : form})

def delete_reservations(request, restaurant_id, profile_id):
    # create a ModelForm instance using the data in request.POST
  form = ReservationForm(request.POST)
  if form.is_valid():
    new_reservations = form.save(commit=False)
    new_reservations.profile_id = profile_id
    new_reservations.restaurant_id = restaurant_id
    new_reservations.save()
  return render(request, 'reservation.html', {'restaurant_id': restaurant_id, 'profile_id': profile_id, 'reservation_form' : form})
  
