from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from operator import attrgetter

from pages.models import Service,Vendor

# Create your views here.
def home_view(request,*args, **kwargs):
	return render(request,"vendor_landing.html",{})

def vendor_apply_view(request,*args, **kwargs):
	service_objects = sorted(Service.objects.all(),key=attrgetter('created_at'),)
	context= {"services":service_objects }
	return render(request,"vendor_apply.html",context)

def vendor_search_landing_view(request,*args, **kwargs):
	service_objects = sorted(Service.objects.all(),key=attrgetter('created_at'),)
	context= {"services":service_objects }
	return render(request,"vendor_search_landing.html",context)

def vendor_search_results_view(request):
	query = request.GET.get('vendor')
	results = Vendor.objects.filter(service_id=query)
	context= { "vendors":results }
	return render(request,"vendor_search_results.html",context)


# def vendor_view(request,pk):
# 	vendor_obj = Vendor.objects.get(pk=pk)
# 	context= { "vendor":vendor_obj }
# 	return render(request,"vendor_profile.html",context)