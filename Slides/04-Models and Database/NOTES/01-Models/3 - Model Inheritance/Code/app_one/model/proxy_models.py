from django.db import models 

class User_Account(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()

class User_Profile(User_Account):
    class Meta:
        proxy = True
        
