from re import I
from struct import pack
from django.shortcuts import render, redirect
from crms_app.models import *
from crms_app.forms import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect

from pcims_app.models import *

# Create your views here.
login_URL = "/crms/testLogin/"

def customerHome(request):
    return render(request, 'crms_app/pages/home.html')

def catalogCustomer(request):
    return render(request, 'crms_app/pages/catalogCustomer.html')

def catalogMonthly(request):
    return render(request, 'crms_app/pages/catalogMonthly.html')

def catalogProduct(request):
    products = Product.objects.filter(isarchived=False)
    photos = ProductPhotos.objects.all()
    i = 1
    for product in products:
      product['id'] = i
      for photo in photos:
        if product['name'] == photo['product']:
          if not photo['filename'] == 'https://lzd-img-global.slatic.net/g/tps/tfs/TB1oP2bbQvoK1RjSZFNXXcxMVXa-300-200.png':
            product['photo'] = photo['filename']
          break
      if not product.__contains__('photo'):
        product['photo'] = 'https://wallpaperaccess.com/full/1285952.jpg'
      i += 1
    
    # print(products[0])

    context = {
        'products': products
    }
    return render(request, 'crms_app/pages/catalogProduct.html', context)



def searchPage(request):
    if(request.method == "POST"):
      print(list(request.POST.items()))
      print(dict(request.POST.items()))
    return render(request, 'crms_app/pages/searchPage.html')

# def detailedProduct(request,pk):
#     data = {}
#     reviewForm = CustomerReviewForm()
#     try:
#         customer = AuthUser.objects.get(id=request.user.id)
#         data["isRegistered"] = True
#     except AuthUser.DoesNotExist:
#         data["isRegistered"] = False
#     product = Product.objects.get(id=pk)
#     reviews = CustomerReview.objects.filter(product=product)
#     reviewNum = len(reviews)
#     print(reviews)
#     print(reviewNum)
#     mean_rating = 0
#     if(reviewNum != 0):
#         for review in reviews:
#             mean_rating += review.rating
#         mean_rating = mean_rating/reviewNum
#     data['reviewNum'] = reviewNum
#     data['reviews'] = reviews
#     data["mean_rating"] = mean_rating

#     if(request.method == "POST" and data.get("isRegistered")):
#         review, created = CustomerReview.objects.get_or_create(customer=customer,product=product)
#         reviewForm = CustomerReviewForm(request.POST, instance=review)
#         if(reviewForm.is_valid()):
#             reviewForm.save()
#             messages.success(request, "The review was created on "+ product.name)
#             return redirect(f"/crms/detailedProduct/{pk}")
#     data['product'] = product
#     data['reviewForm'] = reviewForm

#     return render(request, 'crms_app/pages/detailedProduct.html', data)

def detailedProduct(request):
    data = {}
    reviewForm = CustomerReviewForm()
    customer = []
    try:
        customer = AuthUser.objects.get(id=request.user.id)
        data["isRegistered"] = True
    except AuthUser.DoesNotExist:
        data["isRegistered"] = False
    customerInformation = {}
    try:
      if customer != []:
        customerInformation = CustomerInformation.objects.get(customer=customer)
    except CustomerInformation.DoesNotExist:
      pass
    data["customer"] = customer
    data["customerInformation"] = customerInformation
    
    reviews = CustomerReview.objects.filter(product=product['id'])
    print(product)
    reviewNum = len(reviews)
    print(reviews)
    print(reviewNum)
    mean_rating = 0
    if(reviewNum != 0):
        for review in reviews:
          mean_rating += review['rating']
        mean_rating = mean_rating/reviewNum
    data['reviewNum'] = reviewNum
    data['reviews'] = reviews
    data["mean_rating"] = mean_rating

    if(request.method == "POST" and data.get("isRegistered")):
        review, created = CustomerReview.objects.get_or_create(customer=customer,product=product)
        reviewForm = CustomerReviewForm(request.POST, instance=review)
        if(reviewForm.is_valid()):
            reviewForm.save()
            messages.success(request, "The review was created on "+ product.name)
            return redirect(f"/crms/detailedProduct/")
    data['photos'] = photos
    data['product'] = product
    data['reviewForm'] = reviewForm

    return render(request, 'crms_app/pages/detailedProduct.html', data)

def submitProductComplaint(request, pk):
    data = {}
    productComplaintForm = ProductComplaintForm()
    data["productComplaintForm"] = productComplaintForm
    try:
        customer = AuthUser.objects.get(id=request.user.id)
        data["isRegistered"] = True
    except AuthUser.DoesNotExist:
        data["isRegistered"] = False
    
    product = Product.objects.get(id=pk)
    data["product"] = product
    if(request.method == "POST" and data.get("isRegistered")):
        productComplaint, created = ProductComplaint.objects.get_or_create(customer=customer,product=product)
        productComplaintForm = ProductComplaintForm(request.POST, instance=productComplaint)
        if(productComplaintForm.is_valid()):
            productComplaintForm.save()
            messages.success(request, "A complaint was created on "+ product.name)
            return redirect(f"/crms/detailedProduct/{pk}")

    return render(request, 'crms_app/pages/submitProductComplaint.html',data)

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
    customer = AuthUser.objects.get( Q(id=pk,user_type=2) | Q(id=pk,user_type=3) )
    customerInformation, isNew = CustomerInformation.objects.get_or_create(customer=customer)
    form = CustomerInformationUpdateForm(instance=customerInformation)
    data = {}
    data["customerInformation"] = customerInformation
    print(isNew)
    print(customer)
    print(customerInformation.picture)
    print(vars(customerInformation))
    if(request.method == "POST"):
        form = CustomerInformationUpdateForm(request.POST,request.FILES,instance=customerInformation)
        
        if(form.is_valid()):
            form.save()
            return redirect("/crms/customerInformation/"+pk)
    data["customer"] = customer
    data["customerInformation"] = customerInformation
    data["form"] = form
    data["isNew"] = isNew
    

    return render(request, 'crms_app/Customer Information/customerInformation.html', data)



