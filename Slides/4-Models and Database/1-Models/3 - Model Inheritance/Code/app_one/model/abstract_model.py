from django.db import models

class Name(models.Model):
    name = models.CharField(max_length = 150)
    age = models.IntegerField()
    address = models.CharField(max_length = 250)
    def __str__(self):
        return 
    class Meta:
        abstract = True
