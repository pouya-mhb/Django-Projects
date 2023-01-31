from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def post_list (request):
    posts = Post.objects.all()
    context = {
            'posts':posts
        }
    return render(
        request,'PostList.html',context
    )