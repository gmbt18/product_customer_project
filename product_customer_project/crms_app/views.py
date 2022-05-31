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
# for email
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
# for models
from pcims_app.models import *
# for hashing bulk_create() authusers
from django.contrib.auth.hashers import make_password

# Create your views here.
login_URL = "/crms/login/"

def customerHome(request):
    return render(request, 'crms_app/pages/home.html')

def catalogCustomer(request):
    return render(request, 'crms_app/pages/catalogCustomer.html')

def catalogMonthly(request):
    # unique_product_photos = ProductPhotos.objects.all().values('product').distinct()
    photos = ProductPhotos.objects.all().distinct('product')[:16]
    products = []
    for photo in photos:
        products.append(Product.objects.get(name=photo.product))
    context = {
        "products": products,
        "photos": photos
    }
    return render(request, 'crms_app/pages/catalogMonthly.html', context)

def catalogProduct(request):
    products = Product.objects.filter(isarchived=False)
    # print(products.values())
    photos = ProductPhotos.objects.all()
    productsCpy = [product for product in products.values()]
    photosCpy = [photo for photo in photos.values()]
    # print(photos.values())
    # print(productsCpy)
    i = 0
    for product in productsCpy:
        product['category'] = products.filter(name=product['name'])[0].category.name
        for photo in photosCpy:
            if product['id'] == photo['product_id']:
                if not photo['filename'] == 'https://lzd-img-global.slatic.net/g/tps/tfs/TB1oP2bbQvoK1RjSZFNXXcxMVXa-300-200.png':
                    product['photo'] = photo['filename']
                    continue
                continue
        if not product.__contains__('photo'):
            product['photo'] = 'https://wallpaperaccess.com/full/1285952.jpg'
        product["getRatings"] = products[i].getRatings
        product["complaintsCount"] = getProductComplaintsCount(product['id'])
        i += 1

    # print(productsCpy[0])
    # print(products[0].getRatings)

    context = {
        'products': productsCpy
    }
    return render(request, 'crms_app/pages/catalogProduct.html', context)



def searchPage(request):
  auth_users = []
  customers = []
  if request.user.is_superuser:
    auth_users = AuthUser.objects.all()
    customers = CustomerInformation.objects.all()
    # customers = CustomerInformation.objects.all()[:100]
  context = {
    "auth_users": auth_users,
    "customers": customers
  }
  # print(customers)
  # if(request.method == "POST"):
  #   print(list(request.POST.items()))
  return render(request, 'crms_app/pages/searchPage.html', context)

def detailedProduct(request,pk):
    data = {}
    customerReviewers = []
    reviewForm = CustomerReviewForm()
    try:
        customer = AuthUser.objects.get(id=request.user.id)
        data["isRegistered"] = True
    except AuthUser.DoesNotExist:
        data["isRegistered"] = False
    product = Product.objects.get(id=pk)
    # print(customer, request.user)

    reviews = CustomerReview.objects.filter(product=product)
    photos = ProductPhotos.objects.all().filter(product=product)
    reviewNum = len(reviews)
    mean_rating = 0
    if(reviewNum != 0):
        for review in reviews:
            mean_rating += review.rating
            customerReviewers.append(getCustomerInformation(review.customer))
        mean_rating = mean_rating/reviewNum
    data['reviewNum'] = reviewNum
    data['reviews'] = reviews
    data["mean_rating"] = mean_rating
    data["customerReviewers"] = customerReviewers
    data['product'] = product
    data['photos'] = photos
    # print(customerInformation.values()[0])
    # print(customerInformation.first().picture.url)
    
    if(data.get("isRegistered")):
        customerInformation, isInfoCreated = CustomerInformation.objects.get_or_create(customer=customer)
        if(customerInformation.picture):
            data['picture'] = customerInformation.picture.url
        else:
            data['picture'] = customerInformation.picture
        data['customerInformation'] = customerInformation

        reviewForm = CustomerReviewForm()
        if(request.method == "POST" and data.get("isRegistered")):
            print("post items")
            files_values = request.FILES.copy()
            files_values['picture'] = customerInformation.picture

            review, created = CustomerReview.objects.get_or_create(customer=customer,product=product)
            print(review)
            reviewForm = CustomerReviewForm(request.POST, files_values, instance=review)
            print('errors')
            print(reviewForm.errors)
            print(list(reviewForm.errors))
            if(reviewForm.is_valid()):
                reviewForm.save()
                print("Form is valid")
                messages.success(request, "The review was created on "+ product.name)
                return redirect(f"/crms/detailedProduct/{pk}")

        data['reviewForm'] = reviewForm

    return render(request, 'crms_app/pages/detailedProduct.html', data)

