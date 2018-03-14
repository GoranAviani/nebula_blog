from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post

# Create your views here.
from django.contrib.auth import (
    logout,
)

def index(request):
    blog_post_list  = Post.objects.all().order_by('-post_id')

    return render (request, 'index.html', {'blog_post_list':blog_post_list})


def contact(request):
    return render(request,'perasis/contact.html')

def post_detail(request,post_id,post_slug):
    post_to_show = get_object_or_404(Post, post_id=post_id, post_slug=post_slug)
    return render (request, "blog_post/post_detail.html",{"post_to_show":post_to_show})

def response_check_upload_image(request):
    return render(request,'blog_post/image_not_allowed_to_upload.html')


def login(request):
    return redirect('/admin/')

def logout_view(request):
    logout(request)
    return render(request,"index.html")
