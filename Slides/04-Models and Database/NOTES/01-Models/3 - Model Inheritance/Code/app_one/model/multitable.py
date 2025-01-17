from django.db import models 

class First(models.Model):
    name = models.CharField(max_length=100)
    
class Second(First):
    age = models.IntegerField()
    
class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=120)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


""" 
console code

# Create a place object

# Create five Place objects
place1 = Place(name="Central Park", address="59th St & 5th Ave, New York, NY")
place2 = Place(name="Eiffel Tower", address="Champ de Mars, 5 Ave Anatole France, 75007 Paris")
place3 = Place(name="Colosseum", address="Piazza del Colosseo, 1, 00184 Roma RM, Italy")
place4 = Place(name="Great Wall of China", address="China")
place5 = Place(name="Taj Mahal", address="Dharavi Road, Agra, Uttar Pradesh, India")

# Save the objects to the database
place1.save()
place2.save()
place3.save()
place4.save()
place5.save()

# creating restaurant objects
restaurant1 = Restaurant(name="Pizza Palace", address="123 Main St", serves_pizza=True)
restaurant2 = Restaurant(name="Burger Barn", address="456 Oak Ave")
restaurant3 = Restaurant(name="Hot Dog Heaven", address="789 Elm St", serves_hot_dogs=True)
restaurant4 = Restaurant(name="Family Diner", address="101 Maple Rd", serves_pizza=True, serves_hot_dogs=True)
restaurant5 = Restaurant(name="The Coffee Shop", address="202 Pine St")

# Save the objects to the database
restaurant1.save()
restaurant2.save()
restaurant3.save()
restaurant4.save()
restaurant5.save()



"""