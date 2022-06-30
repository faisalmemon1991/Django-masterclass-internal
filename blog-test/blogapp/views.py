from django.shortcuts import render
from blogapp.models import Post

# Create your views here.
def index(request):
    top_blogs = Post.objects.all().order_by('-view_count')
    recent_blogs = Post.objects.all().order_by('-last_updated')

    context = {'top_blogs': top_blogs, 
                'recent_blogs': recent_blogs}
    return render(request, 'blogapp/index.html', context)  