import requests
from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    all_blogs = Blog.objects.all()  # will show All ogbejct from DB
    # If you want to show only first 5 items from DB on the page use this:
    all_blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'all_blogs': all_blogs})

def detail(request, blog_id):
    opened_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {"blog":opened_blog})
