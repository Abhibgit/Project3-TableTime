from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('restaurant/', views.restaurant_index, name='restaurant'),
  path('userprofile/', views.userprofile_index, name='userprofile'),
  path('restaurant_reservation/', views.restaurant_reservation, name='restaurant_reservation'),
  path('account_settings/', views.account_settings, name='account_settings'),
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/login/', views.login, name='login'),
  path('savedrestaurants/', views.savedrestaurants_index, name='index'),
]