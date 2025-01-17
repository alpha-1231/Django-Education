from django.db import models 
class OtherModel(models.Model):
    pass

class Base(models.Model):
    m2m = models.ManyToManyField(
                                OtherModel,related_name="%(app_label)s_%(class)s_related",
                                related_query_name="%(app_label)s_%(class)ss")
    class Meta:
        abstract = True
    