from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def home_view(request,*args, **kwargs):
	return render(request,"vendor_landing.html",{})

def vendor_apply_view(request,*args, **kwargs):
	return render(request,"vendor_apply.html",{})