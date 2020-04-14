from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from operator import attrgetter
import json
import requests
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode
from django.views.generic.detail import DetailView
from pages.models import Service,Vendor

service_details = [(0, 'Contact Us') ,(1, 'Image Retouching') ,(2, 'Second Photographer') ,(3, 'Boutique Company') ,(4, 'Drone Footage') ,(5, 'Love Story / Concept Film') ,(6, 'Documentary') ,(7, 'Cinematography') ,(8, 'Mixed (Documentary & Cinematography)')]


def api_request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()

def get_business_reviews(api_key, business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    if business_id:
        business_path = settings.YELP_BUSINESS_PATH + business_id + "/reviews"
        return api_request(settings.YELP_API_HOST, business_path, api_key)
    else:
        return {}

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
	yelp_reviews = get_business_reviews(settings.YELP_API_KEY, vendor_detail.yelp_slug)
	first_details=[vendor_detail.first_service_details]
	second_details=[vendor_detail.second_service_details]
	first_details = [service_details[int(item)][1] for l in first_details for item in l]
	second_details = [service_details[int(item)][1] for l in second_details for item in l]
	context= {"vendor": vendor_detail, "first_service_details": first_details,"second_service_details": second_details, "yelp_reviews": yelp_reviews}
	return render(request,"profile.html",context)