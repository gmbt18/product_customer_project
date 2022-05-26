from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
urlpatterns = [
    path('', views.customerHome, name="customerHome"),
    path('catalogCustomer/', views.catalogCustomer, name="catalogCustomer"),
    path('catalogMonthly/', views.catalogMonthly, name="catalogMonthly"),
    path('catalogProduct/', views.catalogProduct, name="catalogProduct"),
    # Search
    path('searchPage/', views.searchPage, name="searchPage"),
    path('detailedProduct/', views.detailedProduct, name="detailedProduct"),
    path('detailedProduct/<str:pk>', views.detailedProduct, name="detailedProduct"),
    path('login/', views.login_page, name="login"),
    path('passwordChange/', views.passwordChange, name="passwordChange"),
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
    path('testChangePassword/', views.testChangePassword, name="testChangePassword"),

    path('password_reset/', views.password_reset_request, name="crms_password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='crms_app/TEST-Register-Login/test-passwordForgot-done.html'), name="crms_password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='crms_app/TEST-Register-Login/test-passwordReset-confirm.html', success_url = reverse_lazy('crms_password_reset_complete')), name="crms_password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='crms_app/TEST-Register-Login/test-passwordReset-complete.html'), name="crms_password_reset_complete"),
    # CustomerInfos
    path('customerInfo/<str:pk>', views.customerInfo, name="customerInfo"),
    path('customerInfoAdd', views.customerInfoAdd, name="customerInfoAdd"),
    path('customerInfoUpdate/<str:pk>', views.customerInfoUpdate, name="customerInfoUpdate"),
    path('customerInformation/<str:pk>', views.customerInformation, name="customerInformation"),
    path('productComplaint/<str:pk>', views.productComplaint, name="productComplaint"),
    path('customerReview/<str:pk>', views.customerReview, name="customerReview"),
    path('removeReview/<str:pk>', views.removeReview, name="removeReview"),
    path('submitProductComplaint/<str:pk>', views.submitProductComplaint, name="submitProductComplaint"),
    path('subscribeCatalog/', views.subscribeCatalog, name="subscribeCatalog"),
    path('unsubscribeCatalog/', views.unsubscribeCatalog, name="unsubscribeCatalog"),

]

