from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth import login
from .models import Profile, Reservations, Reviews
from .forms import ReviewForm
from .forms import ReservationForm
import requests
import os
from django.contrib.auth.decorators import login_required
 
YELP_KEY = os.environ['YELP_KEY']


# Create your views here.

def home(request):
  return render(request,'homepage.html')

@login_required
def user_profile_index(request):
  user_profile = Profile.objects.get(user=request.user)
  reservations = Reservations.objects.filter(user_id=user_profile.id)
  return render(request,'userprofile/index.html', {'user_profile': user_profile, 'reservations': reservations})

def account_settings(request):
  return render(request,'accountsettings/account_settings.html')

@login_required
def saved_restaurants_index(request):
  savedrestaurants=[]
  return render(request, 'savedrestaurants/index.html/', {'savedrestaurants': savedrestaurants})    

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = ProfileForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('user_profile')
    else:
      error_message = 'Invalid sign up - try again'
  form = ProfileForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def restaurant_detail(request, restaurant_name, restaurant_id):
  print(restaurant_id)
  print(restaurant_name)
  r=requests.get(f"https://api.yelp.com/v3/businesses/{restaurant_id}", headers={'Authorization':f'Bearer {YELP_KEY}'})
  restaurant_info = r.json()
  user_profile = Profile.objects.get(user=request.user)
  reviews_form = ReviewForm()
  review_data = Reviews.objects.filter(restaurant=restaurant_id)
  return render(request, 'restaurantpage/restaurant_detail.html', {'restaurant_info': restaurant_info, 'reviews_form': reviews_form, 'profile_id': user_profile.id, 'review_data': review_data, 'restaurant_name': restaurant_name})

@login_required
def add_review(request, restaurant_id):
    # create a ModelForm instance using the data in request.POST
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.restaurant = restaurant_id
    new_review.save()
  return redirect('detail', restaurant_id=restaurant_id)

@login_required
def add_reservations(request, restaurant_name, restaurant_id, profile_id):
    # create a ModelForm instance using the data in request.POST
  form = ReservationForm(request.POST)
  if form.is_valid():
    print(form)
    new_reservations = form.save(commit=False)
    new_reservations.user_id = profile_id 
    new_reservations.restaurant_id = restaurant_id
    new_reservations.restaurant_name = restaurant_name
    new_reservations.save()
    return redirect('user_profile')
  else:
    return render(request, 'reservation.html', {'restaurant_id': restaurant_id, 'profile_id': profile_id, 'reservation_form' : form, 'restaurant_name': restaurant_name})

@login_required
def update_reservations(request, reservation_id):
  reservation = Reservations.objects.get(id=reservation_id)
  if request.method == 'POST':
    form = ReservationForm(request.POST, instance=reservation)
    print("form: ", form)
    if form.is_valid():
      form.save()
      return redirect('user_profile')
  else:
    form = ReservationForm(instance=reservation)
    return render(request, 'reservation/reservation_update.html', {'reservation_form': form, 'reservation_id': reservation_id})

@login_required
def delete_reservations(request, reservation_id):
  Reservations.objects.get(id=reservation_id).delete()

  return redirect('user_profile')

def search_restaurant(request):
  res = requests.get(f"https://api.geocod.io/v1.7/geocode?q={request.POST['location']}&country=CA&api_key={os.environ['GEOCODIO_API']}")
  geo_location = res.json()
  lat = geo_location['results'][0]['location']['lat']
  lng = geo_location['results'][0]['location']['lng']
  r=requests.get("https://api.yelp.com/v3/businesses/search", params = {'latitude': lat, 'longitude': lng, 'term': request.POST['term']}, headers={'Authorization':f'Bearer {YELP_KEY}'})
  business_data = r.json()
  user_profile = Profile.objects.get(user=request.user)
  return render(request, "restaurantpage/restaurant.html", {'business_data': business_data['businesses'], 'profile_id': user_profile.id})

