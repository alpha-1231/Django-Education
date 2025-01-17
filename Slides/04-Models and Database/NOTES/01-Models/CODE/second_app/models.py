from django.db import models

# Create your models here.
"""
commands:
# 1 for registering the changes in the database
python manage.py makemigrations [app_name]

# 2 To make the database table
python manage.py migrate

"""
# describing many to one relationship
"""
# first parent model
class model_name(models.Model):
    field1 = models.Field_Type(attributes......)

# second child model
class model_child(models.Model):
    field_name = models.ForeignKey(model_name,on_delete=models.CASCADE)    
    field_name = models.Field_Type(attributes.......)    
"""
# many to one relationship model
class Car(models.Model):
    name = models.CharField(max_length=120)

class Car_Models(models.Model):
    manufacturer = models.ForeignKey(Car,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=120)

# describe many to many relationship
""" 
# first parent model
class model_name(models.Model):
    field1 = models.Field_Type(attributes......)

# second child model
class model_child(models.Model):
    field_name = models.ManyToManyField(model_name)    
    field_name = models.Field_Type(attributes.......)   

"""
class Toppings(models.Model):
    toppings_name = models.CharField(max_length=120)

class Pizza(models.Model):
    pizza_toppings=models.ManyToManyField(Toppings)
    pizza_name = models.CharField(max_length=120)

# using the  middle models for storing extra information
""" 
# first model
class model_name(models.Model):
    field1 = models.Field_Type(attributes......)

# second model
class model_name(models.Model):
    field_name = models.ManyToManyField(model_name,through="model_name")    #through = write middle model name
    field1 = models.Field_Type(attributes......)

# middle model
class model_name(models.Model):
    model_one_field = models.ForeignKey(first_model,on_delete=models.CASCADE)
    model_two_field = models.ForeignKey(second_model,on_delete=models.CASCADE)
    field1 = models.Field_Type(attributes......)
    
"""

class Person(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name


class Group(models.Model):
    group_name = models.CharField(max_length=120)
    members = models.ManyToManyField(Person,through="Membership")
    def __str__(self):
        return self.group_name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=120)    

""" 
codes:
# to activate terminal
python manage.py shell

from second_app.models import Person,Group,Membership

creating persons + 1
>>> person_one = Person(name = "person_one")
>>> person_one.save()
>>> person_two = Person(name = "person_two") 
>>> person_two.save() 
>>> person_three = Person(name = "person_three")
>>> person_three.save() 

creating groups +2
>>> group_one = Group(group_name = "group_one")
>>> group_one.save()
>>> group_two = Group(group_name = "group_two")
>>> group_two.save()
>>> group_three = Group(group_name = "group_three")
>>> group_three.save()

creating memberships +3
>>> membership_one = Membership(person=person_one, group=Group_one,date_joined=date(2000,11,11))
>>> membership_one.save()
>>> membership_two = Membership(person=person_two, group=Group_one,date_joined=date(2000,10,10)) 
>>> membership_two.save()

# getting data
# group
>>> Group.objects.all()
>>> Person.objects.all()
>>> Membership.objects.all()

# using add
>>> from datetime import date
>>> group_two.members.add(person_two,through_defaults={"date_joined":date(1999,3,3),"invite_reason":"just nothing"}) 

# 
"""

# overriding save methods
class Other_Model(models.Model):
    name = models.CharField(max_length=230)
    def save(self, *args, **kwargs):
        print("Hello there , Save is called")
        super().save(*args, **kwargs) # Call the real save() method
        """ 
        >>> from second_app.models import Other_Model
        >>> Other_Model.objects.create(name="vishu")
        Hello there , Save is called
        <Other_Model: Other_Model object (1)>
        
        >>> a = Other_Model(name="vishu")
        >>> a.save()
        Hello there , Save is called
        """
        
# one to one relationship
# first parent model
"""
class model_name(models.Model):
    field1 = models.Field_Type(attributes......)

# second child model
class model_child(models.Model):
    field_name = models.ForeignKey(model_name,on_delete=models.CASCADE)    
    field_name = models.Field_Type(attributes.......)    
"""

class One_One(models.Model):
    name = models.CharField(max_length=120)

class One_Two(models.Model):
    relation = models.OneToOneField(One_One,max_length=120,on_delete=models.CASCADE)
