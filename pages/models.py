from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import JSONField

# Create your models here.

events = [(0, ('Contact Us')),(1, ('Proposal')),(2, ('Engagement')),(3, ('Pre-Wedding')),(4, ('Wedding & Reception'))]

service_details = [(0, 'Contact Us') ,(1, 'Image Retouching') ,(2, 'Second Photographer') ,(3, 'Boutique Company') ,(4, 'Drone Footage') ,(5, 'Love Story / Concept Film') ,(6, 'Documentary') ,(7, 'Cinematography') ,(8, 'Mixed (Documentary & Cinematography)')]

class Service(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	service_name = models.CharField(max_length=30,unique=True)
	service_description = models.CharField(max_length=30)
	cover_img = models.CharField(max_length=200)
	application_link = models.CharField(max_length=200)

	def __str__(self):
		return self.service_name


class Vendor(models.Model):
	company_name = models.CharField(max_length=200,unique=True)
	slug = models.SlugField(max_length=200, unique=True,null=True,blank=True)
	profile_pic = models.CharField(max_length=200,null=True,blank=True)
	first_name = models.CharField(max_length=50,null=True,blank=True)
	last_name = models.CharField(max_length=50,null=True,blank=True)
	primary_location = models.CharField(max_length=30,null=True)
	state = models.CharField(max_length=10,null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
	website_url = models.CharField(max_length=200,null=True,blank=True)
	instagram = models.CharField(max_length=30,null=True,blank=True)
	description = RichTextField(null=True)
	service_id = models.ForeignKey(Service, on_delete=models.SET_NULL,null=True,related_name='first_service')
	first_service_details = MultiSelectField(choices=service_details,max_length=10, default=0)
	first_delivery_profile = JSONField(null=True)
	events = MultiSelectField(choices=events,max_length=10, default=0, blank=True)
	second_service = models.ForeignKey(Service, on_delete=models.SET_NULL,null=True,related_name='second_service',blank=True)
	second_service_details = MultiSelectField(choices=service_details,max_length=10, default=0,blank=True)
	second_delivery_profile = JSONField(null=True,blank=True)
	cover_img_one = models.CharField(max_length=200,null=True,blank=True)
	cover_img_two = models.CharField(max_length=200,null=True,blank=True)
	cover_img_three = models.CharField(max_length=200,null=True,blank=True)
	featured_video = models.CharField(max_length=15,null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.company_name
