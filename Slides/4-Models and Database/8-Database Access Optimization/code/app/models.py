from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=120)
    

class Toppings(models.Model):
    name = models.CharField(max_length=120)
    

class Pizza(models.Model):
    name = models.CharField(max_length=120)
    toppings = models.ManyToManyField(Toppings)


