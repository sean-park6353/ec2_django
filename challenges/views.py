from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Eat no meat for enitre month")


def faburary(request):
    return HttpResponse("Walk for at least 20 minutes every daty!")