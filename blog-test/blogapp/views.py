from django.shortcuts import redirect, render
from blogapp.form import CommentForm
from blogapp.models import Bookmark, Comments, Post, Tag, WebsiteMeta
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    top_posts = Post.objects.all().order_by('-view_count')
    recent_posts = Post.objects.all().order_by('-last_updated')
    featured_blog = Post.objects.filter(is_featured = True)
    website_info = None
    if WebsiteMeta.objects.all().exists():
        website_info = WebsiteMeta.objects.all()[0]

    if featured_blog:
        featured_blog = featured_blog[0]

    context = {'top_posts': top_posts, 
                'recent_posts': recent_posts,
                'featured_blog':featured_blog,
                'website_info':website_info}
    return render(request, 'blogapp/index.html', context)  


def post_page(request, slug):
    post = Post.objects.get(slug = slug)
    form = CommentForm()

    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent = None
            if request.POST.get('parent'):
                parent = request.POST.get('parent')
                parent_obj = Comments.objects.get(id=parent)
                if parent_obj:
                    comment_reply = comment_form.save(commit=False)
                    comment_reply.parent = parent_obj
                    comment_reply.post = post
                    comment_reply.save()
            comment = comment_form.save(commit=False)
            postid =request.POST.get('post_id')
            post = Post.objects.get(id=postid)
            comment.author = request.user
            comment.post = post
            comment.save()
    
    if post.view_count is None:
        post.view_count = 1
    else:
        post.view_count = post.view_count + 1
    post.save()

    # Liked logic
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    number_of_likes = post.number_of_likes()
    post_is_liked = liked

    # How can you exclude current post from recent
    recent_posts = Post.objects.all().order_by('-last_updated')[0:3]

    # Related posts are posts which are by same author excluding the existing post that is loaded
    related_posts = Post.objects.filter()[0:3]

    tags = Tag.objects.all()
    comments = Comments.objects.filter(post=post, parent=None)
    replies= Comments.objects.filter(post=post).exclude(parent=None)

    context = {'post':post,'recent_posts':recent_posts, 'related_posts':related_posts, 'tags':tags, 'form':form,'comments':comments, 'number_of_likes':number_of_likes, 'post_is_liked':post_is_liked}
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


def search_posts(request):
    search_query = ''
    if request.GET.get('q'):
        search_query = request.GET.get('q')
    posts = Post.objects.filter(title__icontains = search_query)
    print(search_query)
    context = {'posts':posts, 'search_query':search_query}
    return render(request, 'blogapp/search.html', context)

def all_posts(request):
    all_posts = Post.objects.all()
    context = {'all_posts':all_posts}
    return render(request, 'blogapp/all_posts.html', context)

def like_post(request, slug):
    print(request.POST.get('post_id'))
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_page', args=[str(slug)]))


def bookmark(request):
    liked_posts = Bookmark.objects.all(user=request.user)
    context = {'liked_posts':liked_posts}
    return render(request, 'blogapp/liked_posts.html', context)

def about(request):
    website_info = None
    if WebsiteMeta.objects.all().exists():
        website_info = WebsiteMeta.objects.all()[0]

    context = {'website_info':website_info}
    return render(request, 'blogapp/about.html', context)


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