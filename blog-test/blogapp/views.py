from django.shortcuts import render
from blogapp.models import Post

# Create your views here.
def index(request):
    blogs = Post.objects.all()
    return render(request, 'blogapp/index.html', {'blogs': blogs})  