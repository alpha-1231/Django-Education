from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.conf.urls import handler404


# Create your views here.
def passer(request, exception):
    print(exception)  # Consider using logging instead of print for production
    return HttpResponse("Error in the server. The requested page was not found.", status=404)

# Assign the custom handler to Django's 404 error handler
handler404 = passer


def home(request):
    print("home is in the page. ")
    return HttpResponse("This is home")


def room(request, pk):
    print("This is room number: %d" % pk)
    return HttpResponse("This is room number: %d" % pk)


def host(request, name, pk):
    print("host view is called")
    a = f"Host is {name} and room is {pk} . "
    return HttpResponse(a)


def year(request, pk, year, name):
    try:
        print("-----------------------------------------")
        print(pk)
        a = f"User: {name} stayed in room no: {pk} at {year}"
        print("-----------------------------------------")
    except Exception as err:
        return HttpResponse(err)

    return HttpResponse(a)


def blog(request, pk):
    return HttpResponse(pk, " is passed in the view. ")


def otherblog(request, pagenumber):
    return HttpResponse(pagenumber, " is passed in the view. ")


def defaultView(request, pk=None, ott=None):
    # Assign default values if None
    if pk is None:
        pk = 9
    if ott is None:
        ott = 6
    return HttpResponse(f"pk: {pk} ----------------- ott: {ott}")



def error(request):
    raise Http404("error")


def extr(request,foo):
    return HttpResponse(foo)

def homeReturn(request):
    return render(request,"home.html",status=202)