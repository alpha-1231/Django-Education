from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from .models import UserData

# Create your views here.

def my_view(request):
    with connection.execute_wrapper(wrapper):
        a = UserData.objects.all()
        return HttpResponse(f"Hi from the wrapped view....{a}")













# Wrapper Function
    
def wrapper(execute,sql,params,many,context):
    print("Wrapper is called\n")
    # print(*args)
    print("execute: ",execute,"\n")
    print("sql: ",sql,"\n")
    print("params: ",params,"\n")
    print("many: ",many,"\n")
    print("context: ",context,"\n")
    