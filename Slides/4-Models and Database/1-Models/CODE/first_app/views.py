from django.shortcuts import render
from django.forms import ModelForm

from . models import ChoicesInput
class NewForm(ModelForm):
    class Meta:
        model = ChoicesInput
        fields=["position","sex","fav_color"]

# Create your views here.

def home(request):
    return render(request,"base.html",{"form":NewForm})