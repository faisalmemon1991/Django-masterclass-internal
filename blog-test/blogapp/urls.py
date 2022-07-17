from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>', views.post_page, name='post_page'),
    path("accounts/login/", views.loginUser, name="login"),
    path("search/", views.search_posts, name="search"),
    path("all_posts/", views.all_posts, name="all_posts"),
    path("like_post/<slug:slug>", views.like_post, name="like_post"),
    path("about/", views.about, name="about"),
    path("tag/<slug:slug>", views.tag_page, name="tag_page"),

    path("bookmark/", views.bookmark, name="bookmark"),
]