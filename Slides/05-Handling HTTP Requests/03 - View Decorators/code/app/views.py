from django.views.decorators.common import no_append_slash
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, condition,require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Usar
from django.views.decorators.cache import cache_control,cache_page

# Create your views here.
# @require_http_methods(["GET"])
# def data(request):
#     qs = Usar.objects.all()
#     data = serialize('json',qs)
#     print(data)
#     return JsonResponse(data=data,safe=False)

# @csrf_exempt
# @require_http_methods(["POST"])
# def data(request):
#     data = {
#         "name":"Vishu",
#         "age":"21",
#         "address":"Nepal"
#     }
#     return JsonResponse(data=data,safe=False)

from datetime import datetime
def etagger(request,*args,**kwargs):
    return "new tag"

def lasty(request,*args,**kwargs):
    return datetime.now()


@condition(etag_func=etagger,last_modified_func=lasty)
@cache_control(name="vishu")
@no_append_slash
@require_GET
@csrf_exempt
def data(request):
    data = {"name": "Vishu", "age": "21", "address": "Nepal"}
    return JsonResponse(data=data, safe=False)
