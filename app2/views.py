from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1> this is my first view in app2</h1>')
def second(request):
    return HttpResponse('<h1> this is my second view in app2</h1>')
