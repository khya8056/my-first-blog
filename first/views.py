from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This is khyati</h1>")
