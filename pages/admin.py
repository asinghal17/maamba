from django.contrib import admin

# Register your models here.

from .models import Service,Vendor
  
admin.site.register(Vendor)
admin.site.register(Service)