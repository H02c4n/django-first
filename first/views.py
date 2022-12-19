from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homefirst(req):
    #return HttpResponse('Hi from first')
    return render(req, 'index.html', {"name":"Halil Özcan"})