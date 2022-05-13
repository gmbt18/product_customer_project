from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'pcims_app/home.html')