# def detailedProduct(request):
#     data = {}
#     reviewForm = CustomerReviewForm()
#     customer = []
#     try:
#         customer = AuthUser.objects.get(id=request.user.id)
#         data["isRegistered"] = True
#     except AuthUser.DoesNotExist:
#         data["isRegistered"] = False
#     customerInformation = {}
#     try:
#       if customer != []:
#         customerInformation = CustomerInformation.objects.get(customer=customer)
#     except CustomerInformation.DoesNotExist:
#       pass
#     data["customer"] = customer
#     data["customerInformation"] = customerInformation
    
#     reviews = CustomerReview.objects.filter(product=product['id'])
#     print(product)
#     reviewNum = len(reviews)
#     print(reviews)
#     print(reviewNum)
#     mean_rating = 0
#     if(reviewNum != 0):
#         for review in reviews:
#           mean_rating += review['rating']
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
#             return redirect(f"/crms/detailedProduct/")
#     data['photos'] = photos
#     data['product'] = product
#     data['reviewForm'] = reviewForm

#     return render(request, 'crms_app/pages/detailedProduct.html', data)

@login_required(login_url=login_URL)
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

@csrf_protect
def login_page(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        customer = authenticate(request, username=username, password=password)
        customerInformation = CustomerInformation.objects.filter(customer=customer)

        if customer is not None and (customer.user_type == 2 or customer.user_type == 3):
            if len(customerInformation) == 0:
                # print((CustomerInformation.objects.last()).name)
                # print(CustomerInformation.objects.latest('id'))
                # print((CustomerInformation.objects.last()).id)
                # print('test', customer.id)
                login(request, customer)
                return redirect(f"/crms/customerInfo/{customer.id}")
            else:
                login(request, customer)
                return redirect('/crms/')
        else:
            print("Login Fail.")
            messages.error(request, "Incorrect password or username.")
        
    return render(request, 'crms_app/pages/login.html')

def passwordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/crms/passwordChange')
        else:
            messages.error(request, 'Please correct the error above.')
    else:
        form = PasswordChangeForm(request.user)
    
    data = {
      "form": form,
    }

    return render(request, 'crms_app/pages/passwordChange.html', data)

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = AuthUser.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "crms_app/TEST-Register-Login/password_reset_email.html"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'customer-relationship@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/crms/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="crms_app/TEST-Register-Login/test-forgotPassword-form.html", context={"password_reset_form":password_reset_form})


def register(request):
    form = AuthUserCreationForm()
    if( request.method == "POST"):
        form = AuthUserCreationForm(request.POST)
        if( form.is_valid() ):
            form.save()
            messages.success(request, "Account was created for "+form.cleaned_data.get("username"))
            if request.user.is_superuser:
                customer = AuthUser.objects.last()
                return redirect(f"/crms/customerInfo/{customer.id}")
            return redirect('/crms/login')
    data = {"form": form}
    return render(request, 'crms_app/pages/register.html', data)

# Customer Information
#CustomerInformation Page
@login_required(login_url=login_URL)
def customerInformation(request,pk):
    print('custInfo: ', CustomerInformation.objects.latest('id'))
    print('test')
    customer = AuthUser.objects.get( Q(id=pk,user_type=2) | Q(id=pk,user_type=3) )
    print(customer, pk, customer.id)
    customerInformation, isNew = CustomerInformation.objects.get_or_create(customer=customer, id=(CustomerInformation.objects.last()).id+1)
    # other_users = []
    # other_customers = []
    # if request.user.is_superuser:
    #   other_users = AuthUser.objects.exclude(id=pk)
    #   other_customers = CustomerInformation.objects.exclude(customer=customer)
    # data["other_users"] = other_users
    # data["other_customers"] = other_customers
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
    if not request.user.is_superuser:
        pk = str(request.user.id)
    customer = AuthUser.objects.get( Q(id=pk,user_type=2) | Q(id=pk,user_type=3) )
    print(request.user.id, customer.id)
    customerInformation, isNew = CustomerInformation.objects.get_or_create(customer=customer, defaults={'customer': customer ,'id': (CustomerInformation.objects.last()).id+1})
    form = CustomerInformationUpdateForm(instance=customerInformation)
    other_users = []
    other_customers = []
    if request.user.is_superuser:
      other_users = AuthUser.objects.exclude(id=pk)
      other_customers = CustomerInformation.objects.exclude(customer=customer)
    data = {}
    data["other_users"] = other_users
    data["other_customers"] = other_customers
    data["customerInformation"] = customerInformation
    if(request.method == "POST"):
        form = CustomerInformationUpdateForm(request.POST, request.FILES, instance=customerInformation)
        print(list(request.POST.items()))
        print(request.POST.getlist('[]'))
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
      form = CustomerInformationUpdateForm(request.POST, request.FILES, instance=customerInformation)
    #   print(list(request.POST.items()))
    #   print(list(form.errors))
      if(form.is_valid()):
        form.save()
        # print(request.build_absolute_uri())
        if request.user.is_superuser and 'searchPage' in request.META.get('HTTP_REFERER'):
            return redirect("/crms/searchPage/")
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
            # print(form.cleaned_data)
            # target_username=form.cleaned_data.get("username")
            # print(AuthUser.objects.filter(username=target_username).id)
            if request.user.is_superuser:
              return redirect('/crms/searchPage')
            return redirect('/crms/login')

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
              return redirect(f"/crms/customerInformation/{customer.id}")
            else:
              login(request, customer)
              return redirect('/crms/')
        else:
            print("Login Fail.")
            messages.error(request, "Incorrect password or username.")


    return render(request, 'crms_app/TEST-image.pngRegister-Login/test-login.html')


def testLogout_page(request):
    logout(request)
    return redirect('/crms/login')

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
  sendSubscribeCatalog(request)
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


def getProductsWithComplaints():
    # Returns a list of product with complaints: DISTINCT
    productWithComplaints = []
    productComplaints = ProductComplaint.objects.all()
    for productComplaint in productComplaints:
        if(productComplaint.product not in productWithComplaints):
            productWithComplaints.append(productComplaint.product)
    
    return productWithComplaints

def getProductComplaints(product):
    # Returns a list of productComplaints type
    productComplaints = ProductComplaint.objects.filter(product=product)
    complaints = []
    for complaint in productComplaints:
        complaints.append(complaint)
    return complaints

def getProductComplaintsCount(product):
    productComplaints = ProductComplaint.objects.filter(product=product)
    return len(productComplaints)


def sendSubscribeCatalog(request):
    associated_users = AuthUser.objects.filter(Q(email=request.user.email))
    # photos = ProductPhotos.objects.all().distinct('product')[:16]
    # products = []
    # for photo in photos:
    #     products.append(Product.objects.get(name=photo.product))
    products = Product.objects.all()[:16]
    if associated_users.exists():
        for user in associated_users:
            subject = "Our Monthly Catalog"
            email_template_name = "crms_app/TEST-Register-Login/subscribe-catalog-email.html"
            c = {
            "email":user.email,
            'domain':'127.0.0.1:8000',
            'site_name': 'Website',
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "user": user,
            'token': default_token_generator.make_token(user),
            'protocol': 'http',
            "products": products,
            }
            email = render_to_string(email_template_name, c)
            try:
                send_mail(subject, "Review our monthly catalog", 'customer-relationship@gmail.com' , [user.email], fail_silently=False, html_message=email)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')




def sendMonthlyCatalog(request):
    sendAllSubscribeCatalog(request)
    return redirect("/crms/searchPage/")

def sendAllSubscribeCatalog(request):
    customerInformations = CustomerInformation.objects.filter(Q(isSubscribed=True))
    associated_users = []
    for customerInformation in customerInformations:
        associated_users.append(customerInformation.customer)
    mailing_list = []
    for user in associated_users:
        if(user.email):
            mailing_list.append(user.email)
    print(mailing_list)
    products = Product.objects.all()
    if len(associated_users) > 0:
        subject = "Our Monthly Catalog"
        email_template_name = "crms_app/TEST-Register-Login/monthly-catalog-email.html"
        c = {
        "email":user.email,
        'domain':'127.0.0.1:8000',
        'site_name': 'Website',
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "user": user,
        'token': default_token_generator.make_token(user),
        'protocol': 'http',
        "products": products,
        }
        email = render_to_string(email_template_name, c)
        try:
            send_mail(subject, "Review our monthly catalog", 'customer-relationship@gmail.com' ,mailing_list, fail_silently=False, html_message=email)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')