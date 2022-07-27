from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AuthUser)
admin.site.register(CustomerInformation)
admin.site.register(ProductComplaint)
admin.site.register(CustomerReview)