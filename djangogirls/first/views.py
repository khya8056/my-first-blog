from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

def home(request):
    return render(request,'first/index.html')

def bar(request):
    return render(request,'first/bar.html')

def floor(request):
    return render(request,'first/floor.html')

def beam(request):
    return render(request,'first/beam.html')

def vault(request):
    return render(request,'first/vault.html')
