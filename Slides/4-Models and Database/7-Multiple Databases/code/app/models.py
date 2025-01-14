from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.IntegerField()
    phone = models.BigIntegerField()
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table="info"
