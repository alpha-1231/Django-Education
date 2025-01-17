from django.db import models
from django.db.models import Avg,Min,Max,Count,Sum
from . managers import CustomManager, New_Manager,Manager_third
from .Querysets import CustomQuery,Other_Query

    
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=10)
    roll_no = models.IntegerField()
    objects = models.Manager()
    new_manager = CustomManager()
    new_new_manager = New_Manager()
    other_manager = CustomQuery.as_manager()
    third_manager = Manager_third.from_queryset(Other_Query)()
    
    # other_manager =New_Manager()
    

    def introduction(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")



    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['name']
        default_manager_name="objects"

    def __str__(self):
        return self.name



""" Student.objects.all() 
student1=Student.objects.create(name="name1",age=21,grade="F",roll_no=12)

python manage.py shell
from app.models import *
from os import system
a=system
b="cls"

system('cls')

Student.objects.all()
"""