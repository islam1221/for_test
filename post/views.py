from typing import List
from django.shortcuts import render
from django.http.request import HttpRequest
from .models import BlogPost

def blog_view(request):
    post: List[BlogPost] = BlogPost.objects.all()
    return render(request, 'index.html', context={'blogs':post})

    
def blog_detail_view(request: HttpRequest, id: int):
    blog = BlogPost.objects.get(id=id)
    return render(request, 'blog_detail.html', context={'blog':blog}) 