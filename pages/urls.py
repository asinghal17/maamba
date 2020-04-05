from pages.views import *
from django.urls import path

urlpatterns = [
    path('',home_view, name='home'),
    path('vendor-search/',vendor_search_landing_view, name='vendor-search'),
    path('search/',vendor_search_results_view, name='vendor-search-results'),
    path('vendor-apply/',vendor_apply_view, name='vendor-apply'),
    # path("vendor/<slug:slug>",VendorDetailView.as_view(), name='vendor-detail'),
]