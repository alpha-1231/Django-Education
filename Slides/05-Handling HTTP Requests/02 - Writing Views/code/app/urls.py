from django.urls import path,include
from .views import createData,sendData,errorView


urlpatterns = [
    path("create/",createData,name="create"),
    path("send/<int:pk>/",sendData,name="send"),
    path("error/",errorView,name="error")
]
