from django.shortcuts import render, redirect
from app1.models import *

# Create your views here.

def landing(request):
    return render(request, 'app2/pages/landing.html')

def home(request):
    return render(request, 'app2/pages/home.html')

def viewModels(request):
    model1 = Model1.objects.all()
    model2 = Model2.objects.all()
    data = {
        "model1": model1,
        "model2": model2,
    }
    return render(request, 'app2/pages/viewModels.html', data)