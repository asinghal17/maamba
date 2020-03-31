from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Service(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	service_name = models.CharField(max_length=30)
	service_description = models.CharField(max_length=30)
	cover_img = models.CharField(max_length=200)
	application_link = models.CharField(max_length=200)

	def __str__(self):
		return self.service_name


# class Vendor(models.Model):
# 	company_name = models.CharField(max_length=200)
# 	first_name = models.CharField(max_length=30)
# 	last_name = models.CharField(max_length=30)
# 	phone_number= PhoneNumberField(blank=True)
# 	primary_location = models.CharField(max_length=30)
# 	website_url = models.CharField(max_length=200)
# 	instagram = models.CharField(max_length=20)
# 	description = models.TextField()
# 	service_id = models.ForeignKey(Service, on_delete=models.SET_NULL,null=True)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# 	def __str__(self):
# 		return self.company_name