@login_required(login_url=login_URL)
def customerInfo(request,pk):
    customer = AuthUser.objects.get( Q(id=pk,user_type=2) | Q(id=pk,user_type=3) )
    customerInformation, isNew = CustomerInformation.objects.get_or_create(customer=customer)
    form = CustomerInformationUpdateForm(instance=customerInformation)
    # print(vars(customerInformation))
    data = {}
    data["customerInformation"] = customerInformation
    if(request.method == "POST"):
        form = CustomerInformationUpdateForm(request.POST, request.FILES, instance=customerInformation)
        print(list(form.errors))
        if(form.is_valid()):
            form.save()
            return redirect("/crms/customerInfo/"+pk)
    data["customer"] = customer
    data["customerInformation"] = customerInformation
    data["form"] = form
    data["isNew"] = isNew

    return render(request, 'crms_app/pages/customerInfo.html', data)



def customerInfoAdd(request):
    form = AuthUserCreationForm()
    if(request.method == "POST"):
        form = AuthUserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/crms/customerInfo/")

    data = {"form": form}
    return redirect("/crms/pages/customerInfo.html")
    
def customerInfoUpdate(request,pk):
    customer = AuthUser.objects.get(Q(id=pk,user_type=2) | Q(id=pk,user_type=3))
    customerInformation, created = CustomerInformation.objects.get_or_create(customer=customer)
    form = CustomerInformationUpdateForm(instance=customerInformation)
    if(request.method == "POST"):
      form = CustomerInformationUpdateForm(request.POST, instance=customerInformation)
      print(list(request.POST.items()))
      print(list(form.errors))
      if(form.is_valid()):
        form.save()
        return redirect("/crms/customerInfo/"+pk)
    data = {
      "form": form,
      "customerInformation": customerInformation,
    }
    return redirect("/crms/pages/customerInfo/"+pk)

def customerInfoSubscribe(request,pk):
  customer = AuthUser.objects.get(id=pk,user_type=2)
  customerInformation, created = CustomerInformation.objects.get_or_create(customer=customer)
  form = CustomerInformationUpdateForm(instance=customerInformation)
  if(request.method == "POST"):
    form = CustomerInformationUpdateForm(request.POST, instance=customerInformation)
    print(list(request.POST.items()))
    print(list(form.errors))
    if(form.is_valid()):
      form.save()
      return redirect("/crms/customerInfo/"+pk)
  data = {
    "form": form,
    "customerInformation": customerInformation,
  }
  return redirect("/crms/customerInfo/"+pk)

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
    customer = AuthUser.objects.get( Q(id=pk,user_type=2) | Q(id=pk,user_type=3) )
    customerReview, created = CustomerReview.objects.get_or_create(customer=customer)
    data = {
        "customerReview" : customerReview,
        'created' : created,
    }
    return render(request, 'crms_app/Customer Information/customerReview.html', data)


def removeReview(request, pk):
    review = CustomerReview.objects.get(id=pk)
    product = review.product
    review.delete()
    messages.success(request, "The review was removed on "+ product.name)
    return redirect(f"/crms/detailedProduct/{product.id}")




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
    customer = AuthUser.objects.get( Q(id=pk,user_type=2) | Q(id=pk,user_type=3) )
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


@csrf_protect
def testLogin_page(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        customer = authenticate(request, username=username, password=password)
        customerInformation = CustomerInformation.objects.filter(customer=customer)

        if customer is not None and (customer.user_type == 2 or customer.user_type == 3):
            if len(customerInformation) == 0:
              login(request, customer)
              return redirect(f"/crms/customerInfo/{customer.id}")
            else:
              login(request, customer)
              return redirect('/crms/')
        else:
            print("Login Fail.")
            messages.error(request, "Incorrect password or username.")


    return render(request, 'crms_app/TEST-Register-Login/test-login.html')


def testLogout_page(request):
    logout(request)
    return redirect('/crms/testLogin')

@login_required(login_url=login_URL)
def testChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/crms/testChangePassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    
    data = {
      "form": form,
    }

    return render(request, 'crms_app/TEST-Register-Login/test-changePassword.html', data)


@login_required(login_url=login_URL)
def subscribeCatalog(request):
  customerInformation = getCustomerInformation(request.user)
  customerInformation.isSubscribed = True
  customerInformation.save()
  return redirect(f"/crms/customerInfo/{request.user.id}")

@login_required(login_url=login_URL)
def unsubscribeCatalog(request):
  customerInformation = getCustomerInformation(request.user)
  customerInformation.isSubscribed = False
  customerInformation.save()
  return redirect(f"/crms/customerInfo/{request.user.id}")



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


