from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

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
	slug = models.SlugField(max_length=200, unique=True,null=True)
	first_name = models.CharField(max_length=50,null=True,blank=True)
	last_name = models.CharField(max_length=50,null=True,blank=True)
	primary_location = models.CharField(max_length=30,null=True)
	state = models.CharField(max_length=10,null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
	website_url = models.CharField(max_length=200,null=True)
	instagram = models.CharField(max_length=30,null=True,blank=True)
	description = RichTextField(null=True)
	service_id = models.ForeignKey(Service, on_delete=models.SET_NULL,null=True,related_name='first_service')
	second_service = models.ForeignKey(Service, on_delete=models.SET_NULL,null=True,related_name='second_service',blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.company_name
