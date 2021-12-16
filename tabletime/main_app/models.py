from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
# Create your models here.


#class Restaurant(models.Model):
#    name = models.CharField(max_length = 100)
 #   city = models.CharField(max_length = 100)
  #  cuisine = models.TextField(max_length = 100)
   # cost = models.IntegerField()
    #id = models.CharField(max_length=200, primary_key=True)
    # reservations = models.ManytoManyField(Reservations)


# Connects the User model provided by Django and the additional information needed for the Profile.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    # saved_restaurants = models.ManytoManyField(Saved_restaurants)
    def __str__(self):
        return f"{self.user.username}"


class Reviews(models.Model):
    restaurant = models.CharField(max_length=100)
    comment = models.TextField(max_length = 100)
    star_rating = models.IntegerField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'restaurant_id' : self.restaurant})
    
    
     
# join table for the reservations, choices for occcasions
class Reservations(models.Model):
    date = models.DateField()
    time = models.IntegerField()
    people = models.IntegerField()
    occasion = models.CharField(max_length=100)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    restaurant = models.CharField(max_length=100)
    restaurant_name = models.CharField(max_length=100)
def __str__(self):
    return f"{self.get_restaurant_name()} is booked on {self.date} at {self.time}"

# class Saved_restaurants(models.Model):
#     name = 
 