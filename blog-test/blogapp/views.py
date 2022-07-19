from django import forms
from django.shortcuts import redirect, render
from blogapp.form import CommentForm, SubscribeForm
from blogapp.models import Comments, Post, Tag, WebsiteMeta
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from blogapp.form import NewUserForm
from django.contrib import messages

# Create your views here.
def index(request):
    subscribe_form = SubscribeForm()
    subscribe_successful = None
    top_posts = Post.objects.all().order_by('-view_count')
    recent_posts = Post.objects.all().order_by('-last_updated')
    featured_blog = Post.objects.filter(is_featured = True)
    website_info = None
    if WebsiteMeta.objects.all().exists():
        website_info = WebsiteMeta.objects.all()[0]

    if featured_blog:
        featured_blog = featured_blog[0]

    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            subscribe_successful = 'Subscribed successfully'
            subscribe_form = SubscribeForm()

    context = {'top_posts': top_posts, 
                'recent_posts': recent_posts,
                'featured_blog':featured_blog,
                'website_info':website_info,
                'form':subscribe_form,
                'subscribe_successful':subscribe_successful}
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

    # Bookmark logic
    bookmarked = False
    if post.bookmarks.filter(id=request.user.id).exists():
        bookmarked = True
    is_bookmarked = bookmarked

    # How can you exclude current post from recent
    recent_posts = Post.objects.all().order_by('-last_updated')[0:3]

    # Related posts are posts which are by same author excluding the existing post that is loaded
    related_posts = Post.objects.filter()[0:3]

    tags = Tag.objects.all()
    comments = Comments.objects.filter(post=post, parent=None)
    replies= Comments.objects.filter(post=post).exclude(parent=None)

    context = {'post':post,'recent_posts':recent_posts, 'related_posts':related_posts, 'tags':tags, 'form':form,'comments':comments, 'number_of_likes':number_of_likes, 'post_is_liked':post_is_liked, 'is_bookmarked':is_bookmarked}
    return render(request, 'blogapp/post.html', context)  


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username and passwords do not match')

    return render(request, 'registration/login.html')


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

def all_liked_posts(request):
    all_liked_posts = Post.objects.filter(likes=request.user)
    context = {'all_liked_posts':all_liked_posts}
    return render(request, 'blogapp/all_liked_posts.html', context)

def like_post(request, slug):
    print(request.POST.get('post_id'))
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_page', args=[str(slug)]))


def all_bookmarked_posts(request):
    all_bookmarked_posts = Post.objects.filter(bookmarks=request.user)
    context = {'all_bookmarked_posts':all_bookmarked_posts}
    return render(request, 'blogapp/all_bookmarked_posts.html', context)

def bookmark_post(request, slug):
    print("PRINT ", request.POST.get('post_id'))
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.bookmarks.filter(id=request.user.id).exists():
        post.bookmarks.remove(request.user)
    else:
        post.bookmarks.add(request.user)
    return HttpResponseRedirect(reverse('post_page', args=[str(slug)]))

def about(request):
    website_info = None
    if WebsiteMeta.objects.all().exists():
        website_info = WebsiteMeta.objects.all()[0]

    context = {'website_info':website_info}
    return render(request, 'blogapp/about.html', context)


def tag_page(request, slug):
    tag = Tag.objects.get(slug = slug)
    posts = Post.objects.filter(tags__in = [tag.id])

    top_posts = Post.objects.filter(tags__in = [tag.id]).order_by('-view_count')
    recent_posts = Post.objects.filter(tags__in = [tag.id]).order_by('-last_updated')

    # # How can you exclude current post from recent
    # recent_posts = Post.objects.all().order_by('-last_updated')[0:3]

    # # Related posts are posts which are by same author excluding the existing post that is loaded
    # related_posts = Post.objects.filter()[0:3]

    tags = Tag.objects.all()
    context = {'tag':tag, 'posts':posts,'top_posts':top_posts,'recent_posts':recent_posts,'tags':tags}
    return render(request, 'blogapp/tag.html', context)  



def register_user(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("Form valid")
            return redirect("/")
    return render (request=request, template_name="registration/registration.html", context={"register_form":form})



def subscribe(request):
    subscribe_form = SubscribeForm()

            # return redirect(reverse('thank_you'))
    context={"form":subscribe_form}
    return render(request,"subscribe/subscribe.html",context)