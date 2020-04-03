from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Post

# Create your views here.
class PostListView(ListView):
	template_name = "blog.html"
	queryset = Post.objects.filter(status=1).order_by('-created_at')
	context_object_name = 'post_list'
	paginate_by = 10


class PostDetailView(DetailView):
	# post=get_object_or_404(Post,pk=1)
	# context={ "post":post }
	# return render(request,"post.html",context)
	model=Post 
	template_name="post.html"

# Create your views here.
# def post_list_view(request):
# 	return render(request,"blog.html",{})