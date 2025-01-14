from django.db import models

class oneModel(models.Model):
    name = models.CharField(max_length=120)

class anotherModel(oneModel):
    anothername = models.CharField(max_length=120)
    
