from django.urls import path
from . import views


urlpatterns = [
    path('productHome/', views.productHome, name="productHome"),
]