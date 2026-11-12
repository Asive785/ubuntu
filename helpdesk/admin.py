from django.contrib import admin
from .models import Category, ServiceRequest, RequestUpdate

admin.site.register(Category)
admin.site.register(ServiceRequest)
admin.site.register(RequestUpdate)