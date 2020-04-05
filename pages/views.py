from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from operator import attrgetter
from django.views.generic.detail import DetailView

from pages.models import Service,Vendor

# Create your views here.
def home_view(request,*args, **kwargs):
	return render(request,"home.html",{})

def vendor_apply_view(request,*args, **kwargs):
	# service_objects = sorted(Service.objects.all(),key=attrgetter('created_at'),)
	# context= {"services":service_objects }
	# return render(request,"vendor_apply.html",context)
	return render(request,"apply.html",{})

def vendor_search_landing_view(request,*args, **kwargs):
	service_objects = sorted(Service.objects.all(),key=attrgetter('created_at'),)
	context= {"services":service_objects }
	return render(request,"vendor_search_landing.html",context)

def vendor_search_results_view(request):
	query = request.GET.get('vendor')
	results = Vendor.objects.filter(Q(service_id=query) | Q(second_service=query) )
	context= { "vendors":results }
	return render(request,"vendor_search_results.html",context)


class VendorDetailView(DetailView):
	model=Vendor
	template_name="profile.html"