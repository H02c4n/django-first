from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homesecond(req):
    return HttpResponse('Hi from second')