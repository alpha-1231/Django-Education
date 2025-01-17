from django.db import models
from django.db.models import Avg,Min,Max,Count,Sum
# Create your models here.
class CustomQuery(models.QuerySet):
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

class Other_Query(models.QuerySet):
    def count(self):
        print("Count from the other query is called")
        return super().count()
    

