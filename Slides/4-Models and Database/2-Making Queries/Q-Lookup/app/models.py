from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    
""" 
for i in range(11):
    var_name = "user"+f"{i}"
    Data.objects.create(name=f"user{i}",age=i)
    
"""
