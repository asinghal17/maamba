from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

from blog.models import Post

# Create your views here.
def post_detail_view(request,pk):
	post=get_object_or_404(Post,pk=1)
	context={ "post":post }
	return render(request,"post.html",context)