from django.test import TestCase
from django.utils import timezone
import datetime
from django.urls import reverse

from .models import Question
# Create your tests here.

class QuestionModelTests(TestCase):
    def test_was_published(self):
        """
        was_published_recently() should return True for questions published within the last week.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)
        
        
class QuestionHomeTest(TestCase):
    def test_home(self):
        url = reverse("polls:home")
        response = self.client.get(url)
        print("Response --------------------------------",response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(self.client.get(url), "polls/index.html")
        
        
