from datetime import date

from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default="2020-10-10")
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
    
""" 
class 1 
we can create objects using
    1> instances
    2> Direct creation

    python manage.py shell
    from app.models import *
    
    
# 1 Instance method
# blog
blog1 = Blog(name="blog1",tagline="tagline for blog one")
blog1.save()
blog2 = Blog(name="blog2",tagline="tagline for blog two")
blog2.save()
blog3 = Blog(name="blog3",tagline="tagline for blog three")
blog3.save()
blog4 = Blog(name="blog4",tagline="tagline for blog four")
blog4.save()
blog5 = Blog(name="blog5",tagline="tagline for blog five")
blog5.save()

# author
author1=Author(name="author1",email="author1@gmail.com")
author1.save()
author2=Author(name="author2",email="author2@gmail.com")
author2.save()
author3=Author(name="author3",email="author3@gmail.com")
author3.save()
author4=Author(name="author4",email="author4@gmail.com")
author4.save()
author5=Author(name="author5",email="author5@gmail.com")
author5.save()

# entry
entry1 = Entry(blog=blog1,headline="Entry1 headline",body_text="body for 1",pub_date="2020-10-10")
entry1.save()
entry2 = Entry(blog=blog2,headline="Entry2 headline",body_text="body for 2",pub_date="2020-10-13")
entry2.save()
entry3 = Entry(blog=blog3,headline="Entry3 headline",body_text="body for 3",pub_date="2020-10-11")
entry3.save()
entry4 = Entry(blog=blog4,headline="Entry4 headline",body_text="body for 4",pub_date="2020-10-18")
entry4.save()
entry5 = Entry(blog=blog5,headline="Entry5 headline",body_text="body for 5",pub_date="2020-10-14")
entry5.save()

# 2 Direct Creation
# blog
blog1 = Blog.objects.create(name="blog1",tagline="tagline for blog one")
blog2 = Blog.objects.create(name="blog2",tagline="tagline for blog two")
blog3 = Blog.objects.create(name="blog3",tagline="tagline for blog three")
blog4 = Blog.objects.create(name="blog4",tagline="tagline for blog four")
blog5 = Blog.objects.create(name="blog4",tagline="tagline for blog five")

# author
author1=Author.objects.create(name="author1",email="author1@gmail.com")
author2=Author.objects.create(name="author2",email="author2@gmail.com")
autho3=Author.objects.create(name="author3",email="author3@gmail.com")
author4=Author.objects.create(name="author4",email="author4@gmail.com")
author5=Author.objects.create(name="author5",email="author5@gmail.com")

# entry
entry1 = Entry.objects.create(blog=blog1,headline="Entry1 headline",body_text="body for 1",pub_date="2020-10-5")
entry2 = Entry.objects.create(blog=blog2,headline="Entry2 headline",body_text="body for 2",pub_date="2020-10-4")
entry3 = Entry.objects.create(blog=blog3,headline="Entry3 headline",body_text="body for 3",pub_date="2020-10-6")
entry4 = Entry.objects.create(blog=blog4,headline="Entry4 headline",body_text="body for 4",pub_date="2020-10-7")
entry5 = Entry.objects.create(blog=blog5,headline="Entry5 headline",body_text="body for 5",pub_date="2020-10-8")

# queries method
# 1 updating
a. simple
instance.field_name = Value/ Var_name

b. many to many fields
instance.field.add(*args[class instances])

c. Foreign key
instance.field = class Instance

# 2 retrieving all
a. simple
Model_name.objects.all()

b. many to many fields
instance.field.all()

# 3 Filtering fields
a. simple
Model_name.objects.filter(field=value)
Model_name.objects.filter(**kwargs)

b. many to many fields
instance.field.filter(*args[class instances])

# 4 retreiving one object
a. simple
Model.objects.get(field=value)

b. many to many fields
instance.field.get(*args[class instances])

# 5 field lookup
Model.objects.filter(field__lookup_type=value)

# 6 for deleting 
a. simple
instance.delete()

b. many to many fields
instance.field.remove(*args[class instances])

"""


""" 
from django.db.models import F

"""