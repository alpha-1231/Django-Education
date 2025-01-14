from django.db import models

class Abstract_Model(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True
        
class otherPerson(Abstract_Model):
    pass
