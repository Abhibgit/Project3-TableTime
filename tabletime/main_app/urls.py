from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('restaurant/', views.restaurant, name='restaurant'),
  path('userprofile/', views.userprofile, name='userprofile'),
  path('restaurant_reservation/', views.restaurant_reservation, name='restaurant_reservation'),
  path('account_settings/', views.account_settings, name='account_settings'),
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('savedrestaurants/', views.savedrestaurants_index, name='index'),

]