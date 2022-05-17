from django.urls import path
from . import views

urlpatterns = [
    path('productHome/', views.productHome, name="productHome"),
    path('', views.index, name='index'),
    path('products', views.products, name='productsPage'),
    path('login', views.login, name='loginPage'),
    path('change-password', views.changePassword, name='changePassword'),
    path('suppliers', views.suppliers, name='suppliersPage'),
    path('suppliers/products', views.supplierProducts, name='supplierProductsPage'),
    path('products/sample', views.productReviews, name='productReviewsPage'),
    path('myreviews', views.myReviews, name='myReviewsPage'),
]