from django.shortcuts import render
from .models import Blog

def mon_blog(request):
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/mon_blog.html', {'blogs':blogs})
