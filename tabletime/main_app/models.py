from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Occasions for the reservation feature
OCCASIONS = (
    ('A', 'Anniversary'),
    ('B', 'Birthday'),
    ('C', 'Celebration'),
    ('D', 'Date Night'),
    ('M', 'Business Meeting')
)

class Restaurant(models.Model):
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    cuisine = models.TextField(max_length = 100)
    cost = models.IntegerField()

    # def __str__(self):
    #     self.name = name
    #     self.city = city
    #     self.cuisine = cuisine 
    #     self.cost = cost 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    def __str__(self):
        return f"{self.user.username}"


class Reviews(models.Model):
    comment = models.CharField(max_length = 100)
    star_rating = models.TextField(max_length = 100)

    # def __str__(self):
    #   self. comment = comment 
    #   self.star_rating = star_rating
     
# join table for the reservations, choices for occcasions
class Reservations(models.Model):
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    occasion = models.CharField(max_length=1, choices=OCCASIONS, default=OCCASIONS[2][0])
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
 