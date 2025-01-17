from django.db import models
from django.db.models import Avg,Min,Max,Count,Sum
from . Querysets import CustomQuery,Other_Query

    

class New_Manager(models.Manager):
    def get_queryset(self):
        return CustomQuery(self.model,using=self.db)
    def min_age(self):
        return self.get_queryset().min_age()
        

class CustomManager(models.Manager):
    def average(self):
        return self.aggregate(Avg("age"))
    
    def min_age(self):
        return self.aggregate(Min("age"))
    
    def max_age(self):
        return self.aggregate(Max("age"))
    
    def count_students(self):
        return self.aggregate(num_students = Count("pk"))
    
    def total_age(self):
        return self.aggregate(total_age = Sum("age"))
    
    def get_queryset(self):
        print("The base queryset is from the new model. ")
        return super().get_queryset()
    

class Manager_third(models.Manager):
    def other(self):
        return self.all().order_by("pk")
