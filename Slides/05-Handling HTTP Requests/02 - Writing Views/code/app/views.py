from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,Http404
from .models import UserData
from asgiref.sync import sync_to_async
from django.core.exceptions import PermissionDenied
# Create your views here.
def createData(request):
    data = UserData.objects.create(name="vishu",age=21)
    return HttpResponse("User is created ",data)

async def sendData(request,pk):
    try:
        data = await  sync_to_async(UserData.objects.get)(pk=pk)
    except Exception as err:
        raise Http404(err)
    return HttpResponse(data.name,status=200)

def customError(request,exception):
    return HttpResponse("custom error handler..")

def errorView(request):
    raise PermissionDenied
