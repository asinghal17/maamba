from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View

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

class AdsView(View):
    """Replace pub-0000000000000000 with your own publisher ID"""
    line  =  "google.com, pub-2231402886390185, DIRECT, f08c47fec0942fa0"
    def get(self, request, *args, **kwargs):
        return HttpResponse(line)


# Create your views here.
# def post_list_view(request):
# 	return render(request,"blog.html",{})