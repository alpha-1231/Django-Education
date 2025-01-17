from django.db import models


class Dogs(models.Model):
    name = models.CharField(max_length=255)
    data = models.JSONField(null=True)
    def __str__(self):
        return self.name


"""
queries
from django.db.models import Value
from django.db.models import JSONField
from django.db.models.fields.json import KT


Dogs.objects.create(name="1",data={"name": "dog1","breed": "breed_one"})
Dogs.objects.create(name="2",data={"name": "dog2","breed": "breed_two"})
Dogs.objects.create(name="3",data={"name": "dog3","breed": "breed_three"})
Dogs.objects.create(name="4",data={"name": "dog4","breed": "breed_four"})

"""
