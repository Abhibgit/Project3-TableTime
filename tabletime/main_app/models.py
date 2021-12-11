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

