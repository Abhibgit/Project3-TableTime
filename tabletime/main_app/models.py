from django.db import models

# Create your models here.

class Restaurant(models.Model):
     names = models.CharField(max_length = 50)
     city = models.CharField(max_length = 100)
     cuisine = models.TextField(max_length = 100)
     cost = models.IntegerField()

     def __str__(self):
         self.name = name
         self.city = city
         self.cuisine = cuisine 
         self.cost = cost 

class User(models.Model):
     firstname = models.CharField(max_length = 100)
     lastname = models.CharField(max_length = 100)
     email = models.CharField(max_length = 100)
     phone = models.IntegerField()
     address = models.CharField(max_length = 100)
     picture = models.TextField(max_length = 100)
     notifications = models.BooleanField()

     def __str__(self):
         self.firstname = firstname
         self.lastname = lastname
         self.email = email
         self.phone = phone
         self.address = address
         self.picture = picture
         self.notifications = notifications


class Reviews(models.Model):
     comment = models.CharField(max_length = 100)
     star_rating = models.TextField(max_length = 100)

     def __str__(self):
          self. comment = comment 
          self.star_rating = star_rating
     
     


     
