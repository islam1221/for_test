from django.shortcuts import render
from django.http import HttpResponse,FileResponse
import random
# Create your views here.
a = random.randint(1,100)

def number_r(request):
    return HttpResponse(a)

def picture(request):
    file = .
    return FileResponse()

