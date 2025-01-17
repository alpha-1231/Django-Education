from django.db import models
from first_app.model import abstract_model,inherit_models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    
    
YEAR_IN_SCHOOL_CHOICES=[
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]   
SEX = {
    "M":"Male",
    "F":"Female",
    "O":"Other",
}

class ChoicesInput(models.Model):
    # first method as tuple 
    position = models.CharField(max_length=12, choices=YEAR_IN_SCHOOL_CHOICES)
    
    # second method as mapping
    sex = models.CharField(max_length=12,choices=SEX)
    
    # third method as enumeration
    color_types = models.TextChoices("Colors","GOLD WHITE BLACK PINK")
    fav_color = models.CharField(max_length=12,choices = color_types) 
    
# creating other models
abstract_model.otherPerson
inherit_models.anotherModel

