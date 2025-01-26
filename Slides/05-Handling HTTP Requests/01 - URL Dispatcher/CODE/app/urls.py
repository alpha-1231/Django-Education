from django.urls import include, path
from .views import *

# app_name = "vishu"
patterns = (
    [
        path("", error, name="app_error"),
        path("home/", home, name="home"),
    ],
    "vishu",
)

urlpatterns = [
    path("",include(patterns))
]