from django.shortcuts import redirect, render
from blogapp.form import CommentForm
from blogapp.models import Post, Tag
from django.contrib.auth import login
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    top_blogs = Post.objects.all().order_by('-view_count')
    recent_blogs = Post.objects.all().order_by('-last_updated')
    featured_blog = Post.objects.filter(is_featured = True)
    if featured_blog:
        featured_blog = featured_blog[0]

    context = {'top_blogs': top_blogs, 
                'recent_blogs': recent_blogs,
                'featured_blog':featured_blog}
    return render(request, 'blogapp/index.html', context)  


def post_page(request, slug):
    post = Post.objects.get(slug = slug)
    form = CommentForm()

    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
    
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

    context = {'post':post,'recent_posts':recent_posts, 'related_posts':related_posts, 'tags':tags, 'form':form}
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


def search_blogs(request):
    search_query = ''
    if request.GET.get('q'):
        search_query = request.GET.get('q')
    posts = Post.objects.filter(title__icontains = search_query)
    print(search_query)
    context = {'posts':posts, 'search_query':search_query}
    return render(request, 'blogapp/search.html', context)


def tag_page(request, slug):
    tag = Tag.objects.get(slug = slug)
    posts = Post.objects.get(tags__in = [tag.id])

    # # How can you exclude current post from recent
    # recent_posts = Post.objects.all().order_by('-last_updated')[0:3]

    # # Related posts are posts which are by same author excluding the existing post that is loaded
    # related_posts = Post.objects.filter()[0:3]

    # tags = Tag.objects.all()
    context = {'tag':tag, 'posts':posts}
    return render(request, 'blogapp/tag.html', context)  