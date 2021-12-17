from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('restaurant/search', views.search_restaurant, name='search_restaurant'),
  path('userprofile/', views.user_profile_index, name='user_profile'),
  path('account_settings/', views.account_settings, name='account_settings'),
  path('accounts/signup/', views.signup, name='signup'),
  path('savedrestaurants/', views.saved_restaurants_index, name='saved_restaurants'),
  path('restaurant/<str:restaurant_name>/<slug:restaurant_id>/', views.restaurant_detail, name='detail'),
  path('restaurant/<slug:restaurant_id>/add_review/', views.add_review, name='add_review'),
  path('restaurant/<str:restaurant_name>/<slug:restaurant_id>/add_reservations/<int:profile_id>/', views.add_reservations, name='add_reservations'),
  path('reservations/<slug:reservation_id>/delete_reservations/', views.delete_reservations, name='delete_reservations'),
  path('reservations/<slug:reservation_id>/update_reservations/', views.update_reservations, name='update_reservations'),
]