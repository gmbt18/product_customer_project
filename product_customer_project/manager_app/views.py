from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'manager_app/home.html')