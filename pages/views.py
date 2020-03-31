from django.http import HttpResponse
from django.shortcuts import render

from pages.models import Service

# Create your views here.
def home_view(request,*args, **kwargs):
	return render(request,"vendor_landing.html",{})

def vendor_apply_view(request,*args, **kwargs):
	service_objects = Service.objects.all()
	context= {"services":service_objects }
	return render(request,"vendor_apply.html",context)

# def vendor_view(request,pk):
# 	vendor_obj = Vendor.objects.get(pk=pk)
# 	context= { "vendor":vendor_obj }
# 	return render(request,"vendor_profile.html",context)