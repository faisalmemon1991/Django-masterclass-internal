from django.shortcuts import redirect, render
from blogapp.models import Post, Tag
from django.contrib.auth import login
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    top_blogs = Post.objects.all().order_by('-view_count')
    recent_blogs = Post.objects.all().order_by('-last_updated')

    context = {'top_blogs': top_blogs, 
                'recent_blogs': recent_blogs}
    return render(request, 'blogapp/index.html', context)  


def post_page(request, slug):
    post = Post.objects.get(slug = slug)
    
    if post.view_count is None:
        post.view_count = 1
    else:
        post.view_count = post.view_count + 1
    post.save()

    # How can you exclude current post from recent
    recent_posts = Post.objects.all().order_by('-last_updated')[0:3]

    # Related posts are posts which are by same author excluding the existing post that is loaded
    related_posts = Post.objects.filter()[0:3]

    tags = Tag.objects.all()
    context = {'post':post,'recent_posts':recent_posts, 'related_posts':related_posts, 'tags':tags}
    return render(request, 'blogapp/post.html', context)  


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'blogapp/login.html')