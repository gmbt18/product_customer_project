from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pcims_app/dashboard.html')

def products(request):
    return render(request, 'pcims_app/products.html')

def login(request):
    return render(request, 'pcims_app/login.html')

def changePassword(request):
    return render(request, 'pcims_app/changepassword.html')

def suppliers(request):
    return render(request, 'pcims_app/suppliers.html')
   
def supplierProducts(request):
    return render(request, 'pcims_app/supplierProducts.html')

def productReviews(request):
    return render(request, 'pcims_app/productsample.html')

def myReviews(request):
    return render(request, 'pcims_app/myreviews.html')