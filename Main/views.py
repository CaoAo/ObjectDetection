from django.shortcuts import render
from django.http import HttpResponse
 
def index(request):
    return HttpResponse("Cao Ao")

# Create your views here.
