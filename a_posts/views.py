from django.shortcuts import render
from .models import *
# Create your views here.

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'a_posts/home.html', {'posts' : posts})
