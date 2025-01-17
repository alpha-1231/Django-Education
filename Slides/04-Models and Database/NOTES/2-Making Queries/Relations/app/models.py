from django.db import models

# Create your models here.

# many to one relationship
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class Vehicle(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, related_name="vehicle",on_delete=models.CASCADE)
    name  = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

# many to many relationship
class Disease(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Patient(models.Model):
    diseases = models.ManyToManyField(Disease)
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

# one to one relationship
class Boy(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Girl(models.Model):
    boy = models.OneToOneField(Boy, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
""" 
# creating tables
>>> python manage.py makemigrations
>>> python manage.py migrate
>>> python manage.py shell
>>> from app.models import *

# for clearing the screen
>>> from os import system as cmd
>>> cmd("cls")

# Many to one relationship Queries
1. Data creation
# Creating Manufacturer objects
manufacturer_1 = Manufacturer.objects.create(name="Toyota")
manufacturer_2 = Manufacturer.objects.create(name="Honda")
manufacturer_3 = Manufacturer.objects.create(name="Ford")
manufacturer_4 = Manufacturer.objects.create(name="BMW")
manufacturer_5 = Manufacturer.objects.create(name="Audi")

# Creating Vehicle objects related to manufacturers
vehicle_1 = Vehicle.objects.create(manufacturer=manufacturer_1, name="Corolla")
vehicle_2 = Vehicle.objects.create(manufacturer=manufacturer_1, name="Camry")
vehicle_3 = Vehicle.objects.create(manufacturer=manufacturer_1, name="Prius")
vehicle_4 = Vehicle.objects.create(manufacturer=manufacturer_2, name="Civic")
vehicle_5 = Vehicle.objects.create(manufacturer=manufacturer_2, name="Accord")
vehicle_6 = Vehicle.objects.create(manufacturer=manufacturer_2, name="CR-V")
vehicle_7 = Vehicle.objects.create(manufacturer=manufacturer_3, name="F-150")
vehicle_8 = Vehicle.objects.create(manufacturer=manufacturer_3, name="Mustang")
vehicle_9 = Vehicle.objects.create(manufacturer=manufacturer_3, name="Explorer")
vehicle_10 = Vehicle.objects.create(manufacturer=manufacturer_4, name="X5")
vehicle_11 = Vehicle.objects.create(manufacturer=manufacturer_4, name="M3")
vehicle_12 = Vehicle.objects.create(manufacturer=manufacturer_4, name="Z4")
vehicle_13 = Vehicle.objects.create(manufacturer=manufacturer_5, name="A4")
vehicle_14 = Vehicle.objects.create(manufacturer=manufacturer_5, name="Q5")
vehicle_15 = Vehicle.objects.create(manufacturer=manufacturer_5, name="A8")

# Now, there are 5 manufacturers and 15 vehicles related to them.

# through instance creation
# Creating Manufacturer instances
manufacturer_1 = Manufacturer(name="Toyota")
manufacturer_1.save()

manufacturer_2 = Manufacturer(name="Honda")
manufacturer_2.save()

manufacturer_3 = Manufacturer(name="Ford")
manufacturer_3.save()

manufacturer_4 = Manufacturer(name="BMW")
manufacturer_4.save()

manufacturer_5 = Manufacturer(name="Audi")
manufacturer_5.save()

# Creating Vehicle instances related to manufacturers
vehicle_1 = Vehicle(manufacturer=manufacturer_1, name="Corolla")
vehicle_1.save()

vehicle_2 = Vehicle(manufacturer=manufacturer_1, name="Camry")
vehicle_2.save()

vehicle_3 = Vehicle(manufacturer=manufacturer_1, name="Prius")
vehicle_3.save()

vehicle_4 = Vehicle(manufacturer=manufacturer_2, name="Civic")
vehicle_4.save()

vehicle_5 = Vehicle(manufacturer=manufacturer_2, name="Accord")
vehicle_5.save()

vehicle_6 = Vehicle(manufacturer=manufacturer_2, name="CR-V")
vehicle_6.save()

vehicle_7 = Vehicle(manufacturer=manufacturer_3, name="F-150")
vehicle_7.save()

vehicle_8 = Vehicle(manufacturer=manufacturer_3, name="Mustang")
vehicle_8.save()

vehicle_9 = Vehicle(manufacturer=manufacturer_3, name="Explorer")
vehicle_9.save()

vehicle_10 = Vehicle(manufacturer=manufacturer_4, name="X5")
vehicle_10.save()

vehicle_11 = Vehicle(manufacturer=manufacturer_4, name="M3")
vehicle_11.save()

vehicle_12 = Vehicle(manufacturer=manufacturer_4, name="Z4")
vehicle_12.save()

vehicle_13 = Vehicle(manufacturer=manufacturer_5, name="A4")
vehicle_13.save()

vehicle_14 = Vehicle(manufacturer=manufacturer_5, name="Q5")
vehicle_14.save()

vehicle_15 = Vehicle(manufacturer=manufacturer_5, name="A8")
vehicle_15.save()

2. Data getting
: Forward
>>> Manufacturer.objects.all()
<QuerySet [<Manufacturer: Toyota>, <Manufacturer: Honda>, <Manufacturer: Ford>, <Manufacturer: BMW>, <Manufacturer: Audi>]>
>>> ----------------------------------------------------------------
>>> #getting single manufacturer
>>> a=Manufacturer.objects.all()[0] 

: Backward
>>> #getting single manufacturer
>>> a=Manufacturer.objects.all()[0] 
>>> ------------------------------------------------------------------
>>> #getting the vehicle data
>>> ---------------------------------------------------------------
>>> a.vehicle_set.all()             
<QuerySet [<Vehicle: Corolla>, <Vehicle: Camry>, <Vehicle: Prius>]>
>>> 

3. Data updating
: Forward
>>> a.manufacturer = Manufacturer.objects.all()[1] 
>>> a.manufacturer
<Manufacturer: Honda>
>>> a.manufacturer = Manufacturer.objects.all()[0] 
>>> a.manufacturer
<Manufacturer: Toyota>
>>> a.save()

: Backward
>>> a.vehicle.all()
<QuerySet [<Vehicle: Corolla>, <Vehicle: Camry>, <Vehicle: Prius>]>
>>> a=a.vehicle.all()[0] 
>>> a.name
'Corolla'
>>> a.name = "visu"  
>>> a.name
'visu'
>>>   

4. Data deletion
>>> Manufacturer.objects.all().delete()
(20, {'app.Vehicle': 15, 'app.Manufacturer': 5})

>>>
>>> a = Manufacturer.objects.all()[0].delete()



# many to many relationship Queries
1. Data creation
# Create Disease instances
disease_1 = Disease.objects.create(name="Flu")
disease_2 = Disease.objects.create(name="COVID-19")
disease_3 = Disease.objects.create(name="Cancer")
disease_4 = Disease.objects.create(name="Diabetes")
disease_5 = Disease.objects.create(name="Hypertension")
disease_6 = Disease.objects.create(name="Asthma")
disease_7 = Disease.objects.create(name="Pneumonia")
disease_8 = Disease.objects.create(name="Malaria")
disease_9 = Disease.objects.create(name="Tuberculosis")
disease_10 = Disease.objects.create(name="Cholera")
disease_11 = Disease.objects.create(name="HIV/AIDS")
disease_12 = Disease.objects.create(name="Arthritis")
disease_13 = Disease.objects.create(name="Parkinson's")
disease_14 = Disease.objects.create(name="Epilepsy")
disease_15 = Disease.objects.create(name="Kidney Disease")
disease_16 = Disease.objects.create(name="Stroke")
disease_17 = Disease.objects.create(name="Heart Disease")
disease_18 = Disease.objects.create(name="Obesity")
disease_19 = Disease.objects.create(name="Dengue")
disease_20 = Disease.objects.create(name="Rheumatic Fever")

# Create Patient instances and associate them with diseases
patient_1 = Patient.objects.create(name="John Doe")
patient_1.diseases.set([disease_1, disease_2])  # Patient 1 has Flu and COVID-19

patient_2 = Patient.objects.create(name="Jane Smith")
patient_2.diseases.set([disease_3, disease_4])  # Patient 2 has Cancer and Diabetes

patient_3 = Patient.objects.create(name="Alice Johnson")
patient_3.diseases.set([disease_5, disease_6])  # Patient 3 has Hypertension and Asthma

patient_4 = Patient.objects.create(name="Bob Brown")
patient_4.diseases.set([disease_7, disease_8])  # Patient 4 has Pneumonia and Malaria

patient_5 = Patient.objects.create(name="Charlie Davis")
patient_5.diseases.set([disease_9, disease_10])  # Patient 5 has Tuberculosis and Cholera

patient_6 = Patient.objects.create(name="Diana Wilson")
patient_6.diseases.set([disease_11, disease_12])  # Patient 6 has HIV/AIDS and Arthritis

patient_7 = Patient.objects.create(name="Evan Moore")
patient_7.diseases.set([disease_13, disease_14])  # Patient 7 has Parkinson's and Epilepsy

patient_8 = Patient.objects.create(name="Grace Taylor")
patient_8.diseases.set([disease_15, disease_16])  # Patient 8 has Kidney Disease and Stroke

patient_9 = Patient.objects.create(name="Henry Anderson")
patient_9.diseases.set([disease_17, disease_18])  # Patient 9 has Heart Disease and Obesity

patient_10 = Patient.objects.create(name="Isla Thomas")
patient_10.diseases.set([disease_19, disease_20])  # Patient 10 has Dengue and Rheumatic Fever

patient_11 = Patient.objects.create(name="Jackie Lee")
patient_11.diseases.set([disease_1, disease_4])  # Patient 11 has Flu and Diabetes

patient_12 = Patient.objects.create(name="Katherine Clark")
patient_12.diseases.set([disease_2, disease_8])  # Patient 12 has COVID-19 and Malaria

patient_13 = Patient.objects.create(name="Leo Martinez")
patient_13.diseases.set([disease_3, disease_12])  # Patient 13 has Cancer and Arthritis

patient_14 = Patient.objects.create(name="Monica Perez")
patient_14.diseases.set([disease_6, disease_9])  # Patient 14 has Asthma and Tuberculosis

patient_15 = Patient.objects.create(name="Nathaniel Scott")
patient_15.diseases.set([disease_5, disease_10])  # Patient 15 has Hypertension and Cholera

patient_16 = Patient.objects.create(name="Olivia Harris")
patient_16.diseases.set([disease_11, disease_7])  # Patient 16 has HIV/AIDS and Pneumonia

patient_17 = Patient.objects.create(name="Paul Walker")
patient_17.diseases.set([disease_15, disease_17])  # Patient 17 has Kidney Disease and Heart Disease

patient_18 = Patient.objects.create(name="Quincy Robinson")
patient_18.diseases.set([disease_13, disease_14])  # Patient 18 has Parkinson's and Epilepsy

patient_19 = Patient.objects.create(name="Rita Lewis")
patient_19.diseases.set([disease_16, disease_18])  # Patient 19 has Stroke and Obesity

patient_20 = Patient.objects.create(name="Samuel Young")
patient_20.diseases.set([disease_19, disease_4])  # Patient 20 has Dengue and Diabetes

2. Data getting
>>> Disease.objects.all()
>>> Patient.objects.all()
>>> Patient.diseases.all()
>>> p = Patient.objects.all()[0]
>>> p.name
'John Doe'
>>> p.diseases.all()
<QuerySet [<Disease: Flu>, <Disease: COVID-19>]>
>>> 
--------------- backward ---------------
>>> a.patient_set.all()
<QuerySet [<Patient: John Doe>, <Patient: Jackie Lee>]>

3. Data updating
-- adding relations
patient = Patient.objects.get(name="John Doe")
disease = Disease.objects.get(name="Cancer")
patient.diseases.add(disease)

-- removing relations
patient = Patient.objects.get(name="John Doe")
disease = Disease.objects.get(name="Flu")
patient.diseases.remove(disease)

-- updating relations
patient = Patient.objects.get(name="John Doe")
new_disease = Disease.objects.create(name="Heart Disease")
patient.diseases.set([new_disease])  # Set to only the new disease

4. Data deletion
patient = Patient.objects.get(name="John Doe")
disease = Disease.objects.get(name="Flu")
patient.diseases.remove(disease)

disease = Disease.objects.get(name="Flu")
disease.delete()  # This will delete the disease and the association with patients

>>> # Get the patient
>>> patient = Patient.objects.get(name="John Doe")
>>> 
>>> # Remove all diseases from the patient (but the diseases will not be deleted from the database)
>>> patient.diseases.clear()
>>> 
>>> patient.diseases.all()  
<QuerySet []>

# one to one relationship Queries
1. Data creation
# Create 20 instances of Boy
boys = [
    Boy.objects.create(name="Boy 1"),
    Boy.objects.create(name="Boy 2"),
    Boy.objects.create(name="Boy 3"),
    Boy.objects.create(name="Boy 4"),
    Boy.objects.create(name="Boy 5"),
    Boy.objects.create(name="Boy 6"),
    Boy.objects.create(name="Boy 7"),
    Boy.objects.create(name="Boy 8"),
    Boy.objects.create(name="Boy 9"),
    Boy.objects.create(name="Boy 10"),
    Boy.objects.create(name="Boy 11"),
    Boy.objects.create(name="Boy 12"),
    Boy.objects.create(name="Boy 13"),
    Boy.objects.create(name="Boy 14"),
    Boy.objects.create(name="Boy 15"),
    Boy.objects.create(name="Boy 16"),
    Boy.objects.create(name="Boy 17"),
    Boy.objects.create(name="Boy 18"),
    Boy.objects.create(name="Boy 19"),
    Boy.objects.create(name="Boy 20")
]

# Create corresponding Girl instances, each linked to a Boy via the OneToOneField
girls = [
    Girl.objects.create(boy=boys[0], name="Girl 1"),
    Girl.objects.create(boy=boys[1], name="Girl 2"),
    Girl.objects.create(boy=boys[2], name="Girl 3"),
    Girl.objects.create(boy=boys[3], name="Girl 4"),
    Girl.objects.create(boy=boys[4], name="Girl 5"),
    Girl.objects.create(boy=boys[5], name="Girl 6"),
    Girl.objects.create(boy=boys[6], name="Girl 7"),
    Girl.objects.create(boy=boys[7], name="Girl 8"),
    Girl.objects.create(boy=boys[8], name="Girl 9"),
    Girl.objects.create(boy=boys[9], name="Girl 10"),
    Girl.objects.create(boy=boys[10], name="Girl 11"),
    Girl.objects.create(boy=boys[11], name="Girl 12"),
    Girl.objects.create(boy=boys[12], name="Girl 13"),
    Girl.objects.create(boy=boys[13], name="Girl 14"),
    Girl.objects.create(boy=boys[14], name="Girl 15"),
    Girl.objects.create(boy=boys[15], name="Girl 16"),
    Girl.objects.create(boy=boys[16], name="Girl 17"),
    Girl.objects.create(boy=boys[17], name="Girl 18"),
    Girl.objects.create(boy=boys[18], name="Girl 19"),
    Girl.objects.create(boy=boys[19], name="Girl 20")
]

1. Creating Instances
Create a single Boy instance:
- - boy = Boy.objects.create(name="John")
Create a single Girl instance:
- - girl = Girl.objects.create(boy=boy, name="Jane")
    Create multiple Boy instances:
    - - boys = [
        Boy.objects.create(name=f"Boy {i}")
        for i in range(1, 21)
    ]
    Create multiple Girl instances linked to boys:
    - - girls = [
        Girl.objects.create(boy=boys[i], name=f"Girl {i+1}")
        for i in range(20)
    ]
2. Retrieving Instances
Get all Boy instances:
- - boys = Boy.objects.all()

Get all Girl instances:
- - girls = Girl.objects.all()

Get a specific Boy by primary key:
- - boy = Boy.objects.get(pk=1)

Get a specific Girl by primary key:
- - girl = Girl.objects.get(pk=1)

Get a specific Girl by the associated Boy:
- - boy = Boy.objects.get(name="John")
girl = girl = Girl.objects.get(boy=boy)

Get Boy related to a Girl:
- - girl = Girl.objects.get(name="Jane")
boy = girl.boy

Get the first Boy instance:
- - boy = Boy.objects.first()

Get the first Girl instance:
- - girl = Girl.objects.first()

Get Boy instances with a specific condition (e.g., name contains "John"):
- - boys = Boy.objects.filter(name__icontains="John")

Get Girl instances linked to specific boys (e.g., where boy’s name is "John"):
- - girls = Girl.objects.filter(boy__name="John")

3. Updating Instances
Update a Boy instance:
- - boy = Boy.objects.get(name="John")
boy.name = "John Updated"
boy.save()

Update a Girl instance:
- - girl = Girl.objects.get(name="Jane")
girl.name = "Jane Updated"
girl.save()

Update multiple Boy instances:
- - Boy.objects.filter(name="John").update(name="John Updated")

Update the linked Boy for a Girl:
- - girl = Girl.objects.get(name="Jane")
new_boy = Boy.objects.get(name="New Boy")
girl.boy = new_boy
girl.save()

0. Deleting Instances
Delete a Boy instance:
- - boy = Boy.objects.get(name="John")
boy.delete()

1.Delete a Girl instance:
- - girl = Girl.objects.get(name="Jane")
girl.delete()

2.Delete all Boy instances:
- - Boy.objects.all().delete()

3.Delete all Girl instances:
- - Girl.objects.all().delete()

4.Delete a Boy instance and automatically delete the linked Girl due to CASCADE:
- - boy = Boy.objects.get(name="John")
boy.delete()  # The related Girl instance will be deleted automatically

5. Checking Relationships
Check if a Boy has a related Girl:
- - boy = Boy.objects.get(name="John")
if hasattr(boy, 'girl'):  # or boy.girl if the related object exists
    print("Boy has a girl")
else:
    print("Boy does not have a girl")
Check if a Girl has a linked Boy:
- - girl = Girl.objects.get(name="Jane")
if girl.boy:
    print("Girl has a boy")

6. Aggregation and Counting
Count the number of Boy instances:
- - boy_count = Boy.objects.count()

Count the number of Girl instances:
- - girl_count = Girl.objects.count()

Count how many Girls are linked to a specific Boy:
- - boy = Boy.objects.get(name="John")

girl_count = Girl.objects.filter(boy=boy).count()

7. Querying with Annotations
Count how many girls each boy has (in case of multiple relationships in future):
- - from django.db.models import Count
boys_with_girls = Boy.objects.annotate(num_girls=Count('girl'))

Get the Boy with the most linked Girls:
- - most_girls_boy = Boy.objects.annotate(num_girls=Count('girl')).order_by('-num_girls').first()
8. Relational Queries

Get all Girls related to boys whose names start with "J":
- - girls = Girl.objects.filter(boy__name__startswith="J")

Get all Boys linked to a specific Girl:
- - girl = Girl.objects.get(name="Jane")

boy = girl.boy  # Getting the related boy

9. Existence Check
Check if a Boy exists by name:
- - exists = Boy.objects.filter(name="John").exists()
Check if a Girl exists by name:
- - exists = Girl.objects.filter(name="Jane").exists()

10. Selecting Related Objects Efficiently
Select related Boy while querying Girl to optimize the number of queries:
- - girls = Girl.objects.select_related('boy').all()
Prefetch related Girls for a set of Boys:
- - boys = Boy.objects.prefetch_related('girl').all()

11. Bulk Operations
Bulk update Boy names:
- - Boy.objects.filter(name="John").update(name="John Updated")
Bulk delete Boy instances:
- - Boy.objects.filter(name__icontains="Boy").delete()

12. Using clear() for ManyToMany Relationships
Although the clear() method is typically used with ManyToManyField, it's important to mention:

Clear related Girls for a Boy (hypothetically, if Boy had a ManyToMany with Girl):
- - boy.girl.clear()  # Note: this is only valid for ManyToManyField, not OneToOneField


"""