from django.shortcuts import render, redirect
from crms_app.models import *
from crms_app.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
login_URL = "/crms/testLogin/"

def customerHome(request):
    return render(request, 'crms_app/pages/home.html')

def catalogCustomer(request):
    return render(request, 'crms_app/pages/catalogCustomer.html')

def catalogMonthly(request):
    return render(request, 'crms_app/pages/catalogMonthly.html')

def catalogProduct(request):
    products = [
        {
          "name": "COD Super Bass JBL Charge 3+ Mini Portable Bluetooth Speaker",
          "rating": 4.8,
          "stocks": 100,
          "reorderlvl": 20,
          "sellingprice": 179,
          "discount": 24,
          "isarchived": False
        },
        {
          "name": "120 Mini Portable Wireless Bluetooth Karaoke Speaker with FREE MICROPHONE",
          "rating": 4.7,
          "stocks": 80,
          "reorderlvl": 20,
          "sellingprice": 899,
          "discount": 79,
          "isarchived": False
        },
        {
          "name": "JBL Charge MINI2+ plus Portable Wireless Bluetooth Speaker High Quality",
          "rating": 4.7,
          "stocks": 69,
          "reorderlvl": 20,
          "sellingprice": 399,
          "discount": 58,
          "isarchived": False
        },
        {
          "name": "Original Super Bass Portable Bluetooth Speaker with Mic BT-1308 BT-1315 (3 inch) Wireless Bluetooth",
          "rating": 4.7,
          "stocks": 21,
          "reorderlvl": 20,
          "sellingprice": 100,
          "discount": 75,
          "isarchived": False
        },
        {
          "name": "S6U/s10u Portable Mini LED Bluetooth Speaker",
          "rating": 3.6,
          "stocks": 120,
          "reorderlvl": 20,
          "sellingprice": 75,
          "discount": 22,
          "isarchived": False
        }
    ]
    context = {
        'products': products
    }
    return render(request, 'crms_app/pages/catalogProduct.html', context)



def searchPage(request):
    return render(request, 'crms_app/pages/searchPage.html')

def detailedProduct(request):
    return render(request, 'crms_app/pages/detailedProduct.html')

def login_page(request):
    return render(request, 'crms_app/pages/login.html')

def passwordChange(request):
    return render(request, 'crms_app/pages/passwordChange.html')

def passwordForgot(request):
    return render(request, 'crms_app/pages/passwordForgot.html')

def register(request):
    return render(request, 'crms_app/pages/register.html')

# Customer Information
#CustomerInformation Page
@login_required(login_url=login_URL)
def customerInformation(request,pk):
    customer = AuthUser.objects.get(id=pk,user_type=2)
    customerInformation, created = CustomerInformation.objects.get_or_create(customer=customer)
    form = CustomerInformationUpdateForm(instance=customerInformation)
    if(request.method == "POST"):
        form = CustomerInformationUpdateForm(request.POST, instance=customer)
        if(form.is_valid()):
            form.save()
            return redirect("/crms/customerInformation/"+pk)
    data = {"form": form}
    return render(request, 'crms_app/Customer Information/customerInformation.html', data)


@login_required(login_url=login_URL)
def productComplaint(request,pk):
    customer = AuthUser.objects.get(id=pk, user_type=2)
    productComplaint, created = ProductComplaint.objects.get_or_create(customer=customer)
    data = {
        "productComplaint" : productComplaint,
        'created' : created,
    }
    return render(request, 'crms_app/Customer Information/productComplaint.html', data)

@login_required(login_url=login_URL)
def customerReview(request,pk):
    customer = AuthUser.objects.get(id=pk, user_type=2)
    customerReview, created = CustomerReview.objects.get_or_create(customer=customer)
    data = {
        "customerReview" : customerReview,
        'created' : created,
    }
    return render(request, 'crms_app/Customer Information/customerReview.html', data)







#OPTIONAL
def about(request):
    return render(request, 'crms_app/pages/about.html')

#TESTS
#CRUD
@login_required(login_url=login_URL)
def manageCustomers(request):
    #query
    customers = getCustomersList()
    customerInformations = []
    for customer in customers:
        customerInformations.append(getCustomerInformation(customer))
    # Gets all the customer information
    data = {"customers": customers,
            "customerInformations": customerInformations,
    }
    return render(request, 'crms_app/pages/manageCustomers.html', data)

def create(request):
    form = AuthUserCreationForm()
    if(request.method == "POST"):
        form = AuthUserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/crms/manageCustomers")

    data = {"form": form}
    return render(request, 'crms_app/CRUD/create.html', data)

def update(request,pk):
    customer = AuthUser.objects.get(id=pk,user_type=2)
    customerInformation, created = CustomerInformation.objects.get_or_create(customer=customer)
    form = CustomerInformationUpdateForm(instance=customerInformation)
    if(request.method == "POST"):
        form = CustomerInformationUpdateForm(request.POST, instance=customerInformation)
        if(form.is_valid()):
            form.save()
            return redirect("/crms/manageCustomers")
    data = {"form": form,
    "customerInformation": customerInformation,
    
    }
    return render(request, 'crms_app/CRUD/update.html', data)


def delete(request,pk):
    customer = AuthUser.objects.get(id=pk,user_type=2)
    customer.delete()
    return redirect("/crms/manageCustomers")






#REGISTER-LOGIN
def testRegister_page(request):
    form = AuthUserCreationForm()
    if( request.method == "POST"):
        form = AuthUserCreationForm(request.POST)
        if( form.is_valid() ):
            form.save()
            messages.success(request, "Account was created for "+form.cleaned_data.get("username"))
            return redirect('/crms/testLogin')

    data = {"form": form}
    return render(request, 'crms_app/TEST-Register-Login/test-register.html',data)


def testLogin_page(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        customer = authenticate(request, username=username, password=password)
        
        if customer is not None:
            login(request, customer)
            return redirect('/crms/')
        else:
            print("Login Fail.")
            messages.error(request, "Incorrect password or username.")


    return render(request, 'crms_app/TEST-Register-Login/test-login.html')


def testLogout_page(request):
    logout(request)
    return redirect('/crms/testLogin')


#Auxilliary functions
    #Create Functions

def getCustomersList():
    authUser = AuthUser.objects.filter(user_type=2)
    customers = []
    for customer in authUser:
        customers.append(customer)
    return customers

def getCustomerInformation(authUser):
    customerInformation, created = CustomerInformation.objects.get_or_create(customer=authUser)
    return customerInformation