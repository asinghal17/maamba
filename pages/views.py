from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from operator import attrgetter
from django.views.generic.detail import DetailView

from pages.models import Service,Vendor

service_details = [(0, 'Contact Us') ,(1, 'Image Retouching') ,(2, 'Second Photographer') ,(3, 'Boutique Company') ,(4, 'Drone Footage') ,(5, 'Love Story / Concept Film') ,(6, 'Documentary') ,(7, 'Cinematography') ,(8, 'Mixed (Documentary & Cinematography)')]

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
	service= Service.objects.get(id=query)
	results = Vendor.objects.filter(Q(service_id=query) | Q(second_service=query) ).order_by('company_name')
	context= { "vendors":results,"service":service }
	return render(request,"vendor_search_results.html",context)


def vendor_detail_view(request,slug):
	vendor_detail = get_object_or_404(Vendor, slug=slug,)
	first_details=[vendor_detail.first_service_details]
	second_details=[vendor_detail.second_service_details]
	first_details = [service_details[int(item)][1] for l in first_details for item in l]
	second_details = [service_details[int(item)][1] for l in second_details for item in l]
	context= {"vendor": vendor_detail, "first_service_details": first_details,"second_service_details": second_details}
	return render(request,"profile.html",context)