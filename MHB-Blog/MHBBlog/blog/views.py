from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return HttpResponse('Home')

posts = Post.objects.all()
users = User.objects.all()

global_context = {
    'posts':posts,
    'users':users
}

@login_required
def new_post (request):
    # contains title, body,status
    # auto slug
    # auto date and time
    # auto autor - if user/autor is not none and @login_required
    pass

def post_list (request):
    # user should be able to add new post

    if request.method == 'GET':
        posts = Post.objects.all()
        context = {
            'posts':posts,
        }
        return render(
        request,'PostList.html',context)

    if request.method == 'POST':
        user = User.object.get(username = 'admin') # an instance from the User
        title = 'a good day in mexico'
        slug  = 'a-good-day-in-mexico'
        body  = 'this is a good day in mexico '
        author = user

        new_post = Post.objects.create(user,title,slug,body,author) # an instance from Post model to save
        new_post.save()

        new_post_context = {

            #author
            #status
            #title
            #body
            #date_published

        }

        return render(
        request,'PostList.html',)


    else : pass

def post_detail(request):
    # post details contains :
    # title,body,published date and time,author
    # auto slug
    # auto published date and time

    # user should be able to delete post
    # user should be able to update the post

    # Implement Rating later
    # Implement Comments later
    # Implement Share later
    pass
