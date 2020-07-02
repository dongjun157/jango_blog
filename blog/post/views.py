from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    posts = Post.objects
    return render(request, 'post/index.html', {"posts": posts})