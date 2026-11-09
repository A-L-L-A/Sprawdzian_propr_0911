from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def raport(request):
    return render(request, "portal/raport.html", {"sekcje": []})