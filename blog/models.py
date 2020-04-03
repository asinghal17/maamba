from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

STATUS = ((0,"Draft"),(1,"Publish"))


class Category(models.Model):
	category_name = models.CharField(max_length=30,unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	description = models.CharField(max_length=30)

	def __str__(self):
		return self.category_name


class Post(models.Model):
	title=models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
	status = models.IntegerField(choices=STATUS, default=0)
	cover_img = models.CharField(max_length=200,null=True)
	

	def __str__(self):
		return self.title