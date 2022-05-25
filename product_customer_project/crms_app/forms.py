from django.forms import ModelForm, TextInput, PasswordInput, CharField, HiddenInput, NumberInput
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
from crms_app.models import * 
from django import forms

User = get_user_model()

USER_TYPE_CHOICES = {
        (1, 'Product Manager'),
        (2, 'Customer')
    }

SEX_CHOICES = {
    (0, "Male"),
    (1, "Female"),

}

class AuthUserCreationForm(UserCreationForm):
    attrs = { 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter Password' , 'required': True, } 
    password1 =  CharField( widget=PasswordInput(attrs=attrs) )
    password2 =  CharField( widget=PasswordInput(attrs=attrs) )
    class Meta:
        model = AuthUser
        fields = ['username', 'email', 'user_type', 'password1', 'password2']
        widgets = { 
            #insert bootstrap designs here
            'username': TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput' , 'placeholder':'Enter Username', 'required': True, } ),
            'email': TextInput( attrs={ 'type':'email', 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter Email Address', 'required': True, } ),

        }

class CustomerInformationUpdateForm(ModelForm):
    class Meta:
        model = CustomerInformation
        #insert here attributes of Customer to be included in form
        fields = ['name', 'birthday','sex', 'nationality', 'citizenship', 'picture', 'isSubscribed', 
        'presentAddress', 'permanentAddress', 'billingAddress', 'shippingAddress', 'officeAddress', 
        'personalCPNumber', 'officeCPNumber', 'homeLandlineNumber', 'officeLandlineNumber',
        'personalEmail', 'officeEmail']
        #Insert your design here (optional)
        emailAttributes = TextInput( attrs={ 'type':'email', 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter Email Address', 'required': False, } )
        addressAttributes = TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter Address', 'required': False, } ),
        widgets = { 
            'name': TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter name', 'required': False, } ),
            #'birthday':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter birthday', 'required': False, } ),
            'sex': TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter sex', 'required': False, } ),
            'nationality':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter nationality', 'required': False, } ), 
            'citizenship':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter citizenship', 'required': False, } ), 
            #'picture':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter sex', 'required': False, } ), 
            #'isSubscribed':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter sex', 'required': False, } ), 
            'presentAddress':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter presentAddress', 'required': False, } ), 
            'permanentAddress':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter permanentAddress', 'required': False, } ), 
            'billingAddress':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter billingAddress', 'required': False, } ), 
            'shippingAddress':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter shippingAddress', 'required': False, } ), 
            'officeAddress':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter officeAddress', 'required': False, } ), 
            'personalCPNumber':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter personalCPNumber', 'required': False, } ), 
            'officeCPNumber':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter officeCPNumber', 'required': False, } ), 
            'homeLandlineNumber':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter homeLandlineNumber', 'required': False, } ), 
            'officeLandlineNumber':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter officeLandlineNumber', 'required': False, } ),
            'personalEmail':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter personalEmail', 'required': False, } ), 
            'officeEmail':TextInput( attrs={ 'class': 'form-control', 'id':'floatingInput', 'placeholder':'Enter officeEmail', 'required': False, } ),
        }





class ProductComplaintForm(ModelForm):
    class Meta:
        model = ProductComplaint
        fields = "__all__"

class CustomerReviewForm(ModelForm):
    class Meta:
        model = CustomerReview
        fields = "__all__"


