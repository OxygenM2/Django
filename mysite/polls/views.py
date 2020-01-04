from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("hellwo , this is the message we've received ! ")


