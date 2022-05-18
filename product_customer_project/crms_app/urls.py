from django.urls import path
from . import views


urlpatterns = [
    path('', views.customerHome, name="customerHome"),
    path('catalogCustomer/', views.catalogCustomer, name="catalogCustomer"),
    path('catalogMonthly/', views.catalogMonthly, name="catalogMonthly"),
    path('catalogProduct/', views.catalogProduct, name="catalogProduct"),
    # Search
    path('searchPage/', views.searchPage, name="searchPage"),
    # CustomerInfos
    path('customerInfo/', views.customerInfo, name="customerInfo"),
    path('detailedProduct/', views.detailedProduct, name="detailedProduct"),
    path('login/', views.login_page, name="login"),
    path('passwordChange/', views.passwordChange, name="passwordChange"),
    path('passwordForgot/', views.passwordForgot, name="passwordForgot"),
    path('register/', views.register, name="register"),
    path('about/', views.about, name="about"),
    
    path('manageCustomers/', views.manageCustomers, name="manageCustomers"),
    path('create/', views.create, name="create"),
    path('update/<str:pk>', views.update, name="update"),
    path('delete/<str:pk>', views.delete, name="delete"),

    #TEST (Register-login)
    path('testRegister/', views.testRegister_page, name="testRegister"),
    path('testLogin/', views.testLogin_page, name="testLogin"),
    path('testLogout/', views.testLogout_page, name="testLogout"),

    # CustomerInfos
    path('customerInformation/<str:pk>', views.customer, name="customerInformation"),
    path('productComplaint/<str:pk>', views.productComplaint, name="productComplaint"),
    path('customerReview/<str:pk>', views.customerReview, name="customerReview"),
]