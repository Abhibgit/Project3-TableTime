from django.urls import path
from . import views
from .models import Restaurant
from .models import Reviews, Reservations


urlpatterns = [
  path('', views.home, name='home'),
  path('restaurant/', views.restaurant_index, name='restaurant'),
  path('userprofile/', views.user_profile_index, name='user_profile'),
  # path('restaurant_reservation/', views.restaurant_reservation, name='restaurant_reservation'),
  path('account_settings/', views.account_settings, name='account_settings'),
  path('accounts/signup/', views.signup, name='signup'),
  path('savedrestaurants/', views.saved_restaurants_index, name='saved_restaurants'),
  path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='detail'),
  path('restaurant/<int:restaurant_id>/add_review/', views.add_review, name='add_review'),
  path('restaurant/<int:restaurant_id>/add_reservations/<int:profile_id>/', views.add_reservations, name='add_reservations'),
  path('restaurant/<int:restaurant_id>/delete_reservations/<int:profile_id>/', views.delete_reservations, name='delete_reservations'),
]