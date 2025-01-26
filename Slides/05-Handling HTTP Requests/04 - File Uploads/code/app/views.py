from django.shortcuts import render

# Create your views here.
from django import forms


class FileForm(forms.Form):
    filefield = forms.FileField()


def formView(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        print(request.FILES["filefield"])
        if form.is_valid():
            with open("new.jpg",'wb') as desti:
                for chunk in request.FILES['filefield']:
                    desti.write(chunk)
            print("validation done ---------------------------")
    form = FileForm()

    return render(request, "formd.html", context={"form": form})
