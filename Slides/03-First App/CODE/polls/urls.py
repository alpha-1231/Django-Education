# from django.urls import path
# from .views import home,detail,results,vote

# app_name = "polls"
# urlpatterns = [
#     path("home/",home,name="home"),
#     path("<int:question_id>/",detail,name="detail"),
#     path("<int:question_id>/results/",results,name="results"),
#     path("<int:question_id>/vote/",vote,name="vote"),
# ]

from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
 path("", views.IndexView.as_view(), name="home"),
 path("<int:pk>/", views.DetailView.as_view(), name="detail"),
 path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
 path("<int:question_id>/vote/", views.vote, name="vote"),
 ] 
 