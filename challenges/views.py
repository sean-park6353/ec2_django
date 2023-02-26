from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("This works")


def faburary(request):
    return HttpResponse("This is Faburary page")