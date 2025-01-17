import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    @admin.display(
    description="Published within the last week?",
        ordering="pub_date",
        boolean=True,
    
)

    # def was_published_recently(self):
    #     if  ( (self.pub_date+timezone.timedelta(7)) > timezone.now() ):
    #         print((self.pub_date+timezone.timedelta(7)))
    #         print(timezone.now())
    #         return True
    #     else:
    #         return False

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
